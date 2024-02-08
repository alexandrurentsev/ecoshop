from core.crud.base_repository import BaseRepository
from users.models import Users


class UserRepository(BaseRepository):
    model = Users
