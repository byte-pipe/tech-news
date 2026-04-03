---
title: “Bro, ban me at the IP level if you don't like me!” - The Boston Diaries - Captain Napalm
url: https://boston.conman.org/2025/08/21.1
site_name: hackernews_api
fetched_at: '2025-08-25T23:07:26.271574'
original_url: https://boston.conman.org/2025/08/21.1
author: classichasclass
date: '2025-08-25'
description: “Bro, ban me at the IP level if you don't like me!”
tags:
- hackernews
- trending
---

## Thursday, August 21, 2025

### “Bro, ban me at the IP level if you don't like me!”

More and more I think I'm coming around toAlex Schroeder's Butlerian Jihad.
For reasons,
I'm looking into web activity and so far,
the top webbot this month is one identifying itself as “Thinkbot,”
whichmaybe related tothisAIcompanybut I can't be sure.
Here's how it identifies itself: “Mozilla/5.0 (compatible; Thinkbot/0.5.8; +In­_the­_test­_phase,­_if­_the­_Thinkbot­_brings­_you­_trouble,­_please­_block­_its_IP_address._Thank_you.)”.

Seriously,
that's it.
NoURLto read up on it.
It doesn't look at therobots.txtfile.
Just “bro,
ban me at theIPlevel if you don't like me!”Yeah,
block itsIPaddress.
You mean the 74 unique addresses it used this month alone?Checking eachIPaddress for theASNit's fromshows the 74 address coming from 41 (41!) network blocks!A further check showed that all the network blocks are owned by one organization—Tencent.
I'm seriously thinking that theCCPencourage this with maybe the hope of externalizing the cost of theGreat Firewallto the rest of the world.
If China scrapes content,
that's fine as far as theCCPgoes;
If it's blocked,
that's fine by theCCPtoo
(I say,
as I adjust mytin foil hat).In any case,
I added the following network blocks to my “badbots firewall rule set:”43.130.0.0/18
43.130.64.0/18
43.130.128.0/19
43.130.160.0/19
43.131.0.0/18
43.132.192.0/18
43.133.64.0/19
43.134.128.0/18
43.135.0.0/18
43.135.64.0/18
43.135.192.0/19
43.153.0.0/18
43.153.192.0/18
43.154.64.0/18
43.154.128.0/18
43.154.192.0/18
43.155.0.0/18
43.155.128.0/18
43.156.192.0/18
43.157.0.0/18
43.157.64.0/18
43.157.128.0/18
43.159.128.0/19
43.163.64.0/18
43.164.192.0/18
43.165.128.0/18
43.166.128.0/18
43.166.224.0/19
49.51.132.0/23
49.51.140.0/23
49.51.166.0/23
101.32.0.0/20
101.32.48.0/20
101.33.64.0/19
119.28.64.0/19
119.28.128.0/20
129.226.160.0/19
150.109.32.0/19
150.109.96.0/19
170.106.32.0/19
170.106.176.0/20The above list probably doesn't exhaustively enummerate Tencent's network block ownership,
but it's a start.
The above covers 476,590 uniqueIPaddresses
(excluding the base network and broadcast address for each network block).
I think it's bad that I had to do this,
but with the current landscape of the Internet,
it seems inevitable.
We can't have nice things it seems.#### Discussions about this entryBro, ban me at the IP level if you don't like me | LobstersBro, ban me at the IP level if you don't like me - Lemmy: BestiverseBro, ban me at the IP level if you don't like me | Hacker News
