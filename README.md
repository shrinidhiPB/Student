# Student Course Management API

A RESTful API built with FastAPI for managing students, courses, and enrollments.

## Features

- Student & Course creation
- Many-to-many enrollment
- Email validation
- Pagination for listing students/courses
- Error handling
- Basic unit testing
- SQLite for testing (PostgreSQL compatible)

## Setup Instructions

1. Clone repo & install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:
```bash
uvicorn app.main:app --reload
```

3. API Docs:
Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Sample curl commands

### Create Student:
```bash
curl -X POST http://localhost:8000/students/ -H "Content-Type: application/json" -d '{"name": "Alice", "email": "alice@example.com"}'
```

### Create Course:
```bash
curl -X POST http://localhost:8000/courses/ -H "Content-Type: application/json" -d '{"title": "Math 101", "description": "Intro to Math"}'
```

### Enroll Student:
```bash
curl -X POST http://localhost:8000/enroll/ -H "Content-Type: application/json" -d '{"student_id": 1, "course_id": 1}'
```

## What I Learned

- Designing a normalized database schema
- FastAPI routing and dependency injection
- Using SQLAlchemy ORM relationships
- Implementing clean validations with Pydantic
- Writing modular, testable Python code
