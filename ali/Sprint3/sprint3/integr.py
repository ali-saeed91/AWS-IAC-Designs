import boto3
from sprint3_stack import Sprint3Stack

# https://dynobase.dev/dynamodb-python-with-boto3/
def lambda_handler():
    try:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-2")

        table = dynamodb.Table('Beta-AliStage-AlarmTable68A95781-IG2TVJPZNEV5')
        response = table.scan()
        data = response['Items'] 

        print(response)
        print(data)
        return data
    except Exception as err:
        print('An Error occured :', err)
        raise
lambda_handler()  