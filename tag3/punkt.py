import math

class Punkt2D: #Bauplan
    def __init__(self): #Konstruktor
        self.x = 0 #Parameter
        self.y = 0
        #self.toleranz = 0
        #self.art = "Stein"
        #self.id = 1

    def ausgabe(self):
        print(f"Punkt: [{self.x}, {self.y}]")

    def distanz(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

        





