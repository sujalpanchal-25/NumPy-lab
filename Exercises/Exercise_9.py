'''Part 2: Basic Slicing
arr = np.array([1,2,3,4,5,6,7,8,9,10])
Q6

Get:

[1 2 3 4]
Q7

Get:

[5 6 7 8 9 10]
Q8

Get:

[3 4 5 6]
Q9

Get:

[1 2 3]

without writing the numbers manually.'''

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr)
print('\n')
print(arr[:4])
print('\n')
print(arr[4:])
print('\n')
print(arr[2:6])
print('\n')
print(arr[:3])