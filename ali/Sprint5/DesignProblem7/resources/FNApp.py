from pprint import pprint
import boto3
import json
import os
import constants

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#client


def lambda_handler(event, context):
    """ Extract Bucket name from ENV Variable"""
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
    s3_client = boto3.client('s3',
                    aws_access_key_id=constants.access_key,
                    aws_secret_access_key=constants.secret_access_key
                    ,region_name ='us-east-1')
    s3_bucket_name = os.environ["Buckets"]
    
    """ Extracting Filename from Event """
    method = event["httpMethod"]
    object_name = event["body"]
    
    """ POST API Operation to Generate Presigned URL and Upload File"""
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
    if method=="POST":
        response = s3_client.generate_presigned_post(
                                                        s3_bucket_name,
                                                        object_name,
                                                        ExpiresIn=3600
                                                    )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response)
        }