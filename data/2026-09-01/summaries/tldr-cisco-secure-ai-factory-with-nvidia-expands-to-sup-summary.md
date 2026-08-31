---
title: Cisco Secure AI Factory with NVIDIA Expands to Supermicro Rack-Scale Systems - ServeTheHome
url: https://www.servethehome.com/cisco-secure-ai-factory-with-nvidia-expands-to-supermicro-rack-scale-systems/
date: 2026-09-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-01T09:51:18.455439
---

# Cisco Secure AI Factory with NVIDIA Expands to Supermicro Rack-Scale Systems - ServeTheHome

# Cisco Secure AI Factory with NVIDIA Expands to Supermicro Rack‑Scale Systems – Summary

## Overview
- Cisco announced that its Secure AI Factory, built on NVIDIA technology, will now include rack‑scale systems from Supermicro (both liquid‑cooled and air‑cooled).  
- The offering follows NVIDIA Cloud Partner Reference Architecture (CPRA) compliance and adds Cisco‑validated infrastructure services, AI‑optimized networking, and unified operations.  
- Availability starts in October through Cisco’s enterprise sales and channel partners, with Cisco‑provided support and lifecycle services.

## Reference Architecture & Networking
- **Frontend fabric:** Cisco N9300 Series switches with Cisco Silicon One.  
- **Backend fabric:** Cisco N9100 Series switches using NVIDIA Spectrum‑X silicon.  
- Design supports clusters ranging from ~1,000 to >100,000 GPUs.  
- Specific GPU builds mapped to:
  - NVL72 for Vera Rubin and Grace Blackwell,
  - HGX NVL8 for Rubin and B300,
  - MGX PCIe GPU platforms.

## Validation and Service (CVIS)
- Cisco’s CVIS Toolkit automates provisioning and validation.  
- Specialist‑led delivery provides a validated cluster plus performance and compliance reports.  
- Dedicated CVIS performance clusters support software testing and tool development.  
- Two validated design tracks:
  - **Enterprise Reference Architecture:** <~1,000 GPUs, Cisco Silicon One N9300 switching.  
  - **Cloud Reference Architecture:** 1,000–100,000+ GPUs, N9300 frontend + N9100 backend with Spectrum‑X.

## Supermicro Hardware Portfolio
- Covers major NVIDIA accelerated‑compute platforms:
  - Supermicro MGX systems,
  - NVIDIA HGX B300 NVL8 (air‑cooled & liquid‑cooled),
  - NVIDIA HGX Rubin NVL8,
  - Vera Rubin NVL72 and GB300 NVL72 rack‑scale systems,
  - Cisco UCS X‑Series modular servers.  
- Focus is on model‑training and trillion‑parameter workloads, not edge inference.

## Management & Operations (Cisco Cloud Control)
- Planned release: Q4 2026.  
- Provides unified login, inventory, topology, server, power, cooling, and network management.  
- Integrates Cisco Intersight and Nexus One under a Day 0‑2 operating model.  
- “AI Canvas” offers a single‑pane view for troubleshooting and continuous visibility.

## Service Model
- Cisco will handle support, lifecycle services, Ethernet silicon, optics, security, and observability.  
- Physical hardware repairs (e.g., SSD or GPU replacement) remain the responsibility of Supermicro under a reseller agreement.

## Expert Commentary
- Patrick Kennedy (Editor‑in‑Chief) notes:
  - Supermicro’s high‑volume AI cluster business includes integration, testing, and rapid server development—critical for fast‑evolving AI workloads.  
  - External components such as chillers and in‑row CDUs will be sourced via reseller agreements and require additional engineering.

## Conclusion
- Cisco is bundling Supermicro rack‑scale AI hardware with its own networking, validated designs, sales channels, support, lifecycle services, and unified management.  
- For enterprises already standardized on Cisco networking, this partnership offers a single‑vendor solution for AI cluster deployment, eliminating the need to integrate disparate hardware and management tools.