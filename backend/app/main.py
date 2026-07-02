from app.models import Role
from fastapi import FastAPI

from app.auth.routes import router as auth_router

app = FastAPI(
    title="Student Success Platform",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Student Success Platform Backend Running"
    }