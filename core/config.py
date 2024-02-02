from fastapi import FastAPI
from pydantic_settings import BaseSettings

from core.default_constants import DEFAULT_DB_URL


class Settings(BaseSettings):
    db_url: str = DEFAULT_DB_URL


settings = Settings()
app = FastAPI()


@app.get("/info")
async def info():
    return {
        "db_url": settings.db_url,
    }
