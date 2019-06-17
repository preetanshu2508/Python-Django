x=str(input("enter the string"))
y=str(input("enter second string"))
identical=0
casematch=0
for i in x.split():
 for j in y.split():
  if i==j:
   identical=identical+1 
  elif i.lower()==j.lower():
   casematch=casematch+1
  elif i.upper()==j.upper():
   casematch=casematch+1

if identical>0:
	print("identical found:",casematch)

if casematch>0:
	print ("casematch:",casematch)++

if(casematch==0 and identical==0):
    print ("no matches found")

