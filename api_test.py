import json
import re
import string
from urllib2 import Request, urlopen, URLError
from pprint import pprint

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def request_status(request):
	try:
		response = urlopen(request)
		test = response.read()
	except URLError, e:
		print "Didn't work, got error:",e

	return test

if __name__ == "__main__":
	request = Request('http://www3.septa.org/hackathon/Alerts/get_alert_data.php?req1=rr_route_mfl')
	output = request_status(request)
	
	out = json.loads(output)
	node = out[0]['advisory_message']

	x = cleanhtml(node)
	y = re.sub(r"\t+", "", x)
	print y
