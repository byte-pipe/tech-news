---
title: OpenBSD-current now runs as guest under Apple Hypervisor
url: https://www.undeadly.org/cgi?action=article;sid=20260115203619
site_name: hackernews_api
fetched_at: '2026-01-16T19:08:24.773440'
original_url: https://www.undeadly.org/cgi?action=article;sid=20260115203619
author: gpi
date: '2026-01-16'
description: OpenBSD-current now runs as guest under Apple Hypervisor
tags:
- hackernews
- trending
---

Contributed byPeter N. M. Hansteenon2026-01-15from the hyper-armed dept.

Following a recent series of commits
by
 Helg Bredow (
helg@
)
and
 Stefan Fritsch (
sf@
),
OpenBSD/arm64
 now works as a guest operating system under the
Apple Hypervisor
.

The commits readList: openbsd-cvs
Subject: CVS: cvs.openbsd.org: src
From: Helg Bredow <helg () cvs ! openbsd ! org>
Date: 2026-01-12 18:15:33


CVSROOT:	/cvs
Module name:	src
Changes by:	helg@cvs.openbsd.org	2026/01/12 11:15:33

Modified files:
	sys/dev/pv : viogpu.c

Log message:
viogpu_wsmmap() returns a kva but instead should return a physical
address viabus_dmamem_mmap(9). Without this, QEMU would only show a
black screen when starting X11. On the Apple Hypervisor, the kernel
would panic.Also add calls to bus_dmamap_sync(9) before transferring the framebuffer
to host memory. It was working for me without this, but this ensures
that the host running on another CPU will see updates to the
framebuffer.

Thanks to kettenis@ for reviewing and providing feedback.

ok sf@andList: openbsd-cvs
Subject: CVS: cvs.openbsd.org: src
From: Stefan Fritsch <sf () cvs ! openbsd ! org>
Date: 2026-01-15 9:06:19

CVSROOT:	/cvs
Module name:	src
Changes by:	sf@cvs.openbsd.org	2026/01/15 02:06:19

Modified files:
	sys/dev/pv : if_vio.c

Log message:
vio: Support MTU feature

Add support for the VIRTIO_NET_F_MTU which allows to get the hardmtu
from the hypervisor. Also set the current mtu to the same value. The
virtio standard is not clear if that is recommended, but Linux does
this, too.

Use ETHER_MAX_HARDMTU_LEN as upper hardmtu limit instead of MAXMCLBYTES,
as this seems to be more correct.

If the hypervisor requests a MTU larger than ETHER_MAX_HARDMTU_LEN,
redo feature negotiation without VIRTIO_NET_F_MTU.

With this commit, OpenBSD finally works on Apple Virtualization.

Input and testing from @helg

ok jan@This development will be most welcome for those of us who run with newerApple SiliconMac models.As always, if you have the hardware and the capacity, please take this for a spin (in snapshots now), and report!

Reply

## Latest Articles

* Fri, Jan 1608:51pf: make af-to less magical(0)
* 08:51pf: make af-to less magical(0)
* Thu, Jan 1520:36OpenBSD-current now runs as guest under Apple Hypervisor(0)13:58MAXCPUS on OpenBSD/amd64-current is now 255(0)
* 20:36OpenBSD-current now runs as guest under Apple Hypervisor(0)
* 13:58MAXCPUS on OpenBSD/amd64-current is now 255(0)
* Wed, Jan 1410:41rpki-client 9.7 released(0)
* 10:41rpki-client 9.7 released(0)
* Tue, Jan 1307:08LACPmode removed fromtrunk(4)(0)
* 07:08LACPmode removed fromtrunk(4)(0)
* Wed, Dec 3108:03Miod talks about HP/PA boot blocks(0)07:05OpenBGPD 9.0 released(1)
* 08:03Miod talks about HP/PA boot blocks(0)
* 07:05OpenBGPD 9.0 released(1)
* Tue, Dec 3009:49fw_update(8)now checksdmesg(8)output in addition todmesg.boot(0)
* 09:49fw_update(8)now checksdmesg(8)output in addition todmesg.boot(0)
* Fri, Dec 1209:43The story of Propolice, the OpenBSD stack protector(2)
* 09:43The story of Propolice, the OpenBSD stack protector(2)

## Credits

Copyright ©2004-2008Daniel Hartmeier.
All rights reserved.
Articles and comments are copyright their respective authors,
submission implies license to publish on this web site.
Contents of the archive prior toApril 2nd 2004as well as images
and HTML templates were copied from the fabulous originaldeadly.orgwithJose's andJim's kind permission.
This journal runs asCGIwithhttpd(8)onOpenBSD, thesource codeisBSDlicensed.
undeadly \Un*dead"ly\, a. Not subject to death; immortal. [Obs.]
