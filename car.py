# Object = A "bundle" of related attributes (variables) and methods (function)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# Class = (bluesprint) usesd to design the structure and layout of an object
    
class Car:

    wheel = 4
   
    def __init__(self, model, year, color, for_sale): # this is a dunder method = double underscore (__)
        self.model =  model # This are instance variables
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the car {self.color} {self.model}")

    def stop(self):
        print(f"You stop the car {self.color} {self.model}")

    def describe(self):
        print(f"You drive a {self.color} {self.year} {self.model} with {Car.wheel} wheel")