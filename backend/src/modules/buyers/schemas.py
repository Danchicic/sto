from typing import Optional

from pydantic import BaseModel


class BuyerCreate(BaseModel):
    fio: str
    latitude: float
    longitude: float
    year: int
    company_id: int
    model_id: int
    auto_type_id: int
    cost: int


class Buyer(BuyerCreate):
    id: Optional[int]


class BuyersConditionals(BaseModel):
    company_id: Optional[int]
    model_id: Optional[int]
    auto_type_id: Optional[int]
    cost_max: Optional[int]
    cost_min: Optional[int]
    year: Optional[int]


class Buyers(BaseModel):
    buyers: list[Buyer]
