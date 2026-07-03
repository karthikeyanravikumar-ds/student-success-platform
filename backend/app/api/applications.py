from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.application import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationUpdate,
)
from app.services.application_service import ApplicationService

router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.post(
    "/apply",
    response_model=ApplicationResponse,
)
def apply_for_drive(
    request: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Student",
            "Administrator",
        )
    ),
):
    try:
        return ApplicationService.apply(
            db,
            request,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[ApplicationResponse],
)
def get_applications(
    db: Session = Depends(get_db),
):
    return ApplicationService.get_all(db)


@router.get(
    "/student/{student_id}",
    response_model=list[ApplicationResponse],
)
def get_student_applications(
    student_id: UUID,
    db: Session = Depends(get_db),
):
    return ApplicationService.get_by_student(
        db,
        student_id,
    )


@router.get(
    "/drive/{drive_id}",
    response_model=list[ApplicationResponse],
)
def get_drive_applications(
    drive_id: UUID,
    db: Session = Depends(get_db),
):
    return ApplicationService.get_by_drive(
        db,
        drive_id,
    )


@router.put(
    "/{application_id}",
    response_model=ApplicationResponse,
)
def update_application(
    application_id: UUID,
    request: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    application = ApplicationService.update(
        db,
        application_id,
        request,
    )

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return application


@router.delete(
    "/{application_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_application(
    application_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    deleted = ApplicationService.delete(
        db,
        application_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return None