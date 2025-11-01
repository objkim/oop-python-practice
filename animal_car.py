# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimun necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dogss(Animal):
    def speak(self):
        print("WOOF")

class Catss(Animal):
    def speak(self):
        print("MEOW")

class Carss:

    alive = True

    def speak(self):
        print("HONK")