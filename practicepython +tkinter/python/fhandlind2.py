''''x=input("enter file name")
f=open(x,"w+")
st=int(input("Enter No of students"))
for i in range(1,st+1):
    rn=input("enter your roll no")
    sn=input("Enter student name")
    m=input("Enter Your marks")
    f.write((str)(st)+'\n')
    f.write('Roll no'+rn+'\n')
    f.write('Name'+sn+'\n')
    f.write('Marks'+m+'\n')
print("file saved")
f.close()'''
'''f=open("dd.txt","rt+")

p=f.read(20)
for i in p:

  if i=='a'or i=='i'or i=='o' or i=='u':
   print("vowels",i)
f.close()
'''




