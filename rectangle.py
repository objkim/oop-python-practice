# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self.__width = width # private attribute
        self.__height = height # private attribute

    @property
    def width(self):
        return f"{self.__width:.1f}cm"

    @property
    def height(self):
        return f"{self.__height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than zero")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Width must be greater than zero")

    @width.deleter
    def width(self):
        del self.__width
        print("Width has has been deleted")


    @height.deleter
    def height(self):
        del self.__height
        print("Height has has been deleted")