from products.crud import ProductRepository
from products.router import router


@router.get("/")
def get_product_by_id(product_id: int):
    repository = ProductRepository()
    return repository.get_by_id(product_id=product_id)
