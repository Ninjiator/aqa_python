import faker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from faker import Faker
import random

connection_string = "sqlite:///C:/Oleksii_Docs/aqa_python/lesson_22/sqllite_db"
engine = create_engine(connection_string)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String)

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String)

class Relation(Base):
    __tablename__ = 'relations'
    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.course_id'), primary_key=True)

""""
1. Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу. 
-Переконайтеся, що ці зміни коректно відображаються у базі даних.
2. Запити до бази даних: 
-Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
3. Оновлення та видалення даних: 
-Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних."""

def init_students(stud_num : int, list_of_courses : list[Course]) -> list[Student]:
    fake = Faker()
    stud_list = []
    for s in range(stud_num):
        student = Student(student_name=fake.name())
        stud_list.append(student)
    return stud_list

def init_relations(courses : list[Course], students : list[Student]) -> list[Relation]:
    relations = []
    for student in students:
        r = Relation(student_id=random.choice(students).student_id, course_id=random.choice(courses).course_id)
        relations.append(r)
    return relations

if __name__ == '__main__':

    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    list_of_students = init_students(10)

    course_1 = Course(course_name='Python for AQA')
    course_2 = Course(course_name='C++ for GameDev')
    course_3 = Course(course_name='Human Resources')
    course_4 = Course(course_name='Data Analysis')
    course_5 = Course(course_name='DevOps')


    session.add_all(list_of_students)
    session.add_all([course_1, course_2, course_3, course_4, course_5])
    session.commit()

    list_of_courses = session.query(Course).all()

    relation_1 = Relation(student_id=(random.choice(list_of_students)).student_id,
                          course_id=list_of_courses[0].course_id)

    relation_2 = Relation(student_id=(random.choice(list_of_students)).student_id,
                          course_id=(random.choice(list_of_courses)).course_id)


    session.add_all([relation_1, relation_2])
    session.commit()