---
title: Surely you have ultra-wideband radios on your bins too? | Simon Green
url: https://sjg.io/writing/binrange-have-you-actually-put-the-bins-out/
date: 2026-10-03
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-05T12:21:07.585599
---

# Surely you have ultra-wideband radios on your bins too? | Simon Green

# Surely you have ultra‑wideband radios on your bins too? | Simon Green

## Six bins, several schedules
- The household has six different bins (general waste, food compost, garden waste, two recycling, glass) each on its own collection schedule.  
- Home Assistant’s Waste Collection Schedule integration scrapes council data and shows which bins are due.  
- The author needed a way to verify whether the bins had actually been put out, not just rely on reminders.  

## Two boards and a walk outside
- Initial test used two Makerfabs ESP32‑WROVER/DW3000 boards powered via USB to measure distance with UWB.  
- Antenna orientation was critical: upright boards gave a 100 % success rate at ~10 m versus 37 % flat.  
- Calibration showed accuracy within 2 cm over 10 m; typical outdoor readings were reliable to ~30 m, with occasional gaps up to 37 m.  
- Data were published via MQTT; Home Assistant created separate entities for each tag.  

## Something small enough to put on a bin
- A compact, battery‑powered tag was required for each bin rather than a full development board.  
- Chosen tags: KKM K4W units (nRF52833 MCU, DW3110 UWB radio, LIS3DH accelerometer) using removable CR2477 coin cells.  
- Tags could be re‑flashed with custom firmware; the supplier provided a programming jig.  
- Cost of the prototype hardware (boards, tags, jig) was roughly US $450, noted as a one‑off experimental expense.  

## Updating six bins without taking them apart
- Firmware updates are delivered wirelessly, allowing the tags to be refreshed without removing them from the bins.  

## The box took several goes
- The enclosure for the anchor board required multiple design iterations to achieve a weather‑proof, aesthetically pleasing case.  

## Reminders and Notifications
- Home Assistant combines the UWB “out” detection with the collection schedule to send precise notifications when a bin has actually been placed out.  

## First test in prod
- After integration, the system correctly reported bin status in real‑world use, confirming the feasibility of the UWB approach.  

## Waiting for more bin days
- The author plans to refine the system, explore additional anchor points for directional data, and possibly expand the solution to other households.