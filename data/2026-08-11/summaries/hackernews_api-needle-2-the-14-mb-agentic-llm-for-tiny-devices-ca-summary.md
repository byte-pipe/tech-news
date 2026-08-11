---
title: Needle 2 - The 14 MB Agentic LLM for Tiny Devices | Cactus
url: https://cactuscompute.com/needle
date: 2026-08-10
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-08-11T11:49:24.284485
---

# Needle 2 - The 14 MB Agentic LLM for Tiny Devices | Cactus

# Cactus NeedleAgentic LLM for Tiny Devices
-----------------------------------------------

## Summary

The article introduces Needle 2, a 14MB model designed specifically for tiny devices such as smart home appliances, robots, and sensors. It can be used to call tools, device controls, and perform structured outputs like extracting sentiment or classification results.

## Key Points

- **Model Size**: 14MB
- **Design Goals**: Bringing on-device AI to budget phones and IoT devices (< $200)
- **Function Call & Device Use**: Mapping sentences onto functions without world knowledge or open-ended prose
- **Extraction & Structured Outputs**: Enforcing a schema through contract, resulting in typed fields and an enum classifier
- **Edge-Cloud Collaboration**: Providing learned confidence scores for off-topic requests and returning empty calls for routine control

## Technical Details

### Models

* Size: 14MB
* Parameters: Over 800K per second with up to 500K tok/s of Pi5
* File size: 28MB
* Session RAM: End-to-end precision with tool retrieval on
* Deployment platforms: CQ2-bit, Apple FM

### Framework

The article mentions that there are few hundred MB of RAM available for most edge devices. A suitable solution is expected to be under $200.
 
## Related Information