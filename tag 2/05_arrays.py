from os import abort
import numpy as np

#np.array(L)

np.zeros([3,4])

np.ones([8,7])

a = np.zeros([3,3])
a[2,2] = 5
print(a)

b = np.arange(0,10)
print(b)

c = np.arange(0,10.5,0.5)
print(c)

e = np.linspace(0,1, 5)
print(e)

np.pi * a

np.random.random(10)*100