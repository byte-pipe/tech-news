---
title: Running Your Own AS: BGP on FreeBSD with FRR, GRE Tunnels, and Policy Routing | Larvitz Blog
url: https://blog.hofstede.it/running-your-own-as-bgp-on-freebsd-with-frr-gre-tunnels-and-policy-routing/
date: 2026-02-09
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-09T06:02:26.962142
---

# Running Your Own AS: BGP on FreeBSD with FRR, GRE Tunnels, and Policy Routing | Larvitz Blog

# Running Your Own AS: BGPs on FreeBSD with FFR, GRE Tunnels, and Policy Routing

This article details how to set up a private Autonomous System (AS) on the public internet using FreeBSD, enabling control over your IPv6 address space. It covers obtaining necessary resources, configuring a FreeBSD router with FFR, establishing GRE and GIF tunnels to distribute prefixes, and managing routing for servers with multiple IPv6 address spaces.

## Why Run Your Own AS?

Having a dedicated AS number and IPv6 prefix offers several advantages:

* **Address Portability:** Addresses follow the server, simplifying migrations and updates.
* **Understanding Routing:** Provides deeper insight into internet routing and prefix propagation.
* **Simplified Multi-Provider Architecture:** Streamlines infrastructure when using multiple hosting providers.

## Obtaining Resources

To announce prefixes, you need an AS number and an IPv6 prefix from a Regional Internet Registry (RIR). Individuals typically obtain these through a sponsoring Local Internet Registry (LIR), which is a RIPE member who sponsors their registration. The process involves:

* Requesting resources with the intended use case.
* Creating necessary RIPE database objects (aut-num, inet6num, route6).
* Setting up Route Origin Authorizations (ROAs) to cryptographically bind the prefix to the AS.

Upstream connectivity is also required, with providers willing to carry your BGP sessions.

## Architecture Overview

The setup involves a FreeBSD-based BGP router that peers with upstream providers and downstream servers connected via tunnels. The router announces the originated prefix to upstream providers, while individual subnets are tunneled to downstream servers using GIF tunnels. This allows servers to use their globally routable addresses while maintaining their existing provider-assigned IPv6.

## The BGP Router

The router runs on a FreeBSD virtual machine with direct connectivity to two upstream networks. Key configuration aspects include:

### Network Configuration

The `/etc/rc.conf` file configures the physical interface, tunnel interfaces, and static routes. Important settings include:

* Defining the hostname, security levels, and physical interface.
* Specifying tunnel interfaces (GRE and GIF) with their respective peer addresses and descriptions.
* Configuring a loopback alias for the originated prefix.
* Defining routes for downstream servers, including specific subnets for VPS and the datacenter.
* Implementing a blackhole route for the originated prefix to prevent routing loops.
* Enabling PF firewall, logging, FFR, and ZFS.

### FFR Configuration

Free Range Routing (FRR) manages the BGP sessions. The configuration in `/usr/local/etc/frr/frr.conf` defines:

* The BGP prefix list for the originated prefix.
* Prefix lists to deny reserved or invalid IPv6 prefixes.
* A route map to permit the originated prefix, set community attributes, and add the AS number.

## Key Points

* The blackhole route is crucial for preventing routing loops.
* Point-to-point tunnels use `/128` prefixes.
* Downstream routes target specific subnets at the tunnel endpoints.
* GRE is used for the iFog peering session, while GIF is used for downstream tunnels due to its simplicity.

In summary, this article provides a comprehensive guide to setting up a private AS on FreeBSD, leveraging FFR, GRE, and GIF tunnels for flexible routing and address management.
