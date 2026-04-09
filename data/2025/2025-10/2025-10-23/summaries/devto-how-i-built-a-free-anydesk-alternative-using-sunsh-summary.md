---
title: How I Built a Free AnyDesk Alternative Using Sunshine, Moonlight & Tailscale - DEV Community
url: https://dev.to/thevenice/how-i-built-a-free-anydesk-alternative-using-sunshine-moonlight-tailscale-3lh8
date: 2025-10-22
site: devto
model: llama3.2:1b
summarized_at: 2025-10-23T11:19:08.531193
screenshot: devto-how-i-built-a-free-anydesk-alternative-using-sunsh.png
---

# How I Built a Free AnyDesk Alternative Using Sunshine, Moonlight & Tailscale - DEV Community

# How I Built a Free AnyDesk Alternative Using Sunshine, Moonlight & Tailscale - DEV Community

## Key Points:

• Installed Sunshine and Moonlight on Windows PC to serve as host app.
• Configured Sunshine to stream 1080p/60 FPS from Sunnshine localhost:47990 via Firefox.
• Used Moonlight on MacBook Air to connect to Sunshine client, gaining near-zero latency.
• Set up Secure Simple Mesh VPN (Tailscale) for private remote access from any location worldwide.

## How it Works:

1. **Sunshine**:
	* Host app runs on Windows PC and handles encoding and streaming via Sunshine localhost:47990 port.
	* User configures username, password and app list in Firefox.
2. **Moonlight**:
	* Client connects to Sunshine’s local host URL using Moonlight, gaining automatic IP mapping.
	* Manually maps IP address for optimal performance and latency.

## Optimization:

1. _Resolution_: Setting 1080p/60 FPS ensures smooth streaming while minimizing computational overhead.
2. _Bitrate_: Selecting a bitrate range of 20-40 Mbps (Wi-Fi) yields ideal balance between bandwidth requirements and latency reduction.
3. _Audio Configuration_: Enabling stereo for minimized audio lag helps enhance overall user experience.
4. _Input Settings**: Customizing low-latency mode allows users to prioritize real-time data transmission over video quality.

## Benefits:

1. **Security**: 100% free and open-source, Sunshine and Moonlight offer uncompromised security against malware and unauthorized access.
2. **Free** accessibility: No cost for commercial alternatives like AnyDesk or TeamViewer makes Sunshine & Moonlight an attractive option for enthusiasts and professionals alike.
