import aws_cdk as core
import aws_cdk.assertions as assertions
from design_problem1.design_problem1_stack import DesignProblem1Stack
import pytest

""" Pytest Fixture """
# https://docs.pytest.org/en/7.1.x/explanation/fixtures.html
@pytest.fixture
def fixtureTemplate():
    app = core.App()
    stack = DesignProblem1Stack(app, "sprint5")
    template = assertions.Template.from_stack(stack)
    return template

""" Unit Tests """
# https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/README.html
# https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
# Unit Test #1 Checking if WH and DB Lambda are added
def test_Lambda(fixtureTemplate):
    fixtureTemplate.resource_count_is("AWS::Lambda::Function",3)

# Unit Test #2 Checking that only 1 topic exists in stack
def test_SNS(fixtureTemplate):
    fixtureTemplate.resource_count_is("AWS::SNS::Topic",1)
    
# Unit Test #3 Checking that both Alarm and URL tables exist
def test_DBTables(fixtureTemplate):
    fixtureTemplate.resource_count_is("AWS::DynamoDB::Table",2)
        
# Unit Test #4 Checking CloudWatch Alarm Properties
def test_CloudWatch(fixtureTemplate):
    fixtureTemplate.has_resource_properties("AWS::CloudWatch::Alarm", {
            "MetricName": "Invocations",
            "Namespace": "AWS/Lambda",
            "Period": 300,
            "Statistic": "Sum",
            "Threshold": 2
            }   
        )  
    
# Unit Test #5 Checking for DynamoDB Table Partition and Sort key
def test_DynamoDB(fixtureTemplate):
    fixtureTemplate.has_resource_properties("AWS::DynamoDB::Table", {
            "KeySchema": [
            {
            "AttributeName": "id",
            "KeyType": "HASH"
            },
            {
            "AttributeName": "Timestamp",
            "KeyType": "RANGE"
            }
            ]
        }
    )
    

# Functional Test #1 
def test_functional():
    app = core.App()
    stack = DesignProblem1Stack(app, "sprint5")
    lambda_handler = stack.create_dynamoDB_table
    assert lambda_handler is not None 