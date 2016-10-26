#This script is to pull the stations from Septa's website
#It will first pull the station names and URLs and put them in a dictionary
#Using the URLs the Lat/Long can be scraped

import urllib2
import requests
from bs4 import BeautifulSoup

url = 'http://www.septa.org/maps/transit/mfl.html'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html5lib')
soup.prettify()

front = 'www.septa.org'
for anchor in soup.findAll('area', href=True):
    x = anchor['href']
    print x
    y = x[11:]
    print y
    z = front + y
    print z
    
