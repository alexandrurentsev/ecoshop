from typing import Union

from core.models.db_helper import async_session_maker
from sqlalchemy import select

from product.models import Product
from product.schemas import ProductCreate


class ProductRepository:
    @staticmethod
    async def get_by_id(product_id: int) -> Union[Product, None]:
        async with async_session_maker() as session:
            query = select(Product).filter(Product.id == product_id)
            result = await session.execute(query)
            return result.mappings().all()

    @staticmethod
    async def get_all() -> list[Product]:
        async with async_session_maker() as session:
            query = select(Product)
            result = await session.execute(query)
            return result.mappings().all()

    @staticmethod
    async def create_product(product_in: ProductCreate) -> Product:
        async with async_session_maker() as session:
            product = Product(**product_in.model_dump())
            session.add(product)
            await session.commit()
            return product
