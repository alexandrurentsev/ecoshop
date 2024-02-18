from core.crud import BaseRepository
from user.models import Users


class UserRepository(BaseRepository):
    model = Users
