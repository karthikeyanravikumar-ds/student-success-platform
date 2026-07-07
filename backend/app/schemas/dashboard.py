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

#

class StudentStats(BaseModel):
    total: int
    active: int
    inactive: int


class FacultyStats(BaseModel):
    total: int


class AcademicStats(BaseModel):
    departments: int
    programs: int
    subjects: int


class PlacementStats(BaseModel):
    companies: int
    active_drives: int
    applications: int
    offers: int


class CertificateStats(BaseModel):
    pending: int
    verified: int
    rejected: int


class NotificationStats(BaseModel):
    sent: int


class AdminDashboardResponse(BaseModel):
    students: StudentStats
    faculty: FacultyStats
    academic: AcademicStats
    placement: PlacementStats
    certificates: CertificateStats
    notifications: NotificationStats