import random
from datetime import date, timedelta

from app.database.database import SessionLocal
from app.models.attendance import Attendance, AttendanceStatus
from app.models.student import Student
from app.models.subject import Subject


def seed_attendance():
    db = SessionLocal()

    try:
        students = db.query(Student).filter(Student.is_active == True).all()

        if not students:
            print("No students found.")
            return

        total_records = 0

        for student in students:

            subjects = (
                db.query(Subject)
                .filter(
                    Subject.program_id == student.program_id,
                    Subject.semester == student.current_semester,
                    Subject.is_active == True,
                )
                .all()
            )

            if not subjects:
                continue

            for subject in subjects:

                for day in range(30):

                    attendance_date = (
                        date.today() - timedelta(days=day)
                    )

                    if attendance_date.weekday() >= 5:
                        continue

                    status = random.choices(
                        [
                            AttendanceStatus.PRESENT,
                            AttendanceStatus.ABSENT,
                            AttendanceStatus.LATE,
                            AttendanceStatus.LEAVE,
                        ],
                        weights=[85, 10, 3, 2],
                        k=1,
                    )[0]

                    attendance = Attendance(
                        student_id=student.id,
                        subject_id=subject.id,
                        faculty_id=subject.faculty_id,
                        attendance_date=attendance_date,
                        status=status,
                        remarks=None,
                    )

                    db.add(attendance)
                    total_records += 1

        db.commit()

        print(f"Successfully inserted {total_records} attendance records.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_attendance()