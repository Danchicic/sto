from fastapi import APIRouter

from src.repositories.repositories import CarsRepository

router = APIRouter(prefix="/cars", tags=["Cars"])


@router.get("/")
async def get_all_cars():
    await CarsRepository().get_all()


@router.get("/less_than_30")
async def get_cars_less_than_30():
    pass


@router.get("/new")
async def get_new_cars():
    pass


@router.get("/most_expensive")
async def get_most_expensive_car():
    pass
