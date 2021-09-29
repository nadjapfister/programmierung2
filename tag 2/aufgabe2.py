n = 2000
X = np.random.normal(0, 1 ,n)
Y = np.random.normal(0, 1, n)

# die 2000 Punkte sollen nach ihrem Abstand zu (0,0) eingefärbt werden
D = np.sqrt(X**2 + Y**2)

plt.scatter(X, Y, c = -D)
plt.show()