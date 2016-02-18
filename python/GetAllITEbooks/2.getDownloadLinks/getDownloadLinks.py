import urllib2
import re

def geturl(url):
	page=urllib2.urlopen(url)
	html=page.read()
	links=re.findall(r"(http://.+)Download",html)
	return links[0]
pagelinkfile=raw_input("LinkFileName:\n")
DownloadLinkFile=raw_input("New DownloadLinkFile:\n")
listfile=file(pagelinkfile,'r')
for url in listfile.readlines():
	urlfile=open(DownloadLinkFile,'ab')
	urlfile.write(url)
	urlfile.write(geturl(url))
	urlfile.write('\n')
	urlfile.close()
listfile.close()
