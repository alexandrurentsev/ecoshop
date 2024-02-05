from pydantic import BaseModel
from typing import Union


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdatePartial(ProductBase):
    name: Union[str, None]
    description: Union[str, None]
    price: Union[int, None]
