from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.models.db_helper import db_helper
from core.models.base import Base

from products.router import router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI()

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
