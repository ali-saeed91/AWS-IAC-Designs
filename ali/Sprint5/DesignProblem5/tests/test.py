import json
import boto3
import re
from collections import Counter

arr = []
def lambda_handler(event, context):
    
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
    # bucket = event['Records'][0]['s3']['bucket']['name']
    # key = event['Records'][0]['s3']['object']['key']
    # print(bucket)
    # print(key)
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket
    s3 = boto3.resource('s3')
    s3_object = s3.Bucket('testingskipq').Object('test.txt').get()
    text = s3_object['Body'].read()
    ntext = text.decode()
    print(ntext)
    
    # https://www.techiedelight.com/remove-non-alphanumeric-characters-string-python/
    s = re.sub(r'\W+', ' ', ntext)
    print(s)    # WelcomeUser_12
    s2 = s.split()
    s4 = Counter(s2)
    print(s4)
    for k,v in s4.items():
        arr.append([k,v])
    print(arr)
    
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
                    "Data": str(arr),
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Test Email",
            },
        },
        Source="ali.saeed.sirius@gmail.com",
    )

   
   
    # TODO implement
    # get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))

    # s3 = boto3.client('s3')
    # objs = s3.list_objects_v2(Bucket='testingskipq')['Contents']
    # # for key in s3.list_objects(Bucket='testingskipq')['Contents']:
    # #     print(key['Key'])
    # last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][0]
    # print(objs)
    # print(last_added)
    # https://binaryguy.tech/aws/s3/quickest-ways-to-list-files-in-s3-bucket/
    # s3_client = boto3.client("s3")
    # bucket_name = "testingskipq"
    # response = s3_client.list_objects_v2(Bucket=bucket_name)
    # files = response.get("Contents")
    # for file in files:
    #     print(f"file_name: {file['Key']}, last_added: {file['LastModified']}")
    # sorted_lst = sorted(files,key=itemgetter('LastModified'),reverse = True)
    # print(sorted_lst)
    # latestFile = sorted_lst[0]["Key"]
    # print(latestFile)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
