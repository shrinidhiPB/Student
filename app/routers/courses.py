from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/courses", tags=["Courses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    new_course = models.Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@router.get("/{course_id}", response_model=schemas.CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).get(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/", response_model=List[schemas.CourseOut])
def list_courses(limit: int = Query(10, le=100), offset: int = 0, db: Session = Depends(get_db)):
    return db.query(models.Course).offset(offset).limit(limit).all()
