#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#coding=utf-8
import urllib2
import urllib
import re
import threading
from time import ctime
rlock = threading.RLock()
#myproxy代理地址
# i线程id
def vote(myproxy,i):
    try:
        print "voting...%d..." % i
        #采用代理ip发送数据
        proxy_support = urllib2.ProxyHandler(myproxy)
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        sendt = '投票'.decode('utf-8').encode('gb2312')
        #发送数据目标地址
        url = 'http://cffan9.v.vote8.cn/m/Shortcut/5630538'
        # url = 'http://www.baidu.com'
        #post数据
        values = {}
        req = urllib2.Request(url,urllib.urlencode(values))
        response = opener.open(req)
        html = response.read()
        print(html)
        #print html
        if html.find('投票人数过多'.decode('utf-8').encode('gb2312')):
            print "VOTE %d Faild Plase wait a minute" % i
            return False
        else:
            print "VOTE %d Success" % i
            return
    except Exception:
        print " Error The %d proxy cann't do anything" % i
        return False

if __name__ == "__main__":
    #读取ip.txt文件 ip格式：1.179.128.2:8080@HTTP#泰国
    ipFile = open('ip.txt')
    ipList = ipFile.readlines()
    ipFile.close()

    length = range(len(ipList))
    #print length
    threads = []
    for i in length:
        ipLine = ipList[i]
        stringList = ipLine.split('@')
        ip=stringList[0]
        myproxy = {'http': ip}
        #print myproxy
        t = threading.Thread(target=vote,args=(myproxy,i))
        threads.append(t)
    for i in length:
        threads[i].start()

    for i in length:
        threads[i].join()

    print "all done at", ctime()



