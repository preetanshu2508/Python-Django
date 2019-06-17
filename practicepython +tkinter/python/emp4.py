import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

emp = pd.read_csv('enq.csv', encoding = "ISO-8859-1")
print(emp)
eg=emp.groupby("emp id")
counts=eg.size()
cg=np.arange(len(counts))
plt.figure('payments graph')
plt.xticks(cg,emp['emp id'])
plt.plot(cg,emp['emp id'],color='red',linestyle="-",linewidth=3)

plt.xlabel('emp id',fontsize=17,color='blue')
plt.ylabel('payment',fontsize=17,color='blue')
plt.show()
