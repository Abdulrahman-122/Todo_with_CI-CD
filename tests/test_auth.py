from fastapi.testclient import TestClient
from main.app import app
import uuid
client = TestClient(app)

email=f"john{uuid.uuid4()}@demo.com"
def test_register():
    res = client.post(
        "/auth/register",
        json={
            "username": "John",
            "email": email,
            "password": "TTYSrecrets",
        },
    )
    assert res.status_code == 201


def test_login():
    res = client.post(
        "/auth/login", json={"email": email, "password": "TTYSrecrets"}
    )
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
