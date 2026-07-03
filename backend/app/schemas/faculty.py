from datetime import date
from uuid import UUID

from pydantic import BaseModel


class FacultyCreate(BaseModel):
    user_id: UUID
    department_id: UUID
    employee_id: str
    full_name: str
    designation: str
    qualification: str | None = None
    phone: str | None = None
    joining_date: date | None = None


class FacultyUpdate(BaseModel):
    full_name: str | None = None
    designation: str | None = None
    qualification: str | None = None
    phone: str | None = None
    joining_date: date | None = None
    is_active: bool | None = None


class FacultyResponse(BaseModel):
    id: UUID
    user_id: UUID
    department_id: UUID
    employee_id: str
    full_name: str
    designation: str
    qualification: str | None = None
    phone: str | None = None
    joining_date: date | None = None
    is_active: bool

    class Config:
        from_attributes = True