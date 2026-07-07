from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.department import Department


DEPARTMENTS = [
    {
        "department_code": "315",
        "department_name": "Data Science",
    },
    {
        "department_code": "205",
        "department_name": "Information Technology",
    },
    {
        "department_code": "206",
        "department_name": "Computer Science (AI & ML)",
    },
    {
        "department_code": "204",
        "department_name": "Computer Science (Software Engineering)",
    },
    {
        "department_code": "203",
        "department_name": "Data Science & Artificial Intelligence",
    },
]


def seed_departments():
    db: Session = SessionLocal()

    try:
        for department in DEPARTMENTS:

            exists = (
                db.query(Department)
                .filter(
                    Department.department_code
                    == department["department_code"]
                )
                .first()
            )

            if exists:
                continue

            db.add(Department(**department))

        db.commit()

        print("✅ Departments seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_departments()