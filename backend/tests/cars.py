import pytest
from httpx import AsyncClient
from main import app
from src.repositories.repositories import CarsRepository

host = "http://0.0.0.0:8000"
@pytest.mark.asyncio
async def test_get_all_cars():
    async with AsyncClient(app=app, base_url=host) as client:
        response = await client.get("/cars/")
    assert response.status_code == 200
    assert "cars" in response.json()


@pytest.mark.asyncio
async def test_reserve_car(mocker):
    mocker.patch.object(CarsRepository, "reserve_car", return_value=None)
    async with AsyncClient(app=app, base_url=host) as client:
        response = await client.patch("/cars/reserve_car/1")
    assert response.status_code == 200