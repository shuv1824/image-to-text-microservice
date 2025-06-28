from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_view():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]
