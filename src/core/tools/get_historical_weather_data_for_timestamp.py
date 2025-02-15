from langchain_core.tools import tool
import requests
import os

@tool
def get_historical_weather_data_for_timestamp(lat: float, lon: float, dt: int) -> dict:
  """
  Get access to historical weather data for any timestamp after 1-1-1979

  Parameters:
  "lat"	- required - Latitude, decimal (-90; 90).
  "lon" -	required - Longitude, decimal (-180; 180).
  "dt" - required - Timestamp (Unix time, UTC time zone), e.g. dt=1586468027  
  """
  
  url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={os.getenv('OPENWEATHER_API_KEY')}"
  response = requests.get(url)
  response.raise_for_status()
  return response.json()
