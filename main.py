from fastapi import FastAPI


from rest_v1 import router as products_router
import uvicorn


app = FastAPI()

app.include_router(products_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
