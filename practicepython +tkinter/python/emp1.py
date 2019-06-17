import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cust.csv', encoding = "ISO-8859-1")
print(df)
'''print(df.head())
print(df.tail())'''
'''
print(df.dtypes)
print(['salary'])
#tax=(df['salary']*10)
#print('tax')
df['tax']=df['salary']*.20
print(df)
#df1=df.groupby(['Gender'])
#print(df1)
#print(df1.mean())

#print(df1.sum())
df1=df[df['salary']>780]
print(df1)
df2=df[2:4]
print(df2)
df3=df.loc[2:4,['Gender','salary']]
print(df3)

df4=df.iloc[2:4,[0,2]]
print(df2)

df1=df.sort_values(by='salary')

#create 
#customer id ,custmer name,pphn no ,email,city,gender,dob,premium term(single,hal-yearly,quatry,)
#premium amount,Defaulter(yes,no)'''