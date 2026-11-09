# Tech stack and conventions

## Stack
- Python 3, run inside Anaconda on Windows
- Streamlit for the UI (custom CSS injected with `st.markdown(..., unsafe_allow_html=True)`)
- `requests` for HTTP calls to Open-Meteo
- `google-genai` for Gemini, with a fallback loop over several model names
- `edge-tts` for speech (async, wrapped with `asyncio.run`)
- `pydub` + `ffmpeg` to combine audio and apply the old-loudspeaker effect (high-pass/low-pass filter
  plus white noise); `numpy` + `scipy` to generate the alarm tone
- `python-dotenv` to load the API key from `.env`
- Hosted on Streamlit Community Cloud (see "Hosting" below)
- `streamlit` is pinned to `1.51.0` in `requirements.txt`

## Run
`python -m streamlit run app.py` from the project folder.
Use `python -m pip ...` instead of plain `pip` (PATH problems on this machine).

## Conventions
- All code, comments and UI text are in **English**.
- Functions have docstrings; helper functions live at the top of the file.
- Logic and UI are separated: `weather.py` and `story.py` contain no Streamlit code.
- The UI (including the `st.dialog` pop-up) lives in `app.py`.
- All audio logic lives in `audio.py` (`make_speech`, `radio_filter`, `build_broadcast`).
- Helper functions that turn data dicts into prompt lines live in `story.py`
  (`build_location_lines`, `build_weather_lines`). Optional values are skipped when missing;
  test with `is not None`, never `if value:` (0 and 0.0 are valid weather values).
- `generate_story` returns the story text, or `None` if every model failed. `cached_story` in `app.py`
  raises `RuntimeError` on `None`, so errors are never cached, and `show_warning` shows a plain
  warning (no voice, no alarm tone) in that case.
- `make_alarm.py` is a one-time script that generates `assets/alarm.wav`; the app only reads it.
- Static files (background image, alarm sound) live in `assets/`.

## Security
- The Gemini key lives only in `.env` (GEMINI_API_KEY). Never commit it or hard-code it.
- `.env`, `__pycache__/` and generated audio (`warning.mp3`) are in `.gitignore`.
- Do NOT add `.kiro/` to `.gitignore` (required for the hackathon submission).

## Hosting (Streamlit Community Cloud)
- Choose **Python 3.13** when creating the app. Python 3.14 has no ready-made `pyarrow` wheel for
  `streamlit==1.51.0`, so the install tries to compile it and fails (`cmake` missing).
- Keep `streamlit==1.51.0` pinned. Without the pin the cloud installs a newer Streamlit whose dialog
  markup no longer matches the CSS selector `div[role="dialog"]`, and the pop-up design disappears.
- `packages.txt` contains `ffmpeg`; `requirements.txt` contains `audioop-lts; python_version >= "3.13"`.
- The key is set as the secret `GEMINI_API_KEY` in the app settings, never in the repository.
- After a push the cloud may briefly run new `app.py` with old imported modules (e.g. a `TypeError`).
  Wait a minute and reload first; use "Reboot app" if it persists.
- Logs: "Manage app" shows installation output and the `print` messages (model errors, radio filter).

## Gemini quota
- The free tier allows only about 20 requests per day per model, shared between local tests and the
  hosted app. When it is used up the API returns `429 RESOURCE_EXHAUSTED`.
- Names ending in `-latest` returned `404` on the cloud (newer `google-genai`), so check the model
  list in the cloud log before trusting a name.
- Responses are cached for 15 minutes with `st.cache_data(ttl=900)` to save requests.
- Do not enable anything that requires billing.

## Known gotchas
- Gemini models are sometimes overloaded (503) or retired (404): keep the model fallback list.
- CSS selectors: use stable attributes (`role="dialog"`, `data-testid="stAudio"`),
  never the generated `st-emotion-cache-*` classes.
- Streamlit reruns the whole script on every interaction.
- Do not start the app while a conda install is running.
- `pydub` needs `ffmpeg` on the PATH to read MP3 files (install with
  `conda install -c conda-forge ffmpeg`). Starting Python by full path without activating
  conda gives `WinError 2`: start from the Anaconda Prompt or add `...\Library\bin` to PATH.
- On Python 3.13+ `pydub` additionally needs the `audioop-lts` package.
- If there is no sound, check the headphones/output device first.
