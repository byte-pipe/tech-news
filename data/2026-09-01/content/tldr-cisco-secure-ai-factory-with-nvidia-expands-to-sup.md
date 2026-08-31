---
title: Cisco Secure AI Factory with NVIDIA Expands to Supermicro Rack-Scale Systems - ServeTheHome
url: https://www.servethehome.com/cisco-secure-ai-factory-with-nvidia-expands-to-supermicro-rack-scale-systems/
site_name: tldr
content_file: tldr-cisco-secure-ai-factory-with-nvidia-expands-to-sup
fetched_at: '2026-09-01T09:50:45.833012'
original_url: https://www.servethehome.com/cisco-secure-ai-factory-with-nvidia-expands-to-supermicro-rack-scale-systems/
author: Vic A
date: '2026-09-01'
published_date: '2026-08-29T20:40:18+00:00'
description: The Cisco Secure AI Factory with NVIDIA is expanding to include integrated racks from Supermicro to meet larger scale AI cluster needs
tags:
- tldr
---

* AI

Facebook
X
Pinterest
Linkedin
ReddIt
Email
Print
Copy URL

Cisco NVIDIA AI with Supermicro accelerated compute portfolio

Cisco this week announced that its Secure AI Factory with NVIDIA is expanding to rack-scale infrastructure built around Supermicro liquid-cooled and air-cooled systems. NVIDIA Cloud Partner Reference Architecture compliance anchors the design, joined by Cisco Validated Infrastructure Services, Cisco AI networking, and unified operations. Cisco says it will begin offering the Supermicro systems in October through its enterprise sales and channel ecosystem, with Cisco support and lifecycle services wrapped around the hardware.

## Cisco Secure AI Factory with NVIDIA Expands to Supermicro Rack-Scale Systems

Cisco plans to pair its NCP Reference Architecture, networking, validation services, and management software with liquid-cooled and air-cooled Supermicro rack-scale systems.

Cisco NVIDIA AI with Supermicro rack-scale infrastructure expansion

Cisco’s reference design splits the network between two switch families. Frontend fabric runs on Cisco N9300 Series switches with Cisco Silicon One, while the backend fabric uses Cisco N9100 Series switches built around NVIDIA Spectrum-X silicon. Cisco positions that pairing for clusters spanning roughly 1,000 to more than 100,000 GPUs, mapping it onto NVL72 builds for Vera Rubin and Grace Blackwell, HGX NVL8 systems for Rubin and B300, and MGX PCIe GPU platforms.

Cisco NVIDIA AI with Supermicro NCP reference architecture

CVIS is where Cisco takes ownership of the build. A CVIS Toolkit handles repeatable provisioning and automated validation, specialist-led delivery hands over a validated cluster with a performance and compliance report, and dedicated CVIS performance clusters support software testing and tool development.

Cisco NVIDIA AI with Supermicro validated infrastructure services

Cisco splits its validated designs by scale. An Enterprise Reference Architecture targets AI server clusters under roughly 1,000 (1024?) GPUs on Cisco Silicon One N9300 Series switching, while a Cloud Reference Architecture extends from about 1,000 to more than 100,000 GPUs with an N9300 frontend and an N9100 Series backend carrying NVIDIA Spectrum-X silicon.

Cisco NVIDIA AI with Supermicro enterprise and cloud reference architectures

The Supermicro systems are focused on the AI clusters beyond Cisco Unified Edge and Cisco AI POD offerings. Supermicro’s AI clusters are aimed at model training and trillion-parameter workloads rather than edge inferencing or optimization.

Cisco NVIDIA AI with Supermicro portfolio scale

Cisco says it will begin offering the Supermicro systems in October through its enterprise sales and channel partner ecosystem. Cisco support and lifecycle services will be included, along with the company’s Ethernet silicon, optics, security, and observability portfolio. On a call this week, Patrick asked about who would service the physical boxes. It sounds like if a SSD or GPU needs to be replaced in one of the Supermicro servers, it would be Supermicro doing the physical service.

Cisco NVIDIA AI with Supermicro rack-scale systems beginning in October

The planned Supermicro lineup spans a large portion of NVIDIA’s accelerated computing portfolio. Cisco lists Supermicro MGX systems, NVIDIA HGX B300 NVL8 in air-cooled and liquid-cooled builds, NVIDIA HGX Rubin NVL8, and the Vera Rubin NVL72 and GB300 NVL72 rack-scale systems alongside its UCS X-Series modular servers.

Cisco NVIDIA AI with Supermicro accelerated compute portfolio

Networking at rack scale touches every fabric in the cluster. Cisco maps a management fabric to an N9364E-SG2-O switch with Cisco Silicon One, and frontend and backend fabrics to an N9164E-NS4-O with NVIDIA Spectrum-X silicon, and says that the same fabric scales beyond 100,000 GPUs on a model network operations teams already run.

Cisco NVIDIA AI with Supermicro cluster networking

Management converges on Cisco Cloud Control, planned for calendar Q4 2026. That console adds unified login, inventory, and topology, plus server management, infrastructure power and cooling management, and network management tying Intersight and Nexus One under one Day 0-2 operating model.

Cisco NVIDIA AI with Supermicro Cisco Cloud Control operations

For the operator, the pitch is the entire AI cluster in a single view. Cloud Control renders the cluster fabric and topology, the frontend, backend, storage, and management switches, and servers and storage, with an AI Canvas for troubleshooting and continuous visibility.

Cisco NVIDIA AI with Supermicro unified cluster management

We previously looked at the hardware side inour tour of how Supermicro builds NVIDIA B300 AI factory systems. Cisco plans to add its networking, validation, sales, support, lifecycle services, and management layer around those rack-scale systems.

If you do not know about Supermicro’s AI offerings, the video embedded above shows much of what Cisco will be adding when we did our Supermicro rack-scale AI factory tour.

## Final Words

I asked Patrick Kennedy, our Editor-in-Chief, about this since he has worked with both Cisco and Supermicro in the past.Cisco’s UCS linehas been around for some time, so I wanted ot know why Cisco needed Supermicro. His reaction was simple:

“Supermicro has a high-volume AI cluster business, including all integration, testing, and deployment facilities. They also have a much faster development cycle for new servers than Cisco UCS, which is of paramount importance for AI infrastructure where generations advance much more rapidly. I asked Cisco about whether the outside-the-rack components like chillers, in-row CDUs, and so forth, and it sounds like those will be available under a reseller agreement, but they require additional engineering versus just delivering a rack.” – Patrick Kennedy

Cisco is wrapping Supermicro rack-scale AI infrastructure with its own networking, validated designs, sales channels, support, lifecycle services, and unified management. For enterprises that already standardize on Cisco for networking and want a single vendor accountable for AI cluster deployment, this collaboration removes the need to integrate Supermicro systems, Cisco switches, and third-party management tools separately.