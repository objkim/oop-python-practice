# Super() = Function used in a child class method from a parent class(superclass)
#           Allow you to extend the functionality of thr inherited methods

import unicodeit

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(unicodeit.replace(f"It is a circle with an area of {3.14 * self.radius ** 2}cm^2"))

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
        
    def describe(self):
        super().describe()
        print(unicodeit.replace(f"It is a square with an area of {self.width ** 2}cm^2"))

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
 
    def describe(self):
        super().describe()
        print(unicodeit.replace(f"It is a triangle with an area of {(self.height * self.width) / 2}cm^2"))