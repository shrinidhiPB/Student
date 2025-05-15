from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/enroll", tags=["Enrollments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def enroll_student(enrollment: schemas.Enrollment, db: Session = Depends(get_db)):
    student = db.query(models.Student).get(enrollment.student_id)
    course = db.query(models.Course).get(enrollment.course_id)
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    if course in student.courses:
        raise HTTPException(status_code=400, detail="Already enrolled")
    student.courses.append(course)
    db.commit()
    return {"message": "Enrollment successful"}
