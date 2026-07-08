from pydantic import BaseModel


# ---------- Student Dashboard ----------

class StudentProfileCard(BaseModel):
    full_name: str
    roll_no: str
    department: str
    program: str
    semester: int
    division: str


class AcademicCard(BaseModel):
    current_cgpa: float
    current_semester: int
    latest_sgpa: float | None
    academic_status: str


class AttendanceCard(BaseModel):
    attendance_percentage: float
    present: int
    absent: int
    total: int


class PlacementCard(BaseModel):
    applied_drives: int
    interviews: int
    offers: int


class ResumeCard(BaseModel):
    uploaded: bool


class CertificateCard(BaseModel):
    total: int
    pending: int
    verified: int


class NotificationCard(BaseModel):
    unread: int


class StudentDashboardResponse(BaseModel):
    profile: StudentProfileCard
    academic: AcademicCard
    attendance: AttendanceCard
    placement: PlacementCard
    resume: ResumeCard
    certificates: CertificateCard
    notifications: NotificationCard


class FacultyProfileCard(BaseModel):
    full_name: str
    department: str


class FacultySubjectCard(BaseModel):
    assigned_subjects: int


class FacultyStudentCard(BaseModel):
    total_students: int


class FacultyAttendanceCard(BaseModel):
    attendance_records: int


class FacultyMarkCard(BaseModel):
    marks_uploaded: int


class FacultyResultCard(BaseModel):
    results_published: int


class FacultyNotificationCard(BaseModel):
    unread: int


class FacultyDashboardResponse(BaseModel):
    profile: FacultyProfileCard
    subjects: FacultySubjectCard
    students: FacultyStudentCard
    attendance: FacultyAttendanceCard
    marks: FacultyMarkCard
    results: FacultyResultCard
    notifications: FacultyNotificationCard


class CompanyCard(BaseModel):
    total: int


class DriveCard(BaseModel):
    active: int


class ApplicationCard(BaseModel):
    total: int
    selected: int


class PackageCard(BaseModel):
    highest: float
    average: float


class PlacementNotificationCard(BaseModel):
    unread: int


class PlacementDashboardResponse(BaseModel):
    companies: CompanyCard
    drives: DriveCard
    applications: ApplicationCard
    packages: PackageCard
    notifications: PlacementNotificationCard

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