from dotenv import load_dotenv
import requests
import os
from pprint import pprint

load_dotenv()

def get_current_weather():

    url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("WEATHER_API_KEY")}&q={os.getenv("CITY")}&units=metric'
    weather_data = requests.get(url).json()

    return weather_data

# if __name__ == "__main__":
    
#     weather_data = get_current_weather()

#     print(f"\n*** City: {os.getenv("CITY")} ***\n")
#     print("\n")
#     pprint(weather_data)