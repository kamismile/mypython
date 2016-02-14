# -*- coding: utf-8 -*-

import os
import urllib
import urllib2
import string
import socks
import httplib2
import cookielib
import time
import random
tes='tesseract.exe'
filepath='./'
imgurl='http://example.com/vote/img.jsp'
myurl="http://example.com/vote"
voteInfoId='xxxxxxxx'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0'}#,
#         'Cookie':'324E661DE12427BD71CE63DF436A80D1'}
imgfile=filepath + '/img.jpg'
outfile=filepath + '/out'
proxy_file=filepath+'/proxy.txt'
user_file=filepath+'/user2.txt'
cookieFilename=filepath +'/cookies.txt'
#myproxy_line='211.142.236.137:80'
#cookieJarFileLWP=cookielib.LWPCookieJar(cookieFilename)
cookieFileJar=cookielib.FileCookieJar(cookieFilename)
#opener=urllib2.build_opener(urllib2.ProxyHandler({'http':myproxy_line}),urllib2.HTTPCookieProcessor(cookieMozillaJar))
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieFileJar))
f_user=open(user_file)

f_proxy=open(proxy_file)
proxy_all=f_proxy.read().split('\n')
f_user=open(user_file)
user_all=f_user.read().split('\n')
count=1
cookieFileJar=cookielib.FileCookieJar(cookieFilename)#使用cookie登陆

while True:
    i=random.randint(1,100)
    j=random.randint(1,60)
    #print user_all.length()    
    user_line=user_all[i]
    myproxy_line=proxy_all[j]

    for myproxy_line in [myproxy_line]:#f_proxy:

        #使用代理和cookie
        opener=urllib2.build_opener(urllib2.ProxyHandler({'http':myproxy_line}),urllib2.HTTPCookieProcessor(cookieFileJar))
        try:
            response2=opener.open(imgurl,timeout=1)#返回二进制图片
        except Exception,e:
            print 'I can not connect the server,try again'
            continue

        content=response2.read()
        fp=file(imgfile,'wb')#将二进制图片保存
        fp.write(content)
        fp.close()
        outcmd="%s %s %s -l eng digits -psm 7" %(tes,imgfile,outfile)
        print 'I begin to recognize the CAPTCHA code ..'
        os.system(outcmd)
        code_file=open(filepath+'/out.txt')
        mycode_line=code_file.readline()
        code_file.close()

        if len(mycode_line)<=3:
            print 'I guess the CAPTCHA code is %s,but I think it\'s error.' % (mycode_line)
            continue
        mycode=mycode_line[0:4]
        print 'I guess the CAPTCHA code is %s' % (mycode)
        mylist=user_line.split('----')
        proxy_list=myproxy_line.split(':')
        myid=mylist[0]#.decode('utf-8')
        myname=mylist[1]#.decode('utf-8')
        mycomm=mylist[2]#.decode('utf-8')
        data={'method':'vote',
              'voteInfoId':voteInfoId,
              'forward':'***',
              'info1':myid,
              'info2':myname,
              'info3':mycomm,
              'inputCode':mycode,
              'submit':'确定'}
        print 'Now I begin to vote...'
        print 'the user is %s' % (myid)
        print 'the name is %s' % (myname)
        print 'the comment is %s' % (mycomm)
        post_data=urllib.urlencode(data)
        try:
            response=opener.open(myurl,post_data)
        except Exception,e:
            print 'I can\'t connect the server ,so vote is failure'
            continue
        content=response.read()
        #img_req=opener.open(imgurl)
        #cookieFileJar.save(cookieFilename)
        #req=opener.open(myurl,post_data)
        #req=urllib2.Request(myurl,data=post_data,headers=headers)
        fp=file('test.html','w')
        print 'I put the received html to the file test.html'
        fp.write(content)
        fp.close()
        #outcmd="%s %s %s" %(tes,imgfile,outfile)
        #count+=1
        #print cookieFileJar