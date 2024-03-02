from fastapi import APIRouter, Response
from core.exception.user import (
    UserAlreadyExistsException,
)
from user.services.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)

from user.repositories import UserRepository

from user.schemas import AuthUser


router = APIRouter(tags=["Auth & Пользователи"])


@router.post("/register")
async def register_user(data_for_register: AuthUser):
    email = data_for_register.email
    existing_user = await UserRepository.find_one_or_none(email=email)
    if existing_user:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(data_for_register.password)
    await UserRepository.add(
        email=data_for_register.email, hashed_password=hashed_password
    )


@router.post("/login")
async def login_user(response: Response, data_for_login: AuthUser):
    email = data_for_login.email
    password = data_for_login.password

    user = await authenticate_user(email, password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("product_access_token", access_token, httponly=True)
    return {"access_token": access_token}
