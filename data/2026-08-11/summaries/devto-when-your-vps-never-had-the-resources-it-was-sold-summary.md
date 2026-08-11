---
title: When Your VPS Never Had the Resources It Was Sold With - DEV Community
url: https://dev.to/pascal_cescato_692b7a8a20/when-your-vps-never-had-the-resources-it-was-sold-with-302o
date: 2026-08-05
site: devto
model: llama3.2:1b
summarized_at: 2026-08-11T11:46:43.105421
---

# When Your VPS Never Had the Resources It Was Sold With - DEV Community

**Debugging Invisible Hypervisor Provisioning Gaps**

**Key Points:**

* The author upgraded their infrastructure from one provider to another and experienced IPv4 and disk provisioning issues.
* Both problems were due to gaps in the promised and actual configurations, not Linux-related errors.
* The author has identified a pattern of such issue where an offer promises more resources than the actual allocation.

**Summary:**

The article discusses experiences with invisible hypervisor provisioning gaps. The author upgraded their infrastructure from one provider to another and encountered these issues:

1. **IPv4 Provisioning Issues:** After upgrading to a new instance, IPv4 addresses showed up but no ICMP (Internet Control Message Protocol) responses were received from the VPS or gateway. The issue was resolved after some troubleshooting.
2. **Disk Provisioning Issues:** When installing CyberPanel, the author encountered an "No space left on device" error. Upon checking the disk's allocation, they found that the actual allocated storage was not what was promised (3.5 GB vs 10 GB). This discrepancy led to a pattern of such issues where offers promise more resources but actual allocations are less.

**Maintenance and Troubleshooting:**

The author discovered that resizing or growing a filesystem can only extend it into space that's already allocated, making tools like `resize2fs` and `growpart` ineffective. Understanding why these provisioning gaps occur is crucial:

* `resize2fs` and `growpart` cannot be used to increase the amount of storage.
* Resizing an existing partition does not increase the total disk size.
* Understanding the specific allocation scheme (10 GB vs 20 GB) is a critical factor in identifying and resolving such issues.

The pattern described in the article highlights the importance of thoroughly checking configurations before upgrading infrastructure and using resources to their full potential.