'''Challenge Questions 🔥
arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

Q22
Print:
7

Q23
Print:
[5 6 7 8]

Q24
Print:
[4 8 12]

Q25
Print:
[1 3]

using slicing.'''

import numpy as np

arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

print(arr[1,2])
print('\n')
print(arr[1])
print('\n')
print(arr[:,3])
print('\n')
print(arr[0,0:3:2])