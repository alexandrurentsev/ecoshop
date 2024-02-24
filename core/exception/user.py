from fastapi import status
from core.exception.base import BaseException

class UserNotFoundException(BaseException):
    def __init__(self, email: str):
        detail = f"User with id {email} not found"
        status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(status_code=status_code, detail=detail)


class InvalidPasswordException(BaseException):
    def __init__(self):
        detail = "Invalid password"
        status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(status_code=status_code, detail=detail)


class UserAlreadyExistsException(BaseException):
    def __init__(self):
        detail = "User already exists"
        status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(status_code=status_code, detail=detail)
