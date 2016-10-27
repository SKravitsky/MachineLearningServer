#This script is to pull the stations from Septa's website
#It will first pull the station names and URLs and put them in a dictionary
#Using the URLs the Lat/Long can be scraped

import re
import urllib2
import json
import datetime
import os
from bs4 import BeautifulSoup

today = datetime.date.today().strftime("%m%d%Y")
StationJSON = "Station-" + today + ".json"
LocationJSON = "Location-" + today + ".json"
FileLocation = "./"

def CheckJSON(jsonfile):
    if os.path.isfile(FileLocation + jsonfile):
        return True
    else:
        print "The file does not exist"
        print "Creating file %s" % (jsonfile)
        f = file(jsonfile, "w+")
        f.close()
        return False

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

    StationCheck = CheckJSON(StationJSON)
    LocationCheck = CheckJSON(LocationJSON)
    
    if StationCheck:
        with open(StationJSON, 'r') as readfile:
            StationDict = json.load(readfile)
    else:
        StationDict = ParseLinks(url,front)
        with open(StationJSON, 'w') as outfile:
            json.dump(StationDict, outfile)
    
#    if LocationCheck:
#        print "True"
#    else:
#        LocationDict = ParseLocation(StationDict) 
