from typing import Union

from pydantic import BaseModel


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
