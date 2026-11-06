import streamlit as st
from weather import get_coordinates, get_weather
from weather_codes import weather_descriptions
from story import generate_story

st.title("Cursed Weather Report")
city = st.text_input("Enter a town") # input of the desired town

if st.button("Generate warning"): # button to generate a story
    latitude, longitude = get_coordinates(city)
    temperature, weather_code, wind_speed = get_weather(latitude, longitude)
    description  = weather_descriptions[weather_code]
    story = generate_story(description , temperature, wind_speed)
    st.write(story)