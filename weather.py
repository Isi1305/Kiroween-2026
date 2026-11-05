import requests
from weather_codes import weather_descriptions

def get_coordinates(location):
    """Get the coordinates (latitude and longitude) for a given location using the Open-Meteo API."""
    # Get the location data from the Open-Meteo API
    url = "https://geocoding-api.open-meteo.com/v1/search" 
    params = {
        "name": location,
        "count": 1,
        "language": "de"
    }

    response = requests.get(url, params=params) # Send a GET request to the API with the specified parameters
    data = response.json() # Answer in JSON format and store it in the variable 'data'

    result = data["results"][0]
    return result["latitude"], result["longitude"]

def get_weather(latitude, longitude):
    """Get the current weather for the specified coordinates using the Open-Meteo API."""
    # Get the weather forecast for the specified location
    url = "https://api.open-meteo.com/v1/forecast"
    forecast_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code,wind_speed_10m"
    }

    forecast_response = requests.get(url, params=forecast_params)
    weather_data = forecast_response.json()

    weather_result = weather_data["current"]
    return weather_result["temperature_2m"], weather_result["weather_code"], weather_result["wind_speed_10m"]

if __name__ == "__main__":
    latitude, longitude = get_coordinates("Bad Dürkheim")
    temperature, weather_code, wind_speed = get_weather(latitude, longitude)
    print(f"Temperatur: {temperature} °C, Wind: {wind_speed} km/h, Code: {weather_code}")


    description = weather_descriptions[weather_code]
    print(f"Weather description: {description}")
