# Cursed weather report
The app shows the current weather of the city the user inputs. This generates an emergency broadcast inspired by
fake horror emergency broadcasts on Youtube.

> Fictional entertainment, not a real alert

> Live demo: The link to the App will be here in February.

> (If the app is asleep, click the wake-up button and wait a moment.)
> (The app uses the free version of Gemini API so it can only generate a limited amount of reports.)

Features 
- Real-time weather for any city. Enter a city name, and the app retrieves the actual temperature, wind, and weather conditions for that location.
- The announcement knows the location. The city, country, region, population, and elevation are incorporated into the story using real-world data.
- AI-generated emergency broadcasts. An AI writes the warning in the style of an emergency alert, with the weather itself portrayed as the threat. Behind the scenes, a chain of multiple AI models is used, automatically switching to the next model if one fails.
- Spoken with an alarm tone. A synthetic voice reads the warning aloud, accompanied by a custom-generated emergency alert tone consisting of two overlapping sine waves at 853 Hz and 960 Hz.
- Visual design: An emergency warning pop-up featuring red-and-black hazard stripes over a darkened, ghostly background image.
- Robust and reliable: If an unknown city is entered, the app displays a friendly message instead of crashing. A clear disclaimer also informs users that everything is fictional.

How to run locally: Python, pip install -r requirements.txt, ffmpeg, .env with GEMINI_API_KEY, streamlit run app.py or python -m streamlit run app.py.

Credits & licenses: Open-Meteo (CC BY 4.0, free for non-commercial use only) Weather and location data by Open-Meteo.com (CC BY 4.0). Data is transformed into a fictional story. [Open-Meteo.com](https://open-meteo.com/), 
Pixabay-picture by StockSnap (https://pixabay.com/de/photos/schwarz-und-weiß-unheimlich-geist-2603731/),
Google Gemini API: broadcast text (AI generated),
Edge-TTS (Microsoft Speech Service via an unofficial library): Voice,
AGPL-3.0

Built with Kiro Web: .kiro/ Steering, Specs and a Hook. No Kiro IDE due to already having a set up IDE for Python.
