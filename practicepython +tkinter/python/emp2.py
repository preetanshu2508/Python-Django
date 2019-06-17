import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', encoding = "ISO-8859-1")

#print(df)
'''df['service'].fillna(df['service'].sum(),inplace=True)
print(df)'''
'''df.insert(4,'test',df['salary']+500)
print(df)'''
'''df.columns=['a','b','c','d']
print(df)'''
'''df1=df[df['salary']>1500]
print(df1)
df2=df[(df['salary']>3500)&(df['city']=='agra')]
print(df2)'''

df1=pd.read_csv('data2.csv',encoding = "ISO-8859-1")
#print(df1)
#print(df.append(df1))
p=pd.merge(df,df1,on='emp id')
#print(p)
df2=pd.DataFrame(p)
#print(df2)



#printname of city and holidays list of employee

df3=pd.DataFrame(p,columns=['city','holidays'])
print(df3)
#print sum of salaries group by city

df4=df2.groupby(['city'])['salary'].agg('sum')
print(df4)
#df5=df13.groupby('city').groups
#print(df5)



#print holiday of employees who belongs to delhi city
df5=df2.groupby(['agra','holidays'])
print(df5)


#pint sum of payments where services greater than 10 years