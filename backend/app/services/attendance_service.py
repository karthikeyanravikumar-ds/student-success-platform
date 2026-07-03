from app.repositories.attendance_repository import AttendanceRepository
from app.schemas.attendance import AttendanceCreate, AttendanceUpdate


class AttendanceService:

    @staticmethod
    def create(db, attendance: AttendanceCreate):
        return AttendanceRepository.create(
            db,
            attendance.model_dump(),
        )

    @staticmethod
    def get_all(db):
        return AttendanceRepository.get_all(db)

    @staticmethod
    def get_by_id(db, attendance_id):
        return AttendanceRepository.get_by_id(
            db,
            attendance_id,
        )

    @staticmethod
    def get_by_student(db, student_id):
        return AttendanceRepository.get_by_student(
            db,
            student_id,
        )

    @staticmethod
    def get_by_subject(db, subject_id):
        return AttendanceRepository.get_by_subject(
            db,
            subject_id,
        )

    @staticmethod
    def get_by_faculty(db, faculty_id):
        return AttendanceRepository.get_by_faculty(
            db,
            faculty_id,
        )

    @staticmethod
    def get_by_date(db, attendance_date):
        return AttendanceRepository.get_by_date(
            db,
            attendance_date,
        )

    @staticmethod
    def update(db, attendance_id, request: AttendanceUpdate):
        attendance = AttendanceRepository.get_by_id(
            db,
            attendance_id,
        )

        if attendance is None:
            return None

        data = request.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(attendance, key, value)

        return AttendanceRepository.update(
            db,
            attendance,
        )

    @staticmethod
    def delete(db, attendance_id):
        attendance = AttendanceRepository.get_by_id(
            db,
            attendance_id,
        )

        if attendance is None:
            return False

        AttendanceRepository.delete(
            db,
            attendance,
        )

        return True