---
title: "Technical note: transfer files over an ethernet patch cable (Maurycy's blog)"
url: https://maurycyz.com/misc/etherfiles/
date: 2026-08-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-01T09:52:23.433878
---

# Technical note: transfer files over an ethernet patch cable (Maurycy's blog)

# Technical note: transfer files over an ethernet patch cable

## Main procedure
- Connect two computers directly with a standard Ethernet patch cable.  
- Assign IPv6 addresses on each host (e.g., `fd42:dead:beef::1/48` on the sender, `fd42:dead:beef::2/48` on the receiver) and bring the interfaces up with `ip link set dev eth0 up`.  
- Verify connectivity with `ping`.  
- Transfer a file using `socat` and `dd`:  
  - Receiver: `socat - TCP6-LISTEN:1234 | dd status=progress > big_file.tar.gz`  
  - Sender: `socat - 'TCP6-CONNECT:[fd42:dead:beef::2]:1234' < big_file.tar.gz`  

## Performance
- A normal patch cable and Ethernet ports can reach ~900 Mbit/s (≈6.7 GB per minute).  
- High‑end NICs can achieve much higher rates, still far exceeding USB flash drives or cloud‑based transfers.

## Comparison with other methods
- **Cloud storage**: Requires two network transfers, is often throttled, and can be costly.  
- **Wi‑Fi LAN**: Typically slower, prone to dropouts, and rarely reaches multi‑gigabit claims in typical home environments.  
- **Removable storage (USB)**: Limited by cable quality and host/device architecture; copying to and from the drive halves effective speed.  
- **USB‑C / Thunderbolt**: Linux now supports `/dev/tbstreamX` for direct USB‑C links, but hardware availability is limited.

## Why Ethernet is preferred
- Inexpensive, widely available, and reliably reaches gigabit speeds between arbitrary devices.  
- Differential signaling with transformers provides strong immunity to RFI and ground‑level shifts.  
- Can be used without a full TCP/IP stack; raw link‑layer frames work even on a switched LAN, making it simple for microcontroller data transfers.

## Related tool
- `ethtransfer.sh`: a minimal shell script that automates file copies over Ethernet.