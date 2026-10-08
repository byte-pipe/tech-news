---
title: BIGWORDS.PAGE: Turn any screen into a sign
url: https://bigwords.page/
date: 2026-10-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-08T12:51:45.141413
---

# BIGWORDS.PAGE: Turn any screen into a sign

# BIGWORDS.PAGE – Turn any screen into a sign

## Overview
- Creates full‑screen signs, timers, or messages from a single URL.
- No account, app, or server storage required; the URL fragment contains the entire display.
- Works on any device with a web browser, from phones to large displays.

## Creating a link manually
1. Write the message after the `#` in the URL.  
   Example: `https://bigwords.page/#Hello World`
2. Add visual settings with `&key=value` parameters.  
   Example: `...#Hello World&bg=000000&fg=ffd60a&font=4`
3. Use `%0A` for line breaks and `%23` to encode a heading (`#`).  
   Example: `...#%23 Room 204%0AMeeting in progress`
4. Separate slides with `||`; set slide interval with `&interval=`.  
   Example: `...#Coffee ☕||Tea 🍵||Water 💧&interval=2`

## Example use cases
- **Arrivals sign** – welcoming message with pulse animation.  
- **Quiz timer** – countdown with custom zero‑time text.  
- **Café Wi‑Fi** – display network name, password, QR code, and optional image.  
- **New Year countdown** – live countdown to a specific date.  
- **On‑air indicator** – simple “ON AIR” with pulse effect.  
- **Gate or room sign** – heading and sub‑text for boarding information.  
- **News ticker** – scrolling text with customizable speed and colors.  
- **Birthday greeting** – animated rainbow text.  
- **Quiet/recording notice**, **exam room timer**, **daily agenda**, **menu QR code**, and many more.

## Core features
- **Auto‑fit**: text automatically scales to fill the screen size.  
- **Device agnostic**: runs in any modern browser on phones, tablets, laptops, or smart TVs.  
- **Markdown support**: bold, italic, headings, and line breaks are rendered.  
- **Slides**: multiple messages separated by `||` rotate on a timer.  
- **Countdowns**: insert `{countdown}` and define an end date with `&until=` or a duration with `&timer=`.  
- **QR codes & images**: generate Wi‑Fi, call, text, email links, or embed base64 images directly in the URL.  
- **Privacy by design**: the message lives in the URL fragment, which browsers never send to a server.