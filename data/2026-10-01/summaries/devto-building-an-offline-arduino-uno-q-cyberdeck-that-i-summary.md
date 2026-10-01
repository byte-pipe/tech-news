---
title: Building an Offline Arduino UNO Q Cyberdeck That Identifies Birdsong and Draws Vintage Field Notes - DEV Community
url: https://dev.to/cloudinary/building-an-offline-arduino-uno-q-cyberdeck-that-identifies-birdsong-and-draws-vintage-field-notes-1cjg
date: 2026-09-30
site: devto
model: llama3.2:1b
summarized_at: 2026-10-01T17:20:15.947978
---

# Building an Offline Arduino UNO Q Cyberdeck That Identifies Birdsong and Draws Vintage Field Notes - DEV Community

## Overview of the DIY Cyberdeck Project

This DIY cyberdeck project is built on the Arduino UNO Q, a popular offline Raspberry Pi alternative, to help naturalists capture field notes, identify birdsong using Edge Impulse, and generate vintage field sketches with Cloudinary's image generation API.

## Hardware Components

* Arduino UNO Q (4 GB)
* 5" HDMI screen and USB 5-in-1 hub
* USB camera
* USB microphone
* Power bank and USB-Micro-USB cable

## Key Components

* Cloudinary's image generation API for generating style-matched images with reference images
* Gemma LLM (Large Language Model) for natural language processing and AI note generation
* Edge Impulse birdsong model for identifying birdsong
* Netlify Function for sync and hosting the cyberdeck

## Architecture

The project is designed to run locally and sync with a community site only when you choose. The architecture includes:

* Mic > Edge Impulse birdsong model
* Camera > photo > Cloudinary image generation
* Keyboard/mouse > sketch + notes > SQLite database
* Gemma LLM > AI note > Octokit: open PR on GitHub (optional)
* Arduino UNO Q (App Lab, Chromium kiosk) > Astro rebuild > live site

## Software Requirements

* Arduino IDE (for wiring and coding)
* Apple App Lab (for development and debugging)
* Cloudinary's image generation API
* Netlify Function
* Gemma LLM (Large Language Model)
* Edge Impulse birdsong model
* SQLite database

## Requirements

* Local AI on device (with local support and security considerations)
* Data governance, security, and privacy (with a focus on community involvement and non-profit initiatives)