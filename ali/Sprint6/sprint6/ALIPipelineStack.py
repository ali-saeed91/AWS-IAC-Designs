import aws_cdk as cdk
from aws_cdk import Stack
from aws_cdk import aws_iam as iam_
from constructs import Construct
import aws_cdk.pipelines as pipelines_
import aws_cdk.aws_codepipeline_actions as actions_
import aws_cdk.aws_codebuild as codebuild
from sprint6.ALIStage import ALIStage

class ALIPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        """ Access the Github source repository """
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.pipelines/CodePipelineSource.html
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk/SecretValue.html 
        source=pipelines_.CodePipelineSource.git_hub("alisaeed2022skipq/Sirius_Python", "main",
                                                       authentication= cdk.SecretValue.secrets_manager("ALIToken"),
                                                       trigger= actions_.GitHubTrigger('POLL')
                                                       )
        
        """ Add CodeBuildStep step to synthasize application """
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/CodeBuildStep.html
        synth = pipelines_.ShellStep("Synth",
                                     input = source,
                                     commands = ["cd ali/Sprint6/",
                                                 "npm install -g aws-cdk",
                                                 "pip install -r requirements.txt",
                                                 "pip install -r requirements-dev.txt",
                                                 "cdk synth"],
                                     primary_output_directory = "ali/Sprint6/cdk.out"
                                    
                                     )
        
        """ Unit and Functional Tests """ 
        unit = pipelines_.ShellStep("UnitTest",
                                    input = source,
                                    commands = [
                                                "cd ali/Sprint6/",
                                                "npm install -g aws-cdk",
                                                "pip install -r requirements.txt",
                                                "pip install -r requirements-dev.txt",
                                                "pytest",
                                                ]
                                        )
        
        """ Build Docker Image for Pyresttest """                                    
        # https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker-custom-image.html
        pyresttest = pipelines_.CodeBuildStep("PyrestApiTests",
                                            commands=[],
                                            build_environment = codebuild.BuildEnvironment(build_image = codebuild.LinuxBuildImage.from_asset(self, "Image", directory="docker-images/").from_docker_registry(name="docker:dind"),
                                            privileged = True
                                            ),
                                            partial_build_spec = codebuild.BuildSpec.from_object(
                                                {
                                                    "version": 0.2,
                                                    "phases": {
                                                        "install": {
                                                        "commands": [
                                                            "nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://127.0.0.1:2375 --storage-driver=overlay2 &",
                                                            "timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\""
                                                        ]
                                                        },
                                                        "pre_build": {
                                                        "commands": [
                                                            "cd ali/Sprint6/docker-images",
                                                            "docker build -t apitest:ali ."
                                                        ]
                                                        },
                                                        "build": {
                                                        "commands": [
                                                            "docker run --name pyrestests apitest:ali"
                                                        ]
                                                        }
                                                    }
                                                }
                                            )
        )
        """ Creating the pipeline """
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/README.html#cdk-pipelines
        pipeline = pipelines_.CodePipeline(self, "ALIPipelineSprint6", synth =synth)
        
        """ Creating instances of Application for Testing """
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.core/Stage.html
        """ Adding Beta Stage for Unit test using Pytest and Functional Test using Pyresttest Docker Image """
        betaTesting = ALIStage(self, "Beta")
                                 
        """ Adding Tests to Beta Stage """                     
        pipeline.add_stage(betaTesting, pre=[unit], post=[pyresttest]) 
          
        """ Adding a Manual Approval Step in Pre Production Stage """
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/AddStageOpts.html          
        prod = ALIStage(self, "Prod")
        pipeline.add_stage(prod, pre=[
                pipelines_.ManualApprovalStep("PromoteToProd")
    ])
        