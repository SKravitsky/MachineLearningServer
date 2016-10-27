#This script is to pull the stations from Septa's website
#It will first pull the station names and URLs and put them in a dictionary
#Using the URLs the Lat/Long can be scraped

import urllib2
import requests
from bs4 import BeautifulSoup

def ParseLinks(url, website):
    try:
        page = None
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html5lib')
    finally:
        if page:
            page.close()
    StationDict = SoupLinks(soup)
    return StationDict

def SoupLinks(soup):
    soup.prettify()
    StationDict = {}
    for anchor in soup.findAll('area', href=True):
        x = anchor['href']
        y = x[11:]
        temp = y[25:]
        StationName = temp[:-5]
        if y[1:2] == 't':
            pass
        else:
            FullURL = front + y
        StationDict[FullURL] = StationName
        print FullURL
        print StationName
    print StationDict
    return StationDict

if __name__ == "__main__":
    url = 'http://www.septa.org/maps/transit/mfl.html'
    front = 'www.septa.org'
    StationDict = ParseLinks(url,front)
    print StationDict
