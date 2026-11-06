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
    "gemini-flash-lite-latest",
]
story = None # try every model in the list until one works
for model in models:
    try:
        response = client.models.generate_content(
            model=model, 
            contents=f"""You are a screenwriter specializing in atmospheric, high-concept disaster horror movies.
                        Create a short, terrifying horror movie scene (4–6 sentences) based on the CURRENT WEATHER CONDITIONS:
                        - Weather: {description}
                        - Temperature: {temperature}°C
                        - Wind speed: {wind_speed} km/h

                        CORE RULES:
                        1. The weather itself MUST be the primary threat or the trigger of the horror. It must be impossible to separate the horror from the actual weather conditions.
                        2. Take inspiration from horror emergency alerts/broadcasts.
                        3. Introduce a terrifying phenomenon, an unexplained event or a survival threat directly connected to the weather.
                        4. Include one disturbing survival rule that people must follow to stay alive.
                        5. Build suspense, dread and a sense of impending catastrophe. Make the reader feel that something terrible is happening RIGHT NOW.
                        6. Avoid generic ghosts, serial killers or unrelated supernatural events.
                        7. No gore. Psychological and supernatural horror are welcome.
                        8. Make every story original, cinematic, immersive and suitable for a mature audience.
                        9. It should act as weather report DO NOT bring characters into it. 
                        10. The weather report should be the horror
                        11. **CIVIL DEFENSE EMERGENCY:** should be at the start.

                        IMPORTANT: Do not simply mention the weather. MAKE THE WEATHER THE MONSTER.

                        Write as if this were a scene from a horror movie, not a traditional short story."""
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