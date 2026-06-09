import numpy as np

a1 = np.arange(24).reshape(6,4)
print(a1)
print('\n')
print(a1[2])
print('\n')
print(a1[4:,2:])

print('\n')
for i in a1:
    print(i)
print('\n')

for i in np.nditer(a1):
    print(i)