from fastapi import APIRouter, Response
from core.exception.user import (
    InvalidPasswordException,
    UserAlreadyExistsException,
    UserNotFoundException,
)
from user.services.auth import create_access_token, get_password_hash, verify_password
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
    user = await UserRepository.find_one_or_none(email=data_for_login.email)
    password = data_for_login.password
    if not user:
        raise UserNotFoundException(data_for_login.email)
    hashed_password = get_password_hash(password)
    pasword_is_valid = verify_password(password, hashed_password)
    if not pasword_is_valid:
        raise InvalidPasswordException()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("product_access_token", access_token, httponly=True)
    return {"access_token": access_token}
