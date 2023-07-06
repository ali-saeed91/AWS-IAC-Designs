import os   
import json
import boto3
from operator import itemgetter

""" Get API Table from env Variable """
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
dynamodb=boto3.resource('dynamodb',region_name='us-east-2')
table_name = os.environ['ARGTable']
table = dynamodb.Table(table_name)

new_list = []
arr = []
out = []

def lambda_handler(event, context):

    """ Executing functions to fetch DynamoDB Data """
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
    response = table.scan()
    data=response["Items"]
    
    """ Parsing the DynamoDB Data"""
    # https://www.pythonpool.com/dictionary-to-list-python/
    for i in range(len(data)):
        val = data[i]
        new_list = list(val.values())
        arr.append(new_list)
    
    """ Sorting 2D Array """    
    # https://www.delftstack.com/howto/python/sort-2d-array-python/    
    sorted_lst = sorted(arr,key=itemgetter(2),reverse = True)
    
    """ Fetching Latest 10 Records """
    slength = len(sorted_lst)
    if slength > 10:
        res = (sorted_lst[:10])
    else:
        res = sorted_lst
        
    """ Printing Values wrt Timestamp"""
    # https://bobbyhadz.com/blog/python-print-list-in-columns#
    headers = ['Values','Timestamps']
    print(f' {headers[0]: <10}   {headers[1]: <15}\n-------------------------------------------')
    for row in res:
        print(f'| {row[4]: <10} | {row[2]: <15} |\n-------------------------------------------')
    
    
        
    return {
        'statusCode': 200,
        'body': json.dumps('Success! Records Found!')
    }