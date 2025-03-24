# Make sure you have 'requests' installed: pip install requests
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data