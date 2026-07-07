from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from io import BytesIO

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get("/transcript/{student_id}")
def generate_transcript(
    student_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Faculty",
            "Placement Officer",
            "Student",
        )
    ),
):
    pdf = ReportService.generate_transcript(
        db,
        student_id,
    )

    return StreamingResponse(
        BytesIO(pdf),
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            f'attachment; filename="transcript_{student_id}.pdf"'
        },
    )