#coding=utf-8
import urllib2
#使用raw_input()是为了与2.7版本兼容，3.x版本使用input()函数，在这里使用需要在输入的字符串两边加上单引号
url="http://" + raw_input("url(Eg: www.baidu.com):\n")
pagecode=raw_input("Input pagecode: gb2312 gbk utf-8\n")
response=urllib2.urlopen(url)
html=response.read()
print html.decode(pagecode)
