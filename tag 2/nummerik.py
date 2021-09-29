import numpy as np

a = np.array([1,2.9890789,3,4], dtype=np.float64)

b = np.array(list(range(0,11))) / 10

c = np.array([  [1,2,3], [4,5,6], [7,8,9]])

print(2*a)
print(b)
print(c[:,0])
print(c.shape)

print(3 in c)
print(10 in c)
