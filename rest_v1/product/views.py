from fastapi import APIRouter, Depends, status
from product.repositories import ProductRepository
from product.schemas import ProductCreate

from user.services.dependencies import get_current_user
from user.models import Users

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


@router.get("/all")
async def get_all_products(user: Users = Depends(get_current_user)):
    return await product_repository.get_all()
