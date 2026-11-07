import streamlit as st
from weather import get_coordinates, get_weather
from weather_codes import weather_descriptions
from story import generate_story
import asyncio
import edge_tts

async def make_speech(text, filename="warning.mp3"):
    communicate = edge_tts.Communicate(
        text,
        voice="en-US-ChristopherNeural",
        rate="-10%",
        pitch="-10Hz",
        volume="+0%"
    )
    await communicate.save(filename)

@st.dialog("CIVIL DEFENSE EMERGENCY BROADCAST")
def show_warning(description, temperature, wind_speed):
    with st.spinner("RECEIVING TRANSMISSION…"):
        story = generate_story(description, temperature, wind_speed)
        asyncio.run(make_speech(story))

    st.write(story)
    st.audio("warning.mp3", autoplay=True)

st.title("Weather Report")
city = st.text_input("Enter a town")

if city:
    latitude, longitude = get_coordinates(city)
    temperature, weather_code, wind_speed = get_weather(latitude, longitude)
    description = weather_descriptions[weather_code]

    show_warning(description, temperature, wind_speed)
