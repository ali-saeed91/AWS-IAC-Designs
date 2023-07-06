import os
import boto3
import json
import constants as constants

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
# https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-retrieve
table_name = os.environ['URLTable']
table = dynamodb.Table(table_name)

# Getting All Table Data
urls = []
response = table.scan()
Lists = response["Items"]
for l in Lists:
   urls.append(l['URL'])

def lambda_handler(event, context):
    try:   
        # https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html
        Method = event["httpMethod"]
        URL = event["body"]
        
        """ Performing CRUD Operations """
        # https://dynobase.dev/dynamodb-python-with-boto3/
        if Method == "GET":
            response = table.scan()
            Lists = response["Items"]
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps(urls)
            }
        
        if Method == "POST":
            response = table.put_item(
                Item={
                    "URL": URL
    
                    }
                )
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': "Success! URL Added"
            }
        
        if Method == "PATCH":
            current = URL[0]
            update = URL[1]
            response = table.update_item(
                Key={
                    'URL': current
                },
                UpdateExpression='SET URL = :val1',
                ExpressionAttributeValues={
                    ':val1': update
                },
            )
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': "Success! URL Updated"
            }
        
        if Method == "DELETE":
            response = table.delete_item(
                Key={
                    "URL": URL
                }
            )
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': "Success! URL Deleted"
            }
    
        if len(urls) != 0:
            return {
                    'statusCode': 200,
                    'headers': {
                        'Content-Type': 'application/json'
                    },
                    'body': ("Success! URL List: ",set(urls))
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