"""Application settings, read from environment variables and `.env` (validated at startup)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Prototype"
    database_url: str = "sqlite:///data/prototype.db"
    session_secret: str = "change-me-in-.env"
    auth_required: bool = True
    log_level: str = "info"
    default_language: str = "de"


settings = Settings()
