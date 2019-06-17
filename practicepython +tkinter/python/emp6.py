import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

emp = pd.read_csv('enq.csv', encoding = "ISO-8859-1")
print(emp)

plt.hist(emp['payment'],bins=4,color='red',normed=False,alpha=0.5)
plt.show()