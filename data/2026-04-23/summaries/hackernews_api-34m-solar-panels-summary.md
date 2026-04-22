---
title: 3.4M Solar Panels
url: https://tech.marksblogg.com/american-solar-farms-v2.html
date: 2026-04-22
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:46:05.228941
---

# 3.4M Solar Panels

# 3.4M Solar Panels Summary

## Dataset Overview
- Version 2 of the Ground‑Mounted Solar Energy in the United States (GM‑SEUS) dataset was released, expanding from 2.9 M to over 3.4 M panels.  
- The new release also adds a rooftop array dataset.  

## Workstation
- CPU: AMD Ryzen 9 9950X, 5.7 GHz, 16 cores / 32 threads, L1 1.2 MB, L2 16 MB, L3 64 MB.  
- Cooling: liquid cooler in a Cooler Master HAF 700 case.  
- Memory: 96 GB DDR5 @ 4,800 MT/s.  
- Storage: Crucial T700 4 TB NVMe M.2 SSD (read up to 12,400 MB/s) with heatsink.  
- Power: 1,200 W fully modular Corsair PSU.  
- Motherboard: ASRock X870E Nova 90.  
- OS: Ubuntu 24 LTS running under Microsoft’s Ubuntu for Windows on Windows 11 Pro (GPU driver constraints).  

## Software Prerequisites
- GDAL 3.9.3 installed from the `ubuntugis-unstable` PPA.  
- DuckDB v1.5.1 (CLI) with extensions: h3, lindel, json, parquet, spatial.  
- DuckDB configured to load all extensions at startup via `~/.duckdbrc`.  
- QGIS 4.0.1 used for map rendering, with the HCMGIS plugin for Esri basemaps.  

## Data Preparation
- Downloaded the 3.4 GB ZIP from Zenodo and extracted all GeoPackage (`*.gpkg`) files.  
- Dataset projection: Albers Equal Area (EPSG: ... parameters shown in the article).  

## Rooftop Arrays Conversion
- Converted `GMSEUS_RooftopArrays_2025_v2_0.gpkg` to Parquet using DuckDB v1.4.4 (v1.5.1 raised exceptions).  
- Applied field cleaning (e.g., converting `-9999.0` to NULL) and geometry transformation to EPSG:4326.  
- Added a bounding‑box JSON column (`bbox`).  
- Ordered rows by Hilbert curve for spatial locality.  
- Output file: `GMSEUS_RooftopArrays_2025_v2_0.parquet` (ZSTD compression level 22, row group size 15 000).  
- Record count: **5,822**.  
- Column summary (selected highlights):  
  - `area`: 2.77 % NULL, 5,180 unique values, range 15 – 487,111 m².  
  - `azimuth`: 89.63 % NULL, 156 unique values, max ≈ 530°.  
  - `modType`: 0 % NULL, two values (`c‑si`, `thin‑film`).  
  - `grndCvr`: 97.61 % NULL, two values (`impervious`, `vegetation`).  

## Panels Conversion
- Converted `GMSEUS_Panels_Final_2025_v2_0.gpkg` to Parquet with the same cleaning, geometry handling, and ordering steps.  
- Output file: `GMSEUS_Panels_Final_2025_v2_0.parquet`.  
- Record count: **3,429,157**.  
- Column summary (overview):  
  - `arrayID`, `panelID`: cast to integer.  
  - `rowSpace`: `-9999.0` treated as NULL.  
  - Geometry transformed to EPSG:4326 and stored as WKB.  

## Key Takeaways
- Version 2 of GM‑SEUS provides a substantially larger panel inventory and introduces rooftop arrays, enabling more comprehensive solar‑energy analyses.  
- The author’s high‑performance workstation and open‑source GIS stack (GDAL, DuckDB, QGIS) facilitate efficient data cleaning, transformation, and storage in columnar Parquet format.  
- Detailed column‑level statistics reveal extensive missing data in several attributes (e.g., azimuth, tilt, ground cover), which should be considered in downstream modeling.