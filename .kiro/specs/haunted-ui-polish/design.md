# Design: Haunted UI polish

## Overview
Two independent parts:
1. **Visual:** CSS overlays for scanlines, noise and a one-shot glitch, injected from `app.py`.
2. **Audio:** a small filter step in `audio.py` between speech generation and the final mix.

## Visual design (app.py)

### Overlay layer
A pseudo-element on the app container (`.stApp::after`) covers the whole page:
- `pointer-events: none` so clicks and typing still work (Req 2.4)
- `position: fixed; inset: 0` and a low `z-index` below the pop-up (Req 2.3)
- Background = `repeating-linear-gradient` for scanlines plus a very low-opacity noise texture
  (a small inline SVG with `feTurbulence`, so no extra asset file is needed)

Stable selectors only: `.stApp`, `div[role="dialog"]`, `[data-testid="stAudio"]`.
Never the generated `st-emotion-cache-*` classes.

### Pop-up
Untouched (Req 5). The overlay must sit **behind** `div[role="dialog"]`; check the layering in
the browser.

### Glitch burst
- A `@keyframes` animation (small horizontal offsets, brief colour-channel split, short
  brightness change) that runs **once** (`animation: glitch 0.9s steps(...) 1`).
- It is started by injecting a small `<style>` block from `show_warning` at the moment the
  dialog opens.
- Safety: at most three changes per second, and a
  `@media (prefers-reduced-motion: reduce)` rule that disables it (Req 3.3, 3.4).
- **Open technical question:** Streamlit reruns the script, so a one-shot animation may
  replay or not start at the right moment. This must be tried in the browser. Fallback:
  Req 3.5.

## Audio design (audio.py)

New function `radio_filter(voice)`:
1. high-pass filter around 300 Hz and low-pass filter around 3000 Hz (telephone/loudspeaker band)
2. generate quiet white noise with numpy and overlay it
3. return the processed `AudioSegment`

`build_broadcast` becomes: `tone + radio_filter(voice) + tone` (the tone stays clean, Req 4.3).
The filter call is wrapped in `try/except`; on failure the original voice is used (Req 4.4).
The exact cut-off values and noise level are tuned by ear.

## Data flow
```
make_speech -> warning.mp3 -> radio_filter -> tone + voice + tone -> broadcast.mp3 -> st.audio
```

## Error handling
- Filter or noise failure: fall back to the unprocessed voice.
- Glitch not reliable: fall back to constant subtle noise.

## Testing approach
- Visual: check in the browser that the pop-up text is crisp, the page behind has
  scanlines, clicks work, and the glitch lasts about one second.
- Audio: listen to the result; the words must stay understandable.
- Accessibility: turn on "reduce motion" in the operating system and confirm no glitch.
