from uuid import UUID
from fastapi import File, UploadFile
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.subject import (
    SubjectCreate,
    SubjectResponse,
    SubjectUpdate,
)
from app.services.subject_service import SubjectService

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"],
)


@router.get(
    "",
    response_model=list[SubjectResponse],
)
def get_subjects(
    db: Session = Depends(get_db),
):
    return SubjectService.get_all(db)


@router.get(
    "/{subject_id}",
    response_model=SubjectResponse,
)
def get_subject(
    subject_id: UUID,
    db: Session = Depends(get_db),
):
    subject = SubjectService.get_by_id(
        db,
        subject_id,
    )

    if subject is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Subject not found",
        )

    return subject


@router.post(
    "",
    response_model=SubjectResponse,
)
def create_subject(
    subject: SubjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    return SubjectService.create(
        db,
        subject,
    )


@router.put(
    "/{subject_id}",
    response_model=SubjectResponse,
)
def update_subject(
    subject_id: UUID,
    request: SubjectUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    subject = SubjectService.update(
        db,
        subject_id,
        request,
    )

    if subject is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Subject not found",
        )

    return subject


@router.delete(
    "/{subject_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_subject(
    subject_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    deleted = SubjectService.delete(
        db,
        subject_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Subject not found",
        )

    return None

@router.post(
    "/{student_id}/resume",
    summary="Upload Student Resume",
)
def upload_student_resume(
    student_id: UUID,
    file: UploadFile = File(...),
    db=Depends(get_db),
):
    student = StudentService.upload_resume(
        db,
        student_id,
        file,
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return {
        "message": "Resume uploaded successfully",
        "student": student,
    }