class Punkt:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x}, {self.y})"


# ------------------------------------


a = Punkt(2,3)
print(a) #<__main__.Punkt object at 0x000001E8A8B8F190>

b = Punkt(4,5)
print(b)

