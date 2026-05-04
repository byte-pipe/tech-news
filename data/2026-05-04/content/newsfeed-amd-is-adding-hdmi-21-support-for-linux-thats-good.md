---
title: AMD is adding HDMI 2.1 support for Linux. That's good news for the Steam Machine. - Ars Technica
url: https://arstechnica.com/gaming/2026/05/amd-is-adding-hdmi-2-1-support-for-linux-thats-good-news-for-the-steam-machine/
site_name: newsfeed
content_file: newsfeed-amd-is-adding-hdmi-21-support-for-linux-thats-good
fetched_at: '2026-05-04T20:14:27.366473'
original_url: https://arstechnica.com/gaming/2026/05/amd-is-adding-hdmi-2-1-support-for-linux-thats-good-news-for-the-steam-machine/
date: '2026-05-04'
published_date: '2026-05-04T16:26:49+00:00'
description: Fixed Rate Link being added now; Display Stream Compression coming soon.
tags:
- ars-technica
- gaming
- amd
- hdmi
---

Text
 settings

Last year, we noted how the long-standing vagaries ofHDMI licensing and open source AMD driver developmentcombined to prevent the upcomingSteam Machine from receiving official support for the HDMI 2.1 display standard. Now, though, it seems that AMD is making real progress on adding full HDMI 2.1 compliance to its Linux amdgpu driver in the near future.

In patch series notes for an amdgpu driver updateposted on Friday(andnoticed by Phoronix), AMD’s Harry Wentland says that the company is finally adding HDMI FRL (Fixed Rate Link) support to the popular Linux display driver. That’s the feature thatallows for higher bandwidth on compatible HDMI cablescompared to the TMDS standard found on HDMI 2.0 and earlier. That in turn enables direct support for higher resolutions, dynamic HDR, and features like Variable Refresh Rate that aren’t supported in HDMI 2.0.

Wentland notes that this update is still just “a representative subset of HDMI compliance,” in part because it is missing the code to support theDisplay Stream Compression(DSC) that allows for even higher resolutions and frame rates up to 10K at 100 Hz. But Wentland adds that DSC support “is still being tested and will be sent out later,” and that “a full compliance run” for HDMI 2.1 is “in the works.” An AMD driver developer with the handle agd5f alsocommented on Phoronix, noting that “a full implementation [of HDMI 2.1] will ultimately be available once the patches are ready and have completed compliance testing.”

This is all good news for Steam Machine buyers and other Linux gamers who want to finally make use of high-end display features that werefirst standardized in 2017. Valve says it has been using workarounds likechroma subsamplingandAMD Freesync supportto squeeze better Steam Machine performance out of the HDMI 2.0 bandwidth currently supported by AMD’s Linux drivers. The coming introduction of full HDMI 2.1 support in amdgpu should obviate the need for those workarounds, though.

It’s unclear whetherthe HDMI Forum’s original legal issues with any open source implementation of HDMI 2.1have been resolved or if that organization will allow Linux devices to advertise as HDMI 2.1-compliant (we’ve reached out to the HDMI Forum for comment). For now, though, it seems clear that AMD is finally comfortable adding the HDMI 2.1 features it says have been ready and waiting to its Linux drivers for years now. In December, Valve said that “we’ve been working on trying to unblock things” regarding AMD drivers, and it’s nice to see those efforts finally bearing fruit on AMD’s side.

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland has been the Senior Gaming Editor at Ars Technica since 2012, writing primarily about the business, tech, and culture behind video games. He has journalism and computer science degrees from University of Maryland. He once 
wrote a whole book about 
Minesweeper
.
 

1. 1.Amazon stuck with months of repairs after drone strikes on data centers
2. 2.Toyota built a $10 billion private utopia—what’s going on in there?
3. 3.Musk’s “World War III” threat in Twitter lawsuit haunts him at OpenAI trial
4. 4.Man dies covered in necrotic lesions after amoebas eat him alive
5. 5.Infrasound waves stop kitchen fires, but can they replace sprinklers?

Customize