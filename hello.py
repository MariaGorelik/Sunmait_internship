from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Модель данных для предсказания
class PredictRequest(BaseModel):
    feature1: float
    feature2: float

# Эндпоинт для проверки доступности сервиса
@app.get("/ping")
async def ping():
    return {"message": "pong"}

# Эндпоинт для предсказания
@app.post("/predict")
async def predict(request: PredictRequest):
    # Простая модель предсказания: сумма feature1 и feature2
    prediction = request.feature1 + request.feature2
    return {"prediction": prediction}

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)