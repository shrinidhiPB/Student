from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import List, Optional

class CourseBase(BaseModel):
    title: str
    description: str

    @validator("title")
    def title_must_have_min_length(cls, v):
        if len(v) < 3:
            raise ValueError("Course title must be at least 3 characters long")
        return v

class CourseCreate(CourseBase): pass

class StudentBase(BaseModel):
    name: str
    email: EmailStr

    @validator("name")
    def name_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Name cannot be empty")
        return v

class StudentCreate(StudentBase): pass

class StudentOut(StudentBase):
    id: int
    courses: List[int] = []
    class Config: orm_mode = True

class CourseOut(CourseBase):
    id: int
    students: List[int] = []
    class Config: orm_mode = True

class Enrollment(BaseModel):
    student_id: int
    course_id: int
