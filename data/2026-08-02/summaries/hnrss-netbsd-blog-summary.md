---
title: NetBSD Blog
url: https://blog.netbsd.org/tnf/entry/netbsd_11_0_released
date: 2026-08-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-02T06:02:47.363239
---

# NetBSD Blog

# NetBSD 11.0 released!

## Announcement
- The NetBSD project announces the release of NetBSD 11.0 (posted August 01, 2026).  
- A detailed release announcement is available for further information.

## Installation
- Consult the installation notes for your specific architecture.  
- Download the preferred install image from the CDN.  
- For ARM‑based devices, obtain a pre‑configured U‑Boot image from the bootable ARM images page.  
- ISO images are split:
  - < 700 MB images for CD‑ROM media.  
  - Full‑size DVD images (identified by “-dvd.iso”).  
- For flash‑based media (e.g., USB drives), use the `.img` files and decompress them first (e.g., with `gunzip` or 7‑Zip).

## Support
- Report installation or runtime issues via the NetBSD mailing lists or by filing a problem report.

## Security note
- The number of security issues has risen sharply with AI tools; the release includes open security issues rather than delaying the launch.  
- Open security‑related pull‑up requests (and associated GNATS reports):
  - **hdaudio(4)**: Apply access checks to ioctl commands, PR60492; workaround – remove `/dev/hdaudio*`.  
  - **ipfilter**: Fix remotely triggerable null‑pointer dereference, PR60484; not included in any released kernel by default.  
  - **pf**: Fix use‑after‑free in fragment reassembly, PR60485; PF is deprecated and not included in any released kernel by default.

## Release process
- The release was delayed while awaiting stable releases of third‑party components.  
- Release candidates were used to give users time to test changes.  
- The process is largely automated, but manual steps remain (e.g., security officer signing release hashes).  
- Overall speed is limited by the slowest step: transferring every file for every architecture over the network.

## Future plans
- All open pull‑up requests will be merged into the stable branch shortly after the 11.0 release.  
- NetBSD 11.1 is targeted for release within the next two months.

## Comments
- The post has received 5 comments.