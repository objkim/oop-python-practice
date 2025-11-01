# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed
#                 They can contain abstract methods, which are declared but have no implementation
#                 Abstract classes benefits:
#                 1. Prevents instantiation of the class itself
#                 2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Cars(Vehicle):
   
   def go(self):
       print("You drive the car")

   def stop(self):
       print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
       print("You drive the mototcycle")

    def stop(self):
       print("You stop the motorcycle")

class Boat(Vehicle):

    def go(self):
       print("You sail the boat")

    def stop(self):
       print("You anchor the boat")