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

models = [
    "gemini-flash-latest",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-2.5-flash",
    "gemini-flash-lite-latest",
]
story = None # try every model in the list until one works
for model in models:
    try:
        response = client.models.generate_content(
            model=model, 
            contents=f"Write a short horror story (3-4 sentences) set in a town where the current weather is: {description}, {temperature}°C, wind {wind_speed} km/h. Make the weather central to the horror. It can be psychological, or supernatural horror but not gory. It should not be suitable for a general audience but a mature one."
        )
        story = response.text
        break # if the story is generated successfully, break the loop
    except Exception as e:
        print(f"Error with model {model}: {e}")
        continue # if the model fails, try the next one

if story is None:
    print("Every model is currently down. Please try again later.")
else:
    print(story)