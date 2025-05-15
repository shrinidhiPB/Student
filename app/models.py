from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

enrollment_table = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
    Column("enrolled_on", DateTime, default=datetime.utcnow)
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    courses = relationship("Course", secondary=enrollment_table, back_populates="students")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    students = relationship("Student", secondary=enrollment_table, back_populates="courses")
