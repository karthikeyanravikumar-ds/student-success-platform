from uuid import UUID

from sqlalchemy.orm import Session

from app.models.company import Company


class CompanyRepository:

    @staticmethod
    def create(db: Session, data: dict):
        company = Company(**data)

        db.add(company)
        db.commit()
        db.refresh(company)

        return company

    @staticmethod
    def get_all(db: Session):
        return db.query(Company).all()

    @staticmethod
    def get_by_id(db: Session, company_id: UUID):
        return (
            db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

    @staticmethod
    def update(db: Session, company: Company):
        db.commit()
        db.refresh(company)
        return company

    @staticmethod
    def delete(db: Session, company: Company):
        db.delete(company)
        db.commit()

    @staticmethod
    def update_logo_path(
        db: Session,
        company: Company,
        logo_path: str,
    ):
        company.logo_path = logo_path

        db.commit()
        db.refresh(company)

        return company