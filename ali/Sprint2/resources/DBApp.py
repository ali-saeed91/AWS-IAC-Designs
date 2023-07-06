from dynamoDB_putData import DynamoDB

def lambda_handler(event, context):
    """ Extract Event Data for Table """
    message_id = event["Records"][0]["Sns"]["MessageId"]
    subject = event["Records"][0]["Sns"]["Subject"]
    timestamp = event["Records"][0]["Sns"]["Timestamp"]
    
    """ Creating object for inserting values in DynamoDb"""
    dynamoDb_obj = DynamoDB()
    dynamoDb_obj.put_Data(message_id, subject, timestamp)