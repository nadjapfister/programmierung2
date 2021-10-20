# variante 1
class Temperatur:
    def __init__ (self,c):
        self.celsius = c

    def __str__ (self):
        return str(self.celsius) + chr(8451)

t_muttenz = Temperatur (9.9)
t_zurich = Temperatur (11)

if t_zurich.celsius > t_muttenz.celsius:
    print("pech gehabt")
else:
    print("hahahahahahahah")


# ------------------------------------------------------
# variante 2
class Temperatur:
    def __init__ (self,c):
        self.celsius = c

    def __str__ (self):
        return str(self.celsius) + chr(8451)

    def __gt__ (self, other):
        return self.celsius > other.celsius

    def __lt__ (self, other):
        return self.celsius < other.celsius

    def __eq__ (self, other):
        return self.celsius == other.celsius


t_muttenz = Temperatur (9.9)
t_zurich = Temperatur (11)

if t_zurich < t_muttenz:
    print("pech gehabt")
else:
    print("hahahahahahahah")