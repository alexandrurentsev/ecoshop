from fastapi import APIRouter
from products.crud import ProductRepository



router = APIRouter(
    prefix="/product",
    tags=["Product"],
)


@router.get("/")
def get_product_by_id(product_id: int):
    repository = ProductRepository()
    return repository.get_by_id(product_id=product_id)
