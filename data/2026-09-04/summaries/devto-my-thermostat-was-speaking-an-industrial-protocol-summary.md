---
title: My Thermostat Was Speaking an Industrial Protocol. Just Not to Me. - DEV Community
url: https://dev.to/managerfx/my-thermostat-was-speaking-an-industrial-protocol-just-not-to-me-2a0p
date: 2026-09-03
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-09-04T07:26:37.211419
---

# My Thermostat Was Speaking an Industrial Protocol. Just Not to Me. - DEV Community

# My Thermostat Was Speaking an Industrial Protocol. Just Not to Me.

## Background and motivation
- I am a senior software engineer with little hardware experience, only basic DIY projects on ESP32.
- The appeal of hardware hacking is turning code into physical actions (fans, valves) that solve real problems.
- Without AI assistance I would have stopped at the first RS‑485 module; AI helped me continue.

## The problem
- My living‑room Delta Controls eZNT‑T331 thermostat controls three zones via a central HVAC controller.
- It has no API, cloud, or app, and the only interface is a serial bus used by the system’s controller.
- Replacing it would require costly integration; instead I decided to communicate with it directly.

## Phase 0 – discovery and preparation
- Inventory: the thermostat, its end‑user manual, no technical datasheet or protocol spec.
- Found a hidden installer menu (default password) showing a “MAC address” like “14”, indicating a bus node address.
- Identified the device as the BACnet MS/TP variant (RS‑485 token‑ring network) after researching the model.
- Studied BACnet MS/TP in depth: frame format, CRCs, token passing, Poll‑For‑Master, ReadPropertyMultiple, SubscribeCOV.
- Established a safety rule: *only put a frame on the wire if I can fully explain its purpose*.

### Risks I needed to avoid
1. **Address conflict** – two masters with the same node address break the ring. I listened first and chose a free address (125).
2. **Timing violation** – transmitting out of turn collides with other frames and stalls the bus. My firmware limits to one BACnet operation per tick and avoids blocking calls.
3. **Semantic error** – a correctly formed WriteProperty could misconfigure the HVAC system. I committed to extensive reading before any writing.

## Phase 1 – reconnaissance (AI‑independent work)
- Removed the thermostat, located the RS‑485 differential pair (A and B), and tapped it non‑destructively.
- Connected a Waveshare Industrial USB‑to‑RS485 converter (FT232RL with proper protection) to my laptop for reliable monitoring.
- Began passive listening to capture traffic, confirming bus activity and node addresses before injecting any frames.