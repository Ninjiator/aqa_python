from __future__ import annotations                                      # to resolve forward reference in annotations
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


student_course_table = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.student_id"), primary_key=True),
    Column("course_id", ForeignKey("courses.course_id"), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String)
    courses = relationship(
        'Course',
        secondary=student_course_table,
        back_populates='students')

    def __str__(self):
        course_names = [course.course_name for course in self.courses]
        return (
            f"Student:\n"
            f"  id: {self.student_id}\n"
            f"  name: {self.student_name}\n"
            f"  courses: {course_names}\n"
        )

    def enroll(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def drop(self, course : Course) -> None:
        if course in self.courses:
            self.courses.remove(course)

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String)
    students = relationship(
        'Student',
        secondary=student_course_table,
        back_populates='courses')

    def __str__(self):
        student_names = [student.student_name for student in self.students]
        return (
            f"Course:\n"
            f"  id: {self.course_id}\n"
            f"  name: {self.course_name}\n"
            f"  students: {student_names}\n"
        )



