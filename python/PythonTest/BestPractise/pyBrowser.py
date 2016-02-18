import mechanize
from bs4 import BeautifulSoup
import time
import urllib
import string

print '========Welcome to Mechanize Browser.========'
link="http://"+raw_input("Input a URL(e.g. www.baidu.com):\n")
br=mechanize.Browser()
r=br.open(link)
html=r.read()
soup=BeautifulSoup(html,'html.parser')
print 'You are browsing:'+soup.title.string
num=int(raw_input("Please input a number:\n1.Get Links\n2.Print Html\n3.Download Pics\n9.Back\n0.Quit\n"))
while num!=0:
	if num==1:
		print "Links in this page:\n"
		page_link=[]
		i=0
		for link in br.links():
			print str(i)+'.'+link.url+':'+link.text.decode("gb2312")
			page_link.append(link.url)
			i=i+1
		link_num=int(raw_input("Select a link:\n"))
		new_link=br.click_link(url=page_link[link_num])
		r=br.open(new_link)
		print br.geturl()
		html=r.read()

	if num==2:
		print html.decode("gb2312")
    
	if num==3:
		soup=BeautifulSoup(html,'html.parser')
		img_link=[]
		j=0
		for key in soup.find_all('img'):
			print j,key.get('src'),key.get('alt')
			img_link.append(key.get('src'))
			j=j+1
		img_num=int(raw_input("Select a pic:\n"))
		img_name=raw_input("Input save filename:\n")
		image=urllib.URLopener()
		image.retrieve(img_link[img_num],img_name)
	if num==9:
		br.back()
		print br.geturl()

	num=int(raw_input("Please input a number:\n1.Get Links\n2.Print Html\n3.Download Pics\n9.Back\n0.Quit\n"))
	
	
	