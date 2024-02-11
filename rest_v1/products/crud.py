from typing import Union
from fastapi import Depends

from sqlalchemy import select

from core.models.db_helper import async_session_maker
from core.models.product import Product
from rest_v1.products.schemas import ProductCreate
from users.dependencies import get_current_user
from users.models import Users


class ProductRepository:
    @staticmethod
    async def get_by_id(product_id: int) -> Union[Product, None]:
        async with async_session_maker() as session:
            query = select(Product).filter(Product.id == product_id)
            result = await session.execute(query)
            return result.mappings().all()

    @staticmethod
    async def create_product(product_in: ProductCreate) -> Product:
        async with async_session_maker() as session:
            product = Product(**product_in.model_dump())
            session.add(product)
            await session.commit()
            return product

    @staticmethod
    async def get_all(user: Users = Depends(get_current_user)):
        print(user, type(user), user.email)
