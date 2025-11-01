# Class variables = Shares among all instance of a class
#                   Defined outside the constructor
#                   Allow you to share data among all object created from that class

class Student:

    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1