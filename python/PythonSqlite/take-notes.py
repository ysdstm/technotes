import sqlite3

print '========Welcome to Python Notes========'

conn = sqlite3.connect('notes.db')
cursor=conn.cursor()

num=int(raw_input("Please input a number:\n1.Add new notes.\n2.Add new category\n0.Quit\n"))

while num!=0:
	if num==1:
		title=raw_input("Input note title:\n").decode("utf-8")
		content=raw_input("Input content:\n").decode("utf-8")
		comment=raw_input("Input comment:\n").decode("utf-8")
		categoryid=int(raw_input("Input cagtegoryid:"))
		print "You are going to add the note in category" + str(categoryid) + "\n"
		print title
		print content
		print comment
		confirm=int(raw_input("Please confirm:\n1.yes\n2.no:\n"))
		if confirm==1:
			cursor.execute("insert into notes (title,content,categoryid,comment) values (?,?,?,?)",(title,content,categoryid,comment))
			conn.commit()
		num=int(raw_input("Please input a number:\n1.Add new notes.\n2.Add new category\n0.Quit\n"))
