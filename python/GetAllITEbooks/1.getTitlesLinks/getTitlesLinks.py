import urllib2
import re
url=raw_input('Input Categories Url:(eg. Python: http://www.allitebooks.com/web-development/python/page/):\n')
i=1
max=raw_input('Input Maximum PageNo.:\n')
while(i<=max):
	newurl=url+str(i)+'/'
	print newurl
	page=urllib2.urlopen(newurl)
	html=page.read()
	links=re.findall(r"(http://.+)h2",html)
	for link in links:
		print link
	i=i+1

