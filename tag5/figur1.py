from punkt import Punkt
import math

class Figur:

    def __init__(self, name="Figur"):
        self.name = name

    def umfang(self):
        return 0

    def __str__(self):
        return self.name

#-------------------------------------------------------------------------------

class Kreis(Figur):
    def __init__(self, m, r):
        super().__init__("Kreis")
        if type(m) != Punkt:
            raise TypeError("Mittelpunkt muss Klasse Punkt sein")

        self.Mittelpunkt = m
        self.Radius = r

    def umfang(self):
        return 2*self.r*math.pi

    def __str__(self):
        return f"{self.name}: Mittelpunkt {self.Mittelpunkt}, Radius {self.Radius}"

k = Kreis(Punkt(0,0), 1)
print (k)

# d = Dreieck(Punkt (0,0), Punkt(4,2), Punkt(2,3))
# print(d)
