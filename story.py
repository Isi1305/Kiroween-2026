import os
from dotenv import load_dotenv
from google import genai
from weather import get_coordinates, get_weather
from weather_codes import weather_descriptions

# Get the coordinates for Bad Dürkheim and fetch the current weather data
latitude, longitude = get_coordinates("Bad Dürkheim")
temperature, weather_code, wind_speed = get_weather(latitude, longitude)
description = weather_descriptions[weather_code]

load_dotenv() # read .env file
api_key = os.getenv("GEMINI_API_KEY") # get the value of the GEMINI_API_KEY 

client = genai.Client(api_key=api_key) # Create a client object for the Gemini API using the provided API key

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"Write a short horror story (3-4 sentences) set in a town where the current weather is: {description}, {temperature}°C, wind {wind_speed} km/h. Make the weather central to the horror. It can be psychological, or supernatural horror but not gory. It should not be suitable for a general audience but a mature one.")

print(response.text)