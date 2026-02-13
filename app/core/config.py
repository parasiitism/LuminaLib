from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # Security
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Providers
    STORAGE_PROVIDER: str = "local"
    LLM_PROVIDER: str = "mock"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
