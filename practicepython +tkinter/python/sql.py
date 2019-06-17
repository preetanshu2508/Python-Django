import pymysql


db=pymysql.connect('localhost','root','root','test')
cur=db.cursor()

x=str(input("enter name"))
y=int(input("enter roll no"))
z=str(input("enter sem"))
f=str(input("enter city"))

#st="delete from student where Rollno=2"
#st="update student set name='Rahul' where RollNo=22"

#st="select * from student where RollNo=%d "%x
st="insert into student values('%s',%d,'%s','%s')" %(x,y,z,f)

try:

	cur.execute(st)
	db.commit()
	print("sdone")
	#data=cur.fetchall()
	'''for  row in data:
		print('Name',row[0])
		print('RollNo',row[1])
		print('Sem',row[2])
		print('City',row[3])'''
	
	



except:
	print('issue occure')
	db.close()
