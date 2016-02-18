import urllib2
import re
import time

#url='http://www.mmrosi.com/x/201511/1683.html'
#page=urllib2.urlopen(url)
#html=page.read()
#links=re.findall(r"/plus/(download.+)target",html)
#print links[0]

def geturl(url):
	page=urllib2.urlopen(url)
	html=page.read()
	links=re.findall(r"/plus/(download.+)target",html)
	return links[0]

listfile=file("rslist2.txt","r")
for url in listfile.readlines():
	urlfile=open("url.txt","ab")
	urlfile.write(url)
	urlfile.write(geturl(url))
	urlfile.write("\n")
	urlfile.close()
	time.sleep(5)
listfile.close()
