import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"lat": -6.2088, "lon": 106.8456, "appid": api_key, "units": "metric"}

response = requests.get(url, params=params)
print("Status:", response.status_code)
print(response.json())
