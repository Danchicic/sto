from sqlalchemy import select

from src.database import async_session
from src.database.models.shared import Buyer, Car
from src.database.models.shops import Shop

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
