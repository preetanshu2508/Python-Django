import numpy as np
'''d=np.array([2,6,7])
y=np.array([[1,2,4],[4,5,6],[6,7,7]])
print(d*y)'''
x=np.arange(2,60,5)
a=x.reshape(3,4)
print(a)
b=a.T
print(b)
y=np.arange(8).reshape(2,4)
print(y)
print(y.flat[3])#finding index of  by making in single dimension