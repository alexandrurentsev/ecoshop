from fastapi import APIRouter

from core.models.product import Product
from rest_v1.products.crud import ProductRepository


router = APIRouter(tags=["Products"])

product_repository = ProductRepository()

# @router.get("/", response_model=list[Product])
# async def get_products(
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await product_repository.get_all_products(session=session)


# @router.post(
#     "/",
#     response_model=Product,
#     status_code=status.HTTP_201_CREATED,
# )
# async def create_product(
#     product_in: ProductCreate,
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await product_repository.create_product(
# session=session, product_in=product_in
# )


@router.get("/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    repository = ProductRepository()
    return repository.get_by_id(product_id=product_id)



