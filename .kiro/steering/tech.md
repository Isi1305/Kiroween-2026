# Tech stack and conventions

## Stack
- Python 3, run inside Anaconda on Windows
- Streamlit for the UI (custom CSS injected with `st.markdown(..., unsafe_allow_html=True)`)
- `requests` for HTTP calls to Open-Meteo
- `google-genai` for Gemini, with a fallback loop over several model names
- `edge-tts` for speech (async, wrapped with `asyncio.run`)
- `pydub` + `ffmpeg` to combine audio; `numpy` + `scipy` to generate the alarm tone
- `python-dotenv` to load the API key from `.env`

## Run
`python -m streamlit run app.py` from the project folder.
Use `python -m pip ...` instead of plain `pip` (PATH problems on this machine).

## Conventions
- All code, comments and UI text are in **English**.
- Functions have docstrings; helper functions live at the top of the file.
- Logic and UI are separated: `weather.py` and `story.py` contain no Streamlit code.
- The UI (including the `st.dialog` pop-up) lives in `app.py`.

## Security
- The Gemini key lives only in `.env` (GEMINI_API_KEY). Never commit it or hard-code it.
- `.env`, `__pycache__/` and generated audio (`warning.mp3`) are in `.gitignore`.
- Do NOT add `.kiro/` to `.gitignore` (required for the hackathon submission).

## Known gotchas
- Gemini models are sometimes overloaded (503) or retired (404): keep the model fallback list.
- CSS selectors: use stable attributes (`role="dialog"`, `data-testid="stAudio"`),
  never the generated `st-emotion-cache-*` classes.
- Streamlit reruns the whole script on every interaction.
- Do not start the app while a conda install is running.
