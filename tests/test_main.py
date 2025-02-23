from fastapi.testclient import TestClient
from hello import app 

client = TestClient(app)

def test_ping():
    """Проверяем, что сервер работает"""
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "server is working"}

def test_predict():
    """Проверяем, что /translate работает"""
    response = client.post("/translate", json={"text": "Hello world"})
    assert response.status_code == 200
    assert "translated_text" in response.json()
