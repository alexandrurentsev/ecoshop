from fastapi import APIRouter, HTTPException, Response, status
from user.services.auth import create_access_token, get_password_hash, verify_password
from user.repositories import UserRepository

from user.schemas import AuthUser

# TODO декомпозицию выполнить

router = APIRouter(tags=["Auth & Пользователи"])


@router.post("/register")
async def register_user(data_for_register: AuthUser):
    existing_user = await UserRepository.find_one_or_none(email=data_for_register.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    hashed_password = get_password_hash(data_for_register.password)
    await UserRepository.add(
        email=data_for_register.email, hashed_password=hashed_password
    )


@router.post("/login")
async def login_user(response: Response, data_for_login: AuthUser):
    user = await UserRepository.find_one_or_none(email=data_for_login.email)
    # TODO условие в отдельную функцию + объединить
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    hashed_password = get_password_hash(data_for_login.password)
    pasword_is_valid = verify_password(data_for_login.password, hashed_password)
    if not pasword_is_valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    # sub - имя переменной, рекомендованное самим jwt
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("product_access_token", access_token, httponly=True)
    return {"access_token": access_token}
