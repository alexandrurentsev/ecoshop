from fastapi import FastAPI
from products.views import router
import uvicorn

app = FastAPI()

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)