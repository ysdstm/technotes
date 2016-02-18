import urllib2
import re
import time

url='http://www.mmrosi.com/x/list_1_'
i=1
while(i<2):
	newurl=url+str(i)+".html"
	print newurl
	page=urllib2.urlopen(newurl)
	html=page.read()
	links=re.findall(r"/x/(201.+)img",html)
	for link in links:
		print link
	i=i+1
	time.sleep(5)
