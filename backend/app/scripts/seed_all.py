from app.scripts.seed_roles import seed_roles
from app.scripts.seed_departments import seed_departments
from app.scripts.seed_programs import seed_programs
from app.scripts.seed_admin import seed_admin
from app.scripts.seed_faculty import seed_faculty
from app.scripts.seed_students import seed_students
from app.scripts.seed_subjects import seed_subjects
from app.scripts.seed_companies import seed_companies


def seed_all():
    print("=" * 60)
    print("Student Success Platform Database Seeder")
    print("=" * 60)

    print("\nSeeding Roles...")
    seed_roles()

    print("\nSeeding Departments...")
    seed_departments()

    print("\nSeeding Programs...")
    seed_programs()

    print("\nSeeding Administrator...")
    seed_admin()

    print("\nSeeding Faculty...")
    seed_faculty()

    print("\nSeeding Students...")
    seed_students()

    print("\nSeeding Subjects...")
    seed_subjects()

    print("\nSeeding Companies...")
    seed_companies()

    print("\n" + "=" * 60)
    print("🎉 Database seeding completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    seed_all()