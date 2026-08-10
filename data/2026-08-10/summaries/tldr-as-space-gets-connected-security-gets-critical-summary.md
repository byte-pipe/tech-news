---
title: As Space Gets Connected, Security Gets Critical
url: https://semiengineering.com/as-space-gets-connected-security-gets-critical/
date: 2026-08-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-10T15:31:30.509974
---

# As Space Gets Connected, Security Gets Critical

# As Space Gets Connected, Security Gets Critical

## Overview
- NASA is extending terrestrial‑style internet to lunar and deep‑space assets, creating high‑value data streams that could be targeted by ransomware groups or hostile nations.  
- The emerging lunar network, LunaNet, will rely on Delay/Disruption Tolerant Networking (DTN) to keep links reliable despite long distances and intermittent connectivity.

## Communication Technologies
- **Radio‑frequency (RF) options**: 4G LTE is the initial choice for lower risk and mature ecosystem; 5G/6G are being evaluated for stronger zero‑trust features and network slicing.  
- **Optical inter‑satellite links (OISLs)**: Laser‑based links are expected to dominate as data rates approach 100 Gbps because they are less vulnerable to eavesdropping and jamming.  
- **Power amplifiers**: Gallium‑nitride (GaN) on silicon, silicon carbide, and gallium arsenide are being used for high‑efficiency, high‑output‑power RF front‑ends; GF’s eight‑inch GaN‑on‑silicon process aims to keep critical components domestically sourced.

## LunaNet Architecture
- Deploys DTN as the core framework to tolerate delays and disruptions between rovers, astronauts, orbiters, and ground stations.  
- Supports multiple HD video streams, extensive telemetry, and scientific data.  
- Bandwidth targets around 20 MHz, with latency dominated by the Moon‑Earth distance rather than network congestion.

## Security Requirements
- **Hardware‑rooted trust**: secure boot, measured boot, and root‑of‑trust mechanisms are mandatory.  
- **Post‑quantum cryptography**: prepares the network for future quantum threats.  
- **Over‑the‑air (OTA) updates**: enable patching of firmware and reconfiguration of rad‑tolerant FPGAs after deployment.  
- **Zero‑trust architecture**: 5G introduces stronger mutual authentication and network slicing to isolate mission‑critical traffic.  
- **Supply‑chain integrity**: domestically manufactured components (e.g., U.S.‑made GaN amplifiers) reduce risk of embedded hardware trojans.

## Threat Landscape
- Attack vectors include denial‑of‑service, ransomware, data exfiltration, and tampering of on‑orbit hardware.  
- Physical inaccessibility of space assets limits traditional maintenance, making proactive security from design onward essential.  
- Both nation‑state actors and cybercriminals have incentives to disrupt or exploit mission‑critical communications.

## Outlook
- Commercial mining, scientific exploration, and intelligence gathering on the Moon and Mars will increase demand for robust, high‑throughput links.  
- As optical links gain market share and 5G/6G technologies mature, the emphasis will shift from raw bandwidth to resilient, end‑to‑end security.  
- Ongoing collaboration between NASA, industry partners (e.g., Nokia, Synopsys, GlobalFoundries, Rambus), and security experts is critical to safeguard the next generation of space networks.