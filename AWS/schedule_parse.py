#!/usr/bin/env python

import bs4 as bs
import HTMLParser
import csv
import os.path
import time
from collections import OrderedDict
from urllib2 import Request, urlopen, URLError

dict = {}
dict_list = {}
lines = {
    'mfl_69_w' : "http://www.septa.org/schedules/transit/w/MFL_1.htm",
    'mfl_69_sat' : "http://www.septa.org/schedules/transit/s/MFL_1.htm",
    'mfl_69_sun' : "http://www.septa.org/schedules/transit/h/MFL_1.htm",
    'mfl_f_w' : "http://www.septa.org/schedules/transit/w/MFL_0.htm",
    'mfl_f_sat' : "http://www.septa.org/schedules/transit/s/MFL_0.htm",
    'mfl_f_sun' : "http://www.septa.org/schedules/transit/h/MFL_0.htm",
    'bsl_fern_w' : "http://www.septa.org/schedules/transit/w/BSL_1.htm",
    'bsl_fern_sat' : "http://www.septa.org/schedules/transit/s/BSL_1.htm",
    'bsl_fern_sun' : "http://www.septa.org/schedules/transit/h/BSL_1.htm",
    'bsl_att_w' : "http://www.septa.org/schedules/transit/w/BSL_0.htm",
    'bsl_att_sat' : "http://www.septa.org/schedules/transit/s/BSL_0.htm",
    'bsl_att_sun' : "http://www.septa.org/schedules/transit/h/BSL_0.htm",
    }

'''
#If we want to use an API
def schedule_Picker(line):
    return{
        'mfl_69_w' : "http://www.septa.org/schedules/transit/w/MFL_1.htm",
        'mfl_69_sat' : "http://www.septa.org/schedules/transit/s/MFL_1.htm",
        'mfl_69_sun' : "http://www.septa.org/schedules/transit/h/MFL_1.htm",
        'mfl_f_w' : "http://www.septa.org/schedules/transit/w/MFL_0.htm",
        'mfl_f_sat' : "http://www.septa.org/schedules/transit/s/MFL_0.htm",
        'mfl_f_sun' : "http://www.septa.org/schedules/transit/h/MFL_0.htm",
        'bsl_fern_w' : "http://www.septa.org/schedules/transit/w/BSL_1.htm",
        'bsl_fern_sat' : "http://www.septa.org/schedules/transit/s/BSL_1.htm",
        'bsl_fern_sun' : "http://www.septa.org/schedules/transit/h/BSL_1.htm",
        'bsl_att_w' : "http://www.septa.org/schedules/transit/w/BSL_0.htm",
        'bsl_att_sat' : "http://www.septa.org/schedules/transit/s/BSL_0.htm",
        'bsl_att_sun' : "http://www.septa.org/schedules/transit/h/BSL_0.htm",
    }.get(line,'error')
'''

def csv_Check(line_name, date):
    csv_name = line_name + date
    if os.path.isfile(csv_name):
        return True
    else:
        return False


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
    temp = []
    table = soup.find('table', id="timeTable")
    
    for rows in table.findAll('th'):
        name = rows.text
        data = name.split("StopID:")
        if data[0] == 'AT&T;':
            data[0] = 'AT&T'
        temp.append(data[0])
        dict[data[1]] = data[0]

    list_half = temp[:len(temp)/2]
    return list_half


def csv_Writing(key_name, file_ending, new_dict):
    csv_file_name = key_name + file_ending
    with open(csv_file_name, 'wb') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(new_dict.keys())
        writer.writerows(zip(*new_dict.values()))


def dict_Sort(old_dict, list_half):
    sorted_dict = OrderedDict()
    for item in list_half:
        sorted_dict[item] = old_dict[item]

    return sorted_dict


def get_Time_Station(soup, list_half, file_ending, key_name):
    for key, value in dict.iteritems():
        value2 = value.decode('utf-8')
        dict_list['%s' % value2] = []
    
    for key, value in dict.iteritems():
        time = soup.find('td', title=value)        
        for tags in time.findAll('td'):
            #print(tags.string)
            temp = tags.string.replace(u'\xa0','')
            temp2 = temp.replace(u'\u2014', '-')
            dict_list['%s' % value].append(temp2)

    new_dict = dict_Sort(dict_list, list_half)
    csv_Writing(key_name, file_ending, new_dict)
    
        
def main():
    current_time = time.strftime("%m_%Y")
    file_ending = "_" + current_time + ".csv"


    for key, value in lines.iteritems():
        if csv_Check(key, file_ending):
            print(key + file_ending + " already exists")
        else:
            main_source = source(value)
            soup = soupify(main_source)
            list_half = get_ID_Station(soup)
            get_Time_Station(soup, list_half, file_ending, key)
            print("Finished " + key + "_" + file_ending)
            dict_list.clear()
            dict.clear()



def lambda_handler(event, context):
    print event
    main()


if __name__ == "__main__":
    main()
