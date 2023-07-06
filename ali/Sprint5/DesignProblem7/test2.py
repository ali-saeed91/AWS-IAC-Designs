from pprint import pprint
import boto3
import constants


# session = boto3.Session()

s3_client = boto3.client('s3',
                    aws_access_key_id=constants.access_key,
                    aws_secret_access_key=constants.secret_access_key
                    ,region_name ='us-east-1')

s3_bucket_name = 'testingskipq2'
object_name = 'pattern.rar'


# def create_bucket():
#     response = s3_client.create_bucket(Bucket=s3_bucket_name)
#     pprint(response)


response = s3_client.generate_presigned_post(
    s3_bucket_name,
    object_name,
    ExpiresIn=3600
)
pprint(response)
    
    
    # def file_download():
    #     response = s3_client.generate_presigned_url(
    #         'get_object',
    #         Params={
    #             'Bucket': s3_bucket_name,
    #             'Key': object_name
    #         },
    #         ExpiresIn=3600
    #     )
    
    #     pprint(response)
    
    
    # create_bucket()
    # file_upload()
    # file_download()