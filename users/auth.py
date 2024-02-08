from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from core.config import settings

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
