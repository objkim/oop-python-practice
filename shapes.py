# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAY TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shapes(ABC):

    @abstractmethod
    def area(self):
        pass

class Circles(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Squares(Shapes):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
class Triangles(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.height * self.base * 0.5
    
class Pizza(Circles):
    def __init__(self, recipe, radius):
        super().__init__(radius)
        self.recipe =  recipe