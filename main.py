from fastapi import FastAPI


from rest_v1 import router as rest_v1
from pages.router import router as router_pages
import uvicorn


app = FastAPI()

app.include_router(rest_v1)
app.include_router(router_pages)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
