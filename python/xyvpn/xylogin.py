import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
import time

hosturl = 'http://home.zhxin.net/portal/index.html'

posturl = 'http://home.zhxin.net/portal/login'
  

cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
  
h = urllib2.urlopen(hosturl)  
  

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'}  

postData = {'utf8' : '&#x2713;',
	'authenticity_token' : 'XPUWie8/pucc/HjUFnAjA9fYrhcLWm/aNjq0oemgGKY=',
	'act' : 'login',
	'email' : 'zwinzhu@163.com',
	'password' : 'riwfnyuki'}

postData = urllib.urlencode(postData)  


request = urllib2.Request(posturl, postData, headers)  
print request  
response = urllib2.urlopen(request)  
text = response.read()  
print text

print "============================================================"

old_url='http://home.zhxin.net/home/main_servers'
req=urllib2.Request(old_url)
response=urllib2.urlopen(old_url)
print 'Old url:'+old_url
print 'Real url:'+response.geturl()
print response.read()
html=response.read()
links=re.findall(r"<td><strong>.+",html)
for link in links:
	print link
