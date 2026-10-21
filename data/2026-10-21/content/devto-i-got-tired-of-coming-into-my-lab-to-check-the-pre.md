---
title: I Got Tired of Coming into my Lab to Check the Pressure of my Cryocooler so I Built a Tool to do it for Me - DEV Community
url: https://dev.to/pahorton/i-got-tired-of-coming-into-my-lab-to-check-the-pressure-of-my-cryocooler-so-i-built-a-tool-to-do-it-4ob7
site_name: devto
content_file: devto-i-got-tired-of-coming-into-my-lab-to-check-the-pre
fetched_at: '2026-10-21T22:06:21.426037'
original_url: https://dev.to/pahorton/i-got-tired-of-coming-into-my-lab-to-check-the-pressure-of-my-cryocooler-so-i-built-a-tool-to-do-it-4ob7
author: Paul Horton
date: '2026-10-21'
description: 'This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady ... Tagged with devchallenge, hf26challenge, tigerdata, githubcopilot.'
tags: '#devchallenge, #hf26challenge, #tigerdata, #githubcopilot'
---

Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady Submission 🦥

This is a submission for theHacktoberfest Open-Source AI Challenge Week 3: Slow and Steady

## The Backstory

Hi! I'm Paul and I work as a postdoc in an astrophysics lab as a systems engineer. One of the regular texts I get from my PI is "can you check the pressure on the cryocooler." Our cryocooler, nicknamed Mountain Dewar, is essentially a big cylinder where we test sensitive detectors for space exploration. Our lab moved recently so we're testing Mountain Dewar in a new space after being in retirement for years.

As part of the testing, we got a great deal on a vacuum pump and a bunch of used vacuum parts off eBay that we're trying ensure hold a seal. This means we pump down the cryocooler, taking out all of the air, and then monitor the pressure over time.

Our way of doing this is a multimeter connected to a pressure sensor, where values from 0 to 10V are converted into Torr based on a table in the manual. Because it's just a multimeter, we don't have live pressure data and have to run our tests on a Friday and then check back on Monday to check if it worked.

Myself and a grad student decided to test the capabilities of the lab by building a Voltmeter PCB with a spare Raspberry Pi we had in the lab. He designed a board with a two channel ADC with a voltage differential that we were able to connect to the Pi to give us values from 0 to 12V. We realized that monitoring the pressure wasn't the only thing we had to do in the lab so we made it versatile enough to monitor whatever we wanted.

Once we had a board built and the capabilities of reading voltages, I knew there was more I could do to truly make my life easier.

## What I Built

Starting with a clean OS on a Raspberry Pi 4B and our new PCB, I began working on the software. Initially this was a task I planned on giving to a prospective new undergrad in our lab but after they were unable to join the group, I decided to see what GitHub Copilot was able to accomplish for a hardware project. I found anAdafruit OLED bonnetthat fit nicely on top of the PCB and gave us the ability to get a quick visual for the channels without needing to pull up a monitor.

I was absolutely shocked at how quickly Copilot was able to take my test code for reading the ADCs to creating a working UI on the OLED. I began asking it to add a settings menu with the little joystick and buttons and it was able to do it almost flawlessly. At this point, my PI's request to have a gauge on top of the Cryocooler was done but I realized I could go so much further

### Making it Live

My test on if this could be accomplished was done but I realized I could go further. TigerData was a tool I was curious about because most of my work revolves around time series data. Given I had a sensor spitting out constant voltages, TimescaleDB, was the obvious choice. TimescaleDB has the ability to natively give me summarization of data so I can more easily query it.

From there, I connected the Pi to the internet and have it stream data from the device to the TigerData Cloud. Given it's a relatively small stream, the free tier is perfect for my use case. I then had Copilot build out a simple web interface for the device. Finally, I hosted it all on Vercel.

Once I got it all up and running, I decided to have some fun with it. Check out some of these easter egg themes

* /neoNeo Brutalist with colors matching Mountain Dewar
* /neonNeon Brutalist
* /ngeCyber Militaristic in the style of Neon Genesis Evangelleon
* /98Windows 98 (definitely still needs some work)

## Demo with Dummy Data

pi-voltmeter-demo.vercel.app

## Code

## PaHorton/pi_voltmeter

# Pi voltmeter

CM4 + ADS1115 (2 channels, single-ended A0/A1) + Adafruit 128x64 OLED bonnet.

## Features

* Live value of both channels, converted by a selectable formula.
* Formula files:<name>.txt, line 1 = unit, line 2 = expression inV(e.g.degC/V * 100). Functions: sqrt, log, ln, log10, log2, exp, abs, sin, cos
tan, asin, acos, atan, pow, min, max, round; constants pi, e. Invalid files are skipped.
* On-screen menu:Aor joystick press opens it, up/down selects, left/right changes a
value,Bgoes back. Items: formula per channel, N (seconds between timestamped records in the CSV / future DB), ADC range
display refresh period, USB logging. Settings persist insettings.json.
* Plug in a USB stick: validformulas/*.txton it are copied to the Pi. WithUSB log: ON, readings are written tovoltmeter_logs/log_<time>.csvon the stick
(new file per insertion; header + one row…

View on GitHub

## How I Built It

This was built with Copilot using a Python application running on a Raspberry Pi to pull data from an ADC, provide a live display on an OLED, and stream data to a TimescaleDB table on TigerData Cloud.

The front end is Flask, FastAPI, and Tailwind CSS for theming. For rendering live data I'm using Chart.js and pulling data from TigerData with the help of theirtime_bucketandmake_intervalsystems.

## Why Does Open Innovation Matter?

We wanted to make this system open source as other labs can very easily have use cases for this. Our PCB is available by request and all of the code is located on GitHub so anyone can easily deploy this for their own lab.

## The Lazy Payoff

The day after we got it up and running, my PI asked me to turn off the vacuum pump and give him updates on if it's holding pressure. I was able to just share the website with him and he could monitor it himself without me having to go check it every few hours, instantly giving me the freedom to stay at my desk as we watch the pressure increase.

## Prize Categories

### Best Use of TigerData

A Raspberry Pi continuously reads two channels from an ADS1115 converter on our cryocooler, logging its pressure and temperature. This is append-only, timestamped sensor data that is almost always queried by a time window, which is exactly what TigerData is built for. My project uses:

* Hypertables: the readings table is partitioned by time. The Pi writes to it directly and buffers readings in memory if the network drops.
* time_bucket(): graphs from 1 minute to 24 hours are averaged down to about 300 points, so every zoom level stays fast and readable.
* last(): the live gauges fetch the newest value for each channel in a single query.
* Continuous aggregates: a one-minute rollup serves graphs of 6 hours or longer, and it matches the raw data to within 0.012 V.
* Compression and retention policies: data is compressed after one day and dropped after 90 days.

I store raw voltage and apply the conversion formulas downstream, so correcting a formula never corrupts historical data. The dashboard connects through a read-only role, and a demo mode with simulated data lets me share the site without exposing live readings.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse