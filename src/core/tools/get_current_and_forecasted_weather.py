from langchain_core.tools import tool
import requests
import os

@tool
def get_current_and_forecasted_weather(lat: float, lon: float, exclude: str) -> dict:
  """
  Current and forecasted weather data from OpenWeather.
  Get access to current weather, minute forecasts for 1 hour, hourly forecasts for 48 hours, daily forecasts for 8 days.

  Parameters:
  "lat"	- required - Latitude, decimal (-90; 90).
  "lon" -	required - Longitude, decimal (-180; 180).
  "exclude" - optional - By using this parameter you can exclude some parts of the weather data from the API response. It should be a comma-delimited list (without spaces) that includes the following values: current, minutely, hourly, daily, alerts.
  """
  
  url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={os.getenv('OPENWEATHER_API_KEY')}"
  response = requests.get(url)
  response.raise_for_status()
  return response.json()
