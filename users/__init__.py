from users.models import Users
from fastapi import APIRouter
from users.router import router as users_router

__all__ = ("Users",)


router = APIRouter()
router.include_router(router=users_router, prefix="/auth")
