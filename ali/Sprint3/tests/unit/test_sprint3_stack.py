import aws_cdk as core
import aws_cdk.assertions as assertions
from sprint3.sprint3_stack import Sprint3Stack
import pytest

""" Pytest Fixture """
# https://docs.pytest.org/en/7.1.x/explanation/fixtures.html
@pytest.fixture
def fixtureTemplate():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)
    return template

""" Unit Tests """
# https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/README.html
# https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
# Unit Test #1 Checking if WH and DB Lambda are added
def test_Lambda(fixtureTemplate):
    fixtureTemplate.resource_count_is("AWS::Lambda::Function",2)

# Unit Test #2 Checking that only 1 topic exists in stack
def test_SNS(fixtureTemplate):
    fixtureTemplate.resource_count_is("AWS::SNS::Topic",1)
    
# Unit Test #3 Checking CloudWatch Alarm Properties
def test_CloudWatch(fixtureTemplate):
    fixtureTemplate.has_resource_properties("AWS::CloudWatch::Alarm", {
            "MetricName": "URL_LATENCY",
            "Namespace": "AliSaeedNamespace",
            "Period": 300,
            "Statistic": "Average",
            "Threshold": 0.6
            }
        )  
    
# Unit Test #4 Checking for DynamoDB Table Partition and Sort key
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
    
# Unit Test #5 Checking for Lambda IAM policy for writing into DynamoDB      
def test_IAMPolicy(fixtureTemplate):
    fixtureTemplate.has_resource_properties("AWS::IAM::Policy", {
        "PolicyDocument": {
            "Statement": [
            {
            "Action": "dynamodb:*",
            "Effect": "Allow",
            "Resource": [
                {
                "Fn::GetAtt": [
                "AlarmTable68A95781",
                "Arn"
                ]
                },
                {
                "Ref": "AWS::NoValue"
                }
            ]
            }
            ],
            "Version": "2012-10-17"
            }
        }
    )
# Functional Test #1 
def test_functional():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    lambda_handler = stack.create_dynamoDB_table
    assert lambda_handler is not None 