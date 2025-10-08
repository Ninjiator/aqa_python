class Student:
    def __init__(self, first_name, last_name, age, average_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_mark = average_mark

    def set_average_mark(self, average_mark):
        self.average_mark = average_mark

student_1 = Student("Marko", "Polo", 28, 88)
student_1.set_average_mark(95)
print(student_1.average_mark)
