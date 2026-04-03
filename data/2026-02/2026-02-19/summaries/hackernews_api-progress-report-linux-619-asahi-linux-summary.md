---
title: Progress Report: Linux 6.19 - Asahi Linux
url: https://asahilinux.org/2026/02/progress-report-6-19/
date: 2026-02-18
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-19T06:03:44.480083
---

# Progress Report: Linux 6.19 - Asahi Linux

# Progress Report: Linux 6.19

* Asahi Linux celebrates its 5th anniversary, evolving from a basic serial port setup to a well-supported desktop platform for Apple Silicon. This growth has spurred significant interest in Arch64 on Apple devices, leading to fixes for platform-specific software bugs.
* A recurring question from the community has been regarding USB-C display output and DisplayPort Alt Mode support. Asahi's response, inspired by id Software, is "done when it's done."
* The "fairydust" branch, a culmination of years of reverse engineering by Sven, Janne, and marcan, has achieved basic DisplayPort output via USB-C on a specific machine. However, it has limitations including support for only one display, issues with hot/cold plugging, and potential color/timing problems with certain setups. It is intended for developers to assist in resolving these issues.
* Significant progress has been made in supporting the M3 series of MacBooks. Three new contributors have joined the effort, writing preliminary device trees and kernel patches. Basic functionality like keyboard, touchpad, WiFi, NVMe, and USB3 are working, similar to the state of M1 support at the initial beta release.
* The current state of M1 and M2 support is intended to be the baseline for M3 support, but a release is not imminent. A major hurdle is that the graphical environment is currently software-rendered, impacting performance. Reverse engineering of the M3 GPU and improvements to the DCP firmware interface are ongoing.
* Several features are still under development and will not be included in the near term, such as Energy-Aware Scheduling and speaker safety for M3 devices.
* The 14" and 16" MacBook Pro displays offer excellent color accuracy, brightness, and a 120 Hz refresh rate. However, macOS's ProMotion feature hides refresh rates above 60 Hz, requiring specific configurations.
