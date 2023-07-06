import boto3

# https://dynobase.dev/dynamodb-python-with-boto3/
def lambda_handler():
    try:
        """ Executing Integration Test to check DynamoDB Table integration with Alarm data from Lambda """
        dynamodb = boto3.resource('dynamodb', region_name="us-east-2")

        table = dynamodb.Table('Beta-AliStage-URLTable1792207E-1D7O8XF0GPM8')
        response = table.scan()
        data = response['Items'] 
        
        print(response)
        # print(data)
        return data
    except Exception as err:
        print('An Error occured :', err)
        raise
lambda_handler()  