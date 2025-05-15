from fastapi import FastAPI
from .routers import students, courses, enrollments
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Course Management API")

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)
