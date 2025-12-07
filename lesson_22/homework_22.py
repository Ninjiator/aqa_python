import random
from Models.models import Student, Course, Base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from faker import Faker

connection_string = "sqlite:///C:/Oleksii_Docs/aqa_python/lesson_22/sqllite_db"
engine = create_engine(connection_string)
fake = Faker()


def create_students(stud_num: int) -> list[Student]:
    stud_list = []
    for s in range(stud_num):
        student = Student(student_name=fake.name())
        stud_list.append(student)
    return stud_list

def create_courses() -> list[Course]:
    l_courses = [Course(course_name='Python for AQA'),
                Course(course_name='C++ for GameDev'),
                Course(course_name='Human Resources'),
                Course(course_name='Data Analysis'),
                Course(course_name='DevOps')]
    return l_courses

def allocate_students_on_course(studs_list: list[Student], courses_list: list[Course]) -> None:
    index = 0
    while index < len(studs_list):
        rand_course = random.choice(courses_list)
        rand_student = random.choice(studs_list)
        rand_student.enroll(rand_course)
        index = index + 1

def get_student_courses(session : Session, student_id: int) -> list[Course]:
    student = session.get(Student, student_id)
    if student is None:
        return []
    return student.courses

def get_course_students(session : Session, course_id : int) -> list[Student]:
    course = session.get(Course, course_id)
    if course is None:
        return []
    return course.students

def delete_course(session : Session, course_id : int) -> bool:
    course = session.get(Courses, course_id)
    if course is None:
        return False
    session.delete(course)
    session.commit()
    return True

def delete_student(session : Session, student_id : int) -> bool:
    student = session.get(Student, student_id)
    if student is None:
        return False
    session.delete(student)
    session.commit()
    return True

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    list_of_students = create_students(20)
    session.add_all(list_of_students)
    session.commit()

    list_of_courses = create_courses()
    session.add_all(list_of_courses)
    session.commit()

    allocate_students_on_course(list_of_students, list_of_courses)
    session.commit()


    print(*get_student_courses(session, 7))
    print(*get_course_students(session, 5))
