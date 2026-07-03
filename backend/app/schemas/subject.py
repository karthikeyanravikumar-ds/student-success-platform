from uuid import UUID

from pydantic import BaseModel


class SubjectCreate(BaseModel):
    department_id: UUID
    program_id: UUID
    faculty_id: UUID
    subject_code: str
    subject_name: str
    semester: int
    credits: int


class SubjectUpdate(BaseModel):
    subject_name: str | None = None
    semester: int | None = None
    credits: int | None = None
    faculty_id: UUID | None = None
    is_active: bool | None = None


class SubjectResponse(BaseModel):
    id: UUID
    department_id: UUID
    program_id: UUID
    faculty_id: UUID
    subject_code: str
    subject_name: str
    semester: int
    credits: int
    is_active: bool

    class Config:
        from_attributes = True