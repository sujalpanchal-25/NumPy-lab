'''Exercise 7: Python List vs NumPy

Create:

lista = [1,2,3,4,5]
arr = np.array([1,2,3,4,5])

Print:

sys.getsizeof(1) * len(lista)
arr.itemsize * arr.size

Observe which uses less memory.'''

import numpy as np
import sys

lista = [1,2,3,4,5]
arr = np.array([1,2,3,4,5])



print(sys.getsizeof(1) * len(lista))
print(arr.itemsize * arr.size)