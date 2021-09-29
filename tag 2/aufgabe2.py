from math import exp
import numpy as np
import matplotlib.pyplot as plt
import random


def f(x,y):
    return (np.exp(-x**2)*np.sin(y))
    
n = 256
x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)
X, Y = np.meshgrid(x, y)

fig7 = plt.figure()
pp7 = fig7.add_subplot(111)
plt.title("Aufgabe 2.1 - Nadja Pfister")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")

img = pp7.contourf(X, Y, f(X,Y), 12, cmap='winter') 
fig7.show()

fig71  = plt.figure()
plot71 = fig71.add_subplot(111, projection='3d')
plt.title("Aufgabe 2.2 - Nadja Pfister")
plot71.plot_surface(X, Y, f(X,Y), cmap='winter')
fig71.show()