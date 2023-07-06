import json
import boto3
import re
from collections import Counter


def lambda_handler(event, context):
    
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']
    print(filename)
    
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket
    s3 = boto3.resource('s3')
    s3_object = s3.Bucket(str(bucket)).Object(str(filename)).get()
    text = s3_object['Body'].read()
    decoded = text.decode()
    
    # https://www.techiedelight.com/remove-non-alphanumeric-characters-string-python/
    s = re.sub(r'\W+', ' ', decoded)
    sArr = s.split()
    dic = Counter(sArr)
    
    """ Verify Email """
    # https://www.learnaws.org/2020/12/18/aws-ses-boto3-guide/
    # ses_client = boto3.client("ses", region_name="us-east-2")
    # response = ses_client.verify_email_identity(
    #     EmailAddress="ali.saeed.sirius@gmail.com"
    # )
    # print(response)

    # https://www.learnaws.org/2020/12/18/aws-ses-boto3-guide/
    ses_client = boto3.client("ses", region_name="us-east-2")
    CHARSET = "UTF-8"

    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                "ali.saeed.sirius@gmail.com",
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": json.dumps(dic),
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": json.dumps("Words & Frequency of "+ str(filename)),
            },
        },
        Source="ali.saeed.sirius@gmail.com",
    )
    
    """ Get API Table from env Variable """
    # https://www.beabetterdev.com/2022/10/01/how-to-insert-multiple-dynamodb-items-at-once-with-boto3/
    dynamodb=boto3.resource('dynamodb',region_name='us-east-2')
    # table_name = os.environ['ARGTable']
    table = dynamodb.Table('testingtb')
    with table.batch_writer() as batch:
        for k,v in dic.items():
            response = batch.put_item(Item={
                "word": k,
                "frequency": str(v),
                "Filename": filename
            })
   
    return {
        'statusCode': 200,
        'body': json.dumps('Success Data Sent!')
    }
