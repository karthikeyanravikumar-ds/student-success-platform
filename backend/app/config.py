from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    ENV: str

    # Database
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Uploads
    UPLOAD_FOLDER: str
    MAX_UPLOAD_SIZE: int

    # Frontend
    FRONTEND_URL: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()