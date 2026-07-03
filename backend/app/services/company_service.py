from app.repositories.company_repository import CompanyRepository
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyService:

    @staticmethod
    def create(db, request: CompanyCreate):
        return CompanyRepository.create(
            db,
            request.model_dump(),
        )

    @staticmethod
    def get_all(db):
        return CompanyRepository.get_all(db)

    @staticmethod
    def get_by_id(db, company_id):
        return CompanyRepository.get_by_id(
            db,
            company_id,
        )

    @staticmethod
    def update(
        db,
        company_id,
        request: CompanyUpdate,
    ):
        company = CompanyRepository.get_by_id(
            db,
            company_id,
        )

        if company is None:
            return None

        data = request.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(company, key, value)

        return CompanyRepository.update(
            db,
            company,
        )

    @staticmethod
    def delete(db, company_id):
        company = CompanyRepository.get_by_id(
            db,
            company_id,
        )

        if company is None:
            return False

        CompanyRepository.delete(
            db,
            company,
        )

        return True