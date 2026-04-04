---
title: Build your own Dial-up ISP with a Raspberry Pi - Jeff Geerling
url: https://www.jeffgeerling.com/blog/2026/build-your-own-dial-up-isp-with-a-raspberry-pi/
date: 2026-04-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-05T01:02:14.321337
---

# Build your own Dial-up ISP with a Raspberry Pi - Jeff Geerling

# Build your own Dial‑up ISP with a Raspberry Pi

## Introduction
- I wanted to recreate a late‑1990s dial‑up ISP using the original AirPort‑equipped iBook G3 and modern hardware.  
- The goal was to combine 56 Kbps dial‑up speeds with 802.11b Wi‑Fi, emulating how most users accessed the Internet in 1999.

## Hardware
- **Single‑board computer** – Raspberry Pi (any model, $40).  
- **Phone line simulator** – Viking DLE‑200B Two‑Way Line Simulator ($120) to emulate the Plain Old Telephone System.  
- **56 K USB modem** – StarTech.com model ($45).  
- Additional phone cords to connect the modem to the simulator and the simulator to a client computer (the iBook G3).  
- Optional: bell‑style telephone for audible ring debugging; dip‑switch #3 set to “UP” to lower audio volume and improve modem speed.

## Software
- **mgetty** – Handles incoming modem calls, negotiates with remote modems, and hands the connection to PPP.  
- **PPP (pppd)** – Authenticates the remote user and creates a network bridge so the client appears on the local network.  
- Configuration is automated via an Ansible playbook in my `pi‑isp` GitHub repository.  
- Reference resources: Doge Microsystems’ Dial‑up Server Wiki and Webmin’s PPP Dial‑in Server documentation.  
- Logs can be monitored with `journalctl -fu mgetty`; manual modem interaction possible with `minicom -D /dev/ttyACM0`.

## Connection Performance
- Typical stable speed: **33.6 kbps** (≈2.8 KB/s).  
- Occasionally limited to 28.8 kbps or lower; higher speeds require digital line equipment, which the simulator does not provide.  
- Speed adjustments made via the `AT+MS` command in the `init‑chat` script of the Ansible playbook.

## Proxy for Modern Web Content
- Modern sites are unusable on 1999 browsers due to TLS and heavy HTML/CSS/JS.  
- I run **Macproxy Classic** on the Pi to strip modern web assets, delivering a simplified page that old browsers (IE 5, Netscape) can render.  
- After enabling proxy in IE 5, the iBook can browse my own site and other simplified pages over the dial‑up link.

## Dial‑up over Wi‑Fi
- Refurbished the iBook’s original battery (18650 cells) to restore >6 hours of runtime, avoiding the heavy power adapter.  
- Connected the iBook wirelessly to the original AirPort Base Station (802.11b, 11 Mbps max) while the Pi provided the dial‑up service.  
- Noted stability issues with the vintage AirPort after prolonged use, likely due to thermal design constraints.

## Takeaways
- A Raspberry Pi plus a modest phone‑line simulator can faithfully recreate a local dial‑up ISP.  
- The setup demonstrates the contrast between 1990s network speeds and today’s high‑speed Wi‑Fi, while preserving the nostalgic experience of connecting via a 56 K modem.  
- Adding a lightweight proxy makes the modern Internet accessible to legacy hardware, completing the retro‑computing loop.