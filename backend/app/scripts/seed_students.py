from datetime import date

from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
from app.database.database import SessionLocal
from app.models.department import Department
from app.models.program import Program
from app.models.role import Role
from app.models.student import Student
from app.models.user import User


STUDENTS = [
    ("25315B2001", "Aarav Sharma"),
    ("25315B3002", "Priya Patel"),
    ("25315B3003", "Rohit Iyer"),
    ("25315B3004", "Sneha Nair"),
    ("25315B3005", "Aditya Mehta"),
    ("25315B3006", "Kavya Iyer"),
    ("25315B3007", "Rahul Verma"),
    ("25315B3008", "Ananya Rao"),
    ("25315B3009", "Arjun Kumar"),
    ("25315B3010", "Neha Singh"),
]

DEFAULT_PASSWORD = "Student@123"


def seed_students():
    db: Session = SessionLocal()

    try:

        role = (
            db.query(Role)
            .filter(Role.role_name == "Student")
            .first()
        )

        if role is None:
            print("❌ Student role not found.")
            return

        department = (
            db.query(Department)
            .filter(Department.department_code == "315")
            .first()
        )

        if department is None:
            print("❌ Department not found.")
            return

        program = (
            db.query(Program)
            .filter(Program.program_code == "BSDS")
            .first()
        )

        if program is None:
            print("❌ Program not found.")
            return

        created = 0

        for roll_no, full_name in STUDENTS:

            email = f"{roll_no.lower()}@vsit.edu.in"

            user = (
                db.query(User)
                .filter(User.email == email)
                .first()
            )

            if user is None:

                user = User(
                    role_id=role.id,
                    email=email,
                    password_hash=hash_password(DEFAULT_PASSWORD),
                    is_active=True,
                )

                db.add(user)
                db.commit()
                db.refresh(user)

            student = (
                db.query(Student)
                .filter(Student.roll_no == roll_no)
                .first()
            )

            if student:
                continue

            student = Student(
                user_id=user.id,
                department_id=department.id,
                program_id=program.id,
                roll_no=roll_no,
                full_name=full_name,
                gender=None,
                dob=None,
                phone=None,
                division="B",
                admission_year=2025,
                graduation_year=2028,
                current_semester=1,
                is_active=True,
            )

            db.add(student)
            created += 1

        db.commit()

        print(f"✅ {created} students seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_students()