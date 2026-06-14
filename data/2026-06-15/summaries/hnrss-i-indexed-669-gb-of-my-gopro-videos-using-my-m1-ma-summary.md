---
title: I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models | Hacker News
url: https://news.ycombinator.com/item?id=48528029
date: 2026-06-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-15T06:02:08.645335
---

# I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models | Hacker News

# I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models

## Overview
- The author had 2,207 GoPro videos (≈ 669 GB, 15 h 13 m total) and wanted to locate interesting moments from his cycling trips without uploading to the cloud.  
- Built a local pipeline on an Apple M1 Max that:
  - Extracts frames at low resolution  
  - Runs open‑source vision models for classification and face detection  
  - Transcribes audio with Whisper‑style models  
  - Converts visual, textual, and audio data into embeddings  
  - Stores embeddings in a vector database and metadata in an SQL database  
  - Enables semantic search by text, image, or audio query  
  - Sends selected clips directly to a DaVinci Resolve timeline for editing  

## Results
- Successfully indexed 628 videos (668.68 GB, 15 h 13 m of footage).  
- Metrics table (referenced in the original blog) details processing time per stage, GPU/CPU utilization, and storage overhead.  

## Technical Highlights
- Utilized the M1 Max’s unified memory and dedicated neural engine, which provide high memory bandwidth and fast inference for AI models.  
- Ran models locally; no data left the machine.  
- Planned future support for containerised GPU usage (e.g., Docker with MPS).  

## Community Feedback & Related Tools
- **Jumper** – suggested as an alternative for offline video search with NLE integrations.  
- Similar projects: indexing a year of video locally (Simbastack blog).  
- DaVinci Resolve 21 now includes AI IntelliSearch; some users note it processes locally and may support face search.  
- Hardware comparison: M1 Max’s memory bandwidth far exceeds typical x86 CPUs, making it especially suited for AI workloads.  
- Discussion about applying the pipeline to adult content: requires specialized models or LoRA fine‑tuning to handle content filters.  
- Docker GPU support on Apple silicon mentioned (podman + runkit, vLLM‑metal).  

## Future Directions
- Add support for Docker containers to leverage MPS GPU acceleration.  
- Explore frame‑level embeddings for more precise action‑based searches.  
- Gather user feedback for new features in the open‑source code, desktop app, or blog post.