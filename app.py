import streamlit as st
from weather import get_coordinates, get_weather
from weather_codes import weather_descriptions
from story import generate_story
from gtts import gTTS

st.title("Cursed Weather Report")
city = st.text_input("Enter a town") # input of the desired town

if city: # city is put in
    latitude, longitude = get_coordinates(city)
    temperature, weather_code, wind_speed = get_weather(latitude, longitude)
    description  = weather_descriptions[weather_code]
    story = generate_story(description, temperature, wind_speed)

    with st.spinner("RECEIVING TRANSMISSION…"):
        story = generate_story(description, temperature, wind_speed)

    st.write(story)

    # Text to Speech and save it as MP3
    tts = gTTS(text=story, lang="en")
    tts.save("warning.mp3")

    # Play MP3
    st.audio("warning.mp3", autoplay=True)