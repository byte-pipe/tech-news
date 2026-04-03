---
title: The (successful) end of the kernel Rust experiment [LWN.net]
url: https://lwn.net/Articles/1049831/
site_name: hackernews_api
fetched_at: '2025-12-10T19:07:22.882425'
original_url: https://lwn.net/Articles/1049831/
author: rascul
date: '2025-12-10'
description: Rust in the kernel is no longer experimental
tags:
- hackernews
- trending
---

LWN
.net

News from the source






User:


Password:



 |


 |


Log in
 /

Subscribe
 /

Register

# The (successful) end of the kernel Rust experiment

[Posted December 10, 2025 by corbet]


The topic of the Rust experiment was just discussed at the annual
Maintainers Summit. The consensus among the assembled developers is that
Rust in the kernel is no longer experimental — it is now a core part of the
kernel and is here to stay. So the "experimental" tag will be coming off.
Congratulations are in order for all of the Rust for Linux team.

(Stay tuned for details in our Maintainers Summit coverage.)to post comments



### NicePosted Dec 10, 2025 4:25 UTC (Wed)
 byktkaffee(subscriber, #112877)
 [Link] (17 responses)You got me for a second### NicePosted Dec 10, 2025 4:45 UTC (Wed)
 byjosh(subscriber, #17465)
 [Link] (11 responses)Phoronix would be proud of that headline.### NicePosted Dec 10, 2025 4:48 UTC (Wed)
 bycorbet(editor, #1)
 [Link] (2 responses)Ouch. That is what I get for pushing something out during a meeting, I guess. That was not my point; the experimentisdone, and it was a success. I meant no more than that.### NicePosted Dec 10, 2025 5:24 UTC (Wed)
 byjosh(subscriber, #17465)
 [Link]Huh. I had figured it was a playful attempt at clickbait; it didn't occur to me that the headline's double meaning could be an accident.(And don't worry, you'd have to fall *very* far, very consistently, to limbo under the low bar Phoronix has set for clickbait.)### NicePosted Dec 10, 2025 5:47 UTC (Wed)
 bysjvn(guest, #19124)
 [Link]Made me look! :-)### NicePosted Dec 10, 2025 6:04 UTC (Wed)
 byrolexhamster(guest, #158445)
 [Link] (7 responses)>Phoronix would be proud of that headline.Elitist much?Notwithstanding the low quality user comments on Phoronix and somewhat challenged writing in its news items, the site does provide useful info by way of frequent updates of what's happening in and around the open source ecosystem. Its benchmarks have also uncovered problems in the Linux kernel. In certain ways it's complementary to LWN's coverage.### NicePosted Dec 10, 2025 7:49 UTC (Wed)
 byCyberax(✭ supporter ✭, #52523)
 [Link] (2 responses)And their benchmark suite is genuinely pretty neat.### NicePosted Dec 10, 2025 11:09 UTC (Wed)
 byrossburton(subscriber, #7254)
 [Link] (1 responses)Oh it's really not that impressive really. There's nothing readily available that's better but that doesn't mean it's objectively good.Fun fact: Clear Linux wins in many of the phoronix benchmarks because the default bashrc does export CFLAGS=-O3.(caveat: this was the case when I was researching what Clear does to get better scores on identical hardware some years ago, but I don't believe anything has changed since then)### NicePosted Dec 10, 2025 17:12 UTC (Wed)
 byhiguita(guest, #32245)
 [Link]Of course they could be better, but while you dig what is happening, most people will not or even can't not dig in to all apps/systems/distros. While i understand some kernel options or apps , others are totally unknown for me.Phoronix benchmarks makes no clain or change, install the system and test... that is the result. if you do not do anything else, expect those results! if you dig in to it, you can finetune more ... but on other end, you also see that "optimized distros" can have much better results in some items, but almost no difference on others, so you also know if it is even worth investing time trying to optimize something or not. For many apps/games, is not worth the time to optimize it more to get 5% or less more performance (and like O3, risk of getting more bugs)A benchmark that tries to optimize every single app is not only lot of work, but also no system and workload is the same, the best option for one setup may not be the best one for another, so that would be always a problem for someone.As for hardware and distros/kernel evolution over time, they are actually very useful, we can see how a new hardware is performing and even postpone buying one a few months, where you get better performance and possible better price also.or how much updating the distro may help in some setups.finally the news, yes, he tends to overreact to some news or rumors, but it got much better with time and for one men show, he actually track way many projects and report back when something happens, so you know things that usually don't show up in other placesSo yes, phoronix is not perfect, it could be better in some areas, but is good enough, specially being a one men show and not aa team of people. Many of the issues would probably be mitigated if there was more people working as different opinions and reviewing would catch most of the issues or too personal opinions### NicePosted Dec 10, 2025 9:26 UTC (Wed)
 bylkundrak(subscriber, #43452)
 [Link] (1 responses)we all know it's a guilty please### NicePosted Dec 10, 2025 9:27 UTC (Wed)
 bylkundrak(subscriber, #43452)
 [Link]*pleasuresorry, commenting before my morning frontal lobotomy### NicePosted Dec 10, 2025 11:08 UTC (Wed)
 byfarnz(subscriber, #17727)
 [Link]Phoronix also tends to benchmark in the "dumb but obvious" way - just follow the instructions, don't take the time to understand it in depth and tweak obsessively until it's as good as it's going to get. This is useful, because it exposes cases where something is genuinely useful once tweaked into shape, but where the defaults are bad and need fixing.### NicePosted Dec 10, 2025 17:36 UTC (Wed)
 byclump(subscriber, #27801)
 [Link]Phoronix has long had a toxicity problem. Moderation is horrible to non-existent, and news items often touch far too frequently on low-value information. For example, how many news items are needed for display manager contributor issues or file system drama?I do like that Phoronix can cover useful desktop news.### NicePosted Dec 10, 2025 7:57 UTC (Wed)
 byalspnost(guest, #2763)
 [Link]Same here - for a second, I thought they were about to rip it all out for v6.20 -> 7.0!### NicePosted Dec 10, 2025 9:07 UTC (Wed)
 byadobriyan(subscriber, #30858)
 [Link]> Predictable end of the kernel Rust experiment### NicePosted Dec 10, 2025 9:32 UTC (Wed)
 byevalir(subscriber, #171462)
 [Link]Had us in the first half, ngl### NicePosted Dec 10, 2025 13:07 UTC (Wed)
 byhailfinger(subscriber, #76962)
 [Link]That headline was a masterpiece of triggering an emotional rollercoaster. "WTF no way" ... "phew".Well done!### JedizlapulgaPosted Dec 10, 2025 14:15 UTC (Wed)
 byJedizlapulga(guest, #180979)
 [Link]Sincerely speaking### MemePosted Dec 10, 2025 6:32 UTC (Wed)
 bymrcroxx(guest, #161669)
 [Link] (2 responses)> Mike: rachel and i are no longer dating>> rachel: mike that's a horrible way of telling people we're married### MemePosted Dec 10, 2025 13:58 UTC (Wed)
 byrsidd(subscriber, #2582)
 [Link] (1 responses)Edited by mike after comments:> Mike: rachel and i are (successfully) no longer dating### MemePosted Dec 10, 2025 14:49 UTC (Wed)
 byjaa(subscriber, #14170)
 [Link]Brilliant, thank you, this made my day.(as did the emotionally roller-coaster news item)### hilarity ensuesPosted Dec 10, 2025 10:11 UTC (Wed)
 bycbushey(guest, #142134)
 [Link] (1 responses)The original title and associated comments gave me a good laugh. Thank you.### I forgotPosted Dec 10, 2025 10:22 UTC (Wed)
 bycbushey(guest, #142134)
 [Link]In my original post I neglected to suggest that the original title should qualify as a notable qotw. Sorry for the self reply and thanks for the comment preview feature because it helped me catch a typo.### I was looking for a reason.Posted Dec 10, 2025 15:57 UTC (Wed)
 bystumbles(guest, #8796)
 [Link] (2 responses)Well, guess its time to switch back to Microsoft.### I was looking for a reason.Posted Dec 10, 2025 16:08 UTC (Wed)
 byfarnz(subscriber, #17727)
 [Link] (1 responses)Bad news in that respect - Microsoft isusing Rust in the Windows kernel, too.### I was looking for a reason.Posted Dec 10, 2025 17:56 UTC (Wed)
 byktkaffee(subscriber, #112877)
 [Link]Pretty sure they actually shipped it, too, some pieces of the windowing system.





Copyright © 2025, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
