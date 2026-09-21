---
title: "Apple Mac Studio (M5 Ultra) review: Local model citizen outpaces DGX Spark and Threadripper | Tom's Hardware"
url: https://www.tomshardware.com/desktops/mini-pcs/apple-mac-studio-m5-ultra-review
date: 2026-09-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-22T08:46:51.804238
---

# Apple Mac Studio (M5 Ultra) review: Local model citizen outpaces DGX Spark and Threadripper | Tom's Hardware

# Apple Mac Studio (M5 Ultra) review: Local model citizen outpaces DGX Spark and Threadripper

## Verdict
- The Mac Studio with M5 Ultra is a compact, quiet workstation that delivers strong overall performance, very high memory throughput, and the ability to run large AI models locally.

## Pros
- M5 Ultra provides powerful CPU and GPU performance.  
- 1.2 TB/s memory bandwidth enables efficient local AI workloads.  
- Small footprint and quiet operation.  
- Abundant front‑ and rear‑panel ports for peripherals and displays.

## Cons
- Memory and SSD upgrades are expensive.  
- No post‑purchase upgradeability; RAM is soldered and SSDs are not user‑replaceable.

## Design (2026)
- Unchanged silver, square aluminum chassis, 7.7 × 7.7 × 3.7 inches, 8 lb (M5 Ultra version).  
- Heavier copper fin stack and vapor chamber for cooling compared to M5 Max.  
- Power button and ventilation holes on the rear; air intake through a built‑in bottom stand.  
- Kensington lock slot on the bottom (requires special adapter).

## Specifications
- **Processor:** Apple M5 Ultra, 36‑core CPU  
- **Graphics:** Integrated 80‑core GPU (each core with a neural accelerator)  
- **Neural Engine:** 32‑core  
- **Memory:** 256 GB LPDDR5 unified (512 GB announced for later)  
- **Storage:** 4 TB SSD (non‑user‑replaceable)  
- **Networking:** Apple N1, Wi‑Fi 7, Bluetooth 6, Thread  
- **Front ports:** 2 × Thunderbolt 5 (USB‑C), SD‑XC (UHS‑II) card reader  
- **Rear ports:** 4 × Thunderbolt 5, 2 × USB‑A, HDMI 2.1, 10 Gb Ethernet, 3.5 mm headphone jack  
- **Power supply:** 480 W continuous  
- **OS:** macOS 27.0 Golden Gate  
- **Price (tested configuration):** $12,299  

## Ports & Upgradeability
- Front: 2 × Thunderbolt 5 + SDXC slot.  
- Rear: 4 × Thunderbolt 5, 2 × USB‑A, HDMI 2.1, 10 Gb Ethernet, headphone jack.  
- No internal upgrade path: RAM is soldered, SSD not sold by Apple; external storage is the practical expansion method.

## M5 Ultra Chip
- First Apple quad‑die design: two dual‑die M5 Max SOCs linked via UltraFusion, delivering >4.4 TB/s inter‑die bandwidth.  
- Memory bandwidth up to 1.2 TB/s, supporting large LLMs on‑device.  
- 80 GPU cores each with a neural accelerator; 32‑core neural engine.  
- Media engine adds hardware H.264, HEVC, AV1 decode and four ProRes encode/decode engines.  
- Cinebench estimates: single‑core 4.6 GHz, multi‑core 4.3 GHz.

## Productivity Performance
- Quiet under load; fan audible only when heavily taxed.  
- Geekbench 7: single‑core 3,770, multi‑core 52,293 – top of the tested workstation field.  
- Handbrake: 4K → 1080p transcoding in 1 min 4 s, ~8 s faster than AMD Ryzen Threadripper 9980X.  
- Blender CPU rendering trails high‑core Threadrippers and Intel Xeon w‑3495X.  
- File copy speed: 2,983 MB/s, beating previous‑gen M3 Ultra and M4 Max.  
- Cinebench 2026 stress test scores consistent (≈17,800–18,100) with average CPU temperature 78 °C.

## Local AI Performance
- Neural‑accelerated GPU cores plus 1.2 TB/s memory bandwidth give superior matrix‑math throughput.  
- Prompt processing speed exceeds Nvidia DGX Spark; tokens‑per‑second throughput is double the M4 Max and ~4× higher than DGX Spark.  
- Tested with Qwen 3.8‑27B‑Q4_K_M model, showing strong isolated GPU performance and benefiting from the fast 36‑core CPU for mixed workloads.  
- Positioned as ready for demanding local or agentic AI tasks, even before clustering.

## Pricing & Target Audience
- Starting at $2,499 for M5 Max configuration – suitable for creators (video editors, photographers, game designers).  
- $12,299 for top‑end M5 Ultra, 256 GB RAM, 4 TB SSD – positioned as an enterprise‑grade device or remote server capable of any workstation task, including intensive AI workloads.