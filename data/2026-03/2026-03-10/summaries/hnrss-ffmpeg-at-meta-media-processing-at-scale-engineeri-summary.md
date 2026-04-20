---
title: FFmpeg at Meta: Media Processing at Scale - Engineering at Meta
url: https://engineering.fb.com/2026/03/02/video-engineering/ffmpeg-at-meta-media-processing-at-scale/
date: 2026-03-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-10T06:02:55.313558
---

# FFmpeg at Meta: Media Processing at Scale - Engineering at Meta

# FFmpeg at Meta: Media Processing at Scale

## Background and Motivation
- Meta executes `ffmpeg` and `ffprobe` tens of billions of times daily, creating unique scalability challenges.
- An internal FFmpeg fork was used for features not yet present upstream, such as threaded multi‑lane encoding and real‑time quality metric computation.
- Over time the fork diverged significantly from the upstream project, making maintenance and rebasing difficult while new upstream releases added codecs, formats, and reliability improvements.

## Migration to Upstream FFmpeg
- Meta collaborated with FFmpeg developers, FFlabs, and VideoLAN to upstream the needed features.
- Threaded multi‑lane transcoding was introduced in FFmpeg 6.0 and refined through 8.0.
- In‑loop decoding for real‑time quality metrics landed in FFmpeg 7.0.
- These upstream changes allowed Meta to deprecate its internal fork entirely.

## Multi‑Lane Transcoding for VOD and Livestreaming
- User uploads trigger generation of multiple DASH encodings (different resolutions, codecs, framerates, quality levels).
- A single FFmpeg command can decode a source once and feed multiple encoder instances, eliminating duplicate decoding and process‑startup overhead.
- Upstream threading now runs all encoder instances in parallel, improving CPU utilization for the >1 billion daily uploads processed by Meta.

## Real‑Time Quality Metrics
- Visual quality metrics (PSNR, SSIM, VMAF) are needed during livestreaming to assess compression impact in real time.
- “In‑loop” decoding inserts a decoder after each encoder, providing original and compressed frames for per‑lane metric calculation within a single FFmpeg command.
- This capability is now part of upstream FFmpeg, removing the need for Meta‑specific patches.

## Upstream vs. Internal Patches
- Features with broad community impact (e.g., efficient threading, real‑time metrics) are contributed upstream.
- Hardware‑specific patches, such as support for Meta’s Scalable Video Processor (MSVP) ASIC, remain internal because external developers lack access to the hardware for testing.
- Meta continuously rebases and validates its internal patches against newer FFmpeg releases to ensure robustness.

## Hardware Acceleration and MSVP
- FFmpeg already supports hardware‑accelerated decoding, encoding, and filtering via standard APIs for NVIDIA NVDEC/NVENC, AMD UVD, and Intel Quick Sync Video.
- Meta added MSVP support using the same API layer, enabling consistent tooling across software and custom ASIC pipelines with minimal platform‑specific quirks.

## Ongoing Commitment
- With upstream multi‑lane encoding and real‑time quality metrics, Meta fully retired its internal FFmpeg fork for VOD and livestream pipelines.
- Continued investment in FFmpeg’s development improves resource utilization, adds new codec support, and enhances reliability, directly benefiting user experiences on Meta’s platforms.
