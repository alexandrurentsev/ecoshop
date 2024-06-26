# Файлик с зависимостями
from datetime import datetime
from fastapi import Request, status, HTTPException, Depends
from jose import jwt, JWTError
from core.config import settings

from user.repositories import UserRepository
from user.models import User


def get_token(request: Request):
    token = request.cookies.get("product_access_token")
    if not token:
        status_code = status.HTTP_401_UNAUTHORIZED
        return HTTPException(status_code=status_code)

    return token


# Depends показывает, что он зависит от функции get_token
async def get_current_user(token: str = Depends(get_token)) -> User:
    fail_status = status.HTTP_401_UNAUTHORIZED
    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
    except JWTError:
        jwt_error_detail = "Токен не является JWT"
        raise HTTPException(status_code=fail_status, detail=jwt_error_detail)

    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=fail_status)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=fail_status)
    user = UserRepository.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=fail_status)

    return user
