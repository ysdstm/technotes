passlist=[]
file=file('realurl.txt','r')
for file_line in file.readlines():
	passlist.append(file_line)
file.close()

for list in passlist:
	print list
