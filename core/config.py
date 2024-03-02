from typing import Literal
from fastapi import FastAPI
from pydantic_settings import BaseSettings

from core.default_constants import (
    DEFAULT_DB_URL,
    DEFAULT_DB_ECHO,
    DEFAULT_ALGORITHM,
    DEFAULT_SECRET_KEY,
    DEFAULT_MODE,
    DEFAULT_REDIS_HOST,
    DEFAULT_REDIS_PORT
)


class Settings(BaseSettings):
    db_url: str = DEFAULT_DB_URL
    db_echo: bool = DEFAULT_DB_ECHO
    SECRET_KEY: str = DEFAULT_SECRET_KEY
    ALGORITHM: str = DEFAULT_ALGORITHM
    MODE: Literal["DEV", "TEST", "PROD"] = DEFAULT_MODE
    REDIS_HOST: str = DEFAULT_REDIS_HOST
    REDIS_PORT: int = DEFAULT_REDIS_PORT

    class Config:
        env_file = ".env"


settings = Settings()
app = FastAPI()


@app.get("/info")
async def info():
    return {
        "db_url": settings.db_url,
        "db_echo": settings.db_echo,
    }
