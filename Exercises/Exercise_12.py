'''Part 5: 2D Array Slicing

Using the same array:
[[10 20 30]
 [40 50 60]
 [70 80 90]]

Q17
Get first row.
Expected:
[10 20 30]

Q18
Get second row.
Expected:
[40 50 60]

Q19
Get third column.
Expected:
[30 60 90]

Q20
Get second column.
Expected:
[20 50 80]
'''

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)

print(arr)
print('\n')
print(arr[0])
print('\n')
print(arr[1])
print('\n')
print(arr[:,2])
print('\n')
print(arr[:,1])
print('\n')