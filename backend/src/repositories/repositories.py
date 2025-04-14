from src.database.models.buyers import Buyer
from src.database.models.cars import CarsModel
from src.database.models.shops import Shop
from . import SQLAlchemyRepository


class ShopsRepository(SQLAlchemyRepository):
    model = Shop


class BuyersRepository(SQLAlchemyRepository):
    model = Buyer


class CarsRepository(SQLAlchemyRepository):
    model = CarsModel
