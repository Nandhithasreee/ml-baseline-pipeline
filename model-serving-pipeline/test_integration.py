from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "ML Model API"}

def test_predict_endpoint_success():
    payload = {"features": [1.0, 2.0, 3.0]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predictions" in data
    assert data["status"] == "success"
    assert data["predictions"] == [2.5, 5.0, 7.5]

def test_predict_endpoint_empty_payload():
    payload = {"features": []}
    response = client.post("/predict", json=payload)
    assert response.status_code == 400