import random
from typing import Optional
from pydantic import BaseModel, model_validator
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.shared import CarsModel
from src.database import get_async_session
from src.database.models.shared import CompanyName, Car, TransmissionType
from src.repositories.repositories import CarsRepository
from pydantic import BaseModel
from . import schemas


class CreateCarRequest(BaseModel):
    features: Optional[str]
    firm: str
    gearbox: str
    model: str
    power: str
    price: str
    year: str
    auto_type: str = 'new'


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


@router.post('/cars')
async def create_car(
        data: CreateCarRequest,
        db: AsyncSession = Depends(get_async_session)
):
    # Поиск связанных записей
    company = await db.execute(select(CompanyName).where(CompanyName.name == data.firm))
    company = company.scalars().first()

    car_model = await db.execute(select(CarsModel).where(
        CarsModel.name == data.model
    ))
    car_model = car_model.scalars().first()

    gearbox = await db.execute(select(TransmissionType).where(TransmissionType.name == data.gearbox))
    gearbox = gearbox.scalars().first()

    # Создание нового автомобиля
    new_car = Car(
        company_id=company.id,
        model_id=car_model.id,
        year=int(data.year),
        engine_power=int(data.power),
        transmission_type_id=gearbox.id,
        features=data.features,
        cost=int(data.price),
        shop_id=1,
        mileage=0,
        auto_type_id=1,
    )

    db.add(new_car)
    await db.commit()
    await db.refresh(new_car)

    return {"status": "success", "car_id": new_car.id}


@router.patch("/reserve_car/{car_id}")
async def reserve_car(car_id: int):
    await CarsRepository().reserve_car(car_id)


@router.delete("/cars/{car_id}")
async def delete_car(
        car_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    # Проверяем существование автомобиля
    result = await db.execute(select(Car).where(Car.id == car_id))
    car = result.scalars().first()

    if not car:
        raise HTTPException(
            status_code=404,
            detail=f"Автомобиль с ID {car_id} не найден"
        )

    # Выполняем удаление
    stmt = delete(Car).where(Car.id == car_id)
    await db.execute(stmt)
    await db.commit()

    return {
        "status": "success",
        "message": f"Автомобиль с ID {car_id} удален",
        "deleted_id": car_id
    }
