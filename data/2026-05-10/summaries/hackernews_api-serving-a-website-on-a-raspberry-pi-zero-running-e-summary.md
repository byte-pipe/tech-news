---
title: Serving a Website on a Raspberry Pi Zero Running Entirely in RAM
url: https://btxx.org/posts/memory/
date: 2026-05-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-10T07:47:28.854129
---

# Serving a Website on a Raspberry Pi Zero Running Entirely in RAM

# Serving a Website on a Raspberry Pi Zero Running Entirely in RAM

## The (Local) Hardware
- Raspberry Pi Zero v1.3  
- 512 MB+ microSD card (used for install and booting into RAM)  
- Waveshare Ethernet HAT (or USB‑OTG adapter)  
- Ethernet cable  
- Micro‑USB power supply  
- Optional: cool case, monitor, HDMI‑to‑mini‑HDMI adapter, keyboard  

## The (External) Hardware
- Tiny VPS for TLS termination (TierHive used in the guide)  
- VPS specs: Alpine Linux, 128 MB RAM, 1 GB NVMe storage, 1 vCPU, ≈ $2 per year  
- Any other provider or Cloudflare can be substituted  

## Preparing the microSD Card
- On macOS: identify the device (`diskutil list`), erase to FAT32 (`diskutil eraseDisk FAT32 ALPINE MBRFormat /dev/diskX`)  
- Extract the Alpine tarball directly onto the card (`tar xzf alpine‑rpi‑*.tar.gz -C /Volumes/ALPINE`)  
- Remove macOS metadata (`find … -name '._*' -delete`, delete `.Spotlight-V100`, `.fseventsd`, `.Trashes`)  
- Eject the card and insert it into the Pi Zero  

## Alpine Linux in Diskless Mode
- Boot into Alpine live, login as `root` (no password)  
- Configure LBU to store changes on the SD card:  
  - `setup -lbu mmcblk0p1`  
  - Create cache directory and point APK cache there  
  - `lbu commit -d` (run after any package install or file change)  
- Run `setup-alpine` and select **none** for disk installation to keep the system RAM‑only  
- Choose keyboard, hostname, eth0 networking, DNS, timezone, mirror, dropbear SSH, root password  
- After reboot, verify RAM‑only root with `df -h /` (should show `tmpfs` or `ramfs`)  

## Software Stack
### darkhttpd (lightweight static server)
- Install: `doas apk add darkhttpd`  
- Create `/etc/init.d/darkhttpd` OpenRC script with command pointing to `/var/www/example.com` and desired port  
- Enable and start: `chmod +x /etc/init.d/darkhttpd`, `rc-update add darkhttpd default`, `rc-service darkhttpd start`  
- Persist files and script with LBU: `lbu include /etc/init.d/darkhttpd`, `lbu include /var/www`  

### nginx (optional for more flexibility)
- Install: `doas apk add nginx`  
- Add site config in `/etc/nginx/http.d/yourdomain.com.conf` (listen 8080, root `/var/www/yourdomain.com`, basic try_files)  
- Enable and start: `rc-update add nginx default`, `rc-service nginx start`  
- Persist with LBU: `lbu include /etc/nginx`, `lbu include /var/www`  

### rsync (for syncing site files)
- Install: `doas apk add rsync`  
- Use from a workstation to push updates to the Pi  

### lbu (Alpine’s backup utility)
- After any configuration change, run `lbu commit -d` to write changes to the SD card  

## Opening Ports
- Only one port (e.g., 80) needs to be forwarded from the router to the Pi’s static LAN IP  
- If the home ISP provides a dynamic public IP, set up DDNS (DuckDNS recommended)  

## TierHive VPS (TLS termination)
- VPS runs HAProxy (pre‑configured) that accepts HTTPS, terminates TLS, and forwards plain HTTP to the Pi’s public IP/port  
- Keeps the Pi’s workload minimal and avoids heavy crypto processing on the 512 MB device  

## Backups & Maintenance
- Regularly run `lbu commit -d` after updates to keep the SD card snapshot current  
- Use rsync or scp to back up `/var/www` and configuration directories to another machine or cloud storage  

## Happy Hosting!
- The Pi Zero serves the site entirely from RAM, uses minimal resources, and benefits from external TLS handling via a cheap VPS.