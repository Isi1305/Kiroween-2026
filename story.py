import os
from dotenv import load_dotenv
from google import genai
from weather import get_coordinates, get_weather, get_location
from weather_codes import weather_descriptions

load_dotenv() # read .env file
api_key = os.getenv("GEMINI_API_KEY") # get the value of the GEMINI_API_KEY 

client = genai.Client(api_key=api_key) # Create a client object for the Gemini API using the provided API key

def build_location_lines(location):
    """Build prompt lines from the location facts that exist."""
    lines = []

    name = location.get("name")
    if name:
        lines.append(f"- City: {name}")

    country = location.get("country")
    if country:
        lines.append(f"- Country: {country}")

    region = location.get("admin1")
    if region:
        lines.append(f"-Region: {region}")

    population = location.get("population")
    if population:
        lines.append(f"- Population: {population}")

    elevation = location.get("elevation")
    if elevation:
        lines.append(f"- Elevation: {elevation} m")

    return chr(10).join(lines)

def build_weather_lines(weather_result):
    """Build prompt lines from the weather facts that exist."""
    weather_lines = []

    apparent_temperature = weather_result.get("apparent_temperature")
    if apparent_temperature:
        weather_lines.append(f"- Feels like: {apparent_temperature} °C")

    humidity = weather_result.get("relative_humidity_2m")
    if humidity:
        weather_lines.append(f"- Humidity: {humidity} %")

    precipitation = weather_result.get("precipitation")
    if precipitation is not None:
        weather_lines.append(f"- Precipitation: {precipitation} mm")

    return chr(10).join(weather_lines)

def generate_story(description, temperature, wind_speed, location, weather_result):
    """Generate a emergency broadcast weather report"""
    location_lines = build_location_lines(location)
    weather_lines = build_weather_lines(weather_result)
    models = [
        "gemini-flash-lite-latest",
        "gemini-flash-latest",
        "gemini-3.5-flash",
        "gemini-3.6-flash",
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
                            {location_lines}
                            {weather_lines}

                            CORE RULES:
                            1. The weather itself MUST be the primary threat or the trigger of the horror. It must be impossible to separate the horror from the actual weather conditions.
                            2. Take inspiration from horror emergency alerts/broadcasts.
                            3. Introduce a terrifying phenomenon, an unexplained event or a survival threat directly connected to the weather.
                            4. Include one disturbing survival rule that people must follow to stay alive but STAY REALISTIC to what a person can do.
                            5. Build suspense, dread and a sense of impending catastrophe. Make the reader feel that something terrible is happening RIGHT NOW.
                            6. Avoid generic ghosts, serial killers or unrelated supernatural events.
                            7. No gore. Psychological and supernatural horror are welcome.
                            8. Make every story original, cinematic, immersive and suitable for a mature audience.
                            9. It should act as weather report DO NOT bring characters into it. 
                            10. The weather report should be the horror.
                            11. **CIVIL DEFENSE EMERGENCY BROADCAST:** should be at the start.
                            12. MAXIMUM 100 words.
                            13. The facts below are material to choose from. Use only the two or three that make the horror stronger. You do not need to mention all of them.
                            14. Every number you do mention must be exact.

                            IMPORTANT: Do not simply mention the weather. MAKE THE WEATHER THE MONSTER.

                            Write as if this were a scene from a horror movie, not a traditional short story."""
            )
            
            story = response.text
            break # if the story is generated successfully, break the loop
        except Exception as e:
            print(f"Error with model {model}: {e}")
            continue # if the model fails, try the next one

    if story is None:
        return "Every model is currently down. Please try again later."
    else:
        return story


if __name__ == "__main__":
    latitude, longitude = get_coordinates("Bad Dürkheim")
    temperature, weather_code, wind_speed = get_weather(latitude, longitude)
    description = weather_descriptions[weather_code]