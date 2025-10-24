
class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)

class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)

class Developer(Employee):
    def __init__(self, programing_language, **kwargs):
        self.programing_language = programing_language
        super().__init__(**kwargs)

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programing_language, team_size):
        self.team_size = team_size
        super().__init__(name=name, salary=salary, department = department, programing_language = programing_language,)

print("Task 1: MRO for TeamLead :\n", TeamLead.__mro__)
lead = TeamLead("Darrel", 20000, "Development", "C++", 5)



from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
        self.name = "Circle"

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def area(self):
        return math.pi * self.__radius * self.__radius

class Square(Figure):
    def __init__(self, side):
        self.__side = side
        self.name = "Square"

    def perimeter(self):
        return 2 * self.__side

    def area(self):
        return self.__side * self.__side

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.name = "Rectangle"

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def area(self):
        return self.__width * self.__height

circle = Circle(5.0)
square = Square(4.0)
rectangle = Rectangle(3.5, 6.0)
list_of_figures = [circle, square, rectangle]

for fig in list_of_figures:
    print(f'Perimeter of {fig.name} is {fig.perimeter()}, area of {fig.name} is {fig.area()}')