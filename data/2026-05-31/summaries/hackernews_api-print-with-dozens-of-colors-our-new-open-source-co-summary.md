---
title: Print with dozens of colors: Our new open-source ColorMix for EasyPrint and PrusaSlicer - Original Prusa 3D Printers
url: https://blog.prusa3d.com/our-new-open-source-colormix-model-in-prusaslicer-and-easyprint_136079/
date: 2026-05-27
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-31T06:01:52.510319
---

# Print with dozens of colors: Our new open-source ColorMix for EasyPrint and PrusaSlicer - Original Prusa 3D Printers

# Print with dozens of colors: Our new open-source ColorMix for EasyPrint and PrusaSlicer

## Overview
- The article introduces **PrusaColorMix**, an open‑source color‑mixing model that lets any multi‑material FDM printer produce dozens of color tones using only five filaments (CMYKW).  
- The workflow is integrated into **PrusaSlicer** and **EasyPrint**, offering more accurate color previews and a painting‑like experience.  
- The model is released under the MIT license, encouraging community inspection, improvement, and reuse.

## Community origins
- Early experiments appeared in slicer forks (OrcaSlicer‑FullSpectrum), test palettes, and community projects such as **PeggyPalette**.  
- Tools like **Justin H. Rahb’s filament‑mixer** helped predict mixed colors, demonstrating the power of open‑source collaboration.  
- Prusa’s internal teams recognized the potential and decided to create a streamlined solution.

## Development workflow
- Calibrated a new color‑mixing model against measured FDM prints.  
- Linked the model to real material data via the **OpenPrintTag Material Database**.  
- Integrated the workflow directly into PrusaSlicer and EasyPrint.  
- Prepared a dedicated **Prusament CMYKW filament set** to ensure reliable results from the first print.  
- Chose the CMYKW (Cyan, Magenta, Yellow, Black, White) palette because the Prusa XL can handle a true black filament, enabling richer color combinations.

## How the mixing works
- Uses the same principle as 2‑D halftoning: alternating thin layers of different filament colors to achieve perceived tones.  
- Human visual resolution blends the interleaved layers, creating smooth colors similar to inkjet printing.  
- By varying the proportion of CMY (and black) layers, a wide gamut of colors can be reproduced without needing a separate filament for each hue.

## Teams and contributors
- **Barbora Marsikova (Prusa Academy)** – championed full‑spectrum printing for beginners.  
- **Prusa Polymers** – produced the CMYKW filament bundle and experimented with additional shades (e.g., PLA Natural Glitter).  
- **PrusaSlicer team** – incorporated the model into upcoming PrusaSlicer 3.0 and prepared profiles for the CORE One INDX.  
- **EasyPrint & Printables team** – rapidly implemented CMYKW slicing and released early test builds.  
- **Ondřej Bartas (Printables & EasyPrint)** – main software engineer behind the ColorMix model.

## Developer’s diary & lessons learned
- Goal: make multicolor FDM printing feel like painting, with a palette UI that “gets out of the way.”  
- Existing slicers (Orca, Bambu) require manual configuration for each mixed color; Prusa’s approach automates prediction and UI.  
- The model builds on prior work (OrcaSlicer‑FullSpectrum, filament‑mixer) but adds Prusa‑specific calibration and material data.  
- Tested ~40 useful color combinations using the CMYKW set on the Prusa XL; identified limitations of CMYW‑only systems (lack of true black).  
- Ongoing work includes fine‑tuning filament shades, transparency, and expanding support to other Prusa printers.

## Takeaway
PrusaColorMix turns a multi‑material printer into a versatile, painter‑like tool, enabling dozens of reliable colors from just five filaments. The open‑source model, integrated into PrusaSlicer and EasyPrint, invites the community to adopt, improve, and extend full‑spectrum 3D printing.