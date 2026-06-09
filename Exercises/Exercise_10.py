'''Part 3: Step Slicing
arr = np.array([10,20,30,40,50,60,70,80,90,100])
Q10

Get:

[10 30 50 70 90]
Q11

Get:

[20 40 60 80 100]
Q12

Reverse the array.

Expected:

[100 90 80 70 60 50 40 30 20 10]'''

import numpy as np 

arr = np.array([10,20,30,40,50,60,70,80,90,100])

print(arr[::2])
print('\n')
print(arr[1::2])
print('\n')
print(arr[::-1])
print('\n')
