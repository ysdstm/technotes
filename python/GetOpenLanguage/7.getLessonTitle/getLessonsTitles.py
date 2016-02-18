import urllib2
import re
url=raw_input('Input Openlanguage Url:(eg. http://openlanguage.com/library/learn-english/9/latest?page=):\n')
i=1
max=raw_input('Input Maximum PageNo.:\n')
while(i<=int(max)):
	newurl=url+str(i)
	print newurl
	page=urllib2.urlopen(newurl)
	html=page.read()
	links=re.findall(r"(<h3>.+)",html)
	for link in links:
		print link
	i=i+1

