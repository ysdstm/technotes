import requests
url='http://222.76.211.84/rosi/image/1461/d.jpg'
r=requests.get(url)
with open('1461.jpg','wb') as code:
	code.write(r.content)
