from pydantic import BaseModel


class StudentDashboardResponse(BaseModel):
    attendance_percentage: float
    current_cgpa: float
    current_semester: int
    applied_drives: int
    interviews: int
    offers: int


class FacultyDashboardResponse(BaseModel):
    assigned_subjects: int
    total_students: int
    attendance_records: int
    marks_uploaded: int
    results_published: int


class PlacementDashboardResponse(BaseModel):
    total_companies: int
    active_drives: int
    total_applications: int
    selected_students: int
    highest_package: float
    average_package: float


class AdminDashboardResponse(BaseModel):
    total_students: int
    total_faculty: int
    total_departments: int
    total_programs: int
    total_users: int
    attendance_percentage: float
    placement_percentage: float