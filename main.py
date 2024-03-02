import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from sqladmin import Admin
from admin.product.views import ProductAdmin
from admin.user.views import UserAdmin
from admin.auth import authentication_backend

from rest_v1 import router as rest_v1
from pages.router import router as router_pages
from images.router import router as router_images
from core.models.db_helper import engine
from core.config import settings

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), "static")

app.include_router(rest_v1)
app.include_router(router_pages)
app.include_router(router_images)

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type" "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

# TODO вынести зависимости в отде
@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"
    )
    FastAPICache.init(RedisBackend(redis), prefix="cache")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
admin.add_view(ProductAdmin)
