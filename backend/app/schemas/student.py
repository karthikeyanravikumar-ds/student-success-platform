from datetime import date
from uuid import UUID

from pydantic import BaseModel


class StudentProfile(BaseModel):
    id: UUID
    roll_no: str
    full_name: str
    gender: str | None = None
    dob: date | None = None
    phone: str | None = None
    division: str | None = None
    admission_year: int | None = None
    graduation_year: int | None = None
    current_semester: int | None = None
    profile_photo_path: str | None = None
    is_active: bool

    class Config:
        from_attributes = True


class StudentCreate(BaseModel):
    user_id: UUID
    department_id: UUID
    program_id: UUID
    roll_no: str
    full_name: str
    gender: str | None = None
    phone: str | None = None
    division: str | None = None
    admission_year: int | None = None
    graduation_year: int | None = None
    current_semester: int | None = None


class StudentResponse(StudentProfile):
    pass

class StudentUpdate(BaseModel):
    roll_no: str | None = None
    full_name: str | None = None
    gender: str | None = None
    phone: str | None = None
    division: str | None = None
    admission_year: int | None = None
    graduation_year: int | None = None
    current_semester: int | None = None
    is_active: bool | None = None