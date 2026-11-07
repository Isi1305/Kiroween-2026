# Requirements: Haunted UI polish

## Introduction
The app already has a darkened ghost photo as background, a red/black hazard-stripe pop-up
and a dark synthetic voice framed by an alarm tone. This spec covers the remaining design
work, taken from the developer's own notes (written before implementation):

- Colors: dark, cool, black, grey (blue was considered and **dropped**, the current look stays)
- Alarm: red, black, striking, the pop-up stays as it is
- Look: ghost background, quiet
- CRT monitor: noise, glitch effect
- Voice: radio, dark, eerie

Guiding principle: **quiet and cold in the background, loud and red only for the alarm.**

## Decisions made
| Question | Decision |
|----------|----------|
| Where does the CRT effect apply? | Only to the page behind the pop-up; the pop-up stays clean and readable |
| Glitch timing | One short burst when the warning appears; otherwise only subtle noise |
| Blue tint | No. Keep the current dark grey look |
| Voice | Like an old loudspeaker (dull, slightly noisy), not heavily distorted |

## Requirements

### Requirement 1: Keep the quiet background
**User story:** As a viewer, I want the background to stay calm so that the alarm stands out.

#### Acceptance criteria
1. THE app SHALL keep the darkened ghost image as page background.
2. THE app SHALL NOT add a blue color tint.

### Requirement 2: CRT monitor look behind the pop-up
**User story:** As a viewer, I want the page to feel like an old monitor.

#### Acceptance criteria
1. THE app SHALL draw faint horizontal scanlines over the page background.
2. THE app SHALL show a subtle, low-opacity noise texture over the page background.
3. THE scanlines and noise SHALL NOT cover or reduce the readability of the pop-up text.
4. THE scanlines and noise SHALL NOT block clicks or typing.

### Requirement 3: Short glitch burst on warning
**User story:** As a viewer, I want a brief glitch when the warning arrives, so it feels like
the signal is breaking.

#### Acceptance criteria
1. WHEN the warning pop-up opens, THE app SHALL play a glitch effect on the page behind it
   for about one second.
2. AFTER the burst, THE page SHALL return to the calm state with only the subtle noise.
3. THE glitch SHALL NOT flash more than three times per second.
4. WHERE the browser asks for reduced motion, THE app SHALL skip the glitch animation.
5. IF the glitch trigger cannot be made to work reliably in Streamlit, THEN THE app SHALL fall
   back to the constant subtle noise only (no flicker).

### Requirement 4: Old-loudspeaker voice
**User story:** As a listener, I want the voice to sound like an old public-address speaker.

#### Acceptance criteria
1. THE audio module SHALL apply a band-limiting filter (cut very low and very high
   frequencies) and a small amount of noise to the synthesized voice.
2. THE voice SHALL remain easy to understand.
3. THE alarm tone before and after the voice SHALL stay unprocessed.
4. IF the voice processing fails, THEN THE app SHALL play the unprocessed voice instead of
   failing.

### Requirement 5: Pop-up stays as it is
#### Acceptance criteria
1. THE pop-up SHALL keep its current hazard stripes, red border and black background.

## Out of scope
- Blue tint.
- New title or alarm icon inside the pop-up (the pop-up stays as it is).
- Revealing the hands after the pop-up is closed (idea for later).
