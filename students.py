# Class methods = Allow operation related to the class itself
#                 Take (cls) as the first parmeter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods =  Best for class-level data or require access to the class itself

class Students:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.total_gpa += 1

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name}: {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"The total students: {cls.count}"
    
    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The GPA of all students is {cls.total_gpa/ cls.count:.2f}"