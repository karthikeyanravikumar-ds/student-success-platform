from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.department import Department
from app.models.faculty import Faculty
from app.models.program import Program
from app.models.subject import Subject


SUBJECTS = [
    ("DS101", "Programming with Python", 1, 4),
    ("DS102", "Mathematics for Data Science", 1, 4),
    ("DS103", "Statistics", 1, 3),
    ("DS104", "Database Management Systems", 2, 4),
    ("DS105", "Data Structures", 2, 4),
    ("DS106", "Machine Learning", 3, 4),
    ("DS107", "Data Visualization", 3, 3),
    ("DS108", "Big Data Analytics", 4, 4),
    ("DS109", "Artificial Intelligence", 5, 4),
    ("DS110", "Deep Learning", 6, 4),
]


def seed_subjects():
    db: Session = SessionLocal()

    try:

        department = (
            db.query(Department)
            .filter(
                Department.department_code == "315"
            )
            .first()
        )

        if department is None:
            print("❌ Department not found.")
            return

        program = (
            db.query(Program)
            .filter(
                Program.program_code == "BSDS"
            )
            .first()
        )

        if program is None:
            print("❌ Program not found.")
            return

        faculty = db.query(Faculty).first()

        if faculty is None:
            print("❌ Faculty not found.")
            return

        created = 0

        for code, name, semester, credits in SUBJECTS:

            exists = (
                db.query(Subject)
                .filter(
                    Subject.subject_code == code
                )
                .first()
            )

            if exists:
                continue

            db.add(
                Subject(
                    department_id=department.id,
                    program_id=program.id,
                    faculty_id=faculty.id,
                    subject_code=code,
                    subject_name=name,
                    semester=semester,
                    credits=credits,
                    is_active=True,
                )
            )

            created += 1

        db.commit()

        print(f"✅ {created} subjects seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_subjects()