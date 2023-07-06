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
)
from constructs import Construct
from resources import constants as constants

class Sprint3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        """ Creating the lambda role and functions to deploy WHApp.py and DBApp.py """
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_lambda/README.html
        lambda_role = self.create_lambda_role()
        fn = self.create_lambda("WHLambda",'./resources','WHApp.lambda_handler',lambda_role)
        fn.apply_removal_policy(RemovalPolicy.DESTROY)
        dbLambda = self.create_lambda("DBLambda",'./resources','DBApp.lambda_handler',lambda_role)
        
        # Obtain AWS Lambda Metrics
        """  
            For the Lambda two metrics are created Duration and Invocation.
            For each of these metrics alarms are created
        """
        # Duration Metric
        duration_metric = fn.metric_duration()
        duration_alarm = cw_.Alarm(self, "Duration_Alarm:",
                metric=duration_metric,
                evaluation_periods=60,
                threshold=20000,
                comparison_operator=cw_.ComparisonOperator.GREATER_THAN_THRESHOLD 
            )
        
        # Invocation Metric
        invocation_metric = fn.metric_invocations()
        invocation_alarm = cw_.Alarm(self, "Invocation_Alarm:",
                metric=invocation_metric,
                evaluation_periods=60,
                threshold=2,
                comparison_operator=cw_.ComparisonOperator.GREATER_THAN_THRESHOLD 
            )
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda/Alias.html
        # Used to make sure each CDK synthesis produces a different Version
        version = fn.current_version
        alias = lambda_.Alias(self, "lambdaAlias",
            alias_name="Prod",
            version=version
            )
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_codedeploy/LambdaDeploymentGroup.html
        deployment_group = cd_.LambdaDeploymentGroup(self, "BlueGreenDeployment",
            # application=application,
            alias=alias,
            alarms= [duration_alarm, invocation_alarm],
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_codedeploy/LambdaDeploymentConfig.html
        # """ Auto Roll Back by Default Policy"""
            deployment_config=cd_.LambdaDeploymentConfig.LINEAR_10_PERCENT_EVERY_1_MINUTE
        )
        """ Creating CRON job """
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_events/Schedule.html
        schedule=events_.Schedule.rate(Duration.minutes(60))
        
        # defining target of the event
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_events_targets/LambdaFunction.html
        target = target_.LambdaFunction(handler=fn)
        
        # defining a rule to convert my lambda into a cronjob by binding event and target
        rule = events_.Rule(self, "WHAppRule",
            description = "rule to generate auto events for lambda function",
            schedule = schedule,
            targets = [target] 
            )
        rule.apply_removal_policy(RemovalPolicy.DESTROY)
        
        """ Creating a SNS Topic and Subscription """
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_sns/Topic.html
        topic = sns_.Topic(self, "WHNotifications")
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_sns_subscriptions/EmailSubscription.html
        topic.add_subscription(subscriptions_.EmailSubscription('ali.saeed.sirius@gmail.com'))
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_sns_subscriptions/LambdaSubscription.html
        topic.add_subscription(subscriptions_.LambdaSubscription(dbLambda))
    
        """  
            For the website two metrics are created availability and latency.
            For each of these metrics alarms are created
        """
        for u in constants.URL:
            dimensions = {'URL': u}
            availability_metric = cw_.Metric(
                metric_name = constants.AvailabilityMetric,
                namespace = constants.nameSpace,
                dimensions_map = dimensions
            )
            availability_alarm = cw_.Alarm(self, "Errors_Avail: " + str(u),
                metric=availability_metric,
                evaluation_periods=60,
                threshold=1,
                comparison_operator=cw_.ComparisonOperator.LESS_THAN_THRESHOLD 
            )
            # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch_actions/SnsAction.html
            availability_alarm.add_alarm_action(cw_actions.SnsAction(topic))
            
            latency_metric = cw_.Metric(
                metric_name = constants.LatencyMetric,
                namespace = constants.nameSpace,
                dimensions_map = dimensions
            )
            latency_alarm = cw_.Alarm(self, "Errors_Latency: " + str(u),
                metric=latency_metric,
                evaluation_periods=60,
                threshold=0.6,
                comparison_operator=cw_.ComparisonOperator.GREATER_THAN_THRESHOLD 
            )
            # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch_actions/SnsAction.html
            latency_alarm.add_alarm_action(cw_actions.SnsAction(topic))
            
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_dynamodb/README.html
        """ Creating DB table """
        dbTable = self.create_dynamoDB_table()
        dbTable.grant_full_access(dbLambda)
        dbLambda.add_environment('Table_Name',dbTable.table_name)       
                   
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
            timeout=Duration.minutes(1)
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
                            iam_.ManagedPolicy.from_aws_managed_policy_name('AmazonDynamoDBFullAccess')       
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
        table = db_.Table(self, "AlarmTable",
            partition_key = db_.Attribute(name="id", type=db_.AttributeType.STRING),
            removal_policy = RemovalPolicy.DESTROY,
            sort_key = db_.Attribute(name="Timestamp",type=db_.AttributeType.STRING),
    )
        return table