from core.models import Base
from sqlalchemy import String, Column

# TODO Перименовать имя модели в единственное число


class Users(Base):
    __tablename__ = "users"
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
