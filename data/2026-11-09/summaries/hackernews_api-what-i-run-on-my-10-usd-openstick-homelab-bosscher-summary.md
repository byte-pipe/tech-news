---
title: What I run on my $10 USD OpenStick homelab | Bosscher
url: https://blog.bosscher.ch/posts/openstick/
date: 2026-11-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-09T16:00:58.441951
---

# What I run on my $10 USD OpenStick homelab | Bosscher

# What I run on my $10 USD OpenStick homelab

## Hardware overview
- 512 MB RAM (≈450 MB usable)  
- Quad‑core ARM Cortex‑A53 @ 1 GHz  
- 4 GB eMMC flash storage  
- 150 Mbit/s Wi‑Fi, 4G modem with GPS  
- Passively cooled → completely silent  
- One programmable LED  

## Operating system & container runtime
- Runs Debian, providing systemd for service management.  
- Uses Podman for lightweight containerization, keeping the footprint small.

## Services I host (memory usage shown as approximate RSS)

- **CastSponsorSkip** – 5–10 MB  
  Skips sponsorships and ads on any Google Cast device; runs unobtrusively in the background.

- **AdGuard Home (my fork)** – 40 MB  
  DNS‑level blocker for spyware, malware, and tracking domains; handles large blocklists efficiently.

- **Zeroclaw** – 64 MB (≈3 MB idle)  
  AI‑agent hub supporting 30+ channels (Telegram, email, WhatsApp, etc.); provides remote monitoring of the OpenStick via Telegram.

- **Cloudflare Tunnel (cloudflared)** – 8–20 MB  
  Exposes local services to the internet securely without opening ports.

- **Beszel** – 20 MB (10 MB agent + 10 MB server)  
  Visual dashboard for CPU, memory, and other metrics with built‑in alerting to Telegram.

- **Dozzle** – (size not listed, overlaps with Beszel)  
  Web UI for viewing Podman container logs; more focused on log inspection than metrics.

- **Gatus** – 10 MB  
  Monitors the health of services (websites, databases, etc.) and provides a clean status page.

- **Fusion RSS** – 22 MB  
  Self‑hosted RSS reader, a free alternative to paid services like Feedly.

- **Shiori** – 10–20 MB  
  Bookmark manager that archives pages automatically; occasional spikes when archiving.

- **Diun** – 9 MB  
  Sends Telegram notifications when a container image has an available update.

## Why it works for a $10 homelab
- Minimal power draw and zero noise thanks to passive cooling.  
- Debian + Podman give a stable, low‑overhead platform.  
- Each service fits comfortably within the limited RAM and storage, allowing a full self‑hosted stack on a tiny, inexpensive device.