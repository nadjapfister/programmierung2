class Fahrzeug:
    def __init__ (self):
        self.farbe = "rot"
        self.raeder = 0
        self.fahrgestellnummer = ""
        self.sitzplaetze = 0

    def fahren(self):
        print ("fährt weg ....")

#-------------------------------------------------------------------------

class PKW(Fahrzeug):
    def __init__ (self):
        super().__init__()
        self.schiebedach = False

    def  __str__(self):
        return f"schiebedach: {self.schiebedach}, Farbe {self.farbe}"

#-------------------------------------------------------------------------

class Fahrrad (Fahrzeug):
    def __init__(self, rahmengrösse, farbe):
        super().__init__(farbe,2)
        self.rahmengrösse = 54


    def __str__(self):
        return f"fahrrad: Rahmengrösse {self.rahmengrösse}, Farbe {self.farbe}"

tesla = PKW()
tesla.schiebedach = True
print(tesla)

scott = Fahrrad(54, "pink")
print (scott)