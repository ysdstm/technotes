import os
import urllib
import urllib2
jpgfile=file('topjpg.txt','r')
for url in jpgfile.readlines():
	#url = 'http://222.76.211.84/rosi/image/1492/d.jpg'
	#get filename "d.jpg"
	filename = os.path.basename(url)
	#get extension name .jpg
	ext=os.path.splitext(url)[1]
	urlarray=url.split('/')
	number=urlarray[5]
	urllib.urlretrieve(url,number+'.jpg')
jpgfile.close()
