from typing import Optional

from pydantic import BaseModel, ConfigDict
from src.core.schemas import BaseTypeModel


class Car(BaseModel):
    year: Optional[int]
    id: Optional[int]
    features: Optional[str]
    engine_power: Optional[int]
    transmission_type: Optional[BaseTypeModel]
    is_reserved: Optional[bool]
    auto_type: Optional[BaseTypeModel]
    model: Optional[BaseTypeModel]
    company: Optional[BaseTypeModel]
    cost: Optional[int]
    mileage: Optional[int]
    model_config = ConfigDict(from_attributes=True)


class Cars(BaseModel):
    cars: list[Car]


class CarResponse(BaseModel):
    car: Car
