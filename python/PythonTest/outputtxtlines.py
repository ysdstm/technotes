urlfile=file('topjpg.txt','r')
for url in urlfile.readlines():
	print url
urlfile.close()
