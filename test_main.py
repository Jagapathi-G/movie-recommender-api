import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_recommend_comedy():
    response = client.post(
        "/recommend",
        json={"genre": "Comedy", "min_rating": 4.0, "n": 5}
    )
    assert response.status_code == 200
    assert "recommendations" in response.json()
    assert len(response.json()["recommendations"]) <= 5
    for movie in response.json()["recommendations"]:
        assert "Comedy" in movie["genres"]
        assert movie["avg_rating"] >= 4.0

def test_recommend_no_genre():
    response = client.post(
        "/recommend",
        json={"min_rating": 4.0, "n": 3}
    )
    assert response.status_code == 200
    assert "recommendations" in response.json()
    assert len(response.json()["recommendations"]) <= 3
