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
- Synthetic speech (Edge-TTS) framed by a generated alarm tone (853 Hz + 960 Hz sine waves,
  built with numpy) before and after the voice. The voice itself is processed to sound like an
  old loudspeaker (band-pass filter plus quiet white noise, `pydub`)
- Real place facts (name, country, region, population, elevation) from the geocoding response and
  extra weather values (feels-like, humidity, precipitation) woven into the text
- Found imagery as haunted background (frosted glass with hands)

## Design direction
- Dark, foggy background with a darkened photo (assets/ghost.jpg)
- The warning pop-up is the only warm color: red/black hazard stripes, like a real alert
- The weather dashboard sits underneath the pop-up: the conditions as one large line, then five
  tiles in a three-column grid (temperature, wind, feels-like, humidity, precipitation)
- The page behind the pop-up has an old-monitor look: faint scanlines and very subtle noise, kept
  quiet on purpose. Principle: quiet and cold in the background, loud and red only for the alarm
- The pop-up stays as it is (hazard stripes, red border); a large "EMERGENCY" title and alarm icon
  were considered and dropped
- Still open: a short glitch burst when the warning opens (see the haunted-ui-polish spec)

## Story rules (see story.py for the exact prompt)
- Weather is the primary threat, with one disturbing survival rule
- Acts like a weather report, starts with "CIVIL DEFENSE EMERGENCY BROADCAST"
- No gore, psychological/supernatural horror only, maximum 100 words
- Place and weather facts are material to choose from, not a checklist; every number mentioned
  must be exact
- The survival rule must be harmless to follow (stay inside, close windows, stay silent). It must
  never involve blocking breathing, swallowing or inhaling anything, or harming oneself or others

## Responsible use
- The broadcast imitates an official alert and uses real data of a real town, so a visible notice
  ("Fictional entertainment, not a real alert") is shown in the pop-up, and no real authority names
  or logos are used
- Weather and place data come from Open-Meteo (CC BY 4.0, free for non-commercial use only);
  credit is shown in the app and in CREDITS.md
