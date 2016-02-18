import requests
import urllib
import urllib2
import re

pagelinkfile=file('OpenLanguageLessonLinks.txt','r')
i=1
for url in pagelinkfile.readlines():
    urlarray=url.split('/')
    lessonname=urlarray[6]
    lessonno=urlarray[4]
    audiourl='http://openlanguage.com/lessons/'+lessonno+'/download-lesson-file?type=2&pass=643bdd49220861ecd5844bde0c19da52'
    r=requests.get(audiourl)
    with open(lessonno+'.'+lessonname+'.pdf','wb') as code:
        code.write(r.content)
    print i
    i=i+1
pagelinkfile.close()

#url='http://openlanguage.com/lessons/4956/download-lesson-file?type=1&pass=643bdd49220861ecd5844bde0c19da52'
#url='http://openlanguage.com/lessons/3829/download-lesson-file?type=1&pass=97389d32e0667db68b84357169eceb80'
#r=requests.get(url)
#with open('4956.mp3','wb') as code:
#	code.write(r.content)
