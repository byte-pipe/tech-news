---
title: "Unlag Neo: Macbook Neo Cursor lag \"fix\" · GitHub"
url: https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf
date: 2026-06-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-25T05:57:03.623034
---

# Unlag Neo: Macbook Neo Cursor lag "fix" · GitHub

# Unlag Neo: A “fix” for the cursor lag on Macbook Neo

- **Problem**  
  - On a MacBook Neo (macOS Tahoe 26.5.1) the mouse cursor lags near the screen edges and inside Terminal windows.  
  - The lag appears when the system switches from a hardware cursor to a software cursor (`CGCursorIsDrawnInFramebuffer()` changes from 0 to 1).  
  - The hardware cursor only returns after about 17 seconds after unlocking the screen.

- **Hypothesised cause**  
  - The transition to a software cursor may be stalled.  
  - At screen edges only part of the cursor is rendered; Terminal may trigger extra graphics work, prompting the OS to use a software cursor.  
  - The 17‑second delay after unlocking suggests some background initialization.

- **Desired proper fix**  
  - Apple should resolve the lag directly.  
  - Alternatively, force the system to always use a software cursor (requires reverse‑engineering WindowServer or disabling SIP).  
  - Investigate what changes after the 17‑second unlock period.

- **Temporary work‑arounds**  
  - Enable macOS Color Filter (e.g., Blue/Yellow) at low intensity – changes colors and fails with Night Shift.  
  - Increase cursor size significantly – a small change does not help.  
  - **Screen Recording** – the most reliable fix: forcing the compositor to use a software cursor eliminates the lag.  
    - An indicator appears in the menu bar; it can be hidden by disabling SIP (not explored).  

- **Preferred solution: Screen Recording**  
  - Minimal CPU/GPU impact (record 1 pixel every 10 seconds, discarding to `/dev/null`).  
  - Implemented via a small script (`create_unlag_neo_app.sh`) that builds a self‑contained `.app`.  
  - The app runs in the background, requests Screen‑Recording and Accessibility permissions, and shows a tiny menu‑bar icon to toggle the fix or pause in fullscreen mode.

- **How to build and use the app**  
  1. Make the script executable: `chmod +x create_unlag_neo_app.sh`.  
  2. Run it: `./create_unlag_neo_app.sh`.  
  3. It creates `Unlag Neo.app`. Move the app to `/Applications` (or any location).  
  4. Launch the app and grant the requested permissions.  
  5. Use the menu‑bar icon to enable/disable the fix or pause when a fullscreen video is playing.

- **Debug / development notes**  
  - Re‑building the app may cause macOS permission dialogs to behave oddly; rename the app, manually adjust permissions, delete `~/Library/Preferences/Unlag Neo.plist`, or kill `cfprefsd`.  
  - The Swift source embedded in the script handles permission alerts, relaunching, and opening the appropriate System Settings panes.  

- **Additional ideas**  
  - Identify what Terminal does that triggers the lag and create a dummy overlay app that mimics the behavior.  
  - Explore forcing a permanent software cursor without screen recording.  

- **Conclusion**  
  - While not a permanent fix, the screen‑recording app effectively removes cursor lag on the MacBook Neo with negligible resource usage, offering a practical interim solution until Apple addresses the underlying issue.