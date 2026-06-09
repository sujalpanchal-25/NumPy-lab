'''Part 4: 2D Array Indexing
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
Q13
Print:
10

Q14
Print:
50

Q15
Print:
90

Q16
Print:
80
'''

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)

print(arr)
print('\n')
print(arr[0,0])
print('\n')
print(arr[1,1])
print('\n')
print(arr[2,2])
print('\n')
print(arr[2,1])