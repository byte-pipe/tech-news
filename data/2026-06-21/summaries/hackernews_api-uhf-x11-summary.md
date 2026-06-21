---
title: UHF X11
url: https://www.lispm.net/apps/uhf-x11/
date: 2026-06-21
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-21T11:06:53.884901
---

# UHF X11

# UHF X11

## Objective
- Turns Apple Vision Pro into a full X11 display server.
- Allows Xlib clients to run in native, pixel‑precise spatial windows on visionOS.
- Example usage:
  - `setenv DISPLAY VISOR.LOCAL:0`
  - Launch typical X11 programs (`xterm`, `xclock`, `xlogo`, `xcalc`, `twm`).

## Specification

### Rootless Spatial Windows
- Each X11 top‑level window appears as an independent visionOS window.
- Users can position windows anywhere in the 3‑D space.

### External X11 Clients
- Accepts TCP connections from trusted machines using standard X11 protocol.

### Beautiful Pixel Rendering
- Presents framebuffer at native resolution.
- Uses nearest‑neighbor scaling for small surfaces to preserve pixel sharpness.

### 80s‑Soaked Effects
- Optional visual presets: CRT scanlines, phosphor masks, glow, vignette.

### MIT‑MAGIC‑COOKIE‑1
- Generates X authority cookies on the device.
- Cookies are copied to client machines for authenticated connections.

### Experimental Indirect GLX
- Supports GLX rendering for OpenGL clients over X11.
- Compatibility varies, similar to early 2000s implementations.

### Custom Font Packs
- Allows importing bitmap font directories from visionOS folders.
- Core X11 fonts are bundled with the application.

## Additional Information
- Installation involves acquiring a QIC tape and installing the distribution.
- Sections on privacy and support are provided within the app.