#!/usr/bin/python

import httplib,sys,re,string
import io
import json


def test(a):
    
    host="dd.woniu.com"
    conn = httplib.HTTPConnection(host)
    
    #1.jump
    #headers = {"Referer": "http://u2.6dad.com/iclk/?s=NTAzNDUxfGh0dHA6Ly93d3cucmVueHguY29tL3BpYy94aW5nYWl6aXNoaS8yMDEwLTExLTEwLzM5MTlfMTQuaHRtbHxodHRwOi8vd3d3LnJlbnh4LmNvbS9waWMveGluZ2FpemlzaGkvMjAxMC0xMS0xMC8zOTE5XzEzLmh0bWx8MTQ0MHg5MDB4MzJ8OHwxfDExLjEuMTAyfDE5fDM2fDE0fDI0MjJ8MTMzMjQ3NTc4NHwxMTEuMTY1LjEzNi4yNTB8MzIzfGNwbXw5fDUzNDh8Njg0fDQzNDk3fDU3OTI=;74721ce836b5935a390692112e20c540;http%3A%2F%2Fdd.woniu.com%2Ft.do%3Fwd%3D12-03-23-LY-LJ-LDLM-2%26sd%3D%7Buid%7D%26r%3Dhttp%253A%252F%252Fly.gg.woniu.com%252Flj%252F201203%252F0017.html"}
    headers = {}
    conn.request("GET","/_tdata.gif?MB-14-05-19-YD-RMJF-LIMEIIOS-1|-|-|29|512F6E59-2B95-4F53-9C7C-868E43136A25",'',headers)
     
    conn.close()
    
    return a

from multiprocessing import Pool
from datetime import datetime,timedelta

if __name__ == '__main__':

# time =100;
# pool = Pool(processes=10)
# start = datetime.now()
# print "start time:%s,run times:%s seconds" % (start,time)
#
# tt = start + timedelta(seconds=time)
# i=0
# while datetime.now()<tt:
#     pool.map(test, range(399))
#     print "no %s (100)" % (i,)
#     i=i+1;
# end=datetime.now()
# print "total request:%s,cost:%s" % (i*100,end-start)
    i=0
    for line in io.open( "d:/log/registration_log_2014060911.log", encoding='utf-8'):
        if (line.find("'gameid': '1'")>0):
            i += 1;
        print(line)
    print(i)
        # print(json.loads(line));

