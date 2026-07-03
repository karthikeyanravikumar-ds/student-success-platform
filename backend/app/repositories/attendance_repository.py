from datetime import date
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.attendance import Attendance


class AttendanceRepository:

    @staticmethod
    def create(db: Session, data: dict):
        attendance = Attendance(**data)
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        return attendance

    @staticmethod
    def get_all(db: Session):
        return db.query(Attendance).all()

    @staticmethod
    def get_by_id(db: Session, attendance_id: UUID):
        return (
            db.query(Attendance)
            .filter(Attendance.id == attendance_id)
            .first()
        )

    @staticmethod
    def get_by_student(db: Session, student_id: UUID):
        return (
            db.query(Attendance)
            .filter(Attendance.student_id == student_id)
            .all()
        )

    @staticmethod
    def get_by_subject(db: Session, subject_id: UUID):
        return (
            db.query(Attendance)
            .filter(Attendance.subject_id == subject_id)
            .all()
        )

    @staticmethod
    def get_by_faculty(db: Session, faculty_id: UUID):
        return (
            db.query(Attendance)
            .filter(Attendance.faculty_id == faculty_id)
            .all()
        )

    @staticmethod
    def get_by_date(db: Session, attendance_date: date):
        return (
            db.query(Attendance)
            .filter(Attendance.attendance_date == attendance_date)
            .all()
        )

    @staticmethod
    def update(db: Session, attendance: Attendance):
        db.commit()
        db.refresh(attendance)
        return attendance

    @staticmethod
    def delete(db: Session, attendance: Attendance):
        db.delete(attendance)
        db.commit()