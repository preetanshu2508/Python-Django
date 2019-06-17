

import numpy as np
a=np.array([[30,40,60],[75,15,10],[45,85,55]])
print(a)
print(np.argmax(a))#highest index
mindex=np.argmax(a,axis=1)#highest indexin row
print(mindex)
print(np.nonzero(a))
b=np.where(a>30)
print(a[b])