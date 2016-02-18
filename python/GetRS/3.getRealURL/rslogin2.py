import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
import time

hosturl = 'http://www.mmrosi.com/member/index.php'

posturl = 'http://www.mmrosi.com/member/index_do.php'
  

cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
  
h = urllib2.urlopen(hosturl)  
  

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'}  

postData = {'fmdo' : 'login',
    'dopost' : 'login',
	'keeptime' : '604800',
	'userid' : 'zasw',
	'pwd' : 'QWEasd&*($%^'}
  

postData = urllib.urlencode(postData)  
  
 
request = urllib2.Request(posturl, postData, headers)  
print request  
response = urllib2.urlopen(request)  
text = response.read()  
print text

print "============================================================"

old_url='http://en.mmrosi.com/member/index.php'
#old_url='http://www.mmrosi.com/plus/download.php?open=2&id=2&uhash=a624a864db380566a4759b8a'
#old_url='http://www.w3cschool.cc'
req=urllib2.Request(old_url)
response=urllib2.urlopen(old_url)
print 'Old url:'+old_url
print 'Real url:'+response.geturl()
print response.read()


print "============================Resolving================================"
def getrealurl(old_url):
	req=urllib2.Request(old_url)
	response=urllib2.urlopen(old_url)
	return response.geturl()

urlfile=file('link_all_new.txt','r')
for url in urlfile.readlines():
	rurlfile=open("realurl.txt","ab")
	rurlfile.write(url)
	rurlfile.write(getrealurl(url))
	rurlfile.write("\n")
	rurlfile.close()
	time.sleep(8)
urlfile.close()

#urlarray=[]
#urlfile=file('link_all_new.txt','r')
#for url in urlfile.readlines():
#	urlarray.append(url)
#urlfile.close()


#for i in range(0,len(urlarray)):
#	rurlfile=open("realurl.txt","ab")
#	rurlfile.write(urlarray[i])
#	rurlfile.write("\n")
#	rurlfile.write(getrealurl(urlarray[i]))
#	rurlfile.write("\n")
#	rurlfile.close()
	

#old_url='http://en.mmrosi.com/member/index.php'
#old_url2='http://www.mmrosi.com/plus/download.php?open=2&id=3&uhash=1182c8357d6712efc60d5a57'
#old_url='http://www.w3cschool.cc'
#req2=urllib2.Request(old_url2)
#response2=urllib2.urlopen(old_url2)

#fo=open("realurl.txt","ab")
#fo.write(old_url2);
#fo.write("\n")
#fo.write(response2.geturl());
#fo.write("\n")
#fo.close()