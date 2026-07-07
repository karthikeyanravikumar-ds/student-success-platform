from datetime import date

from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
from app.database.database import SessionLocal
from app.models.department import Department
from app.models.faculty import Faculty
from app.models.role import Role
from app.models.user import User


FACULTY_EMAIL = "faculty@vsit.edu.in"
FACULTY_PASSWORD = "Faculty@123"


def seed_faculty():
    db: Session = SessionLocal()

    try:

        role = (
            db.query(Role)
            .filter(Role.role_name == "Faculty")
            .first()
        )

        if role is None:
            print("❌ Faculty role not found.")
            return

        department = (
            db.query(Department)
            .filter(Department.department_code == "315")
            .first()
        )

        if department is None:
            print("❌ Department not found.")
            return

        user = (
            db.query(User)
            .filter(User.email == FACULTY_EMAIL)
            .first()
        )

        if user is None:

            user = User(
                role_id=role.id,
                email=FACULTY_EMAIL,
                password_hash=hash_password(FACULTY_PASSWORD),
                is_active=True,
            )

            db.add(user)
            db.commit()
            db.refresh(user)

        faculty = (
            db.query(Faculty)
            .filter(Faculty.user_id == user.id)
            .first()
        )

        if faculty:
            print("ℹ️ Faculty already exists.")
            return

        faculty = Faculty(
            user_id=user.id,
            department_id=department.id,
            employee_id="VSITF001",
            full_name="Demo Faculty",
            designation="Assistant Professor",
            qualification="M.Sc Data Science",
            phone="9876543210",
            joining_date=date(2024, 6, 1),
            is_active=True,
        )

        db.add(faculty)
        db.commit()

        print("✅ Faculty seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_faculty()