from Models.models import Student, Course, Relation, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random

connection_string = "sqlite:///C:/Oleksii_Docs/aqa_python/lesson_22/sqllite_db"
engine = create_engine(connection_string)

""""
1. Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу. 
-Переконайтеся, що ці зміни коректно відображаються у базі даних.
2. Запити до бази даних: 
-Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
3. Оновлення та видалення даних: 
-Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних."""

def init_students(stud_num : int) -> list[Student]:
    fake = Faker()
    stud_list = []
    for s in range(stud_num):
        student = Student(student_name=fake.name())
        stud_list.append(student)
    return stud_list

def init_courses() -> list[Course]:
    l_courses = [Course(course_name='Python for AQA'),
                       Course(course_name='C++ for GameDev'),
                       Course(course_name='Human Resources'),
                       Course(course_name='Data Analysis'),
                       Course(course_name='DevOps')]
    return l_courses

def init_relations(courses : list[Course], students : list[Student]) -> list[Relation]:
    relations = []
    for student in students:
        r = Relation(s_id=student.student_id, c_id=random.choice(courses).course_id)
        relations.append(r)
    return relations


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    list_of_students = init_students(20)
    session.add_all(list_of_students)
    session.commit()

    list_of_courses = init_courses()
    session.add_all(list_of_courses)
    session.commit()

    list_of_relations = init_relations(list_of_courses, list_of_students)
    session.add_all(list_of_relations)
    session.commit()