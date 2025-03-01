import pytest
from httpx import AsyncClient

from app.main import app
from app.security import create_access_token

@pytest.mark.asyncio
async def test_read_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

@pytest.mark.asyncio
async def test_login_for_access_token():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/token", data={"username": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_get_history_authenticated():
    access_token = create_access_token(data={"sub": "test@example.com"})
    headers = {"Authorization": f"Bearer {access_token}"}
    async with AsyncClient(app=app, base_url="http://test", headers=headers) as ac:
        response = await ac.get("/history/1")
    assert response.status_code == 200