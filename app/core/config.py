from pydantic import PostgresDsn, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "MindQuest API"
    DEBUG: bool = True
    DATABASE_URL: PostgresDsn
    SECRET_KEY: str = ''
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
