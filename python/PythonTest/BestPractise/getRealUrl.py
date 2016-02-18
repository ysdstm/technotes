import urllib2

url=raw_input("url:\n")
#req=urllib2.Request(url)
response=urllib2.urlopen(url)
print 'Real url:'+response.geturl()
