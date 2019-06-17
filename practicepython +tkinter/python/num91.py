import numpy as np

'''x=np.arange(8).reshape(2,2,2)
print(x)
print(np.swapaxes(x,2,0))#first column first value interchange with second array first coulm first value'''

'''x=np.array([2],[5],[3])
y=np.array([4,5,6])
z=np.broadcast(x,y)
print(z)'''

#concatenation
'''x=np.array([[2,4],[4,5]])
y=np.array([[2,5],[1,4]])
print(np.concatenate((x,y)))
print(np.concatenate((x,y),axis=1))'''


'''x=np.array([[2,4],[4,5]])
y=np.append(x,[5,6])
print(y)
z=np.delete(x,3)
print(z)
c=np.unique(x)
print(c)'''

x=np.arange(9).reshape(3,3)
y=np.arange(9).reshape(3,3)
'''print(np.add(x,y))
print(np.subtract(x,y))
print(np.divide(x,y))
print(np.multiply(x,y))
print(np.power(x,y))'''
print(np.amin(x,1))
print(np.amax(x,1))





