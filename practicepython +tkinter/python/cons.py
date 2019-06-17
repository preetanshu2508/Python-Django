'''class MyC:
	x=0
	def __init__(self,a=0,b=0):
		print("Hellow Constructer")
		self.x=a
		self.y=b
	def show(self):
		
		print('x is',self.x+self.y)

obj=MyC(10,3)
obj1=MyC()
obj1.show()
obj.show()

#constructer can be pare'''

'''class Load:
	def sum(self,*a):
	
		sum=0
		for i in a:
		 sum=sum+i
		 print(sum)

obj=Load()
obj.sum(10,3)'''

#Instructer this are called when object overload


''''class Myc:
	x=0
	def __init__(self):
		self.x=15
		print('x is',self.x)
	def __del__(self):
		self.x=0
		print('Bye x',self.x)
obj=Myc()
obj1=Myc()
'''

#inhertence:
'''class MyP:
	#def show(self):
	def Hi(self):
		print('Hellow show')
	def sum(self,a,b):
		print('sum is',a+b)

class Mys(MyP):
	def Hi(self):
		print("Hellow pree")
	def Mult(self,a,b):
		print('prod is',a*b)

class My(Mys):
	def sub(self,a,b):
		print('sub is',a-b)

obj=My()
obj.sub(3,2)

obj.sum(1,2)
obj.Hi()#overiding
obj.Mult(2,3)'''


class Abc:
	def show(self):
		print("this is me")

	def hi(self):
		print("this is you")
	def __str__(self):
		return("Hellow I am ABC class")

obj=Abc()
print(obj)