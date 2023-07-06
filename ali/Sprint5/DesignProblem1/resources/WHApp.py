import os
import boto3
import urllib3
import datetime
from cloudwatch_putData import AWSCloudWatch
import constants as constants

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
dynamodb=boto3.resource('dynamodb',region_name='us-east-2')
table_name = os.environ['ARGTable']
table = dynamodb.Table(table_name)

#array for storing values
URL =[]
#for storing values 
values=[]

def lambda_handler(event, context):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/cw-example-using-alarms.html
    """Topic and Alarm Actions using boto3 SDK"""
    topicname=os.environ["topicname"]
    AlarmActions = ["arn:aws:sns:us-east-2:315997497220:{topicname}".format(topicname=topicname)]
    
    
    """ CloudWatch Object """
    cloudwatch_object = AWSCloudWatch()
    
    """ Executing functions to fetch arg1 values """
    response = table.scan()
    lists=response["Items"]
    for l in lists:
        URL.append(l["arg1"])
        
    for i in URL:
        dimensions = [{ 'Name': 'ARG1', 'Value': i}]
       
        value = int(i)

        """ Sending data to CloudWatch """
        # ARG1 Values   
        cloudwatch_object.cloudwatch_metric_data(constants.nameSpace, constants.AvailabilityMetric, dimensions, value )
        cloudwatch_object.cloudWatch_metric_alarm("ARG1_of_ALI_" + str(i),
        AlarmActions,constants.AvailabilityMetric,constants.nameSpace,dimensions,10,"GreaterThanThreshold")
        
        values.append({"arg1" : value})
        
            
    return values
