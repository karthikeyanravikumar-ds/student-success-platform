from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.analytics import (
    AttendanceAnalyticsResponse,
    DepartmentAnalyticsItem,
    PackageAnalyticsResponse,
    PlacementAnalyticsResponse,
    ResultAnalyticsResponse,
)
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/placement",
    response_model=PlacementAnalyticsResponse,
)
def placement_analytics(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Placement Officer",
        )
    ),
):
    return AnalyticsService.placement_analytics(db)


@router.get(
    "/attendance",
    response_model=AttendanceAnalyticsResponse,
)
def attendance_analytics(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Faculty",
        )
    ),
):
    return AnalyticsService.attendance_analytics(db)


@router.get(
    "/results",
    response_model=ResultAnalyticsResponse,
)
def result_analytics(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Faculty",
        )
    ),
):
    return AnalyticsService.result_analytics(db)


@router.get(
    "/packages",
    response_model=PackageAnalyticsResponse,
)
def package_analytics(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
            "Placement Officer",
        )
    ),
):
    return AnalyticsService.package_analytics(db)


@router.get(
    "/departments",
    response_model=list[DepartmentAnalyticsItem],
)
def department_analytics(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
        )
    ),
):
    return AnalyticsService.department_analytics(db)