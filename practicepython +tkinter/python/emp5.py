import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

emp = pd.read_csv('enq.csv', encoding = "ISO-8859-1")
print(emp)
p=emp['payment']
c=emp['city']
col=['blue','green','red','pink','red','violet','black','brown','blue','orange','violet']
plt.pie(p,labels=c,colors=col,autopct="%1.1f%%")
plt.title('payment')
plt.show()