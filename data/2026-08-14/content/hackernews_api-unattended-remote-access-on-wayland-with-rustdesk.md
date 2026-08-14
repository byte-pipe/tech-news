---
title: Unattended Remote Access on Wayland with RustDesk — RustDesk
url: https://rustdesk.com/blog/unattended-remote-access-wayland/
site_name: hackernews_api
content_file: hackernews_api-unattended-remote-access-on-wayland-with-rustdesk
fetched_at: '2026-08-14T19:48:41.639984'
original_url: https://rustdesk.com/blog/unattended-remote-access-wayland/
author: RustDesk Team
date: '2026-08-14'
description: RustDesk brings true unattended remote access to Wayland, with multi-monitor support. A preview build for x86_64 Debian/Ubuntu-based systems is available now.
tags:
- hackernews
- trending
---

Wayland support has been one of the harder parts of Linux remote desktop.

RustDesk can now providetrue unattended access on Wayland, without requiring someone at the remote machine to approve every session.Multi-monitor setups are supported as well.

After the initial setup, you can connect even when no one is at the remote machine — including from thelogin screenafter a reboot.

Watch the demo video on X

For now, we are releasing this as a separate preview build forx86_64 Debian/Ubuntu-based systems:

Download the Wayland unattended access build

Wayland support is still limited in several major remote desktop products. AnyDesk currently requires Xorg for incoming Linux sessions, while TeamViewer still describes Wayland support as experimental for common desktop environments.

We would like to get more real-world testing before making this the default.

Once the implementation is stable, we plan to bring unattended Wayland access to more Linux distributions, includingFedora and Arch Linux, and eventually include it in the standard RustDesk releases.

If you use Wayland, especially with multiple monitors, please give the preview build a try and let us know what works—and what doesn’t.

* RustDesk
* Wayland
* Linux
* unattended-access
Share:
 
 
 
 
 
Back to Blog

## Related Posts

View All Posts »

### Enhanced ACL in RustDesk Server Pro 1.5.0

RustDesk Server Pro now supports user-level ACL and device groups in addition of user groups.

### How to make Flutter 3.24 run on Windows 7?

Since Flutter 3.22 starts to drop support for Windows 7 / 8, we need to modify Flutter engine to restore support for Windows 7.

### RustDesk web client V2 Preview

V2 offers better codecs, international keyboard support, clipboard support, file transfer etc.

### RustDesk for Linux: The Open-Source Remote Desktop

Install and run RustDesk on Linux: .deb, .rpm, Flatpak and AppImage, X11 vs Wayland, headless and unattended access, and self-hosting the server.