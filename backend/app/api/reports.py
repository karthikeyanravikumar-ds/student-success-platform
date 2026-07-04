from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.report import TranscriptResponse
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get(
    "/student/{student_id}/transcript",
    response_model=TranscriptResponse,
)
def student_transcript(
    student_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Faculty",
            "Student",
        )
    ),
):

    report = ReportService.get_student_transcript(
        db,
        student_id,
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return report