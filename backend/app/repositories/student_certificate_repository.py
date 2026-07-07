from uuid import UUID

from sqlalchemy.orm import Session

from app.models.student_certificate import StudentCertificate


class StudentCertificateRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        certificate = StudentCertificate(**data)

        db.add(certificate)
        db.commit()
        db.refresh(certificate)

        return certificate

    @staticmethod
    def get_by_id(
        db: Session,
        certificate_id: UUID,
    ):
        return (
            db.query(StudentCertificate)
            .filter(
                StudentCertificate.id == certificate_id,
            )
            .first()
        )

    @staticmethod
    def get_by_student(
        db: Session,
        student_id: UUID,
    ):
        return (
            db.query(StudentCertificate)
            .filter(
                StudentCertificate.student_id == student_id,
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        certificate: StudentCertificate,
    ):
        db.commit()
        db.refresh(certificate)

        return certificate

    @staticmethod
    def delete(
        db: Session,
        certificate: StudentCertificate,
    ):
        db.delete(certificate)
        db.commit()
    @staticmethod
    def get_pending(db: Session):
        return (
            db.query(StudentCertificate)
            .filter(
                StudentCertificate.verification_status == "Pending"
            )
            .all()
        )

    @staticmethod
    def get_verified(db: Session):
        return (
            db.query(StudentCertificate)
            .filter(
                StudentCertificate.verification_status == "Verified"
            )
            .all()
        )

    @staticmethod
    def get_rejected(db: Session):
        return (
            db.query(StudentCertificate)
            .filter(
                StudentCertificate.verification_status == "Rejected"
            )
            .all()
        )