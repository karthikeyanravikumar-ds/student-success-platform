from uuid import UUID

from pydantic import BaseModel, Field

from app.models.result import ResultStatus


class ResultCreate(BaseModel):
    student_id: UUID
    semester: int = Field(..., ge=1, le=8)


class ResultResponse(BaseModel):
    id: UUID

    student_id: UUID

    semester: int

    total_marks: float

    total_max_marks: float

    percentage: float

    sgpa: float

    cgpa: float

    result_status: ResultStatus

    rank: int | None = None

    remarks: str | None = None

    class Config:
        from_attributes = True