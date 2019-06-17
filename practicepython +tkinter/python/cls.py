	#self key word-is used to refer the current instance variable of methods

class Student:
	rollno=0
	name=''
	age=0
	def getData(self):
		self.rollno=input("enter roll no")
		self.name=input("enter your name")
		self.age=input("enter age")
	def show(self):
		print('roll no',self.rollno)
		print('name',self.name)
		print('age',self.age)


s=Student()
s.getData()
s.show()

