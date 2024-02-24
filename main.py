import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from rest_v1 import router as rest_v1
from pages.router import router as router_pages
from images.router import router as router_images

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), "static")

app.include_router(rest_v1)
app.include_router(router_pages)
app.include_router(router_images)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
