import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df2= pd.read_csv('titanicdata21.csv', encoding = "ISO-8859-1")
#print(emp)

#Ques2
'''df=df2[(df2['Age']>50)]

df3=pd.DataFrame(df,columns=['Name','Age'])
print(df3)'''

#Ques2
df1=pd.read_csv('titanicdata2.csv',encoding = "ISO-8859-1")
#print(df1)
print(df2.append(df1))
p=pd.merge(df2,df1,on='PassengerId')
#print(p)
df3=pd.DataFrame(p)
#print(df)




#df=df3[(df3['Pclass']==3)]
#df4=df[(df['Survived']==1)]


#df13=pd.DataFrame(df4,columns=['Survived','Pclass'])
#print(df13.count())

#df4=df1[(df1['Survived']==1)]
#df15=pd.DataFrame(df4,columns=['Fare'])
#print(df15.mean())

#

#df=df2[(df2['Age']<30) & (df2['Sex']=='female')]

#df3=pd.DataFrame(df,columns=['Name','Sex','Age'])
#print(df3.count())


#df=df2[(df2['Cabin']=='A6') & (df2['Sex']=='male')]
#df3=pd.DataFrame(df,columns=['Name','Sex','Cabin'])
#print(df3.count())



#df=df3[(df3['Cabin_y'].isnull()) & (df3['Survived']==1)&(df3['Sex']=='female')]
#df4=pd.DataFrame(df,columns=['PassengerId'])
#print(df4.count())
#print(df.count())

'''df=df2[(df2['Embarked']=='S')]
df0=df2[(df2['Embarked']=='C')]
print(df.count())
print(df0.count())
'''

df=df3[(df3['Survived']==0)&(df3['Sex']=='male')]
df4=pd.DataFrame(df,columns=['PassengerId'])
print(df4.count())
print(df.count())

