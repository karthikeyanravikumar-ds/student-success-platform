from uuid import UUID

from pydantic import BaseModel, Field

from app.models.mark import ExamType


class MarkBase(BaseModel):
    student_id: UUID
    subject_id: UUID
    faculty_id: UUID

    semester: int = Field(..., ge=1, le=8)

    exam_type: ExamType

    max_marks: int = Field(..., gt=0)

    marks_obtained: float = Field(..., ge=0)

    remarks: str | None = None


class MarkCreate(MarkBase):
    pass


class MarkUpdate(BaseModel):
    semester: int | None = Field(None, ge=1, le=8)

    exam_type: ExamType | None = None

    max_marks: int | None = Field(None, gt=0)

    marks_obtained: float | None = Field(None, ge=0)

    remarks: str | None = None


class MarkResponse(BaseModel):
    id: UUID

    student_id: UUID
    subject_id: UUID
    faculty_id: UUID

    semester: int

    exam_type: ExamType

    max_marks: int

    marks_obtained: float

    grade: str

    remarks: str | None = None

    class Config:
        from_attributes = True