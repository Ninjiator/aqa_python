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

class Diamond:
    def __init__(self, side, angle_a):
        self.side = float(side)
        self.angle_a = angle_a
        self.__angle_b = 180.0 - angle_a


    def get_angle_b(self):
        return self.__angle_b

    def get_angle_a(self):
        return self.angle_a

    def __setattr__(self, name, value):
        if name == 'side':
            if value <= 0:
                raise AttributeError(f'self.side should be bigger that zero')
            else:
                object.__setattr__(self, name, value)
        elif name == 'angle_a':
            if value <= 0:
                raise AttributeError(f'angle_a should be bigger that zero')
            elif value >= 180:
                raise AttributeError(f'angle_a cannot be bigger than 179')
            else:
                object.__setattr__(self, name, value)
                self.__angle_b = 180.0 - self.angle_a
        elif name == '__angle_b' and value + self.angle_a > 180:
            raise AttributeError(f'angle_a + angle_a cannot be > 180')
        else:
            object.__setattr__(self, name, value)

    def __str__(self):
        return f'side is {self.side}, angle_a is {self.angle_a}, angle_b is {self.__angle_b}'


#Task from HM8
class Student:
    def __init__(self, first_name, last_name, age, average_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__average_mark = average_mark

    def set_average_mark(self, average_mark):
        self.__average_mark = average_mark

    def get_average_mark(self):
        return self.__average_mark

#Tasks from HM7

def sum_of_two_numbers(number1, number2):
    return number1 + number2

def average_in_list(list_numbers):
    return sum(list_numbers) / len(list_numbers)

def reverse_the_string(string):
    reversed_string = string[::-1]
    return reversed_string

def get_the_longest_word(list_of_words):
     sorted_list = sorted(list_of_words, key=len, reverse=True)
     return sorted_list[0]

#Task from HM 6.4
def sum_of_even_numbers_in_list(list_of_numbers):
    summ = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            summ += number
    return summ

#Task from HM 6.3
def eject_str_from_list(lst):
    lst2 = []
    for k in lst:
        if type(k) == str:
            lst2.append(k)
    return lst2