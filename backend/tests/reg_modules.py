import pytest
from httpx import AsyncClient
from main import app

host = "http://0.0.0.0:8000"
@pytest.mark.asyncio
async def test_auth_user(mocker):
    mocker.patch("src.modules.reg_module.utils.send_verification_code", return_value=123456)
    async with AsyncClient(app=app, base_url=host) as client:
        response = await client.post("/auth/auth", json={"phone_number": "+71234567890"})
    assert response.status_code == 200
    assert response.json()["message"] == "Verification code sent successfully"


@pytest.mark.asyncio
async def test_verify_code(mocker):
    mocker.patch("src.modules.reg_module.routes.validate_code", return_value=True)
    async with AsyncClient(app=app, base_url=host) as client:
        response = await client.get("/auth/verify_code", params={"role": "user", "code": 123456, "phone_number": "+71234567890"})
    assert response.status_code == 200
    assert response.json()["message"] == "auth success"