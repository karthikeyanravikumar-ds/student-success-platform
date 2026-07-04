from pydantic import BaseModel


class SubjectMark(BaseModel):
    subject_code: str
    subject_name: str
    exam_type: str
    marks_obtained: float
    max_marks: int
    grade: str


class SemesterResult(BaseModel):
    semester: int
    sgpa: float
    cgpa: float
    percentage: float


class TranscriptResponse(BaseModel):
    student_name: str
    roll_no: str
    department: str
    program: str
    current_semester: int

    semesters: list[SemesterResult]
    subjects: list[SubjectMark]