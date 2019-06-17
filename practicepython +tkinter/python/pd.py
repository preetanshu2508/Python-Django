import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''data=np.array(['abc','def','ghi'])
s=pd.Series(data)
print(s)'''

'''data=np.array(['abc','def','ghi'])
s=pd.Series(data,index=[501,502,503])
print(s)
'''
'''''data={'roll_no':1,'Name':'preetanshu','marks':102}
s=pd.Series(data,index=['roll_no','Name','marks'])
print(s)'''
''''
s=pd.Series(5,index=[0,1,2,3,4])
print(s)

s=pd.Series([5,2,4,4,4],index=['a','b','c','d','e'])
print(s[0])
print(s[1])
print(s[:2])
print(s['b'])

df=pd.DataFrame()  #blank dataframe
print(df)
d=[3,4,5,6,7]
df=pd.DataFrame(d)
print(df)

df=pd.DataFrame()
print(df)
d=[['ABC',35000],['xtx',9000],['ani',900000],['pree',9887766]]
df=pd.DataFrame(d,columns=['Name','Sallary'])
print(df)
df['city']=['agra','delhi','amabala','lknw']
print(df)


df=pd.DataFrame()
print(df)
d={'name':['ani','shi','ayu','vib','son'],'age':[21,22,23,21,21]}
df=pd.DataFrame(d)
print(df)

df=pd.DataFrame(d)
print(df)
d=[{'a':10,'b':30},{'a':10,'b':20,'c':30}]
df=pd.DataFrame(d,index=['FIRST','SECOND'])
print(df)

df=pd.DataFrame()	
print(df)
d={'FIRST':pd.Series([1,2,3],index=['a','b','c']),'SECOND':pd.Series([4,5,6],index=['g','h','i'])}
print(df)
'''







#*********************************28 MARCH*************************#
df=pd.DataFrame()	
print(df)
d=[['INDIA',2001,10,3],['CHINA',2001,12,1],['US',2001,9,4],['UK',2001,11,2],
	['INDIA',2004,15,1],['CHINA',2004,11,3],['US',2004,10,4],['UK',2004,12,2],
	['INDIA',2006,18,2],['CHINA',2006,12,4],['US',2006,19,1],['UK',2006,17,2],
	['INDIA',2008,19,2],['CHINA',2008,15,3],['US',2008,20,4],['UK',2008,19,2],]		
df=pd.DataFrame(d,columns=['COUNTRY','YEAR','POINTS','RANK'])

#print(df)
#print(df.groupby('COUNTRY'))
print(df.groupby('COUNTRY').groups)
#print(df.groupby(['COUNTRY','YEAR']).groups)
#g=df.groupby('YEAR')
#for n,gp in g:
#	print(n)
#	print(gp)
#print(g.get_group(2006))	
'''print(g['POINTS'].agg([np.sum,np.min,np.mean,np.size,np.std]))

#******************

d=pd.DataFrame()
print(df)
d={'Name':['preetanshu','ragini','shubham','hemu','shub','ankur','abhishek','neha'],
    'Age':[67,34,12,31,23,34,44,23],
     'Gender':['male','female','male','male','male','male','male','female'],
      'State':["uttarpradesh",'andhra','karnataka','andhra p','uttarpradesh','uttarpradesh','andhra','karnataka'],
      'Num-children':[2,3,4,5,6,6,7,6],
      'Num-pets':[2,3,4,5,2,5,5,6]}
print(df)
df.plot(kind='Scatter',x='Num-children',y='Num-pets',color=red)
plt.show()'''