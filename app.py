import streamlit as st
from weather import get_coordinates, get_weather
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

set_background("assets/ghost.jpg")

@st.dialog("CIVIL DEFENSE EMERGENCY BROADCAST") # pop up window
def show_warning(description, temperature, wind_speed):
    """The warning is shown on screen with audio playing."""
    with st.spinner("RECEIVING TRANSMISSION…"):
        story = generate_story(description, temperature, wind_speed)
        asyncio.run(make_speech(story)) # make the audio
        broadcast = build_broadcast(voice_path="warning.mp3", output_path="broadcast.mp3")


    st.write(story)
    st.audio(broadcast, autoplay=True) # Autoplays the audio

st.title("Weather Report")
city = st.text_input("Enter a town") 

if city:
    latitude, longitude = get_coordinates(city)
    temperature, weather_code, wind_speed = get_weather(latitude, longitude)
    description = weather_descriptions[weather_code]

    show_warning(description, temperature, wind_speed)

    col1, col2, col3 = st.columns(3) # three columns next to each other
    col1.metric("Temperature", f"{temperature} °C")
    col2.metric("Wind", f"{wind_speed} km/h")
    col3.metric("Weather", f"{description}")