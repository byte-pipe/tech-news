---
title: Denuvo has been cracked in all single-player games it previously protected — 2K Games and Denuvo reportedly retaliate with mandatory 14-day online checks | Tom's Hardware
url: https://www.tomshardware.com/video-games/pc-gaming/denuvo-has-been-bypassed-in-all-single-player-games-it-previously-protected-2k-games-and-denuvo-reportedly-retaliate-with-mandatory-14-day-online-checks
site_name: hnrss
content_file: hnrss-denuvo-has-been-cracked-in-all-single-player-games
fetched_at: '2026-05-03T19:54:59.969826'
original_url: https://www.tomshardware.com/video-games/pc-gaming/denuvo-has-been-bypassed-in-all-single-player-games-it-previously-protected-2k-games-and-denuvo-reportedly-retaliate-with-mandatory-14-day-online-checks
date: '2026-04-28'
published_date: '2026-04-28T10:00:00Z'
description: Temporary success for the red team elicits a collective cheer.
tags:
- hackernews
- hnrss
---

(Image credit: Getty Images)

* Copy link
* Facebook
* X
* Whatsapp
* Reddit
* Pinterest
* Flipboard
* Email

Share this article

31

Join the conversation

Follow us

Add us as a preferred source on Google

Newsletter

Subscribe to our newsletter

We've reported previously on the feats of theskull-and-bones community against Denuvo's DRM. The cat-and-mouse game has essentially come to a head for now, as the pirate crew has "officially" reported that, as of yesterday, there were zero games with Denuvo that haven't been cracked or bypassed.

This development should be of little surprise to those following this story along, but here's a quick recap: in late 2025, the MKDev collective and the prolific DenuvOwO came up witha hypervisor-based bypass (HVB)that installs a kernel-level driver to intercept and respond to Denuvo's checks. While that's not an actual crack, it's good enough for piracy work, as the saying goes. Simultaneously, voices38, a well-known cracker, also fully stripped a few choice titles of Denuvo entirely, includingrecent releases likeResident Evil: Requiem.

As a somewhat predictable response, Denuvo and 2K Gamesreportedly just addeda 14-day mandatory online check to several titles, including NBA 2K25, NBA 2K26, and Marvel's Midnight Suns. This is impossible for the HVB to emulate, as it's a request/response call to Denuvo's servers and thus in practice can't be replicated. At some point, the code that executes this check could be removed, but that requires a full game crack rather than the HBP.

Article continues below 

This harkens back to the dark ages of online requirements for single-player games and is likely to pose a problem for gamers with spotty internet connections or who travel a lot. Needless to say, honest gamers will also be locked out of their games if Denuvo's servers experience problems, too. The "new" check differs from the existing one-time activation that Denuvo performs when the game is first launched, which persists until a hardware or software change.

Regardless, it wasn't difficult to imagine that sooner or later, all extant Denuvo-protected games would fall to the pair of proverbial swords. "Sooner" was the safest bet, and its bell rang yesterday, when the list ofuncracked or non-bypassed gamesdropped to zero. Moreover, while the HVB method previously required users to disable most every single one of Windows'securitymeasures, the current "V3" method has a relatively minor impact on prospective gamers' PCs.

As it stands, to run a HVB game, one needs "only" to disable Core Isolation (aka Memory Protection), and then toggle Driver Signature Enforcement off (DSE), run the game, and turn DSE back on. In fact, the most recent version of the famous "VBS.cmd" script is reportedly even easier to use, and game-agnostic to boot.

Although keeping Memory Integrity off still opens up a significant attack surface, and gamers are required to trust pirates with installing a kernel-level driver, the situation is a far cry (pun intended) from the early 2026 days when it was even necessary to fiddle with motherboards' UEFI and disable Secure Boot.

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

The eyepatch-wearing community is patting itself on the back, with known repacker FitGirl congratulating the collective efforts of DenuvOwO and voices38, as good an endorsement as they come within that crowd. It's also an implicit seal of approval for the relative security of the releases in question, as FitGirl is widely trusted as a release curator.

 

FollowTom's Hardware on Google News, oradd us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

Bruno Ferreira
Contributor

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.