from fastapi import FastAPI
from pydantic_settings import BaseSettings

from core.default_constants import DEFAULT_DB_URL, DEFAULT_DB_ECHO


class Settings(BaseSettings):
    db_url: str = DEFAULT_DB_URL
    db_echo: bool = DEFAULT_DB_ECHO


settings = Settings()
app = FastAPI()


@app.get("/info")
async def info():
    return {
        "db_url": settings.db_url,
        "db_echo": settings.db_echo,
    }
