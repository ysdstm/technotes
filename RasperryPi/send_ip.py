#!/usr/bin/env python
# -*-coding:utf8-*-
import socket
import fcntl
import time
import struct
import smtplib
import urllib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

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
	

# 检查网络连通性
def check_network():
	while True:
		try:
			result=urllib.urlopen('http://baidu.com').read()
			print result
			print "Network is Ready!"
			break
		except Exception , e:
			print e
			print "Network is not ready,Sleep 5s...."
			time.sleep(5)
	return True

# 获得指定接口的ip地址
def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("1.1.1.1",80))
	ipaddr=s.getsockname()[0]
	s.close()
	return ipaddr

if __name__ == '__main__':
	check_network()
	ipaddr=get_ip_address()
	print ipaddr
	sendEmail('smtp.163.com','***@163.com','***','***@163.com <***@163.com>',['***@***.com'],'IP Address Of Raspberry Pi',ipaddr)
