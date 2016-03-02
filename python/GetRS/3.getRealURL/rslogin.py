#code=gb2312
import urllib
import urllib2
import cookielib

url='http://www.mmrosi.com/member/index_do.php'

user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'

values={'fmdo' : 'login',
	'dopost' : 'login',
	'keeptime' : '604800',
	'userid' : 'z**w',
	'pwd' : 'Q****^'}
cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
headers={'User-Agent':user_agent}
data=urllib.urlencode(values) #encode form data
req=urllib2.Request(url,data)#send form data
response=urllib2.urlopen(req)
the_page=response.read()
print the_page

old_url='http://en.mmrosi.com/member/'
#old_url='http://www.mmrosi.com/plus/download.php?open=2&id=2&uhash=a624a864db380566a4759b8a'
#old_url='http://www.w3cschool.cc'
req=urllib2.Request(old_url)
response=urllib2.urlopen(old_url)
print 'Old url:'+old_url
print 'Real url:'+response.geturl()
print response.read()
