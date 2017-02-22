#!/usr/bin/env python

import bs4 as bs
import HTMLParser
import csv
from urllib2 import Request, urlopen, URLError

dict = {}
dict_list = {}

def schedule_Picker(line):
    return{
        'mfl_69_w' : "http://www.septa.org/schedules/transit/w/MFL_1.htm",
        'mfl_69_sat' : "http://www.septa.org/schedules/transit/s/MFL_1.htm",
        'mfl_69_sun' : "http://www.septa.org/schedules/transit/h/MFL_1.htm",
        'mfl_f_w' : "http://www.septa.org/schedules/transit/w/MFL_0.htm",
        'mfl_f_sat' : "http://www.septa.org/schedules/transit/s/MFL_0.htm",
        'mfl_f_sun' : "http://www.septa.org/schedules/transit/h/MFL_0.htm",
        }.get(line,'error')


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
        value2 = value.decode('utf-8')
        dict_list['%s_list' % value2] = []
    
    for key, value in dict.iteritems():
        time = soup.find('td', title=value)
        for tags in time.findAll('td'):
            #print(tags.string)
            temp = tags.string.replace(u'\xa0','')
            temp2 = temp.replace(u'\u2014', '-')
            dict_list['%s_list' % value].append(temp2)
    
    with open('test.csv', 'wb') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(dict_list.keys())
        writer.writerows(zip(*dict_list.values()))
    
        

def main():
    website = schedule_Picker('mfl_f_w')
    main_source = source(website)
    soup = soupify(main_source)
    get_ID_Station(soup)
    get_Time_Station(soup)

def lambda_handler(event, context):
    print event
    main()


if __name__ == "__main__":
    main()
