from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/students", tags=["Students"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.get("/{student_id}", response_model=schemas.StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/", response_model=List[schemas.StudentOut])
def list_students(limit: int = Query(10, le=100), offset: int = 0, db: Session = Depends(get_db)):
    return db.query(models.Student).offset(offset).limit(limit).all()
