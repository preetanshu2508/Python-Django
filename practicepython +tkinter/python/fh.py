c=open("bb.txt","w+")
c.write("this is new file") 




f=open("dd.txt","rt+")
p=f.read(40)
for i in p:
  if i==p.isnumeric():
  	
  	f.write(i)

c.close()
print("file saved")
f.close()
