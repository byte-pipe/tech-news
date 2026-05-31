---
title: AV2 Specification
url: https://av2.aomedia.org
date: 2026-05-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:18:28.368042
---

# AV2 Specification

# AV2 Specification Summary

## Overview
- AV2 is the next‑generation video coding specification from the Alliance for Open Media, building on AV1.
- Designed for superior compression efficiency, enabling high‑quality video at lower bitrates for streaming, broadcasting, and real‑time conferencing.
- Enhancements include support for AR/VR, split‑screen delivery, better screen‑content handling, and a wider visual quality range.
- The AOMedia Video Model (AVM) serves as the official reference software.
- Feedback can be sent to wg‑codec‑chair@aomedia.org or filed on the AVM issue tracker.

## Available Versions
- **v1.0.0 (Current release, 28 May 2026)**
  - AV2 Bitstream & Decoding Process Specification with matching AVM reference software.
  - Accessible online and downloadable as PDF.
  - Includes Additional Tables and a Syntax Browser.
- **v13 Working Draft (Superseded, 5 January 2026)**
  - Earlier development draft retained for reference; “v13” denotes a milestone, not a newer version.

## Using the Specification
- **Full Specification**: Complete document covering scope, definitions, format, syntax, semantics, and decoding process.
- **PDF Version**: Self‑contained PDF of the full v1.0.0 specification for offline use.
- **Additional Tables**: Extracted lookup tables from Section 9 provided as C header files for implementation reference.
- **Syntax Browser**: Split‑pane view of Sections 5 (Syntax Structures) and 6 (Semantics) with side‑by‑side definitions, clickable elements, search, and copy‑to‑clipboard features.
- **Reference Software**: AVM reference implementation corresponding to the v1.0.0 tag.