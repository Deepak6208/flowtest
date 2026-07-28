from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_auto_is_supported():
    response = client.get("/config")
    assert "auto" in response.json()["supported_lines"]


def test_home_is_supported():
    response = client.get("/config")
    assert "home" in response.json()["supported_lines"]
