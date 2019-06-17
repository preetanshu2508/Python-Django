import numpy as np
d=np.array([[2,2,2],[2,5,2],[2,5,6],[5,7,8]])
print(d)
y=np.array([[0,0],[3,3]])
print(d)
c=np.array([[0,2],[0,3]])
f=d[y,c]
print(y)


#print(d[1:])
#print(d[...,1])
#print(d[...,1:])