import numpy as np

ar  = np.array([1,2,3,4])

print(ar)
print(type(ar))

ar2 = np.array([[1,2,3],[4,5,6]])

print(ar2)
print(type(ar))

ar3 = np.zeros((2,2))
ar4 = np.ones((3,3))
print(ar3)
print(ar4)

ar5 = np.identity(4)
print(ar5)

ar6 = np.arange(12)
print(ar6)

ar7 = np.linspace(0,10,3)
print(ar7)

ar8 = ar.copy()
print(ar8)