---
title: 'GitHub - M-Abozaid/esp32-c3-adblock: Pi-hole-class DNS ad-blocker on a $2 ESP32-C3 (no PSRAM): 537k domains as 40-bit FNV-1a hashes in flash, binary-searched. UDP DNS sinkhole + web dashboard. https://youtube.com/shorts/RaxszOUMi8E?feature=share · GitHub'
url: https://github.com/M-Abozaid/esp32-c3-adblock
site_name: github
content_file: github-github-m-abozaidesp32-c3-adblock-pi-hole-class-dns
fetched_at: '2026-10-06T16:47:44.519344'
original_url: https://github.com/M-Abozaid/esp32-c3-adblock
author: M-Abozaid
description: 'Pi-hole-class DNS ad-blocker on a $2 ESP32-C3 (no PSRAM): 537k domains as 40-bit FNV-1a hashes in flash, binary-searched. UDP DNS sinkhole + web dashboard. https://youtube.com/shorts/RaxszOUMi8E?feature=share - M-Abozaid/esp32-c3-adblock'
---

M-Abozaid

 

/

esp32-c3-adblock

Public

* NotificationsYou must be signed in to change notification settings
* Fork128
* Star1.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

32 Commits
32 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
data
data
 
 
docs
docs
 
 
hardware
hardware
 
 
src
src
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_JP.md
README_JP.md
 
 
partitions.csv
partitions.csv
 
 
platformio.ini
platformio.ini
 
 
View all files

## Repository files navigation

# esp32-c3-adblock

日本語 README

APi-hole-style DNS ad-blockerthat runs on a$2 ESP32-C3—no PSRAM required.

📰 Featured onTom's Hardware,XDA Developers, andKorben.

The trick everyone misses: you don't need to keep the blocklist in RAM. Store the
domains assorted 40-bit hashes in flashand binary-search them. 140,000+ domains
fit in ~0.7 MB of flash and are matched in ~10 ms, using~50 KB of RAM.

query in ──▶ extract domain ──▶ FNV-1a hash (+ parent suffixes)
 ──▶ binary-search the flash hash table
 ├─ hit ──▶ answer 0.0.0.0 (sinkholed)
 └─ miss ──▶ forward to upstream resolver, relay the reply

## Why this is interesting

Most ESP32 DNS sinkholes load the blocklist (domainstrings) into RAM, so they
demand PSRAM. This project stores fixed5-byte (40-bit) hashes in flashinstead:

string-in-RAM approach

this (hash-in-flash)

Hardware

ESP32 + PSRAM (~$8)

ESP32-C3, no PSRAM (~$2)

141k domains

~2.5 MB of RAM

0.67 MB of flash

RAM used

most of it

~50 KB

Lookup

string compare

~18 flash reads (~10 ms incl. WiFi RTT)

Collisions

n/a

0 at 141k (1 at 537k)

Why 40 bits?It's the sweet spot for this flash budget. Collisions follow the
birthday bound — at 141k domains you get ~0, at 537k about 1 (i.e. one unlucky
domain gets over-blocked). Dropping to 32 bits would save 20% of the flash but
cost ~7 collisions at 250k; going to 64 bits wastes 3 bytes per domain to solve
a problem you don't have.

The same trick works on bigger chips — it isn't a C3 workaround. On a 16 MB
ESP32-S3 these hashes hold~2.7M domainsvs ~466k for strings in 8 MB of
PSRAM. Hashes in flash beat strings in PSRAM basically everywhere; the C3 just
makes it undeniable.

## Hardware

* AnyESP32-C3board (tested on a C3 SuperMini), 4 MB flash,no PSRAM needed
* ClassicESP32(DevKit / WROOM, 4 MB) also builds:pio run -e esp32dev -t upload(community-contributed, compile-tested; the C3 is the tested target)
* Power it from astable USB source(a phone charger or your router's USB port).
Cheap/loose USB-C→A adapters can brown out the radio during WiFi transmit.
* AUSB-A → USB-C donglelets it plug straight into the spare USB port on the
back of most routers — no power supply, no extra box.

### Enclosure

A printable case for the C3 SuperMini:hardware/esp32-c3-supermini-enclosure.stl

Printing notes:

* No supports needed; 0.2 mm layers, ~15% infill is plenty.
* Keep the antenna end clear.The C3's PCB antenna is the zig-zag trace on the
short edge opposite the USB-C port — don't bury it in solid plastic or put metal
near it, or your RSSI will suffer.
* Leave the vents open: the board idles around 45–55 °C.

## Build & flash (PlatformIO)

One USB flash to get going — after that,firmware and blocklist both update over WiFi(see below).

⚠️Use acurrent PlatformIO— the VSCode PlatformIO extension's bundled core, orpip install -U platformioin a venv. The distro/aptplatformiopackage (e.g. 4.3.4) is
too old and fails withAttributeError: ... 'resultcallback'(issue #4). A one-click browser installer is on the way (hosting TBD).

#
 1. copy the secrets template (gitignored, stays local) and edit it:

#
 - WIFI_SSID / WIFI_PASS are optional — leave the placeholders and use the

#
 on-device setup portal instead (below).

#
 - WEB_USER / WEB_PASS / OTA_PASS are NOT optional: they gate the dashboard's

#
 state-changing endpoints (/ban, /addblock, /upload, /update, /setupdate,

#
 /forgetwifi) and network OTA. Pick real values — these used to be wide

#
 open to anyone on the LAN.

cp src/secrets.example.h src/secrets.h

#
 then edit src/secrets.h

#
 2. build the blocklist hash table (default = StevenBlack base + Hagezi Light,

#
 ~100k entries, WhatsApp/social safe)

python3 tools/build_blocklist.py data/blocklist.bin

#
 3. flash firmware + the blocklist filesystem (the one and only USB flash)

pio run -t upload
pio run -t uploadfs

#
 4. watch it boot, note the IP / open the dashboard

pio device monitor 
#
 -> http://c3adblock.local

### Your own blocklists

build_blocklist.py OUT.bin [SOURCE ...]takes any mix of URLs and local files, in any of
these formats:

* hosts files—0.0.0.0 ads.example.com
* plain domain lists— one domain per line
* AdGuard / Adblock basic rules—||ads.example.com^blocks,@@||ok.example.com^removes a domain (e.g. to mirror an AdGuard Home allowlist)

A blocked domain also blocks its subdomains. Rules a DNS hash list can't express (regex,
wildcards,$modifiers, cosmetic##rules) are skipped and counted. An@@rule only
un-blocks that exact entry — it can't carve a subdomain out of a blocked parent. If a source
can't be downloaded the build stops instead of silently producing a smaller list
(--allow-missingto override).

### WiFi setup (no re-flash needed)

If it can't connect (or you never setsecrets.h), it starts an open access pointC3-AdBlock-XXXXwith a captive portal — join it from a phone, pick your network,
type the password, done. To move it to a new network later: clickForget WiFion
the dashboard, or hold theBOOTbutton while powering on, and the setup portal
comes back. (/forgetwifirequires auth now, so it's no longer a bare URL you can
just visit — see Security below.)

## Over-the-air updates (no more USB)

The dashboard athttp://c3adblock.localdoes it all:

* Blocklist— drop a freshly builtblocklist.binintoBlocklist → Upload, or set a
URL underRemote auto-updateand the device pulls a prebuiltblocklist.binon a schedule. A fresh default list is rebuiltevery Mondayby GitHub Actions and
published at a stable URL, so pasting this once keeps a device current on its own:https://github.com/M-Abozaid/esp32-c3-adblock/releases/download/blocklist/blocklist.bin
* Firmware— upload.pio/build/c3/firmware.binunderFirmware → OTA update; the
device verifies it and reboots into the new image. Or push over WiFi from the CLI:pio run -t upload --upload-port c3adblock.local --upload-protocol espota

4 MB flash tradeoff:firmware OTA needstwoapp slots, which leaves ~1.3 MB for the
blocklist (~250k domains max). The aggressive 537k "ultimate" list only fits the
single-app partition table (no firmware OTA). Pick your tradeoff inpartitions.csv.

## Security

The dashboard's read-only view (/,/stats.json) stays open, but every
state-changing endpoint requiresHTTP Basic Auth(WEB_USER/WEB_PASSfromsecrets.h):

* /ban,/addblock,/unblock,/forgetwifi
* /upload,/update(blocklist and firmware OTA)
* /setupdate,/fetchnow

Network OTA (ArduinoOTA, e.g.pio run -t upload --upload-port c3adblock.local --upload-protocol espota) requiresOTA_PASSfrom the same file.

Without this, anyone who could reach the device on the LAN could reflash it
with arbitrary firmware or rewrite the blocklist with zero credentials — worth
knowing given the device sits in the path of every DNS query on your network.
Custom blocked-domain names are also HTML-escaped before being rendered on the
dashboard, closing a stored-XSS path where a domain string containing markup
(added via/addblock) would otherwise execute in the viewing browser.

Basic Auth here is a LAN-trust-boundary control, not encryption.Everything
is plain HTTP on :80 — this chip has no realistic budget to run a TLS server.
Basic Auth credentials are base64 (not encrypted) and sent on every authenticated
request; anyone who can already sniff your LAN traffic (open/guest WiFi, ARP
spoofing) can read them off the wire. This hardens against the common case —
another device on your network hitting the API with no credentials at all, or a
browser tab CSRF'ing it — not against an on-path network attacker.

CSRF via cached Basic Auth:browsers auto-attach cached Basic Auth
credentials toanysubsequent request to an already-authenticated origin —
including one triggered by a totally unrelated page the same browser visits
later (e.g.<img src="http://c3adblock.local/forgetwifi">, no JS required).
That would let any webpage silently drive this API once you've logged into the
dashboard once, regardless of who's on your LAN. Every mutating endpoint above
now also requires a customX-Requested-With: c3-adblockheader, which a plain<img>/auto-submitted<form>CSRF can't attach (only same-originfetch()can, which is what the dashboard's own JS does) — this is why/forgetwifiis
no longer a bare URL you can visit directly; use the dashboard button instead.

Default credentials:ifsecrets.hstill has the placeholderCHANGE_ME_WEB_PASSWORD/CHANGE_ME_OTA_PASSWORDvalues fromsecrets.example.h, the device boots with a "password" that's public (it's
sitting in this repo's example file). The firmware logs a warning over serial
and shows a banner on the dashboard when this is the case — but it will still
boot and run, so don't skip setting real values insecrets.hbefore trusting
this on a network you don't fully control.

Out of scope for now: the WiFi setup portal's access point (C3-AdBlock-XXXX)
is still open (unencrypted) by design — it needs to be joinable without knowing
a password first. The real WiFi password you type into the portal is only as
safe as that local radio link during the brief setup window.

## Use it

Point a device's DNS at the C3's IP, or add it as asecondary resolverbehind
your main DNS. Test:

dig @
<
c3-ip
>
 doubleclick.net 
#
 -> 0.0.0.0 (blocked)

dig @
<
c3-ip
>
 github.com 
#
 -> real IP (forwarded)

## Gotchas (learned the hard way)

* ModemManager(default on Fedora/Ubuntu) grabs/dev/ttyACM0and toggles
DTR/RTS, whichresets the C3and blocks serial. Fix:sudo systemctl stop ModemManagerecho'ATTRS{idVendor}=="303a", ENV{ID_MM_DEVICE_IGNORE}="1"'|sudo tee /etc/udev/rules.d/99-esp-no-modemmanager.rules
sudo udevadm control --reload-rules&&sudo udevadm trigger
* The C3's USB-Serial-JTAG console can swallow early boot output until the host
connects (while(!Serial)helps).
* DNS clients add anEDNS OPTrecord; a blocked reply must contain only the
question + answer (ANCOUNT=1, NSCOUNT=ARCOUNT=0) or it's malformed.

## Done / how it could grow

* ✅ Web dashboard — per-client block/allow counts, ban a client, add custom domains
* ✅ mDNS (c3adblock.local) for discovery
* ✅ OTA — firmware + blocklist update over WiFi, plus scheduled remote blocklist pulls
* ✅ Captive-portal WiFi setup (no hardcoded creds) + one-click browser web-installer
* ⬜ Bucketed prefix index — ~18 flash reads/lookup → ~1–2 (issue #3), the throughput win
* ⬜ Act as the DHCP server (hand itself out as DNS) for true plug-and-play

## Credits

Inspired bys60sc/ESP32_AdBlocker— the
"answer 0.0.0.0 for blocklisted domains" idea. This is an independent from-scratch
implementation focused on the hash-in-flash optimization for PSRAM-less chips.

## License

MIT — seeLICENSE.