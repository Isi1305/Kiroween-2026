# Cursed weather report
The app shows the current weather of the city the user inputs. This generates an emergency broadcast inspired by
fake horror emergency broadcasts on Youtube.

> Fictional entertainment, not a real alert

> Live demo: The link to the App will be here in February.

(If the app is asleep, click the wake-up button and wait a moment.)
(The app uses the free version of Gemini API so it can only generate a limited amount of reports.)

<img width="1873" height="905" alt="Screenshot 2026-11-13 135025" src="https://github.com/user-attachments/assets/8b88b98c-4cac-4eac-baa7-73a39d40344c" />
<img width="1865" height="907" alt="Screenshot 2026-11-13 135051" src="https://github.com/user-attachments/assets/48a26faa-3e20-4017-b055-5b32434d0e60" />
<img width="1863" height="909" alt="Screenshot 2026-11-13 135113" src="https://github.com/user-attachments/assets/5c21ac8d-fe5b-4ba9-9a0b-7c3393b90b1b" />
<img width="1867" height="909" alt="Screenshot 2026-11-13 135120" src="https://github.com/user-attachments/assets/2b9c3221-cd9c-41e6-89be-39f3b5b586f4" />

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
