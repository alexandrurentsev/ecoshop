from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

import uvicorn

app = FastAPI()


@app.get("/product/")
def get_product_by_id(product_id: int):
    return {
        f"Продукт с c id: {product_id}"
    }



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)