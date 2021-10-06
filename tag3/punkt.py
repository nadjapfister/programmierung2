import math

class Punkt2D: #Bauplan
    def __init__(self, x=0, y=0): #Konstruktor
        self.x = x #Parameter
        self.y = y
        #self.toleranz = 0
        #self.art = "Stein"
        #self.id = 1

    def ausgabe(self):
        print(f"Punkt: [{self.x}, {self.y}]")

    def distanz(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
       
if __name__ == "__main__":
    a = Punkt(3,4)
    b = Punkt(2,4)
    a.ausgabe(False)
    b.ausgabe(False)
    print(a.distanz(b))




