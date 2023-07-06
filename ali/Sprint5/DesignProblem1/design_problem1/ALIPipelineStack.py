import aws_cdk as cdk
from aws_cdk import Stack
from aws_cdk import aws_iam as iam_
from constructs import Construct
import aws_cdk.pipelines as pipelines_
import aws_cdk.aws_codepipeline_actions as actions_
from design_problem1.ALIStage import ALIStage

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
        # Add CodeBuildStep step to synthasize the application
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/CodeBuildStep.html
        synth = pipelines_.CodeBuildStep("Synth",
                                     input = source,
                                     commands = ["cd ali/Sprint5/DesignProblem1",
                                                 "npm install -g aws-cdk",
                                                 "pip install -r requirements.txt",
                                                 "pip install -r requirements-dev.txt",
                                                 "cdk synth"],
                                     primary_output_directory = "ali/Sprint5/DesignProblem1/cdk.out"
                                     )
        # Create a pipeline
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/README.html#cdk-pipelines
        pipeline = pipelines_.CodePipeline(self, "ALIPipelineSprint5", synth =synth)
        
        # Creating instances of Application for Testing
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.core/Stage.html
        # Adding Beta Stage for Unit test,Functional Tests and Integration Tests using Pytest fixture tests using assertions in stack resources)
        # Adding Integration Testing to check if DynamoDB table is created for Pipeline stage with Alarms being logged 
        """ Integration Test """
        """ Unit Tests and Functional Test """
        betaTesting = ALIStage(self, "Beta")
        pipeline.add_stage(betaTesting, pre=[
                pipelines_.CodeBuildStep("Synth",
                                    input = source,
                                    commands = [
                                                "cd ali/Sprint5/DesignProblem1",
                                                "npm install -g aws-cdk",
                                                "pip install -r requirements.txt",
                                                "pip install -r requirements-dev.txt",
                                                "pytest",
                                                "cd tests/integration/",
                                                "python3 integr.py"
                                                ],
                                                role_policy_statements=[
                                                                        iam_.PolicyStatement(
                                                                                            actions=[ "dynamodb:Scan"],
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
        