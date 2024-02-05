from typing import Union
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


from core.models.db_helper import async_session_maker
from core.models.product import Product


class ProductRepository:
    async def get_product(
        product_id: int
    ) -> Union[Product, None]:
        async with async_session_maker() as session:
            query = select(Product)
            result = await session.execute(query)
            return result.mappings().all()
