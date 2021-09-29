import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)

y= np.sin(x)
y2 = np.cos(x)


plt.subplot(2,1,1)
plt.plot(x,y, "r--")
plt.title("Dies ist eine Sinuskurve")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")


plt.subplot(2,1,2)
plt.plot(x,y2, "k--")
plt.title("Dies ist eine Kosinuskurve")
plt.axis("equal")

plt.xlabel("x")
plt.ylabel("y")
plt.show(  )