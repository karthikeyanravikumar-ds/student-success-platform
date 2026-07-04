from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.dashboard import (
    AdminDashboardResponse,
    FacultyDashboardResponse,
    PlacementDashboardResponse,
    StudentDashboardResponse,
)
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/admin",
    response_model=AdminDashboardResponse,
)
def admin_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    return DashboardService.get_admin_dashboard(db)


@router.get(
    "/faculty",
    response_model=FacultyDashboardResponse,
)
def faculty_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Faculty")),
):
    return DashboardService.get_faculty_dashboard(db)


@router.get(
    "/student",
    response_model=StudentDashboardResponse,
)
def student_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Student")),
):
    return DashboardService.get_student_dashboard(db)


@router.get(
    "/placement",
    response_model=PlacementDashboardResponse,
)
def placement_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Placement Officer")),
):
    return DashboardService.get_placement_dashboard(db)