---
title: Elevators
url: https://john.fun/elevators
date: 2026-07-31
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-01T03:09:44.687514
---

# Elevators

# Elevators

## Overview
- Elevators feel simple but rely on sophisticated algorithms to handle requests and minimize wait times.  
- Common frustration: pressing the call button and waiting for the car to arrive.

## Single‑Car Algorithms
- **SCAN** (patented 1961): elevator travels from the lobby to the top floor, then reverses, stopping for passengers along the way.  
- **LOOK**: similar to SCAN but reverses at the highest requested floor instead of the top floor; this is the behavior most users expect.

## Multiple‑Car Coordination
- A central scheduler assigns each new request to the closest elevator.  
- More advanced strategies improve on the basic nearest‑car assignment.

## Measuring Performance
- Main metric: passenger wait time.  
- Simple thresholds: proportion of rides arriving within 30 seconds or within 90 seconds.  
- Detailed analysis uses the distribution of wait times (histogram) to report p50 (median) and p90 values; users tend to notice the longer p90 waits more than the average.

## Traffic Patterns
- **Morning:** mostly lobby‑to‑upper‑floor trips; worst wait statistics.  
- **Lunch:** mixed inbound and outbound traffic.  
- **Evening:** primarily upper‑floor‑to‑lobby trips.  
- **Inter‑floor:** traffic between floors, generally lighter.

## Smarter Algorithm – RSR (Relative System Response)
- Scores each car based on:
  - ETA to pickup  
  - On‑board load penalty  
  - Same‑direction anti‑bunching penalty  
  - Direction‑match bonus  
  - Idle‑nearby bonus  
  - Low‑load bonus  
- Re‑optimizes every 5 seconds, allowing passengers to be reassigned to a better car if conditions change.

## LOOK vs RSR
- RSR usually reduces wait times at moderate flow rates.  
- At very high flow rates or in small banks, LOOK can outperform RSR because elevators are full and extra logic adds little benefit.  
- Journey time (time spent inside the elevator) differs between the two algorithms but is not covered in depth.

## Destination Dispatch
- Passengers select their destination on a floor kiosk before an elevator arrives.  
- Provides the optimizer with full destination information.  
- Generally results in longer wait times than traditional up/down buttons because it restricts flexibility; only advantageous in very tall buildings with many cars per bank.

## Simulation Tool
- Interactive simulation lets users adjust:
  - Traffic pattern (morning, lunch, evening, inter‑floor)  
  - Number of floors and cars  
  - Flow rate  
  - Algorithm choice (LOOK, RSR, Destination Dispatch)  
- Users can view wait‑time histograms for each configuration.

## Conclusion
- Elevator control involves many trade‑offs and a variety of algorithms.  
- Simple button‑press systems remain effective for most buildings.  
- Advanced methods like RSR can improve performance, but under certain conditions simpler approaches may be superior.