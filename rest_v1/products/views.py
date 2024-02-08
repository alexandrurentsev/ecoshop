from fastapi import APIRouter, Depends, Request, status

from rest_v1.products.crud import ProductRepository
from rest_v1.products.schemas import ProductCreate
from users.dependencies import get_current_user
from users.models import Users

router = APIRouter(tags=["Продукты"])

product_repository = ProductRepository()


@router.post(
    "/",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(product_in: ProductCreate):
    return await product_repository.create_product(product_in=product_in)


@router.get("/{product_id}")
async def get_product_by_id(product_id: int, user: Users = Depends(get_current_user)):
    return await product_repository.get_by_id(product_id=product_id)
