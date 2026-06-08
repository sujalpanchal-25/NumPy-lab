'''
Exercise 4: Memory Usage
arr = np.array([10,20,30,40,50])

Find:

Memory used by one element
Total memory used by the array
'''

import numpy as np

arr = np.array([10,20,30,40,50])

m1 = arr.itemsize
print(m1)
mt = arr.itemsize  * arr.size
print(mt)
