from core.crud.base_repository import BaseRepository
from user.models import Users


class UserRepository(BaseRepository):
    model = Users
