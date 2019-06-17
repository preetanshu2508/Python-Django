'''def update(li,i,value):
 if i>=0 and i<len(li):
  li[i]=value
  
  print(p)
  print(q)
 else:
 	value=value+1
 	
c=[2,11,11,14]
z=8
p=update(c,2,z)
q=update(c,6,z)'''


'''def f(x):
  return(g(x*2))
def g(y):
  return(y+3)

z=f(22)
'''
#recursion factorial
'''def factorial(n):
 if n<=0:
  return(1)
 else:
  val=n*factorial(n-1)
  return(val)

factorial(6)'''

# factor by functiom
# prime no by function

'''def factor(n): 

 def isprime(n):factorlist=[]
 for i in range(1,n+1):
  if n%i==0:
  	factorlist=factorlist+[i]
 return(factorlist)
  factorlist=[]
  for i in range(1,n+1):
   if n%i==0:
  	factorlist=factorlist+[i]
   return(factorlist)
  
 def primesupto(n)
   primelist=[]
   for i in range(1,n+1):
   	if isprime(i):
   	  primelist=primelist+[i]
   return(primelist)	
   return(factor(n)==[1,n])	'''

#list
#count,append,max,min function

'''lt=['abc','12','1234','preeta','hemu','True']
print(lt)
print(lt[0:5])
print(lt[2:])
lt[3]='new value'
print(lt)
del lt[4]
print(lt)
print(len(lt))
lt1,lt2=['abc',25,7],['abc',25,7]
print(lt1)
print(lt2)
lt3=['abc','cde','xyz']
lt4=[2,4,5,6]
print(max(lt4))
print(min(lt4))
lt3.append(1000)
print(lt3)
print(lt3.count('1000'))

#useful function(extend function),reverse,pop,index,insert functions

lty=['AX','xzz','avcc']
lty.extend(lty)
print(lty)
print(lty.index('AX'))
lty.insert(2,1001)
print(lty)
print(lty.pop())
#lty.reverse()
print(lty)
lty.remove('AX')
print(lty)'''

#we have list of cities ,enter a city for user if city already present it will give error other wise city will be added to the list

'''x=str(input("enter your city"))
lt=['agra','kanpur','allahabad']
if x in lt:
	print(error)
else:
   lt.append(x)
   print(lt)



 #tuple exceptions:

 tp=('abc',22,23)
 tp[1]='nm'
 print(tp)
 del tp[2]

'''
 #dictionary:


'''dt={'rollo':101,'name':'abc','age':20}
print(dt)
print(dt['rollno'])
dt['rollno']=12
print(dt)
dt.clear()
print(dt)
del dt
print(dt)'''


'''dt={'rollno':101,'name':'pree','age':20}
dt1=dt.copy()
print(dt1)
print(dt.get('rollno'))
print(dt.get('college','no value is present'))
#print(dt.has_key('rollno'))
print(dt.keys())
print(dt.values())

dt['college']='iet'
print(dt)'''

#write a program to check if any item is repeated in dictionarry

'''i=0
dt={'rollno':101,'name':'pree','age':101}
for i in dt:
 if dt.values(i)==dt.values(i+1):
  i=i+1
  print('repeated')
 else:
  print("not repeated")'''

#command line arguments in python
# all the values which will pass while running the program ,the vlues can be get by importing sis module 
#is like array which contains the value.the first value index is 0 is the program name itself.

'''import sys
print('first value',sys.argv[0])
print('second value',sys.argv[1])
print('third value',sys.argv[2])'''



''''import sys
if len(sys.argv)==4:
 
  x=int(sys.argv[1])
  y=int(sys.argv[3])

  if sys.argv[2]=='+':
	print(x+y)
  elif sys.argv[2]=='-':
	print(x-y)
  elif sys.argv[2]=='x':
	print(x*y)
  elif sys.argv[2]=='/':
	print(x/y)
else:
	print("pass value")'''


#pass any values on command line and print them

'''import sys
x=sys.argv
for i in x:
    print(i)'''


 # we have a list of values ;input values from cmd  line check how many present in list

''''import sys
lt=['agra','allahabad']
i=1
x= sys.argv[i]
if x in lt:

	print(x)
	print(lt.count(x))
 elif
  x=sys.argv[2]
  print(x)
  print(lt.count(x))
else:
	lt.append(sys.argv)
	print(lt)'''


'''def lcm(a,b):
 for i in range(1,10):
  if (a*i)%(b)==0:
  	c=a*i
  	print(c)
  break
   


lcm(12,20)'''

'''def show(a=10,b=10):
   print('a',a)
   print('b',b)


show()
show(15)
show(15,3)
'''

'''def power(a,b):
	c=a**b
	return c


x=power(2,3)
print(x)
'''

'''def show(name,age):
  print('Name is',name)
  print('Age is ',age)

show(age=21,name='Test')
show('abc',12)'''

'''def show(lt):
  lt[2]=95
  return

lt=['abc',20,30,'xyz',True]
show(lt)
print(lt)'''
#Variable no of arguments:

efisplay(*x):
   for m in x:
   	  print('value',m)


display(2)
display(2,5)
display('abc',114,'adc')


  
 
 
