from sqlalchemy import func, select

from src.database import async_session
from src.database.models.shared import *
from src.database.models.shared import Buyer, Car, Shop
from . import SQLAlchemyRepository


class ShopsRepository(SQLAlchemyRepository):
    model = Shop


class BuyersRepository(SQLAlchemyRepository):
    model = Buyer

    async def get_buyers_by_model(self, model_id: int) -> list[Buyer]:
        async with async_session() as session:
            query = select(self.model).where(self.model.model_id == model_id)
            chunked_res = await session.execute(query)
            return chunked_res.scalars().all()


class CarsRepository(SQLAlchemyRepository):
    model = Car

    async def get_most_expensive(self):
        async with async_session() as session:
            subquery = select(func.max(self.model.cost))
            query = select(self.model).where(self.model.cost == subquery)
            chunked_res = await session.execute(query)
            return chunked_res.scalars().one_or_none()


class UserRepository(SQLAlchemyRepository):
    model = User
