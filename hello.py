from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

# You need to sign up at OpenWeatherMap to get an API key
API_KEY = "3981d24f49b14ae702f3fd85fad6f46e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
async def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")
        
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        
        return weather

# To run the app, use the command: uvicorn weather-fastapi-app:app --reload