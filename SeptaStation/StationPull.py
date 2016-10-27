#This script is to pull the stations from Septa's website
#It will first pull the station names and URLs and put them in a dictionary
#Using the URLs the Lat/Long can be scraped

import re
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
        link = anchor['href']
        fixedlink = link[11:]
        if fixedlink[1:2] == 't':
            pass
        else:
            StationName = fixedlink[25:-5]
            FullURL = front + fixedlink
            StationDict[FullURL] = StationName
    return StationDict

def ParseLocation(StationDict):
    LocationDict = {}
    for key, value in StationDict.iteritems():
        LatLong = ParseStations(key, value)
        LocationDict[value] = LatLong
    return LocationDict

def ParseStations(url, station):
    try:
        page = None
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html5lib')
    finally:
        if page:
            page.close()

    LatLong = SoupStations(soup)
    return LatLong

def SoupStations(soup):
    soup.prettify()    
    header = str(soup.head)
    paragraph = header[2000:]
    
    regex = re.search('(?<=LatLng)(.*)',paragraph)
    
    line = regex.group(1)
    longlist = line.split('LatLng')
    notlatlng = longlist[1]
    latlnglist = notlatlng[1:-2]
    LatLong = latlnglist.split(',')

    return LatLong

        

if __name__ == "__main__":
    url = 'http://www.septa.org/maps/transit/mfl.html'
    front = 'http://www.septa.org'
    StationDict = ParseLinks(url,front)
    LocationDict = ParseLocation(StationDict)
    print LocationDict
##    print StationDict        
