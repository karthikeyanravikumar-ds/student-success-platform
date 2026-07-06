from fastapi import FastAPI

from app.api.analytics import router as analytics_router
from app.api.applications import router as application_router
from app.api.attendance import router as attendance_router
from app.api.auth import router as auth_router
from app.api.companies import router as company_router
from app.api.dashboard import router as dashboard_router
from app.api.departments import router as department_router
from app.api.faculty import router as faculty_router
from app.api.interviews import router as interview_router
from app.api.marks import router as mark_router
from app.api.offers import router as offer_router
from app.api.placement_drives import router as placement_drive_router
from app.api.programs import router as program_router
from app.api.results import router as result_router
from app.api.roles import router as role_router
from app.api.students import router as student_router
from app.api.subjects import router as subject_router
from app.api.users import router as users_router
from app.api.reports import router as report_router
from app.exceptions.handlers import register_exception_handlers
from app.core.logging_config import logger
from app.middleware.cors import register_cors
from app.api.uploads import router as upload_router
from fastapi.staticfiles import StaticFiles
from app.api.student_certificates import router as student_certificate_router

app = FastAPI(
    title="Student Success Platform",
    version="1.0.0",
)
register_exception_handlers(app)
register_cors(app)

app.mount(
    "/files",
    StaticFiles(directory="uploads"),
    name="files",
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(student_router)
app.include_router(department_router)
app.include_router(program_router)
app.include_router(faculty_router)
app.include_router(subject_router)
app.include_router(attendance_router)
app.include_router(mark_router)
app.include_router(result_router)
app.include_router(company_router)
app.include_router(placement_drive_router)
app.include_router(application_router)
app.include_router(interview_router)
app.include_router(offer_router)
app.include_router(role_router)
app.include_router(dashboard_router)
app.include_router(analytics_router)
app.include_router(report_router)
app.include_router(upload_router)
app.include_router(student_certificate_router)

@app.get("/")
def home():
    return {
        "message": "Student Success Platform Backend Running"
    }