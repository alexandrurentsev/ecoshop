from fastapi import FastAPI


from rest_v1 import router as products_router
from users import router as users_router
import uvicorn


app = FastAPI()

app.include_router(products_router)
app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
