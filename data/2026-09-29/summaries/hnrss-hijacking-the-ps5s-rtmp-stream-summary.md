---
title: "Hijacking the PS5's RTMP Stream"
url: https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/
date: 2026-09-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-29T07:31:28.062558
---

# Hijacking the PS5's RTMP Stream

# Hijacking the PS5's RTMP Stream

## The Problem
- PS5’s built‑in “Broadcast” button only works with a few supported services.  
- Want to stream gameplay to Discord without buying an expensive capture card.  
- Capture cards cost > $100; looking for a cheaper solution.

## Remote Play
- Remote Play lets the PS5 run on a Mac, then share the Mac’s screen to Discord.  
- Requires all peripherals (controller, headphones) to be connected to the Mac.  
- Issues: occasional input lag and stream quality is fixed by the PS5, not configurable.  
- Goal: avoid re‑configuring hardware for each streaming session.

## How PS5 Streaming Works
- PS5 streams to YouTube/Twitch via RTMP (Real‑Time Messaging Protocol).  
- When “Broadcast” is pressed, the console resolves a Twitch hostname via DNS, then sends the RTMP stream to the returned ingest server.  
- Idea: spoof the DNS response so the stream is directed to a local device instead of Twitch.

## Finding the Right Hostname
- Initial attempt to spoof `ingest.twitch.tv` failed because it is a discovery endpoint (HTTPS on port 443) that returns the actual ingest server and validates TLS certificates.  
- YouTube’s RTMP ingest uses plain RTMP (port 1935) and works, but YouTube’s API check stops the broadcast after ~60 seconds.  
- By monitoring DNS logs, discovered the real RTMP server hostname: `ingest.global-contribute.live-video.net` → `aps30.contribute.live-video.net`.  
- Spoofing `*.contribute.live-video.net` redirects the true RTMP endpoint without TLS issues.

## DNS Trick
- Uses `dnsmasq` on macOS to resolve all Twitch ingest domains to the Mac’s LAN IP (e.g., `192.168.8.175`).  
- Example `dnsmasq.conf` entries redirect multiple Twitch subdomains to the Mac.  
- Configured a GL.iNet router (OpenWRT) to provide the Mac’s IP as the DNS server for the PS5 via a DHCP option tag (`tag:PS5,6,192.168.8.175`).  
- PS5 picks up the custom DNS on its next DHCP renewal, requiring no manual changes on the console.

## Receiving the Stream
- Runs `nginx-rtmp` on the Mac to accept the incoming RTMP stream on port 1935.  
- Configuration defines an application `ps5` with live streaming enabled and an `on_publish` HTTP callback to a local menu‑bar app.  
- The app receives the stream name, constructs the full RTMP URL, and makes it available for further use.  
- Stream parameters: 1080p60, H.264 video, AAC stereo audio.

## Watching It
- Uses `mpv` to play the local RTMP stream with a low‑latency profile (`--profile=low-latency --audio-buffer=0.3`).  
- Shares the `mpv` window to Discord, achieving sub‑second delay.  
- Stream can also be piped into OBS for re‑streaming or recording.  
- The setup has been stable for several weeks; source code is publicly available.