import random

import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from src.repositories.repositories import BuyersRepository

host = "http://0.0.0.0:8000"


@pytest.mark.asyncio
async def test_get_all_buyers():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.get("http://127.0.0.1:8000/buyers/")
    assert response.status_code == 200
    assert "buyers" in response.json()


@pytest.mark.asyncio
async def test_create_buyer():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_buyer_1():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_buyer_2():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_buyer_2():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_buyer_2():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_buyer_2():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_buyer_3():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_buyer_4():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_buyer_5():
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        response = await client.post("http://127.0.0.1:8000/buyers/", json={
            "fio": "Test Buyer",
            "latitude": random.random(),
            "longitude": random.random(),
            "year": random.randint(2020, 2030),
            "cost": random.randint(1000000, 100000000),
            "company_id": 1,
            "model_id": 1,
            "auto_type_id": 1
        })
    assert response.status_code == 200
