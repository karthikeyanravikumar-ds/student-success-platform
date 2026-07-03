from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.placement_drive import (
    PlacementDriveCreate,
    PlacementDriveResponse,
    PlacementDriveUpdate,
)
from app.services.placement_drive_service import (
    PlacementDriveService,
)

router = APIRouter(
    prefix="/placement-drives",
    tags=["Placement Drives"],
)


@router.post(
    "",
    response_model=PlacementDriveResponse,
)
def create_drive(
    request: PlacementDriveCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    drive = PlacementDriveService.create(
        db,
        request,
    )

    if drive is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return drive


@router.get(
    "",
    response_model=list[PlacementDriveResponse],
)
def get_drives(
    db: Session = Depends(get_db),
):
    return PlacementDriveService.get_all(db)


@router.get(
    "/{drive_id}",
    response_model=PlacementDriveResponse,
)
def get_drive(
    drive_id: UUID,
    db: Session = Depends(get_db),
):
    drive = PlacementDriveService.get_by_id(
        db,
        drive_id,
    )

    if drive is None:
        raise HTTPException(
            status_code=404,
            detail="Placement drive not found",
        )

    return drive


@router.put(
    "/{drive_id}",
    response_model=PlacementDriveResponse,
)
def update_drive(
    drive_id: UUID,
    request: PlacementDriveUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    drive = PlacementDriveService.update(
        db,
        drive_id,
        request,
    )

    if drive is None:
        raise HTTPException(
            status_code=404,
            detail="Placement drive not found",
        )

    return drive


@router.delete(
    "/{drive_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_drive(
    drive_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    deleted = PlacementDriveService.delete(
        db,
        drive_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Placement drive not found",
        )

    return None