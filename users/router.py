from fastapi import APIRouter

from users.schemas import RegisterUser

router = APIRouter(prefix="/auth", tags=["Auth & Пользователи"])


@router.post("/register")
async def register_user(data_for_register: RegisterUser):
    pass
