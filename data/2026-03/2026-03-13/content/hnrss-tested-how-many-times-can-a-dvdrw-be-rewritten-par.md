---
title: 'Tested: How Many Times Can a DVD±RW Be Rewritten? – Part 2: Methodology & Results | Gough''s Tech Zone'
url: https://goughlui.com/2026/03/07/tested-how-many-times-can-a-dvd%C2%B1rw-be-rewritten-part-2-methodology-results/
site_name: hnrss
content_file: hnrss-tested-how-many-times-can-a-dvdrw-be-rewritten-par
fetched_at: '2026-03-13T03:13:05.374820'
original_url: https://goughlui.com/2026/03/07/tested-how-many-times-can-a-dvd%C2%B1rw-be-rewritten-part-2-methodology-results/
date: '2026-03-08'
published_date: '2026-03-07T07:52:23+00:00'
description: 'Tested: How Many Times Can a DVD±RW Be Rewritten? Methodology and Results'
tags:
- hackernews
- hnrss
---

# Tested: How Many Times Can a DVD±RW Be Rewritten? – Part 2: Methodology & Results

Posted on

March 7, 2026

by

lui_gough

Now that we’vecovered the contenders for this test, I will cover how this test will be performed and go through the results. It was a long time for me, but for you, it’ll just be a few hours between posts …

## Methodology & Limitations

It might sound simple to experimentally determine how many times a DVD±RW can be rewritten – simply write the disc and read the disc until it fails, but this ignores a few nuances, more specifically, how can it feasibly be done and what do the results even mean.

For this test, rather than write my own software to try to write, read and quality scan a disc, I opted to stick to usingOpti Drive Control. Using the software, a test disc can be written and verified, the transfer rate can be checked and quality scans can be performed. The write-verify cycle ensures the disc is at least readable, while transfer rate tests allow for “weaknesses” in the recording quality to be identified based on their impact on the transfer rate. Finally, the quality scan feature allows for the drive to report correctable errors and jitter levels to be able to identify degradation in recording quality before it impacts on the readability of the disc.

But I wasn’t going to have enough lifetime to sit there, click buttons, burn after burn. After all, a 2x burn takes about 30 minutes, and if the disc can survive 1000 cycles – that’d be almost 21 days of burning time alone. A 4x CLV quality scan (my favoured scan rate) takes 15 minutes too, while a TRT and verify added together may take around the same amount of time, assuming the disc is good. So this is abig time investmentthat demands automation.

To do this, I decided to write my own script usingpyautogui. This Python library allows for automating clicks and keystrokes, so I wrote a script that would detect elements on the screen to deduce what was happening and click the appropriate buttons, taking screenshots at the right time so as to capture the results. The script wasreallyflaky at first, in part because I was running on a very old spare computer that was slow to draw the graphs resulting in “broken” screenshots. Furthermore, it seems the theming and styling of Windows is important too, as later versions of Windows may highlight boxes on hover-over, resulting in failed exact-matches for screen snippets. After debugging with a few delays, trying different variants of buttons and building in error-recovery (i.e. sometimes flaky discs just need a “refresh” nudge), I had something ready to unleash on test sample discs.

This leaves the question of which drive I should use for the test. It didn’t take me long, but that old computer I was donated had a practically unused, retail Lite-On iHAS120 6 in it which was a great candidate for testing. This drive supported error scanning with jitter, making it a key asset and quickly became one of my favouriteseven before I bought a duplicator filled with its cousins. Even better, I had two extra drives of the same model in the collection, so if it should fail, I could carry on the experiments with the spares.

The script would use ODC to write a test disc, verify the test disc, run a TRT on the test disc and then a quality scan. It would loop around over and over until the script timed out on an unrecoverable error condition or I stopped it as it exceeded expectations or had previously had a verification error but was not bad enough to cause the script to fail issuing further rewrites. Specifically, the disc wasnotunloaded and reloaded between attempts to save wear and tear on the tray mechanism and reduce noise.

Soon, an issue was discovered due to the slow nature of the media meant that it would take close to a whole year to complete testing, so I employed a second iHAS120 6 in parallel – this one in aUSB 2.0 enclosureconnected to amini-PC. This ran Windows 11, and was both faster and more power efficient. The script needed to be modified for this, but it allowed for improved test throughput.

One downside of Windows 11 is its propensity to download and automatically install updates, which caused a few interruptions to testing. Eventually, I killed the requisite services and firewalled the machine from the internet entirely, to stem the automatic updates.

With a pile of screenshot files, I usedOpenCVto detect the contours around the window, crop out each screenshot and use template matching to determine the type of screenshot. It was also used for template matching to determine the first point of failure.PillowandNumPywas used for image manipulation, including adding a run counter, resaving the image and exporting the sequences as video files which were then re-encoded usingHandbrake. This was the only data-efficient way to represent all of the images without creating an inode exposion, or very very large animated GIF/PNG file.

The key limitations of the experiment, as proposed, are as follows:

* Quality scanning on rewritable discs works, however, it was previously established that some discs return very poor error scan values but remain readable and vice-versa, so it is not definitive regarding the readability status of a disc as there may be impairments that affect a quality scan but which are compensated on a read-out. This is why we also use transfer-rate test and verification of the data to ensure it is readable. The criterion for disc failure is set as thefirst verification run that fails due to an error.
* The resulting cycle life result is valid only for the combination of burner and disc tested – the iHAS120 6 used in the test may be better with some media than others. Furthermore, testing of a single sample does mean that we don’t have visibility on whether the result is consistent for discs of that type or for just that sample. This is unfortunately, a limitation borne of having limited resources in terms of time, energy and recorders that can do everything.
* When rewriting DVD+RW media, a direct overwrite takes place. But rewriting DVD-RW media, it seems ODC runs a full erase on the disc first, before writing. This means that, technically speaking, the DVD-RW discs have done twice the cycles than actually counted (as the full erase is a full write, but not one we made use of). In theory, a restricted overwrite operation on DVD-RW should avoid this, but as ODC does not seem to perform this (and I didn’t bother trying to add additional code to invoke a quick erase first), this behaviour was tolerated even though it increased test length as well.
* The cycle life number may be off by up to three counts in the worst case – this is due to the machines having restarted mid-test resulting in one write being discarded. But this is small compared to the number of cycles envisaged, so is considered “within error margins”.

In all, this was an absoluteepicexperiment that took over half-a-year to run … and then sat around waiting for me to have the time to compile the data in a presentable way.

## Results

Let’s start by looking at each disc type in turn.

### Memorex 8x DVD+RW

I had high hopes for this RITEK-008-000, but alas, perhaps it’s just not a good fit for the drive or the media itself might have quietly gone bad in some way.



While the drive did a Z-CLV 8x burn initially, every subsequent burn was stuck at 6x CLV. It’s as if the drive knew something was not right so refused to go faster. When the system was rebooted because of inevitable Windows Update shenanigans or power outages, we would get a single 8x burn again … but that’s about it.



The smooth readback curves are … a little deceptive.



The first two writes out of the bat are just not good looking. Below are videos running at 5fps that show the results run-after-run. The first failure to verify occurred at just 106 runs.

https://goughlui.com/wp-content/uploads/2026/03/rit08-cr-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/rit08-trt-h264.mp4

The transfer rate test curve gets lumpy and then eventually errors start cropping up around the time verify failure first occurs.

https://goughlui.com/wp-content/uploads/2026/03/rit08-vf-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/rit08-qs-h264.mp4

Quality-wise, the values jump around unpredictably and a spike near 0.5GB might just be characteristic of this particular series of Lite-On drive’s firmware. The lower speed does improve the burn, but PIE-wise it’s a fail all-round and PIFs is mostly fail too with a few burns being perhaps marginal.

### Sony 6x DVD-RW

As I was most interested in the faster discs, I tried these discs first, but surprisingly they fell short of my expectations. As a result, I tested two samples of this – here are some screenshots from the second sample.

A Z-CLV write is achieved at 6x – not CLV even though the drive manages 6x CLV on DVD+RW media. A write in around 10 minutes is noticeably faster than the 15 minutes a 4x burn takes. But the drive does “flicker” and decide to go 4x CLV in later runs.

Smooth reads …

… but all is not well with this quality scan. It’s hit the limit for PIEs and it’s only the first burn. Jitter is a bit high but PIFs are good. Perhaps rewriting faster than 4x is really pushing the phase change medium?

Videos of the full tests of each sample follow.

#### Sample 1

https://goughlui.com/wp-content/uploads/2026/03/sony6a-cr-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/sony6a-trt-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/sony6a-vf-h264.mp4

This sample managed 204 cycles until its first verify failure.

https://goughlui.com/wp-content/uploads/2026/03/sony6a-qs-h264.mp4

For this sample, the disc did well initially but errors started to climb consistently to the point of really being in danger by 50 cycles or so. There are a few error dialogs, as this was an earlier test and I hadn’t quite perfected my script, which is another reason why I opted to test a second … but this drive seems to do so much better in terms of error rates and jitter at 4x than it does at 6x writing.

#### Sample 2

https://goughlui.com/wp-content/uploads/2026/03/sony6b-cr-h264.mp4

I didn’t change anything but get a new sample of the disc and this one seems marginally more willing to burn at 6x rather than 4x. There is still many occasions where it falls back.

https://goughlui.com/wp-content/uploads/2026/03/sony6b-trt-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/sony6b-vf-h264.mp4

This disc managed to make 223 cycles before its first failure, a similar result to the previous sample.

https://goughlui.com/wp-content/uploads/2026/03/sony6b-qs-h264.mp4

By about 40 runs, the error rates had crept up into danger territory, but it seems that we get bursts of better results whenever the drive falls back to 4x. Nevertheless, this is not a very “stable” rewriting characteristic and the jitter level is high, suggesting it’s not writing with a good strategy.

### Victor JVC 6x DVD-RW

Can you tell the difference with a Japanese-made disc? Well, yes, actually. This one consistently achieved 6x writes …

… the first write looked quite good …

… and even though it’s clear the faster writing at 6x did result in lower quality and higher jitter, the PIEs are acceptable, the PIFs are very good and the jitter level is not too bad either. Will it last in the long-run?

https://goughlui.com/wp-content/uploads/2026/03/jvcvd7-cr-h264.mp4

Write-after-write … 6x … no problem!

https://goughlui.com/wp-content/uploads/2026/03/jvcvd7-trt-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/jvcvd7-vf-h264.mp4

Compared to the two Riteks above, this one certainly exceeded my expectation. The first verify failure occurred at run 639. It’s not quite 1000 rewrites in the sense of rewrites of useful data, but if we consider the full-erase between writes, then thisexceedsthe claimed 1000 cycles.

https://goughlui.com/wp-content/uploads/2026/03/jvcvd7-qs-h264.mp4

This disc seems to exhibit a phenomenon where the error rates decrease after the first few writes, sometimes attributed to some annealing. Unfortunately, after the first 130 or so cycles, the error rates swing wildly from burn to burn – perhaps indicating a change in characteristic where the calibration chooses a power that is sometimes “hit” and sometimes “miss”. As expected, the jitter value increases somewhat as the disc ages, as claimed by thePioneer white-paperabout DVD-RW. The spike around 0.5GB shows up late in the discs’ life at the Z-CLV transition point.

This suggests to me that this is a good quality exemplar of what is possible and to be expected as a disc is being worn-down by rewrites.

### TDK 4x DVD+RW (Version 1)

Rather than go through screenshots for the slower varieties of discs, I’ll present just the video time sequences and short commentary.

https://goughlui.com/wp-content/uploads/2026/03/rjpnw11-cr-h264.mp4

Nothing special here – 4x burns are fairly event-free. The drive just chugs away … it’s not like it’s going to fall-back to 2.4x … I’ve never seen it happen.

https://goughlui.com/wp-content/uploads/2026/03/rjpnw11-trt-h264.mp4

There are some wiggles towards the outer, suggesting this disc was never perfectly healthy to begin with. These get significantly worse as we exceed 330 cycles when the first big dips near the outer start to show.

https://goughlui.com/wp-content/uploads/2026/03/rjpnw11-vf-h264.mp4

The disc managed 413 cycles until its first verify error. This is not quite 1000, but is more than I had initially imagined.

https://goughlui.com/wp-content/uploads/2026/03/rjpnw11-qs-h264.mp4

The quality scan graph confirms that the disc isn’t doing well towards the outer, but this behaviour remains relatively stable. As the wear begins, the inner diameter sees random spikes and surges in error rate – I wonder if this is because the drive simply doesn’t choose the right power as its running OPC against “worn” areas or whether the recording layer laser power margin is shrinking meaning the same calibration errors result in bigger influences in the burn.

The failure of this disc was actually visible in some way – there were dark speckles on the recording layer itself. Perhaps these were impurities or pin-prick holes in the reflective layer. Usually they might cause more of a disturbance, but this disc still did well given the degraded state it was in at test conclusion. The fact that the jitter remained low throughout the discs’ life suggests to me that the recording layer may have had more to offer, had it not been plagued by this “disc rot”.

### TDK 4x DVD+RW (Version 2)

https://goughlui.com/wp-content/uploads/2026/03/p041-cr-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/p041-trt-h264.mp4

For a disc type that I’ve previously used and considered not so good, it starts off strong. It’s not until about 190 writes that the outer edge starts to show signs of giving up.

https://goughlui.com/wp-content/uploads/2026/03/p041-vf-h264.mp4

The first verify error occurred at 218 cycles, far from 1000 cycles but it also means that the ailing RICOHJPN-W11 managed to go almost twice as far.

https://goughlui.com/wp-content/uploads/2026/03/p041-qs-h264.mp4

The quality scan suggests very average burn quality on the PIEs, turning to bad by about 80 cycles. PIFs are elevated all round and jitter is a bit variable. Outer diameter failure is clear by about 120 cycles in quality scans and becomes the dominant feature as the runs progress with jitter increasing.

### TDK 4x DVD+RW (Version 3)

https://goughlui.com/wp-content/uploads/2026/03/cmcw02-cr-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/cmcw02-trt-h264.mp4

A spot near the outer edge causes tiny dips that are visible already around 180 cycles in, but this becomes a severe issue as we get into the 800 cycle territory.

https://goughlui.com/wp-content/uploads/2026/03/cmcw02-vf-h264.mp4

This disc managed an impressive 850 cycles to the first verify error. Not bad at all.

https://goughlui.com/wp-content/uploads/2026/03/cmcw02-qs-h264.mp4

Burn quality takes a few burns to settle down to an acceptable PIE but marginal PIF. Outer edge issues are apparent from the start, suggesting this may be the result of ageing, storage or degradation by light or atmosphere. The recording of the bulk of the disc remains stable into the early 400 cycles, but towards the mid-late 400s, the drive and media work to cause a “wave” of error that grows and shrinks, perhaps a consequence of direct overwrite interactions with the previous recording. So this explains why a rewritable disc can have a bad burn, then be followed by a good few burns, then suddenly go bad again.

### Verbatim 4x DVD+RW

https://goughlui.com/wp-content/uploads/2026/03/mkma02a-cr-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/mkma02a-trt-h264.mp4

There are little dips in the TRT right from the outset indicating the burn is a difficult one. By about 60 cycles, the outer starts to waver … then everything goes to crap.

https://goughlui.com/wp-content/uploads/2026/03/mkma02a-vf-h264.mp4

You’d expect a lot from Verbatim … but we only got 96 cycles until the first verify error. As it is a major media brand, the expectation is that it’d be quite compatible, so blaming on the drive seems a bit unlikely. Could this have somehow degraded?

https://goughlui.com/wp-content/uploads/2026/03/mkma02a-qs-h264.mp4

High jitter and a sea of reds … the burn is practically never acceptable …

### BONUS: DC Erase – Can It Revive a Rewritable?

As an owner of the Nu Tech DDW-082, I can definitely say that it was not a particularly good burner in any regard. Flaky firmware, questionable burn quality and compatibility. I regretted the purchase.

But one thing it could do, that no other drive I had could, was a function called DC Erase that was said to revive rewritable discs. This function was said to restore the “bright” surface that you would see from a brand-new virgin rewritable disc. To do this, you’d have to useDVDInfoProto access the functionality.

The Verbatim disc didn’t do well out-of-the-box so I decided to give it a try to see if such a thing would even work …




… so the disc was DC erased and short of a few hairline sections, the disc did have a bright surface.

While all other drives to my knowledge do not have a DC Erase function that is user-accessible, all drives areableto do DC Erase as this is required for the Power Calibration Area prior to calibration:



So the drives are doing it internally for some areas, but generally, this is a function not available otherwise. The reasoning, as far as I have heard, is that this sort of erase wears out the disc more than writing a valid sequence of digital “zeroes” to the surface, but in this case, it seems to have revived the disc for a little longer.

But given the DDW-082’s limited compatibility with slower (4x) media only, I didn’t decide to test this feature out any further.

https://goughlui.com/wp-content/uploads/2026/03/mkma02b-cr-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/mkma02b-trt-h264.mp4

It did return the disc to a passing state for a bit, but the curve still jitters indicating bad burns.

https://goughlui.com/wp-content/uploads/2026/03/mkma02b-vf-h264.mp4

The disc failed at 103 cycles, so it’s within spitting distance of the first test,but not because of a verify error. Instead, it failed because it produced consistent write errors.

https://goughlui.com/wp-content/uploads/2026/03/mkma02b-qs-h264.mp4

The curves are similarly covered in red, although the spikes in jitter seem to be getting worse and haven’t been helped. This suggests there may have been some actual damage to the disc (e.g. scratching on the surface by the pick-up head, or internally to the structures needed for tracking).

### TDK 4x DVD-RW

https://goughlui.com/wp-content/uploads/2026/03/cmcw03-cr-h264.mp4
https://goughlui.com/wp-content/uploads/2026/03/cmcw03-trt-h264.mp4

Around 190 cycles, the disc seems to show a case of outer-edge dips, which gets worse and worse. It seems that outer edge is “lethal” – it’s where the recording layer gets closest to the atmosphere but also light impinging from the side of the disc (e.g. while it’s in its case). Aside from the common cause of physical damage which is not relevant in this test, that’s why you probably shouldn’t expect to fill your discs to the brim and have the outer be just as readable as the inner.

https://goughlui.com/wp-content/uploads/2026/03/cmcw03-vf-h264.mp4

This disc managed 237 cycles before a verify failure, and being a “dash” format disc, if you consider the full erase a cycle, you can double this figure.

https://goughlui.com/wp-content/uploads/2026/03/cmcw03-qs-h264.mp4

Write quality was quite good, PIE wise and marginal on PIF. Jitter is not bad. By about 133 cycles, the outer edge starts taking a dominant role, modulating the error graph while the majority of the burn still seems okay. The inner edge starts to follow and the jitter trend clearly reflects this. So I wonder what’s so problematic about the inner and outer edges – could it be that spin-coating is used and those being the “boundary” points result in film thickness unevenness (a form of edge beading) that makes it more susceptible to recording quality drift?

While nothing was too apparent visually, there was this odd spot where it almost looked like the layer was “pinched” … an uneven spot. As it was in the bulk of the disc and not at the edges, the influence it had on error rates seems rather limited.

### TDK 2x DVD-RW

https://goughlui.com/wp-content/uploads/2026/03/tdkm3-cr-h264.mp4

Writing at 2x feels so slooooooooowwwwww …. I could barely contain my excitement at having to leave this for a month or two ….

https://goughlui.com/wp-content/uploads/2026/03/tdkm3-trt-h264.mp4

Already, from early on, there are a few “blips”, some getting bigger by about 80 runs in. But the disc manages to hang in there despite the blips and dips getting bigger and more severe, by about 180 cycles. The shakiness extends to the whole disc by about 240 cycles, but it refuses to give up.

https://goughlui.com/wp-content/uploads/2026/03/tdkm3-vf-h264.mp4

In fact, I chose to terminate the test at 1008 cycles –no verification failure occurred in over 1000 cycles. Being a dash format, if you consider a full erase as a cycle, this means over 2000 cycles …

https://goughlui.com/wp-content/uploads/2026/03/tdkm3-qs-h264.mp4

Burn quality looked quite good initially but then started to bounce around unpredictably, starting to exceed limits by about 70ish cycles. The phenomenon of “good burn, bad burn” back-to-back seems to rear its head and the jitter seems to creep up as well. The case of this disc managing to survive so long is both a miracle, but also perhaps quite a bit pf luck that in spite of its quite horrific results even at about 370 cycles in, that the drive did not give up trying to read back the data.

### Maxell 2x DVD-RW

https://goughlui.com/wp-content/uploads/2026/03/mxl2x-cr-h264.mp4

Another slow disc … but I’m patient … so let’s go.

https://goughlui.com/wp-content/uploads/2026/03/mxl2x-trt-h264.mp4

The TRT tended to show only minor flickers, mainly on the outside edge before the disc failed to verify.

https://goughlui.com/wp-content/uploads/2026/03/mxl2x-vf-h264.mp4

This one managed 327 cycles, which is a bit more than the “plus” format high-speed Ritek discs managed.

https://goughlui.com/wp-content/uploads/2026/03/mxl2x-qs-h264.mp4

Butn quality was quite good overall even though jitter was a bit on the high side. Spikes started to develop but quality didn’t get bad until about 130-160 cycles when the error humps started to grow higher and higher.

### Overall Summary

In total, the results are summarised below:

The only disc that achieved a full 1000+ cycles without an error was the TDK 2x DVD-RW (TDK502sakuM3). All other discs failed, mostly due to a read error in verification, with the DC-erased MKM-A02-000 failing with a write error. If we consider that “dash” format discs were erased fully before rewrite, that would be indeed impressive, suggesting the TDK 2x disc completed 2000+ cycles while the JVC Victor managed 1200+ cycles.

On the “plus” side, the CMC MAG-W02-000 got close at 850 cycles, but there were also disappointments. The Verbatim MKM-A02-000 managed just shy of 100 fresh from the box, and achieved about the same after being “revived” with a DC Erase by the Nu Tech DDW-082. Perhaps there was some form of degradation that I could not see visibly. The 8x RITEK-008-000 also managed around 100 cycles and in both cases, it seems the write quality was horrible out-of-the-box. Perhaps the iHAS120 just doesn’t like those discs. The PHILIPS-041-000 failed sooner than the RICOHJPN-W11-001 which matches up with my prior experience.

At least, in this small sample, it would seem that a few of those “plus” format discs did very badly – be it compatibility or age-related causes, resulting in there being an apparent skew towards “dash” format being more durable.

In the past, I heard of rumours that rewriting would damage the ATIP grooves (plus) or pre-pits (dash), or that the embossed area on a DVD-RW would eventually become damaged, but I’m not sure any of that is actually the case. It’s more likely that the material itself may be degrading or incompletely changing between amorphous and crystalline forms, resulting in a lower signal-to-noise ratio. To use an analogy – if you were to use pencil and paper, writing and erasing over and over again, the paper wouldn’t be quite as clean as it was when you started, so the contrast between light and dark would reduce until everything was just sort of “grey”. Perhaps DC Erasing might be able to condition the surface to a more uniform state to help revive the recording layer, but as it shouldn’t be doing anything beyond what normal laser powers would do to the recording layer, I suspect it wouldn’t have much of lasting impact.

That being said, the jitter spikes on the Verbatim MKM-A02 usually indicate something bad is happening to the ability of the pick-up head to track the grooves. I wonder if that is actual damage to the tracking information or some kind of defect not visible to the eye that’s causing the drive some difficulty.

It should be noted that failures were often observed to be transitory – one pass would fail but the following pass would succeed. Eventually, the rates of failure would increase, leading to back-to-back failures. This is the nature of “luck” when you’re on the edge of failure and success – something as simple as random noise or a slightly different write or reading condition could cause it to go one way or the other. But it may also indicate that wear is causing the recording layer to respond inconsistently – if it does so during optimum power calibration, the burner could end up picking a worse-than-ideal write laser power and end up suffering a poorer burn than necessary. This is especially relevant as the drive doesn’t have an active W-OPC strategy, instead seemingly “blindly” writing away after an initial OPC is performed. Either way, it does indicate the erosion of all the available error correction margin – so it’s basically a very fragile recording.

As this test did all writes and reads back-to-back, it doesn’t explore the endurance of the phase change layer after its been heavily exercised. I’ve read some comments (although I can’t recall where) that suggested that phase-change layers that have been cycled a lot may become prone to having their crystalline states turn amorphous more easily or almost spontaneously resulting in a lower data retention lifetime. Whether this is the case is not known and determining this was not one of the aims of this experiment.

### Bonus: Drive Status

After completion of this round of tests (and another I haven’t posted about), my two drives have racked up ….

… 3725 burns, for a total operation time of 2900 hours and …

… a total of 1523 burns for a total of 1120 hours.So that’s about 4020 hours across two drives, 5248 burns and both drives are still seemingly operating just fine.While everything mechanical will wear out over time due to use, these drives even though they are somewhat light-weight and tinny, still seem to be rather strong. As a result, those duplicator drives with 500-or-so writes on them are still perhaps considered rather young! But then again, I’ve had more than a few personal drives of mine do a lot less work and suffer a sudden laser diode failure too … so it’s sometimes luck-of-the-draw.

## Conclusion

While it seems that rewritable discs claim a rewritable lifetime of 1000 writes or sometimes more, in practice even when handling damage to the disc is taken out of the equation, a majority of discs fail to achieve this level of rewrites. Granted, some of the discs are likely old and potentially degraded, but it would seem a couple-of-hundred rewrites is more realistic limit given this combination of Lite-On iHAS120 6 and media. One disc did achieve 1000 cycles – the TDK 2x DVD-RW, but it seemed to be clinging on all the way, aided by the fact the drive just didn’t seem to give up even when the burn quality looked hopeless.

It was nice to see that 8x and 6x recording was achievable, albeit in Z-CLV and not consistently, with the higher speed Ritek discs delivering horrific burn quality in general, but perhaps this is the fault of the iHAS120 to some extent. The JVC is the only “high speed” disc to perform well. As suggested by the Pioneer white paper, increased jitter is observed as the disc reaches exhaustion.

After the exhaustion of one Verbatim disc, I decided to let my Nu-Tech DDW-082’s “fabled” DC Erase function try to revive the disc. To its credit, it did revive the disc which allowed it to achieve a cycle life very similar to the “fresh” result, but albeit the quality was always poor and this didn’t do anything to fix it.

Aside from this, there is also the question of whether cycling would affect the endurance of the recorded data or whether structural damage was being done to the disc itself as a result of multiple overwrites. While I couldn’t answer this definitively based on these tests, I suspect the structure of the disc is still very much intact in most cases and that the increased errors may have been the result of the degradation of the recording layers’ response. The only exception may be the Verbatim MKM-A02 which failed due to write errors and had noticeable spikes in jitter which usually occur when the drive can’t accurately track the spiral groove. As for the cause of the phase change material wear-out and its side-effects on data retention lifetime, I can make no conclusion.

This was a big effort to complete in the end … but it was also fascinating to me. Thebadnews is that this post is now over, but the good news is that this experimentmight not be done yet.Thanks to generous donations from pepst and a few more acquisitions from Japan, I’ve managed to amass even more rewritable discs to test. Rather than just test them once or across a few drives … perhaps they should just undergo torture on one drive to see how well they can handle it. After all, my iHAS120 6’s are still fighting fit and I don’t see anyone else doing this!

## Bonus

My thanks to pepst who contacted me by e-mail to share some knowledge, which I much appreciated.

As for the origin of the discs, TDK DVD+RW 4x (Version 2) was manufactured using a Philips stamper by CMC Magnetics. As for the serial numbers, the serial numbers of +RW discs always start with the letter P, while the numbers of “minus” discs always start with the letter M.

That definitely makes sense … although the “dash” format would very much get angry at being called “minus” … that’s a mistake I make all too often! Perhaps that might mean the stamper or the whole plant was moved over to Taiwan, thus carrying the original IFPI code but being a product of Taiwan.

Then, pepst followed up with even more information …

the situation with Philips’ optical disc laboratory was quite interesting. It was called Optical Research and Development (OM&T) and was responsible for inventing and developing the manufacturing process for advanced optical media—basically, they were behind the development of CD-RW, DVD+RW, DVD+R, and later BD-R and BD-RE formats, when it comes to recordable formats.

The primary task was to develop these formats and later license them to other manufacturers and collect patent royalties. The secondary task was to assist mainly smaller manufacturers with the manufacturing process, which meant supplying stampers and manufacturing know-how. For example, Philips OM&T assisted with the entire production process (except for the production line, which came from other suppliers) for the Belgian manufacturer Sentinel and the Taiwanese producer Nanya Plastics, to which they supplied the stampers and provided extensive assistance with the design of the disc layers and complete process know-how. They also helped several other manufacturers to a greater or lesser extent, e.g. in the early days of Daxon and Infomedia (until they had a complete proprietary production process and their own mastering department for the production of their own stampers), and supplied +RW stampers with Philips MIDs (CMC, MBI) to several other manufacturers.

If I am not mistaken, this department was bought by the Indian company MBI in 2007 or 2008, mainly because of its cutting-edge technological processes for fast BD-R and BD-RE, and it essentially ceased to exist quickly. This was at a time when Philips was selling off almost all of its research and manufacturing divisions.

On the contrary, despite the drastic decline in prices and margins for optical discs at that time, MBI was happily buying up everything it could. In addition to OM&T, they bought all the production lines of the bankrupt manufacturer MAM-E & CSI, the American company Imation, and the Japanese company Maxell, which was relatively nonsensical in the given economic situation and at a time when they were unable to fully use even their existing production capacities.

### Like it? Share it!

* Share on Facebook (Opens in new window)Facebook
* Share on X (Opens in new window)X
* Share on Reddit (Opens in new window)Reddit
* Share on LinkedIn (Opens in new window)LinkedIn
* More
* Share on Tumblr (Opens in new window)Tumblr
* Share on Pinterest (Opens in new window)Pinterest
* Share on WhatsApp (Opens in new window)WhatsApp
* Share on Telegram (Opens in new window)Telegram

### Related

## About lui_gough

I'm a bit of a nut for electronics, computing, photography, radio, satellite and other technical hobbies. Click for more
about me!

View all posts by lui_gough
→


This entry was posted in
Computing
,
Tech Flashback
 and tagged
computer storage
,
destruction
,
endurance
,
failure
,
number crunching
,
optical disc
,
optical discs
,
tested
,
vintage stuff
. Bookmark the
permalink
.

### 2 Responses toTested: How Many Times Can a DVD±RW Be Rewritten? – Part 2: Methodology & Results

1. Ron Dsays:March 12, 2026 at 4:43 pmInteresting… I always assumed they would last indefintely as a kid. Never realized they would eventually degrade similar to NANDReply
2. Miessays:March 12, 2026 at 10:42 pmWhen I was a kid I heard you could only write these so many times. I was super careful and think at most I wrote to a DVD-RW like 5 times to the same disk. Then I got antsy.Reply

### Error: Comment is Missing!Cancel reply
