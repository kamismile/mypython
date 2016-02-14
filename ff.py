# coding: UTF-8
__author__ = 'lidong'

import  urllib.request
import urllib.parse
import  http.cookiejar
values={
    'logon.x':'linke',
    'password':'xxxx',
    'username':'xxxxx'
}

logUrl="http://cffan9.v.vote8.cn/m/Shortcut/5630538#&ui-state=dialog"
# logUrl="http://www.baidu.com"

cook=http.cookiejar.CookieJar()

openner=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cook))

openner.addheaders = [{'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B176 MicroMessenger/4.3.2',
                      'Referer': 'https://mp.weixin.qq.com/'}]
openner.addheaders.append(('Cookie', 'ASP.NET_SessionId=vswtb2x0i0j22zbliovtxjwd'))
r=openner.open(logUrl,urllib.parse.urlencode(values).encode())

print(r.read())

# r=openner.open("http://192.168.132.62:8080/kq/kqself/card/carddata.do?b_query=link")
#
# print(r.read().decode('gbk'))

