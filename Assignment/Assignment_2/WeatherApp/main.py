import requests
from dotenv import load_dotenv
import os
import module

load_dotenv()

api_key = os.getenv("weather_api")

city=input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

resp=requests.get(url)
weather=resp.json()

module.print_temp(weather)

module.print_humidity(weather)

module.print_wind(weather)

module.print_time(weather)

