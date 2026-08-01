from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Lincode Enterprise DevOps"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/lincode_db"

    REDIS_URL: str = "redis://localhost:6379"

    AI_SERVICE_URL: str = "http://localhost:8001"

    SECRET_KEY: str = "change-this-secret-key"

    model_config = SettingsConfigDict(
        env_file=".env.example",
        case_sensitive=True,
    )


settings = Settings()
