from app.database.database import SessionLocal
from app.auth.hashing import hash_password
from app.models.user import User
from app.models.role import Role


def seed_admin():
    db = SessionLocal()

    try:
        # Find Administrator role
        admin_role = (
            db.query(Role)
            .filter(Role.role_name == "Administrator")
            .first()
        )

        if admin_role is None:
            print("Administrator role not found.")
            return

        # Check if admin already exists
        existing_user = (
            db.query(User)
            .filter(User.email == "admin@vsit.edu.in")
            .first()
        )

        if existing_user:
            print("Admin user already exists.")
            return

        admin = User(
            email="admin@vsit.edu.in",
            password_hash=hash_password("College123"),
            role_id=admin_role.id,
            is_active=True,
        )

        db.add(admin)
        db.commit()

        print("Admin user created successfully!")

    finally:
        db.close()


if __name__ == "__main__":
    seed_admin()