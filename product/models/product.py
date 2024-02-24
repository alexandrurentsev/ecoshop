from core.models import Base
from sqlalchemy.orm import Mapped, mapped_column


class Product(Base):
    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]
    image_id: Mapped[int] = mapped_column(nullable=True)
