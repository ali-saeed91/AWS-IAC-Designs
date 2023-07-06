import os
import boto3
import json
import datetime
import uuid
import ast

""" Get API Table from env Variable """
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
# https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-retrieve
table_name = os.environ['ARGTable']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:   
        # https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html
        Method = event["httpMethod"]
        
        EV = event["body"]
        """ Convert to JSON string """
        js = json.dumps(EV)
        
        """ Convert JSON string to Python Obj """
        dic = json.loads(js)
       
        """ Convert String Dictionary to Dictionary """
        # https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/?ref=gcse
        res = ast.literal_eval(dic)
        
        """ Extract Value from Dictionary """
        value = res[0]['event1']['attr1']
        
        """ Generate unique Id """
        uid = str(uuid.uuid1())
        """ Timestamp """
        tim = str(datetime.datetime.now())
        """ Extract Api Id"""
        api = event["requestContext"]["apiId"]
        
        """ Performing CD Operations """
        # https://dynobase.dev/dynamodb-python-with-boto3/
        
        if Method == "POST":
            response = table.put_item(
                Item={
                    "id": uid,
                    "Timestamp": tim,
                    "ApiId": api,
                    "Event": EV,
                    "Value": value
    
                    }
                )
    
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': "Success! Value Added"
            }
        
        
        
        if Method == "DELETE":
            response = table.delete_item(
                Key={
                    "id": uid
                }
            )
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': "Success! Value Deleted"
            }
    
        else:     
            return {
                    'statusCode': 200,
                    'headers': {
                        'Content-Type': 'application/json'
                    },
                    'body': "No Data Found"
                }
    except Exception as err:
        print('An Error occured :', err)