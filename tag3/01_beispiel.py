import punkt

a = punkt.Punkt2D() #Instanz
b = punkt.Punkt2D(5,6) #Instanz

a.ausgabe(True)
b.ausgabe(False)

d1 = a.distanz(b)
d2 = b.distanz(a)
d3 = a.distanz(a)

print(d1)
print(d2)
print(d3)