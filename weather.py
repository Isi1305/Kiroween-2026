import requests

# Get the weather data from the Open-Meteo API
url = "https://geocoding-api.open-meteo.com/v1/search" 
params = {
    "name": "Bad Dürkheim",
    "count": 1,
    "language": "de"
}

response = requests.get(url, params=params) # Send a GET request to the API with the specified parameters.
data = response.json() # Answer in JSON format and store it in the variable 'data'.

print(data["results"][0]["latitude"]) # Print the latitude of the location
print(data["results"][0]["longitude"]) # Print the logitude of the location

latitude = data["results"][0]["latitude"] # Store the latitude in a variable
longitude = data["results"][0]["longitude"] # Store the longitude in a variable

# Get the weather forecast for the specified location
url = "https://api.open-meteo.com/v1/forecast"
forecast_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,weather_code,wind_speed_10m"
}

forecast_response = requests.get(url, params=forecast_params)
weather_data = forecast_response.json()

print(weather_data)