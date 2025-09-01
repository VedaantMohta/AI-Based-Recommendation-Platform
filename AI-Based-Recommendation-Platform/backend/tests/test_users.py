from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.db_utils import get_db
from sqlalchemy.orm import Session

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_create_user_duplicate():
    client.post("/users/", json={"username": "testuser", "password": "testpass"})
    response = client.post("/users/", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists"

def test_login_user():
    client.post("/users/", json={"username": "testuser", "password": "testpass"})
    response = client.post("/login/", data={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_user_invalid():
    response = client.post("/login/", data={"username": "invaliduser", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"