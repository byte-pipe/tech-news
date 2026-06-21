---
title: Running microVMs in Proxmox VE, The Easy Way - Tao of Mac
url: https://taoofmac.com/space/blog/2026/06/18/1845
date: 2026-06-19
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-22T00:54:05.880309
---

# Running microVMs in Proxmox VE, The Easy Way - Tao of Mac

# Running microVMs in Proxmox VE, The Easy Way – Summary

## Background
- The author manages a heterogeneous Proxmox cluster ranging from an Atom‑based 2 GB node to an i7‑12700 with 128 GB RAM.  
- Dissatisfied with the trade‑offs between LXC containers (fast but share host kernel) and full VMs (isolated but slow to boot).  

## Goal
- Obtain VM‑level isolation while keeping container‑like boot times.  
- Leverage QEMU’s **microvm** machine type, originally designed for Firecracker‑style workloads.  

## pve‑microvm Package
- Distributed as a single `.deb` that patches Proxmox’s Perl modules at install time.  
- Adds a new `machine: microvm` option to VM configurations; the patched code generates a minimal QEMU command line.  
- Ships:
  - A 12 MB custom Linux 6.12.22 kernel with only virtio, vsock, virtiofs, 9p and Docker‑required modules.  
  - A 1 MB initrd that probes virtio devices and switches root in ~150 ms.  
  - `pve-microvm-template` to build root filesystems from 12 supported OCI base images (Debian, Alpine, Fedora, Rocky, Amazon Linux, etc.).  
  - `pve-oci-import` for direct OCI image import into a PVE‑managed disk.  
  - Web UI extensions (Create µVM button, machine‑type dropdown, conditional panels, bolt icon).  
  - Systemd service `pve-microvm-early.service` to apply patches before `pvedaemon` starts.  

## How It Works
- No BIOS, no GRUB, no legacy devices; the guest boots directly from the host‑provided kernel.  
- Only virtio devices are exposed: a serial console, virtio‑blk, and virtio‑net, all over PCIe transport with non‑transitional devices.  
- The kernel lives on the host (`/usr/share/pve-microvm/vmlinuz`); the guest disk contains only the root filesystem, no `/boot` or per‑guest kernel.  
- Root filesystems are assembled from OCI images, not installed from ISO media.  

## Boot Performance
- Standard VM: 5–10 s to reach login due to firmware, bootloader, and chipset emulation.  
- MicroVM: sub‑300 ms to a fully networked guest with QEMU agent.  
- Example timings:  
  - SmolBSD (NetBSD) boots in 31 ms using MMIO transport.  
  - Debian with Docker and QEMU agent boots < 8 s on first run (apt install), then ~300 ms on subsequent boots.  

## Transport Details
- QEMU microvm supports two virtio transports: MMIO (lighter) and PCIe.  
- Linux guests have a device‑probing bug on QEMU 10.x when using MMIO, causing only virtio‑blk to bind.  
- The author therefore uses PCIe with modern‑only devices for Linux, adding ~50 ms overhead but ensuring reliable driver binding.  

## Advantages Over Traditional Options
- **Isolation**: Same KVM hardware boundary as a full VM.  
- **Speed**: Boot times comparable to containers.  
- **Resource Efficiency**: No emulated chipset, minimal memory footprint.  
- **Uniform Kernel Management**: One host‑side kernel for all microVMs; updates are a single file replace and guest restart.  
- **OS Flexibility**: Supports 21 guest OS types, including exotic ones like Plan 9.  

## Use Cases
- Running lightweight services such as Gitea, Caddy reverse proxies, mini‑firewalls, and AI agents.  
- Deploying Gitea Actions workers where rapid VM start‑up is beneficial.  

## Open Issues & Future Work
- Investigate and fix the Linux MMIO device‑probing bug in the kernel configuration.  
- Encourage community contributions for patches and additional OS support.  

## Conclusion
pve‑microvm turns Proxmox VE into a platform that offers VM‑level security with container‑like agility, by stripping away unnecessary firmware and devices, using a shared host kernel, and automating root‑filesystem creation from OCI images. This approach simplifies kernel updates, reduces boot latency, and expands the range of runnable operating systems within a single Proxmox cluster.