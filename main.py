from fastapi import FastAPI


from rest_v1 import router as rest_v1
import uvicorn


app = FastAPI()

app.include_router(rest_v1)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
