from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.interview import (
    InterviewCreate,
    InterviewResponse,
    InterviewUpdate,
)
from app.services.interview_service import (
    InterviewService,
)

router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"],
)


@router.post(
    "",
    response_model=InterviewResponse,
)
def create_interview(
    request: InterviewCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    interview = InterviewService.create(
        db,
        request,
    )

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found",
        )

    return interview


@router.get(
    "",
    response_model=list[InterviewResponse],
)
def get_interviews(
    db: Session = Depends(get_db),
):
    return InterviewService.get_all(db)


@router.get(
    "/application/{application_id}",
    response_model=list[InterviewResponse],
)
def get_application_interviews(
    application_id: UUID,
    db: Session = Depends(get_db),
):
    return InterviewService.get_by_application(
        db,
        application_id,
    )


@router.put(
    "/{interview_id}",
    response_model=InterviewResponse,
)
def update_interview(
    interview_id: UUID,
    request: InterviewUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    interview = InterviewService.update(
        db,
        interview_id,
        request,
    )

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview not found",
        )

    return interview


@router.delete(
    "/{interview_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_interview(
    interview_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    deleted = InterviewService.delete(
        db,
        interview_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Interview not found",
        )

    return None