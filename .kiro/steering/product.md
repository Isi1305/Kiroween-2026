# Product: Cursed Weather Report

A Streamlit web app built for the Kiroween 2026 hackathon (Frankenstein category).

## Concept
The user enters a town. The app fetches the **real current weather** and turns it into
a **cursed civil-defense emergency broadcast**: a short horror "weather report" that is
shown in a pop-up window and read aloud by a synthetic voice.

The app is horror from the start. It is NOT a normal weather app with a horror option.
The weather itself is the monster; the report is the horror. No characters.

## The stitched-together parts (Frankenstein idea)
- Real weather data (Open-Meteo: geocoding + current weather)
- Generative text (Google Gemini) written as an emergency broadcast
- Synthetic speech (Edge-TTS), planned: alarm tone and distorted radio effect
- Found imagery as haunted background (frosted glass with hands)

## Design direction
- Dark, foggy background with a darkened photo (images/ghost.jpg)
- The warning pop-up is the only warm color: red/black hazard stripes, like a real alert
- The weather tiles (temperature, wind, conditions) sit underneath the pop-up
- Planned: old CRT monitor look (scanlines, flicker), alarm icon, large "EMERGENCY" title

## Story rules (see story.py for the exact prompt)
- Weather is the primary threat, with one disturbing survival rule
- Acts like a weather report, starts with "CIVIL DEFENSE EMERGENCY BROADCAST"
- No gore, psychological/supernatural horror only, maximum 100 words
