import requests

# Get the weather data from the Open-Meteo API
url = "https://geocoding-api.open-meteo.com/v1/search" 
params = {
    "name": "Bad Dürkheim",
    "count": 1,
    "language" : "de"
}

response = requests.get(url, params=params) # Send a GET request to the API with the specified parameters.
data = response.json() # Answer in JSON format and store it in the variable 'data'.

print(data)