---
title: FediMeteo: How a Tiny €4 FreeBSD VPS Became a Global Weather Service for Thousands - IT Notes
url: https://it-notes.dragas.net/2025/02/26/fedimeteo-how-a-tiny-freebsd-vps-became-a-global-weather-service-for-thousands/
date: 2025-12-31
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-31T11:22:58.108000
screenshot: hackernews-fedimeteo-how-a-tiny-4-freebsd-vps-became-a-global.png
---

# FediMeteo: How a Tiny €4 FreeBSD VPS Became a Global Weather Service for Thousands - IT Notes

## Key Points
- Personal introduction to the idea of using FediMeteo for weather forecasting and its connection to the author's grandfather who followed weather patterns.
- Start of designing and planning the project, involving a test VPS in Italy for scalability.

## Design Principles
* Use a small VM to minimize costs: 4€ per month on German provider Milano
* Separate countries into instances for management, security, and flexibility
* Choose free and open-source weather data sources (wttr.in and Open-Meteo) for reliability
* Prioritize accessibility with local language forecasts through text browsers or emojis
- Follow Unix philosophy: use small, self-contained pieces of code
* Utilize minimalistic software (snac): easy to use, efficient, and low resource consumption

## Benefits
- Ability to provide accurate weather forecasts for the user in their preferred language
- Environmentally friendly approach due to the use of a shared VPS and local data sources
- Community-driven project with a developer who is supportive and knowledgeable
