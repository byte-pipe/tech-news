---
title: Discovering Hard Disk Physical Geometry through Microbenchmarking « Blog
url: https://blog.stuffedcow.net/2019/09/hard-disk-geometry-microbenchmarking/
date: 2026-04-30
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-05T00:54:34.782315
---

# Discovering Hard Disk Physical Geometry through Microbenchmarking « Blog

# Discovering Hard Disk Physical Geometry through Microbenchmarking

## Summary
- Hard drives store data on rotating magnetic platters with read/write heads that move radially across concentric tracks.  
- Modern drives no longer use the classic CHS (cylinders‑heads‑sectors) model; only the number of heads (surfaces) remains constant.  
- Microbenchmarks can measure RPM, angular position of each sector, seek times, track boundaries, track skew, and defective‑sector patterns.  
- Full‑stroke seeks on the tested drives required 1.3 – 3.6 revolutions; heads accelerate slowly, so few tracks are reachable within the first revolution.  
- Short‑stroking yields limited seek‑time reduction because even short seeks consume a relatively long time.  
- Seek‑time plots reveal Acoustic Management (AAM): long‑distance seeks are slowed to reduce noise, while short seeks are unaffected.  
- Track boundaries are identified by searching for track‑skew; newer disks use different track densities on each surface.  
- Estimated track pitch on the newest drive is ~80 nm, with an average bit length of ~17 nm.  
- Track layouts vary widely: older drives grouped several head switches before moving to the next cylinder, whereas modern drives switch heads after a small group of adjacent tracks.  
- Multiple skew types exist (cylinder, serpentine, zone change); skew is usually constant across the disk but exceptions were observed (e.g., Maxtor 7405AV, Seagate ST1).  
- Combining seek profiles and track‑size data visualizes defective sectors; most disks contain clusters of bad sectors, some skip entire tracks.  
- The author tested 17 drives ranging from 45 MB (1989) to 5 TB (2015); algorithms are not flawless and microbenchmarking remains challenging.

## Background: Hard‑drive geometry
- Data is organized on platters into recording surfaces, tracks, and sectors.  
- A “cylinder” historically grouped all tracks at the same radius across surfaces; modern drives no longer maintain fixed cylinders.  
- Sector size has shifted from 512 bytes to 4 KB.  
- The physical geometry (track count, sector count per track, surface count) determines total capacity: C × H × S.

## Microbenchmark methodology
1. **Basic read‑access timing** – measures rotation period and sector angular position.  
2. **Seek‑time profiling** – issues controlled seeks of varying distances to build a latency curve.  
3. **Track‑boundary detection** – searches for changes in sector timing indicative of track skew.  
4. **Surface‑count inference** – combines seek patterns and head‑switch timings to estimate the number of recording surfaces.  
5. **Defective‑sector mapping** – uses irregular timing or read errors to locate bad‑sector clusters.

## Key observations from the 17 tested drives
- **RPM stability** across models, but slight variations affect timing precision.  
- **Track pitch** decreased over time, reaching ~80 nm on the latest 5 TB drive.  
- **Bit density** increased to ~17 nm per bit, reflecting advances in magnetic recording technology.  
- **Seek behavior** shows a non‑linear relationship with distance; AAM influences long‑range seeks.  
- **Skew patterns** are generally uniform but can change abruptly at zone boundaries or on specific models.  
- **Defect distribution** tends to form contiguous “holes” rather than isolated bad sectors.  

## Conclusions
- Microbenchmarking can reveal detailed physical characteristics of hard drives without disassembly, though assumptions valid for older drives often fail on modern hardware.  
- The diversity of track layouts and skew behaviors requires adaptable algorithms.  
- Despite limitations, the presented techniques provide valuable insight into drive geometry, performance, and reliability.