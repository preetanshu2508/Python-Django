import numpy as np
a=np.arange(9).reshape(3,3)
print(a)
con=np.mod(a,2)==0 #remainder in boolen
print(con)
print(np.extract(con,a))