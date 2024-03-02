from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from pydantic import EmailStr
from core.config import settings
from core.exception.user import InvalidPasswordException, UserNotFoundException
from user.repositories import UserRepository
from user.schemas.register_user import AuthUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})

    key = settings.SECRET_KEY
    algorithm = settings.ALGORITHM
    encoded_jwt = jwt.encode(to_encode, key=key, algorithm=algorithm)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str) -> AuthUser:
    user = await UserRepository.find_one_or_none(email=email)
    if not user:
        raise UserNotFoundException(email)
    hashed_password = get_password_hash(password)
    pasword_is_valid = verify_password(password, hashed_password)
    if not pasword_is_valid:
        raise InvalidPasswordException()
    return user
