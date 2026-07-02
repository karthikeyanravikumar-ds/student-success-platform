from app.models import Role
from fastapi import FastAPI

app = FastAPI(
    title="Student Success Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Student Success Platform Backend Running"
    }