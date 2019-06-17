import numpy as np

x=np.arange(8).reshape(2,4)
print(x)
print(x.flatten())
print(x.flatten(order='F'))

