# Requirements: Location facts in the broadcast

## Introduction
The geocoding response from Open-Meteo already contains facts about the town the user
searched for (country, region, population, elevation). Today only latitude and longitude
are used. This feature feeds those real facts into the story prompt, so each emergency
broadcast refers to the real place and feels personal ("18,698 residents of Bad Dürkheim").

It also fixes two weaknesses found while planning:
- an unknown town crashes the app (`data["results"][0]` raises an error),
- the geocoding language is German while the app and the broadcast are English.

## Requirements

### Requirement 1: Retrieve location facts
**User story:** As a user, I want the broadcast to mention my real town, so that it feels like
it was written for me.

#### Acceptance criteria
1. WHEN the user enters a town name, THE app SHALL retrieve the town name, country, region,
   population and elevation from the Open-Meteo geocoding API.
2. THE app SHALL request the geocoding results in English.
3. THE app SHALL still obtain latitude and longitude from the same request, so no
   additional API call is needed.

### Requirement 2: Handle missing data
**User story:** As a user, I want the app to keep working when some facts are unknown.

#### Acceptance criteria
1. IF a fact (for example population or region) is missing in the response, THEN THE app
   SHALL leave that fact out of the prompt and continue normally.
2. IF the town cannot be found, THEN THE app SHALL show a short, friendly message instead of
   crashing and SHALL NOT start the story or audio generation.

### Requirement 3: Use the facts in the story
**User story:** As a user, I want the broadcast to use the real facts naturally.

#### Acceptance criteria
1. WHEN the story prompt is built, THE story generator SHALL include all available location
   facts next to the weather data.
2. THE prompt SHALL instruct the model to use the facts naturally and not to change numbers.
3. THE existing story rules (weather is the threat, no characters, no gore, at most 100
   words) SHALL remain unchanged.

### Requirement 4: Credit the data source
**User story:** As the author, I want to follow the data provider's attribution terms.

#### Acceptance criteria
1. THE app SHALL show a short credit line naming Open-Meteo as the source of weather and
   location data.
2. THE README SHALL repeat the credit.

## Out of scope
- Wikipedia text about the town (separate future spec).
- Automatic location detection.
