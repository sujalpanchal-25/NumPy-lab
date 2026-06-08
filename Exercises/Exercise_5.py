'''Exercise 5: Number of Dimensions
For each array, predict ndim before running:

a = np.array([1,2,3])

b = np.array([[1,2,3],
              [4,5,6]])

c = np.array([[[1,2],
               [3,4]]])

What are the values of:'''

import numpy as np

a = np.array([1,2,3])

b = np.array([[1,2,3],
              [4,5,6]])

c = np.array([[[1,2],
               [3,4]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)