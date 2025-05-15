from abc import ABC, abstractmethod
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import delete, insert, select

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

    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_values_by_conditionals(self, conditionals: dict):
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
        async with async_session() as session, session.begin():
            query = delete(self.model).where(self.model.id == id).returning(self.model)
            res_chunked = await session.execute(query)
            return res_chunked.scalars().one_or_none()

    async def add_one(self, data: dict):
        async with async_session() as session, session.begin():
            query = insert(self.model).values(**data).returning(self.model)
            res_chunked = await session.execute(query)
            return res_chunked.scalars().one_or_none()

    async def get_values_by_conditionals(self, conditionals: dict):
        """
        :param conditionals:
            dict where key is a column of model, value is value for comparison,
            for equality key must contain only column name, and value for equality
            you can use conditional less(<=) or over(>=)
            for this condition key must have postfix _min, max, before column name like:
            {
                cost_max: 100, # will be used cost <= 100
                cost_min: 20, # will be used cost >= 100
            }
        :return: list of models
        """
        conditions = []
        for condition_column_name, condition_value in conditionals.items():
            if condition_value is None:
                continue

            condition_filter_type = "equality"

            if "max" in condition_column_name or "min" in condition_column_name:
                *condition_column_name_list, condition_filter_type = (
                    condition_column_name.split("_")
                )
                condition_column_name = "_".join(condition_column_name_list)

            car_filtering_column = getattr(self.model, condition_column_name, None)

            if not car_filtering_column:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid filter name: {condition_column_name}",
                )

            match condition_filter_type:
                case "max":
                    conditions.append(car_filtering_column <= condition_value)
                case "min":
                    conditions.append(car_filtering_column >= condition_value)
                case "equality":
                    conditions.append(car_filtering_column == condition_value)

        async with async_session() as session:
            query = select(self.model).where(*conditions)
            chunked = await session.execute(query)
            res = []
            for el in chunked.scalars().all():
                res.append(el.__dict__)
            return res
