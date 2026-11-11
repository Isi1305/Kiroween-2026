# Implementation plan: Haunted UI polish

The developer writes the code herself; Kiro explains concepts and reviews (see
`.kiro/steering/working-style.md`). Order: function first, then beauty, one thing at a time.

- [x] 1. Old-loudspeaker voice (`audio.py`)
  - [x] 1.1 Write `radio_filter(voice)` with a high-pass and a low-pass filter
  - [x] 1.2 Add quiet white noise with numpy and overlay it
  - [x] 1.3 Use it in `build_broadcast` for the voice only, with a `try/except` fallback
  - [x] 1.4 Tune cut-offs and noise level by ear; check the words stay clear
  - _Requirements: 4.1, 4.2, 4.3, 4.4_

- [x] 2. CRT look behind the pop-up (`app.py`)
  - [x] 2.1 Add a CSS overlay (`.stApp::after`) with scanlines, `pointer-events: none`
  - [x] 2.2 Add the low-opacity noise texture
  - [x] 2.3 Check layering: pop-up text crisp, typing and clicking still work
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 1.1, 1.2, 5.1_

- [ ] 3. Glitch burst on warning (`app.py`)
  - [ ] 3.1 Write the `@keyframes` animation (one second, at most three changes per second)
  - [ ] 3.2 Start it when `show_warning` opens the dialog
  - [ ] 3.3 Add the `prefers-reduced-motion` rule
  - [ ] 3.4 Try it in the browser; if unreliable, apply the fallback (constant noise only)
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

- [ ] 4. Check everything
  - [ ] 4.1 Run the whole flow: town -> glitch -> pop-up -> broadcast -> close
  - [ ] 4.2 Test with reduced motion switched on
  - [ ] 4.3 Take screenshots for the README and the video
  - _Requirements: all_
