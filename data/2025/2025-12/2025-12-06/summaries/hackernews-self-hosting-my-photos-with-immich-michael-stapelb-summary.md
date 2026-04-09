---
title: Self-hosting my photos with Immich - Michael Stapelberg
url: https://michael.stapelberg.ch/posts/2025-11-29-self-hosting-photos-with-immich/
date: 2025-12-06
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-06T11:18:05.562815
screenshot: hackernews-self-hosting-my-photos-with-immich-michael-stapelb.png
---

# Self-hosting my photos with Immich - Michael Stapelberg

## Self-Hosting my Photos with Immich

### Introduction
This article describes how I set up immich, a self-hostable photo manager, on my RYzen 7 Mini PC (ASRock DeskMini X600) for local backup purposes and independence, replacing the cloud service NixCon.

### Hardware

*   I am running immich on my:
    *   Ryzen 7 Mini-PC (ASRock DeskMini X600)
        *   Consumes less than 10 W of power in idle
        *   Has plenty of resources for VMs (64 GB RAM, 1 TB disk)

### Installing immich

*   I created a VM named 'photos' with 500 GB of disk space, 4 CPU cores and 4 GB of RAM.
    *   After initial import, assign more CPU and RAM, but minimal requirements are sufficient for normal usage.

### Setting up Immich on Physical Hardware or Virtual Machines Over the Network

*   I created a VM named "photos" with one of my network storage PCs build, which uses NixOS as its base distribution.
*   For an alternative option to NixOS over the network, instead enable Immich to connect via Tailscale VPN.
*   Because Tailscale uses MagicDNS and TLS certificate provisioning, I can access my photos through https://photos.example.tsnet.

### Initial Photos Import

In the beginning, Immich was not able to import my photos reliably using the official CLI. This was due to a dependency issue with the upload process that required manual restart of the server.

Note: The details mentioned in these steps are written as per the provided code snippet and might need minor adjustments based on real-world applications or configurations.
