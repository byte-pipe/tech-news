---
title: 👾 Server Access Logs with GoAccess - DEV Community
url: https://dev.to/annavi11arrea1/server-access-logs-with-goaccess-333d
date: 2026-06-21
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-23T10:20:58.451325
---

# 👾 Server Access Logs with GoAccess - DEV Community

# 👽 Jetson Orin Nano Web Server Follow‑up

## Overview
- The author set up a mini web server on a Jetson Orin Nano and explored ways to monitor traffic in real time.  
- GoAccess, an open‑source log analyzer, was chosen for both terminal and HTML dashboard views.

## Terminal view
- GoAccess can parse server logs directly in the terminal, presenting organized statistics.  
- The tool offers multiple display modes; detailed usage is covered in the official GoAccess documentation.

## HTML dashboard
- By configuring an Nginx reverse proxy, the GoAccess HTML report can be served locally.  
- The dashboard is human‑readable, theme‑customizable, and includes various charts and settings.

## Future plans
- The author intends to add an agent that reads the logs and triggers alerts based on predefined parameters.  
- They invite the community to share preferred web‑analytics agents and monitoring tools.