from core.models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Users(Base):
    __tablename__ = "users"

    email = Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    hashed_password = Mapped[str] = mapped_column(String(32), nullable=False)
