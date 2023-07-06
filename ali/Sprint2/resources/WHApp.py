import urllib3
import datetime
from cloudwatch_putData import AWSCloudWatch
import constants as constants

def lambda_handler(event, context):
    
    """ CloudWatch Object """
    cloudwatch_object = AWSCloudWatch()
    
    """ Executing functions to fetch website active status and latency """
    values = dict()
    for i in range(len(constants.URL)):
        
        availability = getAvail(constants.URL[i])
        latency = getLatency(constants.URL[i])
        values.update({"availability of " + str(constants.URL[i]): availability,"latency of " + str(constants.URL[i]): latency})

        """ Sending data to CloudWatch """   
        dimensions = [{ 'Name': 'URL', 'Value': constants.URL[i]}]
        cloudwatch_object.cloudwatch_metric_data(constants.nameSpace, constants.AvailabilityMetric, dimensions, availability )
        cloudwatch_object.cloudwatch_metric_data(constants.nameSpace, constants.LatencyMetric, dimensions, latency )
            
    return values

def getAvail(url):
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    if response.status == 200:
        return 1.0
    else:
        return 0.0

def getLatency(url):
    http = urllib3.PoolManager()
    start = datetime.datetime.now()
    response = http.request("GET", url)
    end = datetime.datetime.now()
    delta = end - start             # Take time difference
    latencySec = round(delta.microseconds * .000001, 6)
    return latencySec