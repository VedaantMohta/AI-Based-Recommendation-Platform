import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_recommendation_logic():
    response = client.get("/api/recommendations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_recommendation_for_user():
    user_id = 1  # Example user ID
    response = client.get(f"/api/recommendations/{user_id}")
    assert response.status_code == 200
    assert "recommendations" in response.json()

def test_invalid_user_recommendation():
    invalid_user_id = 9999  # Example of an invalid user ID
    response = client.get(f"/api/recommendations/{invalid_user_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}