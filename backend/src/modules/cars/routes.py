from fastapi import APIRouter
from src.repositories.repositories import CarsRepository

from . import schemas

router = APIRouter(prefix="/cars", tags=["Cars"])


@router.get(
    "/",
    response_model=schemas.Cars,
)
async def get_all_cars():
    res = await CarsRepository().get_all()
    return {"cars": res}


@router.get(
    "/less_than_30",
    response_model=schemas.Cars,
)
async def get_cars_less_than_30():
    res = await CarsRepository().get_values_by_conditionals(
        conditionals={"mileage_max": 30000}
    )
    return {"cars": res}


@router.get(
    "/new",
    response_model=schemas.Cars,
)
async def get_new_cars():
    res = await CarsRepository().get_values_by_conditionals(
        conditionals={"auto_type_id": 1}
    )
    return {"cars": res}


@router.get("/most_expensive", response_model=schemas.CarResponse)
async def get_most_expensive_car():
    res = await CarsRepository().get_most_expensive()
    return {"car": res}
