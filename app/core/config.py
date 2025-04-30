
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env: str = "development"
    database_url: str
    jwt_secret: str
    frontend_origin: str
    google_client_id: str
    google_client_secret: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
