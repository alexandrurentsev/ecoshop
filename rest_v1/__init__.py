from fastapi import APIRouter
from rest_v1.product.views import router as products_router
from rest_v1.user.views import router as users_router

router = APIRouter()
router.include_router(router=products_router, prefix="/products")
router.include_router(router=users_router, prefix="/auth")
