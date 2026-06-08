# ***************LISTS VS NUMPY_ARRAYS********************

import sys ,time
import numpy as np

list = range(100)
array = np.arange(100)

#Memory

#Space Occupied by list

sp = sys.getsizeof(66)*len(list)
print(sp)

#space occupied by array

nsp = array.itemsize*array.size
print(nsp)

#Speed

#speed of List

x=range(100000)
y=range(100000,200000)

start = time.time()

c=[]

for a,b in zip(x,y):
    c.append((a,b))

print(time.time()-start)

#speed of Numpy Array

q=np.arange(100000)
w=np.arange(100000,200000)

start1 = time.time()

c = q+w

print(time.time()-start1)