---
title: Self-hosting my photos with Immich - Michael Stapelberg
url: https://michael.stapelberg.ch/posts/2025-11-29-self-hosting-photos-with-immich/
date: 2025-11-30
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-07T11:28:24.575303
screenshot: hackernews_api-self-hosting-my-photos-with-immich-michael-stapelb.png
---

# Self-hosting my photos with Immich - Michael Stapelberg

## Self-Hosting My Photos with Immich

### Overview of How I Set Up Immich

I decided to explore self-hosting my photos using Immich, an open-source photo manager. **Key Points:**

*   Run on a virtual machine (VM) or barebone server for independence and backup purposes.
*   Use a different cloud service than Google Photos due to restrictions on OAuth scopes in March 2025.

### Hardware

I am running Immich on my ASRock DeskMini X600 Ryzen 7 Mini PC, which consumes less than 10W of power. I'm storing it on a 64GB RAM and 1TB disk.

### Setting Up Immich

After installing NixOS as my base OS, I configured Immich with the following services:

*   `immich` service:
    *   Enable: Enabled to provide access over the local network.
    *   Use:
        +   `tailscale serve --bg`: Forward traffic from localhost 2283 to a Tailscale VPN server.

### Initial Photos Import

Initially, I attempted to import my photos using Immich's CLI. However, this upload was not reliable and had to be restarted manually after each attempt.

*   Main Points from the article:
    *   Set up NixOS as a physical or virtual machine.
    *   Install NixOS in full declarative manner.
    *   Configure Tailscale VPN for Immich access over local network.
