# Multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# Multilevel inheritance = inherit form a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
    pass

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
    pass

class Rabbit(Predator):
    pass

class Hawk(Prey):
    pass

class Fish(Prey, Predator):
    pass