class Vector2:
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__ (self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __sub__ (self, other):
         return Vector2(self.x-other.x, self.y-other.y)

    def __mul__ (self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x*other, self.y*other)
        else:
            return Vector2(self.x*other.x, self.y*other.y)

    #def __truediv__ #division

    #def __rmul__ (self, other):
        # if type(other) == int or type(other) == float:
        #    return Vector2(self.x*other, self.y*other)
       # else:
       #     return Vector2(self.x*other.x, self.y*other.y)

    def __neg__(self): # Negation
        return Vector2(-self.x, -self.y)

    def __abs__ (self): #absolut
        return Vector2(-self.x, -self.y)

    def __str__ (self):
        return f"vector ({self.x}, {self.y})"

# --------------------------------------------------------

a = Vector2(2,3)
b = Vector2(3,4)
g = Vector2(4,4)

print(a)
print(b)

c = a + b

print(c)

# a = [1,2,3]
# b = [2,3,4]

d = a + b

print(d)

e = a - b # sub
print (e)

resultat = a + b + g
print(resultat)

a = Vector2(4,5)
b = Vector2(3,5)

c = a * b
print(c)

d = a *2 #mul
print(d)

#d = 2 *a #rmul
#print(d)


a = Vector2(2,1)
a += Vector2(1,1)
print(a)

a = Vector2(-5,5)
print(a)