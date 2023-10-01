from dotenv import load_dotenv
from pprint import pprint
import requests
import os


load_dotenv()

# city = input("\nEnter a city name for the current weather:    \n")


def get_current_weather(city=""):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n***Get Current Weather Conditions***\n")
    city = input("\nPlease enter a city name: ")
    if not bool(city.strip()):
        city = "Honolulu city"
    weather_data = get_current_weather(city)
    print("\n")
    print(f'Current weather for {weather_data["name"]}')
    print(f'Current weather sky is {weather_data["clouds"]}')
    print(f'Current temp is {weather_data["main"]["temp"]}')
    print(f'Current humidity is {weather_data["main"]["humidity"]}')
    print(f'Current weather feel like {weather_data["main"]["feels_like"]}')
    print(
        f'Current weather described as {weather_data["weather"][0]}')
