import csv
from pathlib import Path

from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
from app.database.database import SessionLocal
from app.models.department import Department
from app.models.program import Program
from app.models.role import Role
from app.models.student import Student
from app.models.user import User

CSV_FILE = Path("app/seed_data/students_dataset_draft_1.csv")

DEFAULT_PASSWORD = "Student@123"
DEFAULT_ADMISSION_YEAR = 2024
DEFAULT_GRADUATION_YEAR = 2027


def get_semester(year: str) -> int:
    year = (year or "").strip().upper()

    mapping = {
        "FY": 1,
        "SY": 3,
        "TY": 5,
    }

    return mapping.get(year, 1)


def clean_phone(phone: str) -> str:
    """
    Converts:
        9876543210.0 -> 9876543210
        +91-9876543210 -> 919876543210
    """
    return "".join(filter(str.isdigit, phone or ""))


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

        created = 0
        skipped = 0

        with CSV_FILE.open(
            mode="r",
            encoding="utf-8-sig",
            newline="",
        ) as csvfile:

            reader = csv.DictReader(csvfile)
            print("Reader fieldnames:", reader.fieldnames)
            print("CSV exists:", CSV_FILE.exists())
            print("CSV path:", CSV_FILE.resolve())

            # Debug: show first line of the file
            csvfile.seek(0)
            print("First line:", repr(csvfile.readline()))
            print("Raw fieldnames:", reader.fieldnames)
            print("Fieldnames type:", type(reader.fieldnames))

            if reader.fieldnames is None:
                print("❌ CSV has no headers.")
                return

            reader.fieldnames = [
                str(field).strip()
                for field in reader.fieldnames
            ]

            print("Processed fieldnames:", reader.fieldnames)

            for index, row in enumerate(reader, start=1):

                cleaned_row = {}

                for key, value in row.items():

                    key = str(key).strip() if key else ""

                    if isinstance(value, list):
                        value = ",".join(str(v).strip() for v in value)
                    else:
                        value = str(value).strip() if value else ""

                    cleaned_row[key] = value

                row = cleaned_row

                print(f"Processing row {index}...")

                roll_no = row.get("ROLL NO", "")
                full_name = row.get("Name", "")
                email = row.get("Email", "").lower()
                phone = clean_phone(row.get("Phone", ""))
                semester = get_semester(row.get("Year", ""))
                division = row.get("Division", "A") or "A"

                # ---------------------------
                # Validation
                # ---------------------------

                if not roll_no:
                    print(f"⚠️ Row {index}: Roll number missing.")
                    skipped += 1
                    continue

                if not email:
                    print(f"⚠️ {roll_no}: Email missing.")
                    skipped += 1
                    continue

                if not email.endswith("@vsit.edu.in"):
                    print(f"⚠️ {roll_no}: Invalid VSIT email -> {email}")
                    skipped += 1
                    continue

                # ---------------------------
                # User
                # ---------------------------

                user = (
                    db.query(User)
                    .filter(User.email == email)
                    .first()
                )

                if user:

                    if user.role_id != role.id:
                        print(
                            f"⚠️ {email} already exists with another role."
                        )
                        skipped += 1
                        continue

                else:

                    user = User(
                        role_id=role.id,
                        email=email,
                        password_hash=hash_password(
                            DEFAULT_PASSWORD
                        ),
                        is_active=True,
                    )

                    db.add(user)
                    db.flush()

                # ---------------------------
                # Student
                # ---------------------------

                student = (
                    db.query(Student)
                    .filter(Student.roll_no == roll_no)
                    .first()
                )

                if student:
                    print(f"⚠️ Student {roll_no} already exists.")
                    skipped += 1
                    continue

                student = Student(
                    user_id=user.id,
                    department_id=department.id,
                    program_id=program.id,
                    roll_no=roll_no,
                    full_name=full_name,
                    gender=None,
                    dob=None,
                    phone=phone,
                    division=division,
                    admission_year=DEFAULT_ADMISSION_YEAR,
                    graduation_year=DEFAULT_GRADUATION_YEAR,
                    current_semester=semester,
                    is_active=True,
                )

                db.add(student)
                created += 1

        db.commit()

        print("\n========== Seed Summary ==========")
        print(f"✅ Students Created : {created}")
        print(f"⏭️ Students Skipped : {skipped}")
        print("==================================")

    except Exception as e:

        db.rollback()

        print(f"\n❌ Error occurred: {e}")
        raise

    finally:

        db.close()


if __name__ == "__main__":
    seed_students()