import matplotlib.pyplot as plt
import math

s = 2*math.pi
n = 10
teilstücke = s / n
xlist = []
ylist = []

for i in range(0,n+1):
    x = -math.pi + i*teilstücke
    xlist.append(x)
    y = math.sin(x)
    ylist.append(y)


plt.plot(xlist,ylist, "ro--")
plt.axis("equal")
plt.show()
