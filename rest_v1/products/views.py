from typing import Union
from fastapi import APIRouter

from core.models.product import Product
from rest_v1.products.crud import ProductRepository
from rest_v1.products.schemas import ProductCreate


router = APIRouter(tags=["Продукты"])

product_repository = ProductRepository()

# @router.get("/", response_model=list[Product])
# async def get_products(
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await product_repository.get_all_products(session=session)


@router.post(
    "/",
    response_model=Product,
)
async def create_product(product_in: ProductCreate):
    return await product_repository.create_product(product_in=product_in)


@router.get("/{product_id}")
async def get_product_by_id(product_id: int) -> Union[Product, None]:
    return await product_repository.get_by_id(product_id=product_id)
