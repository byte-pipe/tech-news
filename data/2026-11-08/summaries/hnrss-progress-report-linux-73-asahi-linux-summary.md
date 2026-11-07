---
title: Progress Report: Linux 7.3 - Asahi Linux
url: https://asahilinux.org/2026/11/progress-report-7-3/
date: 2026-11-07
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:04:46.346058
---

# Progress Report: Linux 7.3 - Asahi Linux

# Progress Report: Linux 7.3 – Summary

## Upstreaming continues
- Ongoing upstream work includes low‑level SoC patches and two major drivers:
  - **macaudio** – required extensive ALSA core changes and adaptations for Apple‑specific speaker/headset amplifiers; driver and devicetree changes total ~3 100 lines.
  - **AVD** – added to the upstream list after only three months in the downstream tree; ~13 000 lines of driver and devicetree code, marking the fastest turnaround for a major SoC component.
- Initial devicetrees for M4 Pro, M4 Max, and M5 (thanks to Yureka) now boot to a TTY; further enablement is in progress.
- Shift toward an upstream‑first workflow: TI USB‑PD, SPMI drivers, and initial Thunderbolt support were developed upstream first and are now merging.

## M3 goes GA
- M3 series support, previously behind an EXPERT flag, is now generally available with no reported issues from early adopters.
- Key improvements:
  - Enabled DCP, boosting performance and battery life.
  - Added sleep support for M3 devices.
  - Made the notch area usable on MacBooks.
- Upcoming updates to m1n1 and the kernel will further refine M3 functionality.

## Crowded House
- Virtualisation of macOS on M4 and M5 series is progressing:
  - M5 requires Exclaves (secure‑kernel‑run isolated apps) communicated via SPTM and the Tightbeam IPC protocol.
  - Some Exclaves can be bypassed via command‑line tweaks, but not all.
  - Sven’s experiment placed the Secure Kernel and Exclave userspace in a separate VM alongside SPTM and macOS, successfully running three EL1 VMs under m1n1.
- This enables reverse‑engineering and virtualization of macOS on both M4 and M5 hardware.

## Hello Triangle(s)!
- M3 GPU differs significantly from M1/M2 GPUs; reverse‑engineering is underway by a new contributor group.
- At XDC 2024, the team demonstrated that m1n1 can initialise the M3 GPU and render a triangle.
- Integration into upstream Mesa will require substantial engineering due to Apple’s unconventional design choices.

## Kept you waiting, huh?
- Thunderbolt support, promised in early 2024, is now arriving:
  - Apple’s custom Thunderbolt controller is a Cortex‑M3 running RTKit with a bespoke router, breaking assumptions in the Linux Thunderbolt subsystem (which was built around Intel controllers).
  - The controller’s reset line is managed via PMGR MMIO writes, a unique coupling that required extensive investigation.
  - Sven delivered a patchset that was submitted upstream first and also merged into the downstream kernel.
- Current functionality:
  - USB 3, XDomain, and Thunderbolt networking work.
  - PCIe and DisplayPort tunnelling (required for most docks) are not yet supported.
- Acknowledgement of Sven’s five‑year effort on this task.

## “The Holy Grail, Doctor Jones”
- Running retail PC games on Asahi Linux remains a major challenge.
- The required stack must translate x86/amd64 binaries to arm64 with low latency, a complex and performance‑critical problem. (Further details were truncated.)