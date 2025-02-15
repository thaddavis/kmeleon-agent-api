from langchain_core.tools import tool
import requests
import os

@tool
def get_weather(lat: float, lon: float, part: str, api_key: str) -> dict:
  """Get weather data from OpenWeatherMap API."""
  url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={os.getenv('OPENWEATHER_API_KEY')}"
  response = requests.get(url)
  response.raise_for_status()
  return response.json()

# @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers."""
#     return a * b