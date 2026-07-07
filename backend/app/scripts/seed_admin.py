from sqlalchemy.orm import Session
from app.auth.hashing import hash_password
from app.database.database import SessionLocal
from app.models.role import Role
from app.models.user import User


ADMIN_EMAIL = "admin@vsit.edu.in"
ADMIN_PASSWORD = "Admin@123"


def seed_admin():
    db: Session = SessionLocal()

    try:

        admin_role = (
            db.query(Role)
            .filter(Role.role_name == "Administrator")
            .first()
        )

        if admin_role is None:
            print("❌ Administrator role not found.")
            return

        admin = (
            db.query(User)
            .filter(User.email == ADMIN_EMAIL)
            .first()
        )

        if admin:
            print("ℹ️ Administrator already exists.")
            return

        admin = User(
            role_id=admin_role.id,
            email=ADMIN_EMAIL,
            password_hash=hash_password(ADMIN_PASSWORD),
            is_active=True,
        )

        db.add(admin)
        db.commit()

        print("✅ Administrator created successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_admin()