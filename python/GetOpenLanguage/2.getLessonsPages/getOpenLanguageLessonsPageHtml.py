import urllib
import urllib2
import re
import cookielib

#opener=urllib2.build_opener()
#opener.addheaders.append(('Cookie','lang=zh_CN'))
#f=opener.open("http://www.openlanguage.com")


cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response=opener.open('http://openlanguage.com/changelang/zh_CN')
for item in cookie:
    print 'Name='+item.name
    print 'Value='+item.value
pagelinkfile=file('OpenLanguageLessonLinks.txt','r')
i=1
for url in pagelinkfile.readlines():
    urlarray=url.split('/')
    lessonname=urlarray[6]
    lessonno=urlarray[4]
    urllib.urlretrieve('http://openlanguage.com/changelang/zh_CN','index.html')
    urllib.urlretrieve(url,lessonno+'.'+str(lessonname)+'.html')
    print i
    i=i+1
pagelinkfile.close()
