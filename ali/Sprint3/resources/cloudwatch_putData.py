import boto3

class AWSCloudWatch:
    
    def __init__(self):
        self.client = boto3.client('cloudwatch')
    
    # https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
    def cloudwatch_metric_data(self, namespace, metric_name, dimensions, value):
        
        """CloudWatch Data Template"""
        response = self.client.put_metric_data(
            Namespace= namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': dimensions,
                    'Value': value,
                },
            ]
        )