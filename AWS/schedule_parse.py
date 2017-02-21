#!/usr/bin/env python

import bs4 as bs
import HTMLParser
import csv
from urllib2 import Request, urlopen, URLError

dict = {}


def source(url_request):
    site = Request(url_request)
    
    try:
        source = urlopen(site).read()
    except URLError, e:
        print "Didn't work, got error:", e

    return(source)


def soupify(source):
    soup = bs.BeautifulSoup(source,'html.parser')
    return(soup)


def get_Times(soup):
    for tags in soup.find_all('td'):
        print(tags.string)


def get_ID_Station(soup):
    table = soup.find('table', id="timeTable")
    
    for rows in table.findAll('th'):
        name = rows.text
        data = name.split("StopID:")
        dict[data[1]] = data[0]


def csv_Writing(output):
    with open('test.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = '|')


def get_Time_Station(soup):
    for key, value in dict.iteritems():
        time = soup.find('td', title=value)
        for tags in time.findAll('td'):
            print(tags.string)
        

def main():
    website = 'http://www.septa.org/schedules/transit/w/MFL_1.htm'
    main_source = source(website)
    soup = soupify(main_source)
    get_ID_Station(soup)
    get_Time_Station(soup)
    for key,value in dict.iteritems():
        print key, value
        print "-----"


def lambda_handler(event, context):
    print event
    main()


if __name__ == "__main__":
    main()
