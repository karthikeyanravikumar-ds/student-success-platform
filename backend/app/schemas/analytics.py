from pydantic import BaseModel


class PlacementAnalyticsResponse(BaseModel):
    total_students: int
    placed_students: int
    placement_percentage: float
    active_drives: int
    total_companies: int


class AttendanceAnalyticsResponse(BaseModel):
    overall_attendance: float
    present: int
    absent: int
    late: int
    leave: int


class ResultAnalyticsResponse(BaseModel):
    average_cgpa: float
    highest_cgpa: float
    pass_percentage: float
    failed_students: int


class PackageAnalyticsResponse(BaseModel):
    highest_package: float
    lowest_package: float
    average_package: float


class DepartmentAnalyticsItem(BaseModel):
    department_name: str
    total_students: int
    placed_students: int
    placement_percentage: float