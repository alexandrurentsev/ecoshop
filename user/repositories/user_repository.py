from core.crud import BaseRepository
from user.models import User


class UserRepository(BaseRepository):
    model = User
