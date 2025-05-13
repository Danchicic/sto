from pydantic import BaseModel, ConfigDict

from src.core.schemas import BaseTypeModel


class Car(BaseModel):
    year: int
    id: int
    features: str
    engine_power: int
    transmission_type: BaseTypeModel
    auto_type: BaseTypeModel
    model: BaseTypeModel
    company: BaseTypeModel
    cost:int
    model_config = ConfigDict(from_attributes=True)


class Cars(BaseModel):
    cars: list[Car]
