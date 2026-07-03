from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.mark import MarkCreate, MarkResponse, MarkUpdate
from app.services.mark_service import MarkService

router = APIRouter(
    prefix="/marks",
    tags=["Marks"],
)


@router.post(
    "",
    response_model=MarkResponse,
)
def create_mark(
    request: MarkCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Faculty",
        )
    ),
):
    return MarkService.create(
        db,
        request,
    )


@router.get(
    "",
    response_model=list[MarkResponse],
)
def get_marks(
    db: Session = Depends(get_db),
):
    return MarkService.get_all(db)


@router.get(
    "/{mark_id}",
    response_model=MarkResponse,
)
def get_mark(
    mark_id: UUID,
    db: Session = Depends(get_db),
):
    mark = MarkService.get_by_id(
        db,
        mark_id,
    )

    if mark is None:
        raise HTTPException(
            status_code=404,
            detail="Mark not found",
        )

    return mark


@router.get(
    "/student/{student_id}",
    response_model=list[MarkResponse],
)
def get_student_marks(
    student_id: UUID,
    db: Session = Depends(get_db),
):
    return MarkService.get_by_student(
        db,
        student_id,
    )


@router.get(
    "/subject/{subject_id}",
    response_model=list[MarkResponse],
)
def get_subject_marks(
    subject_id: UUID,
    db: Session = Depends(get_db),
):
    return MarkService.get_by_subject(
        db,
        subject_id,
    )


@router.get(
    "/faculty/{faculty_id}",
    response_model=list[MarkResponse],
)
def get_faculty_marks(
    faculty_id: UUID,
    db: Session = Depends(get_db),
):
    return MarkService.get_by_faculty(
        db,
        faculty_id,
    )


@router.get(
    "/semester/{semester}",
    response_model=list[MarkResponse],
)
def get_semester_marks(
    semester: int,
    db: Session = Depends(get_db),
):
    return MarkService.get_by_semester(
        db,
        semester,
    )


@router.put(
    "/{mark_id}",
    response_model=MarkResponse,
)
def update_mark(
    mark_id: UUID,
    request: MarkUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Faculty",
        )
    ),
):
    mark = MarkService.update(
        db,
        mark_id,
        request,
    )

    if mark is None:
        raise HTTPException(
            status_code=404,
            detail="Mark not found",
        )

    return mark


@router.delete(
    "/{mark_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_mark(
    mark_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
        )
    ),
):
    deleted = MarkService.delete(
        db,
        mark_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Mark not found",
        )

    return None