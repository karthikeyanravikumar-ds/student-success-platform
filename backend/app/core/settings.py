from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "Student Success Platform"
    APP_VERSION: str = "1.0.0"
    ENV: str = "development"

    # Database
    DATABASE_URL: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Uploads
    UPLOAD_FOLDER: str = "uploads"
    MAX_UPLOAD_SIZE: int = 10485760

    # Frontend
    FRONTEND_URL: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()