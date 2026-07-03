from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.students import router as student_router
from app.api.departments import router as department_router
from app.api.programs import router as program_router
from app.api.faculty import router as faculty_router
from app.api.subjects import router as subject_router
from app.api.attendance import router as attendance_router

app = FastAPI(
    title="Student Success Platform",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(student_router)
app.include_router(department_router)
app.include_router(program_router)
app.include_router(faculty_router)
app.include_router(subject_router)
app.include_router(attendance_router)

@app.get("/")
def home():
    return {
        "message": "Student Success Platform Backend Running"
    }