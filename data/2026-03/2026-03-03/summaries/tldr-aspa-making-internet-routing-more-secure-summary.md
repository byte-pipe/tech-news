---
title: ASPA: making Internet routing more secure
url: https://blog.cloudflare.com/aspa-secure-internet/
date: 2026-03-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-03T06:01:46.435695
---

# ASPA: making Internet routing more secure

# ASPA: making Internet routing more secure

## Overview
- BGP route leaks occur when traffic traverses networks that were not intended to carry it, compromising reliability.
- Existing RPKI/ROA mechanisms verify only the destination (origin) of a route.
- ASPA (Autonomous System Provider Authorization) extends this by cryptographically validating the entire AS_PATH, ensuring traffic follows an authorized route.

## How ASPA Works
- Networks publish ASPA records in the RPKI system, listing the AS numbers of their authorized upstream providers.
- Validation examines the AS_PATH in two directions:
  - **Up‑Ramp** – starting at the origin, each hop must be an authorized provider of the previous hop.
  - **Down‑Ramp** – starting at the destination, each preceding hop must be an authorized customer of the next hop.
- If the up‑ramp and down‑ramp meet (forming a “mountain” shape), the path is considered valid; a gap creates a “valley” indicating a route leak.

## Route Leak Detection Example
- Scenario: AS65538 (customer) receives a route from provider AS65537 and attempts to forward it to another provider AS65538, forming a classic leak.
- Validation steps:
  1. Up‑Ramp check passes up to AS65537.
  2. Down‑Ramp check from the destination ends at AS65538.
  3. The two ramps do not intersect, so ASPA flags the path as invalid.

## Defense Against Forged‑Origin Hijacks
- ASPA can reject paths where an attacker advertises a legitimate origin but uses an unauthorized provider, because the hijacker’s AS is not listed in the victim’s ASPA record.
- Limitation: ASPA does not protect against attacks where a provider fabricates a peering link with a customer (provider‑to‑customer forgery), as ASPA only records provider relationships, not peering agreements.

## Deployment Monitoring
- Cloudflare Radar includes an ASPA deployment monitoring feature:
  - Shows adoption trends over time across the five Regional Internet Registries (RIRs).
  - Allows inspection of ASPA records and changes at the individual Autonomous System level.

## Creating ASPA Objects
- Registries such as RIPE and ARIN provide a simple web interface to create ASPA objects.
- Required information:
  - Your Autonomous System (AS) number.
  - The AS numbers of the upstream providers you purchase transit from (the authorized providers).
