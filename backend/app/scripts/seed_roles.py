from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.role import Role


ROLES = [
    {
        "role_name": "Administrator",
        "description": "System Administrator",
    },
    {
        "role_name": "Placement Officer",
        "description": "Placement Cell Staff",
    },
    {
        "role_name": "Faculty",
        "description": "Faculty Member",
    },
    {
        "role_name": "Student",
        "description": "Student",
    },
]


def seed_roles():
    db: Session = SessionLocal()

    try:
        for role in ROLES:

            exists = (
                db.query(Role)
                .filter(Role.role_name == role["role_name"])
                .first()
            )

            if exists:
                continue

            db.add(Role(**role))

        db.commit()

        print("✅ Roles seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_roles()