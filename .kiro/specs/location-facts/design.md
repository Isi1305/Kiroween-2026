# Design: Location facts in the broadcast

## Overview
`weather.py` returns the whole geocoding result for a town instead of only two numbers.
`app.py` passes the facts on, and `story.py` writes them into the prompt. No new API call,
no new dependency.

## Data flow
```
user input (town)
   -> weather.get_location(town)          # one geocoding request
   -> location dict (name, country, region, population, elevation, latitude, longitude)
   -> weather.get_weather(latitude, longitude)
   -> app.show_warning(description, temperature, wind_speed, location)
   -> story.generate_story(..., location)  # prompt contains weather AND facts
   -> audio.make_speech / build_broadcast
```

## Components and changes

### weather.py
- New function `get_location(town)` returns the first geocoding result as a dict, or `None`
  if nothing was found. Request uses `language="en"`.
- Design decision: return the whole result dict (flexible) instead of a longer tuple
  (every caller would have to unpack all values).
- `get_weather` stays as it is.

### app.py
- Call `get_location(city)`. IF the result is `None`, show `st.warning(...)` and stop.
- Read `latitude` / `longitude` from the dict and call `get_weather`.
- Pass `location` into `show_warning` and on to `generate_story`.
- Add a small credit line for Open-Meteo.

### story.py
- `generate_story` gets a fourth parameter `location`.
- A small helper builds the fact lines and skips missing values, for example:
  `- Location: Bad Dürkheim, Rheinland-Pfalz, Germany`
  `- Population: 18698`
  `- Elevation: 133 m`
- The lines are inserted below the weather lines in the prompt. A new rule asks the model
  to use the facts naturally and keep the numbers exact.

## Data model (geocoding result fields used)
| Field | Use | May be missing |
|-------|-----|----------------|
| name | town name | no |
| country | country name | rarely |
| admin1 | region / state | yes |
| population | residents | yes |
| elevation | metres above sea level | yes |
| latitude, longitude | weather request | no |

## Error handling
- Town not found: `get_location` returns `None`, the app shows a friendly warning.
- Missing optional field: the helper skips the line.
- Network errors keep the current behaviour (out of scope here).

## Testing approach
- Manual check list: a normal town, a town without population data, a nonsense string,
  a town with special characters.
- The helper that builds the fact lines is a pure function and can be tested without
  network access.
