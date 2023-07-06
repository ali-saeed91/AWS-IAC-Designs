from aws_cdk import (
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as target_,
    Duration,
    Stack,
    RemovalPolicy,
    aws_cloudwatch as cw_,
    aws_iam as iam_,
    aws_sns as sns_,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as cw_actions,
    aws_dynamodb as db_,
    aws_codedeploy as cd_,
    aws_apigateway as ag_,
    CfnOutput as co_,
)
from constructs import Construct
# from resources import constants as constants

class DesignProblem2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        """ Creating the lambda role and functions to deploy WHApp.py and ApiApp.py """
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_lambda/README.html
        lambda_role = self.create_lambda_role()
        fn = self.create_lambda("WHLambda",'./resources','WHApp.lambda_handler',lambda_role)
        fn.apply_removal_policy(RemovalPolicy.DESTROY)
       
        apiLambda = self.create_lambda("ApiLambda",'./resources','ApiApp.lambda_handler',lambda_role)
        apiLambda.apply_removal_policy(RemovalPolicy.DESTROY)
              
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_dynamodb/README.html
        """ Creating ARG1 table """
        urlTable = self.create_urldynamoDB_table()
        urlTable.grant_full_access(apiLambda)
        apiLambda.add_environment('ARGTable',urlTable.table_name)
        
        
        """ Adding to WH Lambda Environment for Access to ARG Table """
        # fn.add_environment('topicname',topic.topic_name)
        fn.add_environment('ARGTable',urlTable.table_name)
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_apigateway/README.html
        """ Creating API Gateway """
        api1 = ag_.LambdaRestApi(self, "ALIAPI1",
                                handler= apiLambda,
                                rest_api_name= "ALIGateway_1", 
                                proxy=False
                                ) 
        items = api1.root.add_resource("CRUD1")
        items.add_method("POST")
        items.add_method("DELETE")
        
        """ Creating API Gateway 2 """
        api2 = ag_.LambdaRestApi(self, "ALIAPI2",
                                handler= apiLambda,
                                rest_api_name= "ALIGateway_2",
                                proxy=False
                                ) 
        item = api2.root.add_resource("CRUD2")
        item.add_method("POST")
        item.add_method("DELETE")
        
              
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
    
    def create_urldynamoDB_table(self):
        table = db_.Table(self, "ARGTable",
            partition_key = db_.Attribute(name="id", type=db_.AttributeType.STRING),
            removal_policy = RemovalPolicy.DESTROY,
            sort_key = db_.Attribute(name="Timestamp",type=db_.AttributeType.STRING),
    )
        return table