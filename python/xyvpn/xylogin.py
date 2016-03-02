#!/usr/bin/env python
# -*-coding:utf8-*-
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

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
	'email' : '****@163.com',
	'password' : 'mypassword'}

postData = urllib.urlencode(postData)  


request = urllib2.Request(posturl, postData, headers)  
#print request  
response = urllib2.urlopen(request)  
text = response.read()  
#print text

print "============================================================"

old_url='http://home.zhxin.net/home/main_servers'
req=urllib2.Request(old_url)
response=urllib2.urlopen(old_url)
print 'Old url:'+old_url
print 'Real url:'+response.geturl()
#print response.read()
html=response.read()
links=re.findall(r"<td><strong>.+",html)
vpnserver = links[0]
print vpnserver

#发送邮件的基本函数，参数依次如下
# smtp服务器地址、邮箱用户名，邮箱密码，发件人地址，收件人地址（列表的方式），邮件主题，邮件html内容
def sendEmail(smtpserver,username,password,sender,receiver,subject,msgtext):
	msgRoot = MIMEMultipart('related')
	msgRoot["To"] = ','.join(receiver)
	msgRoot["From"] = sender
	msgRoot['Subject'] =  subject
	msgText = MIMEText(msgtext,'plain','utf-8')
	msgRoot.attach(msgText)
	#sendEmail
	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msgRoot.as_string())
	smtp.quit()

sendEmail('smtp.163.com','***@163.com','***','***@163.com <***@163.com>',['***@***.com'],'XY Server',vpnserver)
