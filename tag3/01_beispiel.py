import punkt

a = punkt.Punkt2D() #Instanz
b = punkt.Punkt2D() #Instanz

a.x = 0
a.y = 0

b.x = 1.0
b.y = 1.0

#a.ausgabe()
#b.ausgabe()

d1 = a.distanz(b)
d2 = b.distanz(a)
d3 = a.distanz(a)

print(d1)
print(d2)
print(d3)