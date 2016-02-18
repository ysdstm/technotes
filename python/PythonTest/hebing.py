file=file("rslist2.txt",'r')
global hurl
hurl=''
for url in file.readlines():
	hurl=hurl+url
print hrul
