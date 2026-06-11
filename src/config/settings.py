from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "InvestigatorAI"

    ENVIRONMENT: str = "development"

    GROQ_API_KEY: str

    DATABASE_PATH: str = "metadata/metadata.db"

    BASE_DIR: Path = Path(__file__).resolve().parents[2]

    INCOMING_DIR: Path = BASE_DIR / "incoming"

    JSON_STORE_DIR: Path = BASE_DIR / "json_store"

    METADATA_DIR: Path = BASE_DIR / "metadata"

    LOG_DIR: Path = BASE_DIR / "logs"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()