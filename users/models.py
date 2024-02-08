from core.models import Base
from sqlalchemy import String, Column


class Users(Base):
    __tablename__ = "users"
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
