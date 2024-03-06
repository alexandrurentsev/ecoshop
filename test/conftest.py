import pytest

from core.config import settings
from core.models.db_helper import engine

from core.models import Base
from user.models import User
from product.models import Product



@pytest.fixture
async def prepare_database():
    assert settings.MODE == "TEST"
    async with engine.begin() as conn:
        await conn. run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
