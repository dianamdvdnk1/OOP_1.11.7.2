from math import *

class NotValidFigure(Exception):
    pass
 
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise NotValidFigure

    def is_valid(self):
        sides = [self.a, self.b, self.c]
        if all([isinstance(side, (int, float)) for side in sides]):
            return all([side > 0 for side in sides]) 
            sortedside = sorted(sides)
            return sortedside[1] < sortedside[-1] + sortedside[0]
            

    def perimeter(self):
        return round(self.a + self.b + self.c,3)

    def squrt(self):
        half_perimeter = (self.a + self.b + self.c) / 2
        return round(sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c)),3)
    
triangle_itog = Triangle(.2, .2, .2)
print(triangle_itog.perimeter())
print(triangle_itog.squrt())

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if not self.is_valid():
            raise NotValidFigure

    def is_valid(self):
        if isinstance(self.radius, (int, float)):
            return self.radius > 0
    
    def dlina(self):
        return round(self.radius **2 * pi, 3)

    def ploshad(self):
        return round(2 * pi * self.radius, 3)

circle_itog = Circle(3)
print(circle_itog.dlina())
print(circle_itog.ploshad())


        