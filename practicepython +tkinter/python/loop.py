#reverse no program:
'''x=24
while (x!=0):
 t=x%10
 print(t)
 x=x//10''


 #functions
 #abs
 '''
'''import math
x=-3
print(abs(x))
print(math.ceil(20.5))
print(math.floor(20.5))

# min function

print(min(12,16,18,9))

#sqrt function
print(math.sqrt(4))


#string repetion

st="this is hemu"
print(st)
print(st[1:7])
print((st[5:7])*3)

# for capatilize
st="this is python"
print(st.capitalize())
w="hellow"
print(w.center(50,'*'))
print(st.count('s'))
#print(st.startstwith('T'))
sst="this is python"
print(sst.expandtabs(15))

Q="this is new java form"
print(Q.find('new'))
print(Q.index('new'))
p="this1234"
pp="this"
print(p.isalnum())
print(pp.isalnum())
print(p.isalpha())  
print(pp.isalpha())
m="01234"
n="0167As"
print(m.isdigit())
print(n.isdigit())


e="abc"
pq="ABC"
print(e.islower())
print(e.isupper())
print(pq.istitle())

#Join functiom
val=("a","b","c")
s="-"
print(s.join(val))

l="hellow"
print(l.ljust(50,'*'))
print(l.rjust(50,'*'))
print(l.lower())
print(l.upper())

#maximum and minimum

st= "this is boy"

print(max(st))
print(min(st))
print(st.replace('i','P'))
wt="this us python****"

print(wt.rstrip('*'))
wx='**python**'
print(wx.strip('*'))
n="this is python"
print(n.swapcase())
print(n.title())
print(n.lower())
print(n.upper())

#write a program to enter username and password and email should contain one @ and one dot
#password should contain ateast 8 char and have upperlower and num'''
''''x=input("enter email id")
for i in x:
	if i.find("@") and i.isalpha() and i=="." and i.isalnum():
	  print("correct")

	else:
		print("write correct")
y=input("enter password")
for z in y:
    if z.find(z.lower()) and z.find(z.upper()) and z.find(z.isalnum()) and i>8	:
     print("correct")

    else: 
      print("wrong")'''


