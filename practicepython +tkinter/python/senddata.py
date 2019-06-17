import pymysql
db=pymysql.connect("localhost","root","root","test")
cur=db.cursor()
print("Welcome to local Search Engine")
entry1=input("Are you a user/admin? \n")
 
	ask=input("Search by \n1.location \n2.location and sublocation \n3.keyword \n")
	if ask=="1":
		loc1=input("Location: ")
		st="select * from localsearch where location='%s'"%loc1
		try:
			cur.execute(st)
			data=cur.fetchall()
			for r in data:
				print("Business: ",r[4])
				print("Address: ",r[5])
				print("City: ",r[6])
				print("Mobile No: ",r[7])
				print("E-mail: ",r[8])
				print("----------------------------------")
		except:
			print("Error!!!")
	if ask=="2":
		loc2=input("Enter Location: ")
		subloc2=input("Enter sublocation: ")
		et="select * from localsearch where location='%s' and sublocation='%s'"%(loc2,subloc2) 
		try:
			cur.execute(et)
			data=cur.fetchall()
			for r in data:
				print("Business: ",r[4])
				print("Address: ",r[5])
				print("City: ",r[6])
				print("Mobile No: ",r[7])
				print("E-mail: ",r[8])
				print("----------------------------------")
		except:
			print("Error!!!")	

	if ask=="3":
		kywrd=input("Keyword: ")
		kt="select * from localsearch where keyword='%s'"%(kywrd)
		try:
			cur.execute(kt)
			data=cur.fetchall()
			for r in data:
				print("Business: ",r[4])
				print("Address: ",r[5])
				print("City: ",r[6])
				print("Mobile No: ",r[7])
				print("E-mail: ",r[8])
				print("----------------------------------")
		except:
			print("Error!!!")	

if entry1=="admin":
	search=int(input("SearchId: "))
	loc=input("Location: ")
	subLoc=input("Sub Location: ")	
	kywrd=input("Keyword: ")
	bussname=input("Business Name: ")
	add=input("Address: ")
	city=input("City: ")
	mobno=int(input("Mobile No: "))
	email=input("E-mail id: ")
	at="insert into localsearch values('%d','%s','%s','%s','%s','%s','%s','%d','%s')"%(search,loc,subLoc,kywrd,bussname,add,city,mobno,email)
	try:	
		cur.execute(at)
		print("Data saved")
		db.commit()
	except:
		print("some Error")	


