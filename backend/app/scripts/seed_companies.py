from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.company import Company


COMPANIES = [
    {
        "name": "Tata Consultancy Services",
        "website": "https://www.tcs.com",
        "email": "careers@tcs.com",
        "phone": "+91-22-67789999",
        "industry": "Information Technology",
        "location": "Mumbai",
        "description": "Global IT services, consulting and business solutions.",
    },
    {
        "name": "Infosys",
        "website": "https://www.infosys.com",
        "email": "careers@infosys.com",
        "phone": "+91-80-28520261",
        "industry": "Information Technology",
        "location": "Bengaluru",
        "description": "Global leader in consulting and digital transformation.",
    },
    {
        "name": "Accenture",
        "website": "https://www.accenture.com",
        "email": "careers@accenture.com",
        "phone": "+91-22-67072000",
        "industry": "Consulting",
        "location": "Mumbai",
        "description": "Technology consulting and professional services.",
    },
    {
        "name": "Capgemini",
        "website": "https://www.capgemini.com",
        "email": "careers.in@capgemini.com",
        "phone": "+91-20-66528000",
        "industry": "Information Technology",
        "location": "Pune",
        "description": "Consulting, technology and engineering services.",
    },
    {
        "name": "Cognizant",
        "website": "https://www.cognizant.com",
        "email": "careers@cognizant.com",
        "phone": "+91-44-42096000",
        "industry": "Information Technology",
        "location": "Chennai",
        "description": "Digital engineering and enterprise modernization.",
    },
    {
        "name": "LTIMindtree",
        "website": "https://www.ltimindtree.com",
        "email": "careers@ltimindtree.com",
        "phone": "+91-22-67766776",
        "industry": "Information Technology",
        "location": "Mumbai",
        "description": "Global technology consulting and digital solutions.",
    },
    {
        "name": "Deloitte",
        "website": "https://www.deloitte.com",
        "email": "careersindia@deloitte.com",
        "phone": "+91-22-61854000",
        "industry": "Consulting",
        "location": "Mumbai",
        "description": "Audit, consulting, tax and advisory services.",
    },
    {
        "name": "IBM",
        "website": "https://www.ibm.com",
        "email": "careers@ibm.com",
        "phone": "+91-80-26789500",
        "industry": "Technology",
        "location": "Bengaluru",
        "description": "Cloud computing, AI and enterprise solutions.",
    },
]

def seed_companies():
    db: Session = SessionLocal()

    try:

        created = 0

        for company in COMPANIES:

            exists = (
                db.query(Company)
                .filter(Company.name == company["name"])
                .first()
            )

            if exists:
                continue

            db.add(
                Company(
                    **company,
                    is_active=True,
                )
            )

            created += 1

        db.commit()

        print(f"✅ {created} companies seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_companies()