import aws_cdk as cdk
from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_iam as iam_
import aws_cdk.pipelines as pipelines_
from aws_cdk.pipelines import CodeBuildStep
import aws_cdk.aws_codepipeline_actions as actions_
from sprint3.ALIStage import ALIStage

class ALIPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Access the Github source repository
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.pipelines/CodePipelineSource.html
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk/SecretValue.html
        source=pipelines_.CodePipelineSource.git_hub("alisaeed2022skipq/Sirius_Python", "main",
                                                       authentication= cdk.SecretValue.secrets_manager("ALIToken"),
                                                       trigger= actions_.GitHubTrigger('POLL')
                                                       )
        # Add shell step to synthasize application
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/ShellStep.html
        synth = pipelines_.CodeBuildStep("Synth",
                                     input = source,
                                     commands = ["cd ali/Sprint3",
                                                 "npm install -g aws-cdk",
                                                 "pip install -r requirements.txt",
                                                 "pip install -r requirements-dev.txt",
                                                 "cdk synth"],
                                     primary_output_directory = "ali/Sprint3/cdk.out"
                                     )
        # Create a pipeline
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/README.html#cdk-pipelines
        pipeline = pipelines_.CodePipeline(self, "ALIPipelineSprint3", synth =synth)
        
        # Creating instances of Application for Testing
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.core/Stage.html
        """ Unit Tests """
        betaTesting = ALIStage(self, "Beta")
        pipeline.add_stage(betaTesting, pre=[
                pipelines_.CodeBuildStep("Synth",
                                    input = source,
                                    commands = [
                                                "cd ali/Sprint3",
                                                "npm install -g aws-cdk",
                                                "pip install -r requirements.txt",
                                                "pip install -r requirements-dev.txt",
                                                "pytest"
                                                ],
                                    role_policy_statements=[
                                                            iam_.PolicyStatement(
                                                                                actions=["dynamodb:Scan"],
                                                                                resources=["*"])
                                                                        ],
                                     )
                                ]
                            )
        
        # Adding Gamma Stage for Functional Test (Checking lambda_handler for Web resource availability and latency)
        """ Functional Test """
        gammaTesting = ALIStage(self, "Gamma")
        pipeline.add_stage(gammaTesting, pre=[
                pipelines_.CodeBuildStep("Synth",
                                    input = source,
                                    commands = [
                                                "cd ali/Sprint3",
                                                "npm install -g aws-cdk",
                                                "pip install -r requirements.txt",
                                                "pip install -r requirements-dev.txt",
                                                "cd tests/functional/",
                                                "python3 func.py"
                                                ],
                                    role_policy_statements=[
                                                            iam_.PolicyStatement(
                                                                                actions=["dynamodb:Scan"],
                                                                                resources=["*"])
                                                                        ],
                                     )
                                ]
                            )
         # Adding Integration Test (# Integraton Testing to check if DynamoDB table is created for current stage and Alarms are logged IAM required)
        """ Integration Test """
        deltaTesting = ALIStage(self, "Delta")
        pipeline.add_stage(deltaTesting, pre=[
                pipelines_.CodeBuildStep("Synth",
                                    input = source,
                                    commands = [
                                                "cd ali/Sprint3",
                                                "npm install -g aws-cdk",
                                                "pip install -r requirements.txt",
                                                "pip install -r requirements-dev.txt",
                                                "cd sprint3/"
                                                "python3 integr.py"
                                                ],
                                    role_policy_statements=[
                                                            iam_.PolicyStatement(
                                                                                actions=["dynamodb:Scan"],
                                                                                resources=["*"])
                                                                        ],
                                    )
                                ]            
                            )         
        # Adding a Manual Approval Step in Pre Production Stage
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/AddStageOpts.html          
        prod = ALIStage(self, "Prod")
        pipeline.add_stage(prod, pre=[
                pipelines_.ManualApprovalStep("PromoteToProd")
    ])
        