import unicodeit
from car import Car # Class and Object (Line 18) 
from student import Student # Class Variable (Line 31)
from animal import Dog, Cat, Mouse # Inheritance (Line 45)
from animal_kingdom import Rabbit, Hawk, Fish # Multiple inheritance and Multilevel inheritance (Line 56)
from vehicle import Cars, Motorcycle, Boat # Abstract class (Line 72)
from shape import Circle, Square, Triangle # super() (Line 84) 
from shapes import Circles, Squares, Triangles, Pizza # Polymorphism (Line 95)
from animal_car import Dogss, Catss, Carss # "Duck typing" (Line 102)
from library import Library, Books # Aggregation (Line 110)
from car_parts import CarPart # Compostion (Line 125)
from company import Company # Nested class (Line 135)
from employee import Employee # Static method (Line 148)
from students import Students # Class methods (Line 160)
from books import Bookss # Magic methods (Line 174)
from rectangle import Rectangle # @property (Line 186)

# Class and Object 
print("Class and Object")
cars = [
    Car("Mustang", 2004, "Red", False),
    Car("Cotvette", 2025, "Blue", True),
    Car("Charger", 2026, "Yellow", True)
]
for all_cars in cars:
    all_cars.drive()
    all_cars.stop()
    all_cars.describe()
print("")

# Class Variable
print("Class Variable")
students = [
    Student("Spongebob", 30),
    Student("Patrick", 35),
    Student("Squidward", 55),
    Student("Sandy", 27)
]
for _ in range(1):
    for all_students in students:
        print(f"The total students is {all_students.num_students}")
        break
print("")

# Inheritance
print("Inheritance")
animals = [
    Dog("Scoody"),
    Cat("Garfield"),
    Mouse("Mickey")
]
for all_animals in animals:
    all_animals.speak()
print("")

# Multiple inheritance and Multilevel inheritance
print("Multiple inheritance and Multilevel inheritance")
animals1 = [
    Rabbit("Bugs"),
    Hawk("Tony"),
    Fish("Nemo"),
]
for all_animals1 in animals1:
    all_animals1.eat()
    all_animals1.sleep()
    if hasattr(all_animals1, "hunt"):
        all_animals1.hunt()
    if hasattr(all_animals1, "flee"):
        all_animals1.flee()
print("")

# Abstract class
print("Abstract class")
vehicles = [
    Cars(),
    Motorcycle(),
    Boat()
]
for all_vehicles in vehicles:
    all_vehicles.go()
    all_vehicles.stop()
print("")

# super() 
print("Super()")
shapes = [
    Circle("Green", False, 5),
    Square("Blue", True, 6),
    Triangle("Red", True, 5, 8)
]
for all_shapes in shapes:
    all_shapes.describe()
print("")

# Polymorphism 
print("Polymorphism")
shapes1 = [Circles(5), Squares(8), Triangles(8, 2), Pizza("Peppro", 9)]
for areas in shapes1:
    print(unicodeit.replace(f"{areas.area()}cm^2"))
print("")

# "Duck typing" 
print('"Duck typing"')
animals2 = [Dogss(), Catss(), Carss()]
for animal in animals2:
    animal.speak()
    print(animal.alive)
print("")

# Aggregation
print("Aggregation")
library =  Library("New York Public Library")
books = [
    Books("Harry Potter....", "J.K. Rowling"),
    Books("The Hobbit", "J. R. R. Tolkein"),
    Books("The Colour of Magic", "Terry Pratchet")
]
print(f"{library.name}")
for all_books in books:
    library.add_book(all_books)
for list_books in library.list_books():
    print(list_books)
print("")

# Compostion  
print("Compostion")
cars = [
    CarPart("Ford", "Mustang", 500, 18),
    CarPart("Chevrolet", "Corvette", 670, 19)
    ]
for all_cars in cars:
    print(all_cars.display_car())
print("")

# Nested class 
print("Nested class ")
company1 = Company("Krusty Krab")
company2 = Company("Chum Bucket")
company1.add_employee("Engene", "Manager")
company1.add_employee("Spongebob", "Cook")
company1.add_employee("Squidward", "Cashier")
company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")
for employee1, employee2 in zip(company1.list_employees(), company2.list_employees()):
    print(f"{employee1} | {employee2}")
print("")

# Static method
print("Static method")
employee = [
    Employee("Eugeune", "Manager"),
    Employee("Squidward", "Cashier"),
    Employee("Spongebob", "Cook"),
    Employee("Sandy", "Rocket Science`s")
    ]   
for all_employee in employee:
    print(all_employee.get_info())
print("")

# Class methods
print("Class methods")
students1 = [
    Students("Spongebob", 3.2),
    Students("Patrick", 2.0),
    Students("Sandy", 4.0)
]
for all_students1 in students1:
    print(all_students1.get_info())
for _ in range(1):
    print(Students.get_count())
    print(Students.get_average())
print("")

# Magic methods
print("Magic methods")
books1 = [
    Bookss("The Hobbit", "J.R.R. Tolkien", 310),
    Bookss("Harry Potter and The Philosopher`s ", "J.K Rowling", 223),
    Bookss("The Lion", "C.s. Lewis", 172)
]
for all_books1 in books1:
    print("The Hobbit" in all_books1)
    print (all_books1['title'])
print("")

# @property
print("@property")
rectangle = Rectangle(3, 4)
rectangle.width = 6
rectangle.height = 7
print(rectangle.width)
print(rectangle.height)
del rectangle.width
del rectangle.height