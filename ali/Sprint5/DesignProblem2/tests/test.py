import boto3
import os
import json
import datetime
import cmd

# Beta-AliStage-AlarmTable68A95781-AFE7FIHN9S4A
# dynamodb=boto3.resource('dynamodb',region_name='us-east-2')
# # table_name = os.environ['URLTable']
# table = dynamodb.Table('')
# URL=[]
# response = table.scan()
# lists=response["Items"]
# for l in lists:
#     # print(l['URL'])
#     URL.append(l['url'])
# print(URL)
# event = {
#   "body": "www.netflix.com",
#   "resource": "/{proxy+}",
#   "path": "/path/to/resource",
#   "httpMethod": "POST",
#   "isBase64Encoded": True,
#   "queryStringParameters": {
#     "foo": "bar"
#   },
#   "multiValueQueryStringParameters": {
#     "foo": [
#       "bar"
#     ]
#   },
#   "pathParameters": {
#     "proxy": "/path/to/resource"
#   },
#   "stageVariables": {
#     "baz": "qux"
#   },
#   "headers": {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch",
#     "Accept-Language": "en-US,en;q=0.8",
#     "Cache-Control": "max-age=0",
#     "CloudFront-Forwarded-Proto": "https",
#     "CloudFront-Is-Desktop-Viewer": "true",
#     "CloudFront-Is-Mobile-Viewer": "false",
#     "CloudFront-Is-SmartTV-Viewer": "false",
#     "CloudFront-Is-Tablet-Viewer": "false",
#     "CloudFront-Viewer-Country": "US",
#     "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Custom User Agent String",
#     "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
#     "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
#     "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
#     "X-Forwarded-Port": "443",
#     "X-Forwarded-Proto": "https"
#   },
#   "multiValueHeaders": {
#     "Accept": [
#       "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
#     ],
#     "Accept-Encoding": [
#       "gzip, deflate, sdch"
#     ],
#     "Accept-Language": [
#       "en-US,en;q=0.8"
#     ],
#     "Cache-Control": [
#       "max-age=0"
#     ],
#     "CloudFront-Forwarded-Proto": [
#       "https"
#     ],
#     "CloudFront-Is-Desktop-Viewer": [
#       "true"
#     ],
#     "CloudFront-Is-Mobile-Viewer": [
#       "false"
#     ],
#     "CloudFront-Is-SmartTV-Viewer": [
#       "false"
#     ],
#     "CloudFront-Is-Tablet-Viewer": [
#       "false"
#     ],
#     "CloudFront-Viewer-Country": [
#       "US"
#     ],
#     "Host": [
#       "0123456789.execute-api.us-east-1.amazonaws.com"
#     ],
#     "Upgrade-Insecure-Requests": [
#       "1"
#     ],
#     "User-Agent": [
#       "Custom User Agent String"
#     ],
#     "Via": [
#       "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)"
#     ],
#     "X-Amz-Cf-Id": [
#       "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=="
#     ],
#     "X-Forwarded-For": [
#       "127.0.0.1, 127.0.0.2"
#     ],
#     "X-Forwarded-Port": [
#       "443"
#     ],
#     "X-Forwarded-Proto": [
#       "https"
#     ]
#   },
#   "requestContext": {
#     "accountId": "123456789012",
#     "resourceId": "123456",
#     "stage": "prod",
#     "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
#     "requestTime": "09/Apr/2015:12:34:56 +0000",
#     "requestTimeEpoch": 1428582896000,
#     "identity": {
#       "cognitoIdentityPoolId": None,
#       "accountId": None,
#       "cognitoIdentityId": None,
#       "caller": None,
#       "accessKey": None,
#       "sourceIp": "127.0.0.1",
#       "cognitoAuthenticationType":None,
#       "cognitoAuthenticationProvider": None,
#       "userArn": None,
#       "userAgent": "Custom User Agent String",
#       "user": None
#     },
#     "path": "/prod/path/to/resource",
#     "resourcePath": "/{proxy+}",
#     "httpMethod": "POST",
#     "apiId": "1234567890",
#     "protocol": "HTTP/1.1"
#   }
# }
# print(event["requestContext"]["requestTime"])
# print(event["requestContext"]["apiId"])

# value = 10
# body = "[{'event1':{'attr1': 10 }}]"

# new = json.loads(body)
# # my = json.loads(body)
# # print(my)
# print(type(new))
# print(type(body))
# headers = [
#     'Values',
#     'Timestamps'
# ]
# arr = [["2","2022-12-07 12:08:00.430830"],["4","2022-12-07 12:08:40.081462"],["1","2022-12-07 12:09:41.928191"],
#        ["3","2022-12-07 12:09:55.149604"],["20","2022-12-07 12:10:17.862442"],["11","2022-12-07 12:10:56.117012"],
#        ["22","2022-12-07 12:11:13.673344"],["13","2022-12-07 12:11:27.512491"],["17","2022-12-07 12:11:49.034601"],
#        ["15","2022-12-07 12:12:10.153498"],["10","2022-12-07 12:09:00.583342"],["6","2022-12-07 12:09:12.701267"]]
# # for i in arr:
# print(f' {headers[0]: <10}   {headers[1]: <15}\n-------------------------------------------')
# # print("________________________________________")    
# for row in arr:
#     print(f'| {row[0]: <10} | {row[1]: <15} |\n-------------------------------------------')
    # print("|"," "," ","Value :",i[0]," "," "," ","|--------------|"," "," "," ","Timestamp :",i[1]," "," ","|")
    # print(*arr, sep = "\n")
# start = datetime.datetime.now()
# print(start)
# # val = my[0]["event1"]["attr1"]
# # print(val)
# arr.sort(reverse=True)
# print(arr)
# import json
# import boto3
# from operator import itemgetter
# from pprint import pprint

# dynamodb=boto3.resource('dynamodb',region_name='us-east-2')
# table = dynamodb.Table("testing")
# new_list = []
# arr = []
# out = []
# # api
# def lambda_handler(event, context):
#     # TODo implement
#     response = table.scan()
#     data=response["Items"]
#     # print(data)
#     # print(len(data))
#     # print(type(data))
#     # print((data[0]))
#     # print(data[-1])
#     # print(type(data[0]))
#     # for key, value in data.iteritems():
#     #     temp = [key,value]
#     #     arr.append(temp)
#     # for k,v in data.items():
#     #     arr.append(list(k,v))
#     # print(arr)
#     for i in range(len(data)):
#         val = data[i]
#         # new_list = zip(val.keys(), val.values()) 
#         new_list = list(val.values())
#         arr.append(new_list)
    
     
#     print(new_list)
#     print(arr)
#     sorted_lst = sorted(arr,key=itemgetter(1),reverse = True)
#     pprint(sorted_lst)
    
#     res = (sorted_lst[:10])
#     for i in res:
#         print("Value :",i[0]," ","Timestamp :",i[1])
    
        
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }
body = "{'event1':{'attr1': 10 }}"
my = json.loads(body)
print(my)
val = my[0]
print(val)