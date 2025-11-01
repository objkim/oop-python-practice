# Static method = A method that belong to a class rather than any object from that class (instance)
#                 Usually used for general utility function

# Instance methods = Best for operation on instances of the class (objects)
# Static methods = Best for utility function that do not need access to class data

class Employee:

    def __init__(self, name, postion):
        self.name = name
        self.position = postion
        self.is_vaild_position(postion)

    def get_info(self):
        return f"{self.name}: {self.position} The is {self.is_vaild_position(self.position)}"
    
    @staticmethod
    def is_vaild_position(postion):
        vaild_postion = ["Manager", "Cashier", "Cook", "Janitor"]
        return postion in vaild_postion