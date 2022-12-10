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
        if all([isinstance(side, (int, float)) for side in sides]) and all([side > 0 for side in sides]):
            sortedside = sorted(sides)
            return sortedside[-1] < sortedside[0] + sortedside[-1]
            
            

    def perimeter(self):
        return round((self.a + self.b + self.c),2)

    def square(self):
        half_perimeter = (self.a + self.b + self.c) / 2
        #return sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))
        return round(sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c)), 2)

triangle_itog = Triangle(.2, .2, .2)
# triangle_itog = Triangle(.8, .7, .13) #dz za
print(triangle_itog.perimeter())
print(triangle_itog.square())

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if not self.is_valid():
            raise NotValidFigure

    def is_valid(self):
        if isinstance(self.radius, (int, float)):
            return self.radius > 0
    
    def dlina(self):
        return round(self.radius **2 * pi, 2)

    def ploshad(self):
        return round(2 * pi * self.radius, 2)

circle_itog = Circle(4)
print(circle_itog.dlina())
print(circle_itog.ploshad())


        