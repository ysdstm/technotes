import urllib2
req=urllib2.Request('http://bbs.csdn.net/callmewhy/')

try: response=urllib2.urlopen(req)

except urllib2.HTTPError, e:
	print e.code
