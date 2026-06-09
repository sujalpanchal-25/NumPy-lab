'''Part 6: Iteration
arr = np.array([100,200,300,400])
Q21

Use a for loop to print:

100
200
300
400'''

import numpy as np

arr = np.array([100,200,300,400])

for i in np.nditer(arr):
    print(i)