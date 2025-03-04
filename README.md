# FastAPI DevContainer Project

This project is a FastAPI-based web application running inside a DevContainer using Docker and Docker Compose. The API provides an endpoint for text processing using the `Helsinki-NLP` model from the `transformers` library.

## 📂 Project Structure
```
.
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
├── hello.py
├── docker-compose.yml
├── requirements.txt
├── tests/
│   ├── test_main.py
```

## 🚀 Getting Started
### 1️⃣ Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [VS Code](https://code.visualstudio.com/)
- [Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### 2️⃣ Running in a DevContainer
1. Open the project folder in VS Code.
2. When prompted, **reopen in DevContainer**.
3. If not prompted, manually open the Command Palette (`Ctrl+Shift+P`), select `Remote-Containers: Reopen in Container`.
4. The container will build and start the FastAPI server at `http://localhost:8000`.

### 3️⃣ Running the API Locally (Without DevContainer)
```sh
# Build and run the container manually
docker-compose up --build
```

## 🛠 API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| `GET`  | `/ping`  | Check if the server is running |
| `POST` | `/predict` | Process text and return output |

### Example Request
```sh
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Hello world"}'
```

## 🧪 Running Tests
Unit tests are automatically run when the container starts. To run tests manually:
```sh
pytest tests
```

## 📝 DevContainer Features
The `devcontainer.json` includes:
- `pytest` for unit testing.
- `ruff` for linting.
- `uv` for package management.

## 📌 Notes
- If build errors occur, try disabling BuildKit: `set DOCKER_BUILDKIT=0`
- If using WSL2, ensure Docker Desktop is set to use WSL integration.

## 📜 License
This project is licensed under the MIT License.

