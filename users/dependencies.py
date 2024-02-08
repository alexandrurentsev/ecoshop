# Файлик с зависимостями
from fastapi import Request, status, HTTPException, Depends
from jose import jwt, JWTError

def get_token(request: Request):
    token = request.cookies.get("product_access_token")
    if not token:
        status_code = status.HTTP_401_UNAUTHORIZED
        return HTTPException(status_code=status_code)

    return token


# Depends показывает, что он зависит от функции get_token
def get_current_user(token: str = Depends(get_token)):

    try:
        payload = jwt.decode()
    except JWTError:
        status_code = status.HTTP_401_UNAUTHORIZED
        return HTTPException(status_code=status_code)


    return
