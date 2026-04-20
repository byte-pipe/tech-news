---
title: A Survey of the 7 Configuration Changes That Turn a Multi-homed Linux Host into a Switch/Router – blog
url: https://patrickmccanna.net/7-configuration-changes-that-turn-a-multi-homed-host-into-a-switch-router/
date: 2026-04-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-05T01:03:22.421952
---

# A Survey of the 7 Configuration Changes That Turn a Multi-homed Linux Host into a Switch/Router – blog

# A Survey of the 7 Configuration Changes That Turn a Multi‑homed Linux Host into a Switch/Router

## Overview
- The article explains how a standard Linux system can be transformed into networking infrastructure such as a router, switch, or Wi‑Fi access point.
- It emphasizes that the difference is not in hardware but in a small set of kernel and userspace configuration changes.
- The author contrasts the typical file‑system‑centric view of servers with the process‑centric view of networking gear and shows that both converge with the same seven steps.

## The Seven Required Changes
1. **Activate IP forwarding** – enable the kernel to forward packets between interfaces.
2. **Define a bridge** – create a virtual link layer device that can bind multiple NICs.
3. **Activate nftables policies** – load netfilter tables that will inspect packets at hook points.
4. **Stateful firewalling with conntrack** – track connections so rules can be applied based on state.
5. **Define NAT and masquerade policies** – translate private addresses to public ones for outbound traffic.
6. **Provide DHCP and DNS via dnsmasq** – supply address and name services to downstream hosts.
7. **Provide Wi‑Fi networks with hostapd** – turn a wireless NIC into an access point.

## Packet Journey Through the Kernel
- A NIC receives a frame, DMA‑places it in a kernel ring buffer, and the driver triggers an interrupt.
- The networking stack strips the Ethernet header, reads the IP destination, and consults the routing table.
- If the destination matches a local interface, the packet is delivered locally; otherwise, with forwarding disabled, it is dropped.
- Enabling forwarding routes the packet to the **FORWARD** netfilter hook, where further processing (filtering, NAT, etc.) occurs.

## Netfilter Hooks (the “hooks” concept)
- Hooks are predefined interception points in the packet path where registered callbacks can inspect, modify, accept, or drop packets.
- The five standard hook points are:

  - **PREROUTING** – before routing decision.
  - **INPUT** – for packets destined to the local host.
  - **FORWARD** – for packets passing through the host.
  - **OUTPUT** – for locally generated packets.
  - **POSTROUTING** – just before leaving an interface.

- Userspace tools (e.g., nft) register functions at these hooks via the netlink socket.

## Detailed Look at Change 1: Activating IP Forwarding
- Controlled by the sysctl parameter `net.ipv4.ip_forward`.
- Persistent configuration is placed in `/etc/sysctl.d/10-forward.conf` with the line `net.ipv4.ip_forward=1`.
- At boot, `systemd-sysctl.service` reads all files in `/etc/sysctl.d/` and writes the values to `/proc/sys/…`.
- Writing `1` to `/proc/sys/net/ipv4/ip_forward` tells the kernel to send non‑local packets to the **FORWARD** hook instead of discarding them.

## Additional Observations
- The same kernel changes are used by Android devices to provide personal Wi‑Fi hotspots.
- Monitoring tools such as `nft list ruleset`, `conntrack -L`, and tracing utilities (`perf trace`, `bpftrace`) can be used to inspect the live state of the netfilter framework.
- The article frames the transformation as a series of “gates” that must be opened, each corresponding to a specific kernel or userspace component.

## Conclusion
- Turning a Linux host into a router/switch requires only seven well‑defined configuration steps.
- Understanding the packet flow, netfilter hooks, and the sysctl mechanism demystifies the process and bridges the perceived gap between traditional servers and dedicated networking appliances.
