import urllib2
import re
url=raw_input("url:\n")
page=urllib2.urlopen(url)
html=page.read()
links=re.findall(r"(http://.+)h2",html)
for link in links:
	print link

