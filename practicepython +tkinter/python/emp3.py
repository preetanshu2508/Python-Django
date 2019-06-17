import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

emp = pd.read_csv('enq.csv', encoding = "ISO-8859-1")
print(emp)
eg=emp.groupby('city')
total=eg["payment"].sum()
counts=eg['city'].size()
avg=total/counts
cg=np.arange(len(counts))
plt.xticks(cg,eg['city'])
plt.bar(cg,avg,align='center',color='blue')
plt.title('Avg payment City Wise',fontsize=18,color='red')
plt.show()