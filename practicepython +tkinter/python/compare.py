x=str(input("enter a string")).split()
y=str(input("enter a second string")).split()
for i in x:
  for j in y:
   if i.find(j)>=0:
  		print("string have common substring")
   else:
    	print("not having common string")
     
