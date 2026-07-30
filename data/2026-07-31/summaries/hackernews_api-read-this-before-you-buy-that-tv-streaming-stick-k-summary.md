---
title: Read This Before You Buy That TV Streaming Stick – Krebs on Security
url: https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/
date: 2026-07-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-31T06:02:09.487563
---

# Read This Before You Buy That TV Streaming Stick – Krebs on Security

# Read This Before You Buy That TV Streaming Stick – Krebs on Security Summary  

## Overview  
- Generic TV streaming sticks (e.g., H96) are marketed as cheap, unlimited‑content devices.  
- Security researchers have long warned that these boxes rent the user’s Internet connection to strangers.  
- New research reveals they also spoof mobile‑phone identities to click ads on AI‑generated sites, forming a large ad‑fraud operation.  

## Investigation by Pedro Falé (Bitsight)  
- Falé registered an expired domain previously used by the devices for telemetry.  
- The domain collected full hardware specs and the list of installed apps from tens of thousands of H96 sticks worldwide.  
- Traffic analysis showed most devices reported themselves as various Android phone models (Samsung, Vivo, Huawei, Xiaomi).  

## Core Components of the Fraud Network  
- Two common apps on the devices are from Zhejiang Fengwo IoT Technology Ltd, operating under the Fengwo Group.  
- Fengwo Group holds patents matching the functionality of these apps.  
- The apps coordinate ad‑click fraud by turning H96 sticks into captive traffic sources that visit AI‑generated websites and click ads.  

## AI‑Generated “Digital Human” Sites  
- The group’s domain (fwgcloud.com) advertises over 120,000 “AI digital humans” for rent.  
- Sites host machine‑generated news articles across many categories but display ads only to devices matching the spoofed mobile profiles.  
- The sites are built with Google’s Blockly visual programming language, allowing low‑skill operators to assemble fraud routines by dragging code blocks.  

## Fraud Execution Flow  
- When a device is assigned a fraud task, it receives a specific Blockly module that can:  
  - Launch a browser silently,  
  - Navigate pages, manage tabs, and click ads.  
- Three vision and reasoning systems are fused to let the bot identify and interact with ads as a human would.  

## Dual‑Mode Operation: Proxy vs. Fraud  
- H96 sticks act either as residential proxies or as ad‑fraud bots, never both simultaneously.  
- Detection of an HDMI signal (TV on) triggers proxy mode to avoid interfering with streaming.  
- When the TV is off, the device switches to ad‑fraud mode, which is more resource‑intensive.  

## Industry Response and Risks  
- Despite FBI and industry warnings, major retailers (Amazon, Best Buy, Newegg) continue to sell many off‑brand Android TV boxes.  
- These devices typically ship with pre‑installed residential‑proxy software that rents the user’s IP address to anonymous customers (scrapers, scalpers, cybercriminals).  
- The boxes are insecure by default, lacking authentication, and have been exploited by botnets to enslave millions of units.  

## Financial Impact  
- Bitsight tracked roughly 38,000 devices contacting the Fengwo domain, estimating ad‑fraud revenue near $50,000 per day, not counting proxy earnings.  
- The estimate is conservative, based on telemetry from a single older Fengwo domain.  

## Conclusions  
- Off‑brand TV streaming sticks are a conduit for both residential‑proxy rental and sophisticated ad‑fraud schemes.  
- The use of AI‑generated sites, mobile‑phone spoofing, and low‑skill Blockly‑based tooling makes the operation scalable and hard to detect.  
- Consumers should avoid these devices, and retailers should reconsider selling insecure, unlicensed streaming hardware.