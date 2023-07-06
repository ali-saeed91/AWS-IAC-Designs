import urllib3
import datetime

url = 'skip.org'

def lambda_handler(url):
   try:  
        """ Executing function to fetch website active status and latency """
        values = dict()
        availability = getAvail(url)
        latency = getLatency(url)
        values.update({"availability of " + str(url): availability,"latency of " + str(url): latency})
        print(" Functional Test Passed : ",values)           
        return values
   except Exception as err:
    print('An Error occured :', err)
    raise

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

lambda_handler(url)