from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy import select, delete

from src.database import async_session


class AbstractRepository(ABC):
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, id: int):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_all(self) -> list[model]:
        async with async_session() as session:
            query = select(self.model)
            res_chunked = await session.execute(query)
            return res_chunked.scalars().all()

    async def get_by_id(self, id: int) -> Optional[model]:
        async with async_session() as session:
            query = select(self.model).where(self.model.id == id)
            res_chunked = await session.execute(query)
            return res_chunked.scalars().one_or_none()

    async def delete_by_id(self, id: int) -> Optional[model]:
        async with async_session() as session:
            async with session.begin():
                query = delete(self.model).where(self.model.id == id).returning(self.model)
                res_chunked = await session.execute(query)
                return res_chunked.scalars().one_or_none()
