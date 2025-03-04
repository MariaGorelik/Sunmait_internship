from fastapi.testclient import TestClient
from hello import app

client = TestClient(app)

class TestPing:
    """Tests for the /ping endpoint"""

    def test_ping(self):
        """Check that the server is working"""
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.json() == {"message": "server is working"}

    def test_ping_invalid_methods(self):
        """Check that non-GET methods are not allowed on /ping"""
        methods = ['post', 'put', 'delete', 'patch', 'options']
        for method in methods:
            response = getattr(client, method)("/ping")
            assert response.status_code == 405  # Method Not Allowed


class TestTranslate:
    """Tests for the /translate endpoint"""

    def test_translate(self):
        """Check that /translate works"""
        text = "Exploring new technologies and solving complex problems is what drives innovation in the modern world."
        response = client.post("/translate", json={"text": text})
        assert response.status_code == 200
        assert "translated_text" in response.json()

    def test_translate_empty_text(self):
        """Check that /translate handles empty text"""
        response = client.post("/translate", json={"text": ""})
        assert response.status_code == 200
        assert "translated_text" in response.json()

    def test_translate_invalid_parameters(self):
        """Check that /translate handles invalid parameters"""
        response = client.post("/translate", json={"wrong_param": "Hello world"})
        assert response.status_code == 422  # Unprocessable Entity

    def test_translate_invalid_method(self):
        """Check that non-POST methods are not allowed on /translate"""
        methods = ['get', 'put', 'delete', 'patch', 'options']
        for method in methods:
            response = getattr(client, method)("/translate")
            assert response.status_code == 405  # Method Not Allowed