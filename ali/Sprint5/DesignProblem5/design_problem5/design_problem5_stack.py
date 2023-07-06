from aws_cdk import (
    aws_lambda as lambda_,
    Duration,
    Stack,
    RemovalPolicy,
    aws_cloudwatch as cw_,
    aws_iam as iam_,
    aws_dynamodb as db_,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
)
from constructs import Construct

class DesignProblem5Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        """ Creating the lambda role and functions to deploy FNApp.py """
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_lambda/README.html
        lambda_role = self.create_lambda_role()
        fn = self.create_lambda("FNLambda",'./resources','FNApp.lambda_handler',lambda_role)
        fn.apply_removal_policy(RemovalPolicy.DESTROY)
                     
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_dynamodb/README.html
        """ Creating DB table """
        dbTable = self.create_dynamoDB_table()
        dbTable.grant_full_access(fn)        
        
        """ Adding to FN Lambda Environment for Access to DB Table """
        fn.add_environment('DBTable',dbTable.table_name)
        
        """ Creating S3 Bucket for FNApp"""
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3/Bucket.html
        bucket = s3.Bucket(self, "AliSaeedBucket")
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(fn))
        bucket.apply_removal_policy(RemovalPolicy.DESTROY)
        
        """ Adding to FN Lambda Environment for Access to S3 Bucket """
        fn.add_environment('Buckets',bucket.bucket_name)      
        
    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda/README.html
    """ 
        Creates lambda function from the construct library.
        
        Parameters:
                assets (str) - Stack file path for the application to be deployed on lambda.
                handler (str) - Handler function to execute.
                role (str) - IAM role for lambda function.
        Return:
                Lambda fucntion
    
    """
    def create_lambda(self,id,asset, handler, role):
        return lambda_.Function(self,
            id = id,
            handler = handler,
            code=lambda_.Code.from_asset(asset),
            runtime=lambda_.Runtime.PYTHON_3_9,
            role = role,
            timeout=Duration.minutes(5)
        )
    
    # Cloudwatch Full Access
    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_iam/Role.html
    """ 
        Create role for IAM user
        
        Parameters:
                assumed by (IPrincipal) - The IAM Principal which can assume this role.
                managed_policies (IManagedPolicy) - A list of managed policies which are associated with this role.
        Return:
                Role Object
    
    """
    def create_lambda_role(self):
        lambdaRole = iam_.Role(self,"lambda-role",
        assumed_by = iam_.ServicePrincipal('lambda.amazonaws.com'),
        managed_policies = [
                            iam_.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess'),
                            iam_.ManagedPolicy.from_aws_managed_policy_name('AmazonDynamoDBFullAccess'),
                            iam_.ManagedPolicy.from_aws_managed_policy_name('AmazonS3FullAccess'),
                            iam_.ManagedPolicy.from_aws_managed_policy_name('AmazonSESFullAccess'),
        ])          
        return lambdaRole
    
    # DynamoDB Table 
    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_dynamodb/Table.html
    """ 
        Create DB Table
        
        Parameters:
                partition_key (Union[Attribute, Dict[str, Any]]) - Partition key attribute definition.
                sort_key (Union[Attribute, Dict[str, Any], None]) - Sort key attribute definition. Default: no sort key
        Return:
                DynamoDB Table
    
    """
    
    def create_dynamoDB_table(self):
        table = db_.Table(self, "WRDTable",
            partition_key = db_.Attribute(name="Word", type=db_.AttributeType.STRING),
            removal_policy = RemovalPolicy.DESTROY,
            sort_key = db_.Attribute(name="Frequency",type=db_.AttributeType.STRING),
    )
        return table