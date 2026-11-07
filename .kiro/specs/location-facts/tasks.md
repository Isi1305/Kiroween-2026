# Implementation plan: Location facts in the broadcast

The developer writes the code herself; Kiro explains concepts and reviews (see
`.kiro/steering/working-style.md`). Tick each task when it is done.

- [ ] 1. Add `get_location` to `weather.py`
  - [ ] 1.1 Send the geocoding request with `language="en"`
  - [ ] 1.2 Return the first result as a dict, or `None` if there are no results
  - _Requirements: 1.1, 1.2, 1.3, 2.2_

- [ ] 2. Use the new function in `app.py`
  - [ ] 2.1 Call `get_location(city)` and show `st.warning` when it returns `None`
  - [ ] 2.2 Read latitude and longitude from the dict and call `get_weather`
  - [ ] 2.3 Pass `location` through `show_warning`
  - _Requirements: 1.3, 2.2_

- [ ] 3. Put the facts into the prompt in `story.py`
  - [ ] 3.1 Add the `location` parameter to `generate_story`
  - [ ] 3.2 Write a helper that builds fact lines and skips missing values
  - [ ] 3.3 Insert the fact lines and the new rule (use facts naturally, keep numbers exact)
  - _Requirements: 2.1, 3.1, 3.2, 3.3_

- [ ] 4. Credit the data source
  - [ ] 4.1 Add a short Open-Meteo credit line to the app
  - [ ] 4.2 Add the credit to the README when it exists
  - _Requirements: 4.1, 4.2_

- [ ] 5. Check it manually
  - [ ] 5.1 Normal town, town without population, nonsense input, special characters
  - [ ] 5.2 Confirm the broadcast mentions the real town and keeps the numbers exact
  - _Requirements: all_
