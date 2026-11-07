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

- [ ] 5. A few more real weather values
  - [ ] 5.1 Look up the exact Open-Meteo variable names (humidity, feels-like, precipitation)
  - [ ] 5.2 Decide: return a dict from `get_weather` and update the callers accordingly
  - [ ] 5.3 Request the extra values and show them as tiles; skip missing ones
  - [ ] 5.4 Add the values to the prompt, numbers kept exact
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [ ] 6. Fiction notice
  - [ ] 6.1 Add "Fictional entertainment, not a real alert" at the bottom of the pop-up
  - [ ] 6.2 Add the same statement to the README and the project description later
  - _Requirements: 6.1, 6.2, 6.3_

- [ ] 7. Check it manually
  - [ ] 7.1 Normal town, town without population, nonsense input, special characters
  - [ ] 7.2 Confirm the broadcast mentions the real town and keeps all numbers exact
  - [ ] 7.3 Confirm the fiction notice is visible in the pop-up without scrolling
  - _Requirements: all_

- [ ] 8. Optional: try property-based testing (PBT)
  The developer wants to try this after tasks 1-7 are done. It is an experiment, not a requirement.
  - [ ] 8.1 Install `pytest` and `hypothesis`
  - [ ] 8.2 Move the fact-line helper into a pure function (no network) so it can be tested
  - [ ] 8.3 Derive properties from the acceptance criteria, for example:
    - missing fields never produce a line and never produce the text `None` (Requirement 2.1)
    - every number that is present appears unchanged in the output (Requirement 3.2)
    - the output is always text, whatever the input (Requirement 2.1)
    - every weather code from `weather_descriptions` returns a non-empty description
  - [ ] 8.4 Run the tests; write down anything unexpected that Hypothesis finds
  - [ ] 8.5 Check whether Kiro's built-in PBT feature (spec requirements to properties) is available in Kiro Web, and report honestly in the write-up either way
  - _Requirements: 2.1, 3.2, 5.4_
