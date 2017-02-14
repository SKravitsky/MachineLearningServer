import json
import re
import string
from urllib2 import Request, urlopen, URLError
from pprint import pprint

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    clean_text = re.sub(cleanr, '', raw_html)
    tabless_text = re.sub(r"\t+", "", clean_text)    
    return tabless_text

def json_formatting(data):
    output = json.loads(data)
    node = output[0]['advisory_message']
    return node

def request_status(request):
    try:
        response = urlopen(request)
        test = response.read()
    except URLError, e:
        print "Didn't work, got error:",e
    return test

def station_picker(station):
    if station == 'mfl':
        request = Request('http://www3.septa.org/hackathon/Alerts/get_alert_data.php?req1=rr_route_mfl')
    elif station == 'bsl':
        request = Request('http://www3.septa.org/hackathon/Alerts/get_alert_data.php?req1=rr_route_bsl')
    else:
        print 'Please enter a valid station, either mfl or bsl'
    output = request_status(request)
    return output

def start_function(station):
    request_output = station_picker(station)
    json_output = json_formatting(request_output)
    cleaned_output = clean_html(json_output)
    print cleaned_output

def lambda_handler(event, context):
    print event
    start_function(event) 
        
