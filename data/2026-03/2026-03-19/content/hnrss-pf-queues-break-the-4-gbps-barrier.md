---
title: PF queues break the 4 Gbps barrier
url: https://undeadly.org/cgi?action=article;sid=20260319125859
site_name: hnrss
content_file: hnrss-pf-queues-break-the-4-gbps-barrier
fetched_at: '2026-03-19T19:23:42.728445'
original_url: https://undeadly.org/cgi?action=article;sid=20260319125859
date: '2026-03-19'
description: 'OpenBSD: PF queues break the 4 Gbps barrier'
tags:
- hackernews
- hnrss
---

Contributed byPeter N. M. Hansteenon2026-03-19from the queueing for Terabitia dept.

OpenBSD
's

PF

packet filter has long supported 
HFSC
 traffic shaping
with the 
queue

rules in

pf.conf(5)
.
However, an internal 32-bit limitation in the 
HFSC

service curve structure (
struct hfsc_sc
) meant that bandwidth values
were silently capped at approximately 4.29 
Gbps
,

” the maximum value of a 
u_int
 "
.

With 10G, 25G, and 100Gnetwork interfaces now commonplace,
OpenBSDdevsmaking huge progress unlocking the kernel forSMP,
and adding drivers for cards supporting some of these speeds,
this limitation started to get in the way.
Configuringbandwidth 10Gon a queue would silently wrap around,
producing incorrect and unpredictable scheduling behaviour.A newpatchwidens the bandwidth fields in the kernel'sHFSCscheduler
from 32-bit to 64-bit integers, removing this bottleneck entirely.
The diff also fixes a pre-existing display bug inpftop(1)where bandwidth values above 4Gbpswould be shown incorrectly.For end users, the practical impact is:PFqueue bandwidth
configuration now works correctly for modern high-speed interfaces.
The familiar syntax just does what you'd expect:queue rootq on em0 bandwidth 10G
queue defq parent rootq bandwidth 8G defaultValues up to 999Gare supported, more than enough for interfaces
today and the future. Existing configurations using values
below 4Gcontinue to work - no changes are needed.As always, testing of-currentsnapshots anddonationsto the OpenBSD Foundation are encouraged.The editors note that the thread titledPF Queue bandwidth now 64bit for >4Gbps queuesontech@has the patch and a brief discussion with theconclusionthat the code is ready to commit by Friday, March 20th, 2026.

Reply

## Latest Articles

* Thu, Mar 1912:58PFqueues break the 4Gbpsbarrier(0)
* 12:58PFqueues break the 4Gbpsbarrier(0)
* Thu, Mar 1218:56Delayed hibernation comes to OpenBSD/amd64 laptops(4)
* 18:56Delayed hibernation comes to OpenBSD/amd64 laptops(4)
* Wed, Mar 1106:29OpenBSD -current moves to7.9-beta(0)
* 06:29OpenBSD -current moves to7.9-beta(0)
* Tue, Mar 1010:29Major update todrm(4)code in OpenBSD-current(to linux 6.18.16)(0)
* 10:29Major update todrm(4)code in OpenBSD-current(to linux 6.18.16)(0)
* Fri, Mar 0613:11The Book of PF, 4th EditionSpotted in the Wild(0)
* 13:11The Book of PF, 4th EditionSpotted in the Wild(0)
* Thu, Mar 0514:39OpenBSD on SGI: a rollercoaster story, as told bymiod@(2)
* 14:39OpenBSD on SGI: a rollercoaster story, as told bymiod@(2)
* Thu, Feb 2616:40tmppathpromise removed frompledge(2)in-current(0)11:06Another subprocess forvmd(8)(0)05:45Game of Trees 0.123 released(0)
* 16:40tmppathpromise removed frompledge(2)in-current(0)
* 11:06Another subprocess forvmd(8)(0)
* 05:45Game of Trees 0.123 released(0)

## Credits

Copyright ©2004-2008Daniel Hartmeier.
All rights reserved.
Articles and comments are copyright their respective authors,
submission implies license to publish on this web site.
Contents of the archive prior toApril 2nd 2004as well as images
and HTML templates were copied from the fabulous originaldeadly.orgwithJose's andJim's kind permission.
This journal runs asCGIwithhttpd(8)onOpenBSD, thesource codeisBSDlicensed.
undeadly \Un*dead"ly\, a. Not subject to death; immortal. [Obs.]