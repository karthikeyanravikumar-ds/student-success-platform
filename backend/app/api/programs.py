from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.program import (
    ProgramCreate,
    ProgramResponse,
    ProgramUpdate,
)
from app.services.program_service import ProgramService

router = APIRouter(
    prefix="/programs",
    tags=["Programs"],
)


@router.get(
    "",
    response_model=list[ProgramResponse],
)
def get_programs(
    db: Session = Depends(get_db),
):
    return ProgramService.get_all(db)


@router.get(
    "/{program_id}",
    response_model=ProgramResponse,
)
def get_program(
    program_id: UUID,
    db: Session = Depends(get_db),
):
    program = ProgramService.get_by_id(
        db,
        program_id,
    )

    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found",
        )

    return program


@router.post(
    "",
    response_model=ProgramResponse,
)
def create_program(
    program: ProgramCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    return ProgramService.create(
        db,
        program,
    )


@router.put(
    "/{program_id}",
    response_model=ProgramResponse,
)
def update_program(
    program_id: UUID,
    request: ProgramUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    program = ProgramService.update(
        db,
        program_id,
        request,
    )

    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found",
        )

    return program


@router.delete(
    "/{program_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_program(
    program_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    deleted = ProgramService.delete(
        db,
        program_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found",
        )

    return None