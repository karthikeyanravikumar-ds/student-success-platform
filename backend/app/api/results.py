from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.result import ResultCreate, ResultResponse
from app.services.result_service import ResultService

router = APIRouter(
    prefix="/results",
    tags=["Results"],
)


@router.post(
    "/generate",
    response_model=ResultResponse,
)
def generate_result(
    request: ResultCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Faculty",
        )
    ),
):
    return ResultService.generate(
        db,
        request,
    )


@router.get(
    "",
    response_model=list[ResultResponse],
)
def get_results(
    db: Session = Depends(get_db),
):
    return ResultService.get_all(db)


@router.get(
    "/{result_id}",
    response_model=ResultResponse,
)
def get_result(
    result_id: UUID,
    db: Session = Depends(get_db),
):
    result = ResultService.get_by_id(
        db,
        result_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Result not found",
        )

    return result


@router.get(
    "/student/{student_id}",
    response_model=list[ResultResponse],
)
def get_student_results(
    student_id: UUID,
    db: Session = Depends(get_db),
):
    return ResultService.get_by_student(
        db,
        student_id,
    )


@router.get(
    "/semester/{semester}",
    response_model=list[ResultResponse],
)
def get_semester_results(
    semester: int,
    db: Session = Depends(get_db),
):
    return ResultService.get_by_semester(
        db,
        semester,
    )


@router.delete(
    "/{result_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_result(
    result_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    deleted = ResultService.delete(
        db,
        result_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Result not found",
        )

    return None