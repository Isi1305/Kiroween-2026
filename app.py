import streamlit as st
from weather import get_coordinates, get_weather, get_location
from weather_codes import weather_descriptions
from story import generate_story
import asyncio
import edge_tts
import base64
from audio import make_speech, build_broadcast

def set_background(image_path):
    """Settings for the background."""
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
                url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # extras for the emergency warning
    st.markdown(
    """
    <style>
    div[role="dialog"] {
        background-color: #000;
        border: 2px solid #d00000;
        background-image:
            repeating-linear-gradient(45deg, #d00000 0 14px, #000 14px 28px),
            repeating-linear-gradient(45deg, #d00000 0 14px, #000 14px 28px);
        background-size: 100% 18px, 100% 18px;
        background-position: top, bottom;
        background-repeat: no-repeat;
    } [data-testid="stAudio"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
    )

    # scanlines
    st.markdown(
        f"""
        <style>
        .stApp::after {{
        content: "";
        position: fixed
        inset: 0;
        pointer-events: none;
        z-index: 1;
        background: repeating-linear-gradient(
            0deg,
            rgba(0, 0, 0, 0.25) 0 1px,
            transparent 1px 3px
        );
        }}
        </style>
        """
        unsafe_allow_html=True
    )


set_background("assets/ghost.jpg")

@st.cache_data(ttl=900)
def cached_story(description, temperature, wind_speed, location, weather_result):
    """Returns the story text, or None if every model failed."""
    story = generate_story(description, temperature, wind_speed, location, weather_result)
    if story is None:
        raise RuntimeError("Every model is currently down. Please try again later.")
    return story

@st.dialog("CIVIL DEFENSE EMERGENCY BROADCAST") # pop up window
def show_warning(description, temperature, wind_speed, location, weather_result):
    """The warning is shown on screen with audio playing."""
    with st.spinner("RECEIVING TRANSMISSION…"):
        try:
            story = cached_story(description, temperature, wind_speed, location, weather_result)
        except RuntimeError:
            st.warning("Every model is currently down. Please try again later.")
            return
        
        asyncio.run(make_speech(story)) # make the audio
        broadcast = build_broadcast(voice_path="warning.mp3", output_path="broadcast.mp3")

    st.caption("Fictional entertainment, not a real alert")
    st.write(story)
    st.audio(broadcast, autoplay=True) # Autoplays the audio

st.title("Weather Report")
city = st.text_input("Enter a town") 
st.caption("Weather and location data by Open-Meteo.com (CC BY 4.0). Data is transformed into a fictional story. [Open-Meteo.com](https://open-meteo.com/)")

if city:
    location = get_location(city)

    if location is None:
        st.warning("Town not found. Please check the spelling.")
    else:
        latitude = location["latitude"]
        longitude = location["longitude"]
        weather_result = get_weather(latitude, longitude)
        temperature = weather_result["temperature_2m"]
        weather_code = weather_result["weather_code"]
        description = weather_descriptions[weather_code]
        wind_speed = weather_result["wind_speed_10m"]

        show_warning(description, temperature, wind_speed, location, weather_result)

        col1, col2, col3 = st.columns(3) # three columns next to each other
        col1.metric("Temperature", f"{temperature} °C")
        col2.metric("Wind", f"{wind_speed} km/h")
        col3.metric("Weather", f"{description}")
        col4, col5, col6 = st.columns(3)

        apparent_temperature = weather_result.get("apparent_temperature")
        if apparent_temperature is not None:
            col4.metric("Feels like", f"{apparent_temperature} °C")

        humidity = weather_result.get("relative_humidity_2m")
        if humidity is not None:
            col5.metric("Humidity", f"{humidity} %")

        precipitation = weather_result.get("precipitation")
        if precipitation is not None:
            col6.metric("Precipitation", f"{precipitation} mm")