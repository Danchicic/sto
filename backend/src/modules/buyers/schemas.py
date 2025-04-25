from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.core.schemas import BaseTypeModel


class BaseBuyer(BaseModel):
    fio: str
    latitude: float
    longitude: float
    year: int
    cost: int


class BuyerCreate(BaseBuyer):
    company_id: int
    model_id: int
    auto_type_id: int


class Buyer(BaseBuyer):
    id: Optional[int]

    model_config = ConfigDict(from_attributes=True)
    company: BaseTypeModel
    model: BaseTypeModel
    auto_type: BaseTypeModel


class BuyersConditionals(BaseModel):
    company_id: Optional[int]
    model_id: Optional[int]
    auto_type_id: Optional[int]
    cost_max: Optional[int]
    cost_min: Optional[int]
    year: Optional[int]
    model_config = ConfigDict(from_attributes=True)


class Buyers(BaseModel):
    buyers: list[Buyer]

    model_config = ConfigDict(from_attributes=True)
