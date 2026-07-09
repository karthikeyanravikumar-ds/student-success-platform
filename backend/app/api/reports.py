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

@router.get("/marksheet/{student_id}")
def generate_marksheet(
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
    pdf = ReportService.generate_marksheet(
        db,
        student_id,
    )

    return StreamingResponse(
        BytesIO(pdf),
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            f'attachment; filename="marksheet_{student_id}.pdf"'
        },
    )


@router.get("/attendance/{student_id}")
def generate_attendance_report(
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
    pdf = ReportService.generate_attendance_report(
        db,
        student_id,
    )

    return StreamingResponse(
        BytesIO(pdf),
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            f'attachment; filename="attendance_{student_id}.pdf"'
        },
    )


@router.get("/placement/{student_id}")
def generate_placement_report(
    student_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Placement Officer",
            "Student",
        )
    ),
):
    pdf = ReportService.generate_placement_report(
        db,
        student_id,
    )

    return StreamingResponse(
        BytesIO(pdf),
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            f'attachment; filename="placement_{student_id}.pdf"'
        },
    )


@router.get("/company/{company_id}")
def generate_company_report(
    company_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Placement Officer",
        )
    ),
):
    pdf = ReportService.generate_company_report(
        db,
        company_id,
    )

    return StreamingResponse(
        BytesIO(pdf),
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            f'attachment; filename="company_{company_id}.pdf"'
        },
    )