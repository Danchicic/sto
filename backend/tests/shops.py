import pytest
from httpx import AsyncClient
from main import app

host = "http://0.0.0.0:8000"
@pytest.mark.asyncio
async def test_get_all_shops():
    async with AsyncClient(app=app, base_url=host) as client:
        response = await client.get("/shops/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)