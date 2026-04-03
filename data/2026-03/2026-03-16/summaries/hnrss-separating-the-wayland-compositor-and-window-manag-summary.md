---
title: Separating the Wayland Compositor and Window Manager
url: https://isaacfreund.com/blog/river-window-management/
date: 2026-03-15
site: hnrss
model: llama3.2:1b
summarized_at: 2026-03-16T11:29:28.159755
---

# Separating the Wayland Compositor and Window Manager

# Separating the Wayland Compositor and Window Manager

## Brief Overview of Traditional Wayland Architecture
The traditional Wayland implementation combines a Wayland display server with a window manager into a single program. This design choice leads to a monolithic wayland compositor, requiring both systems to handle significant work.

## New 0.4.0 Release of river: A Non-Monolithic Wayland Compositor

### Key Features and Advantages

* **Non-Monolithic Architecture**: river splits the window manager into two separate programs (display server and window manager), breaking away from the traditional monolithic architecture.
* **Stableriver-window-management-v1protocol**: Provides full control over window position, keys, and other policies to user-facing applications. Also provides frame-perfect rendering, good performance, and low-level plumbing for the display server.
* ** river's Compositor Role**
	+ Combines buffered data from visible windows into a single buffer to be displayed by the kernel.

## Understanding X11 Architecture and Wayland

* `xinitcb` uses `user events` between the `X Window System` process, `display server`, and `compositor`: The traditional architecture route input events from a user in their interactive session through an event queue (like an event pipe ) to another program with less access.

### Traditional Wayland Solution

1. Display servers separate: receive input
2. Send it to window managers, but displays don’t help with rendering (and other compositor tasks) in that case
3. Each `display server` tries its own version of the rendering solution based off user key bindings 
4. There will be display events and changes made over several display servers: these can result in unnecessary round trips 

### river Solution Breaks Away from Traditional Wayland Architects

1. Non-monolithic design avoids traditional problems
2. Supports windows manager capabilities directly (vs using a 'display server')
3. Uses Stableriver-window-management-v1protocol for full control of application interaction with windows