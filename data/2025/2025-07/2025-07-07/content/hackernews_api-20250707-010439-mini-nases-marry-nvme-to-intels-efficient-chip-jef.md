---
title: Mini NASes marry NVMe to Intel's efficient chip | Jeff Geerling
url: https://www.jeffgeerling.com/blog/2025/mini-nases-marry-nvme-intels-efficient-chip
site_name: hackernews_api
fetched_at: '2025-07-07T01:04:39.275600'
original_url: https://www.jeffgeerling.com/blog/2025/mini-nases-marry-nvme-intels-efficient-chip
author: ingve
date: '2025-07-05'
description: Mini NASes marry NVMe to Intel's efficient chip
tags:
- hackernews
- trending
---

# Mini NASes marry NVMe to Intel's efficient chip

I'm in the process of rebuilding my homelab from the ground up, moving from a 24U full-size 4-post rack to amini rack.

One of the most difficult devices to downsize (especiallyeconomically) is a NAS. But as my needs have changed, I'm bucking the trend of alldatahoardersand I needlessstorage than the 120 TB (80 TB usable) I currently have.

It turns out, when you stop running an entire YouTube channel in your home (I'm in a studio now), you don't need more than a few terabytes, so my new conservative estimate is6terabytes of usable space. That's within the realm of NVMe SSD storage for a few hundred bucks, so that's my new target.

Three new mini NASes were released over the past year that are great candidates, and I have relationships with all three companies making them, so I am lucky to have been offered review units of each:

* GMKtec G9
* Aiffro K100
* Beelink ME mini

I've compiledallmy experience with the three NASes into one concise YouTube video, which I've embedded below:

However, I thought I'd at least give a few notes here for those interested in reading, not watching.

Generally, all three mini NASes use an Intel N100/N150 chip, and divvy up its 9 PCIe Gen 3 lanes into 4 (or in the Beelink's case, 6) M.2 NVMe SSD slots. They all have 2.5 Gbps networking, though the GMKtec and Beelink havedual2.5 Gbps NICs.

The difference is in the execution, and each box has one or two minor issues that keep me from giving a whole-hearted recommendation. When you're dealing with tiny devices, there'salwaysa compromise. So you have to see which compromises you're most willing to deal with. (Or just buy a full size NAS if you have the space/power for it.)

## GMKtec G9

I previously reviewed this NAS in April; see my blog postThe (almost) perfect mini NAS for my mini rack.

That 'almost' is doing a lot of heavy lifting, though; there were inherent cooling issues if you ran the box with four NVMe drives, and it was bad enough GMKtec went through a design revision.

Their newer version of the G9 has a much larger cooling vent on the side, and I believe they may have tweaked some other aspects of the design. I'm not sure how it ends up, though, so I'll have to post an updated review if I can get my hands on one of these updated models.

## Aiffro K100

The K100 is even smaller than the G9, and it keeps things cool much better, likely owing to much more ventilation on the sides, a heatsink that covers VRMs (Voltage Regulation Modules) and some of the other hot chips, and a full metal enclosure.

The major downside is despite costing $299 (over $100 more than the G9's base spec), it drops eMMC (so you have to install an OS on one of the 4 NVMe SSDs, or on an external USB stick), and drops WiFi (this is wired only—and a single 2.5 Gbps port versus 2 on the other two mini NASes.

The BIOS is also very light on customization, only really allowing tweaking the power restore behavior and performance profile.

But it's very quiet (less than 37 dBa under load), absolutely tiny, and uses the least power of all the Intel mini NASes I tested.

## Beelink ME mini

Speaking of quiet, the ME mini is even more quiet. It's notsilent, but the larger fan and 'chimney' heatsink design (reminiscent of Apple's Trash Can Mac) mean it can keep from throttling even in 'performance' mode indefinitely—and barely scratch 35 dBa while doing so.

It has not 4 but6NVMe slots, though 5 of those slots are PCIe Gen 3 x1 (one lane of bandwidth is 8 GT/sec), and the last slot is x2 (two lanes).

If you order one with a Crucial SSD pre-installed, it will be installed in that last x2 slot for maximum performance—and the test unit I was shipped came with Windows 11 preinstalled.

But it has built-in eMMC (64 GB), and I installed Ubuntu on that for my testing. Another nice feature is a built-in power supply, which is quite rare on these mini PCs. Often you buy the thing based on the size of the mini PC, then hanging out back, there's a DC power supply the same size as the mini PC!

Not here, it's got a small power supply tucked inside one part of the heatsink, though I'm not sure how much thermal transfer there is between the heatsink and the power supply. I didn't encounter any overheating issues, though, and even with the preinstalled Crucial SSD only touching the thermal pad where the NVMe controller chip sits (there was an air gap between the thermal pad and all the flash storage chips), I didn't have any concerns over thermals.

It did run a little hotter overall than the K100, but it was also in full performance/turbo boost mode, whereas the K100 comes from the factory with a more balanced power profile.

## Conclusion

The G9 is definitely the winner in terms of price, but the cooling tradeoffs at least with the initial revision I reviewed were not worth it, because it would lock up and reboot if it overheated. The ME mini is currently $209 (starting) on pre-sale, but that price could go up:

All three NASes would perform fine for my homelab needs, giving at least around 250 MB/sec of read/write performance, though the Beelink seems to suffer a little splitting out all those NVMe slots with x1 bandwidth:

And as I mentioned earlier, the K100 was definitely the most efficient, partly due to it shipping with a balanced power profile instead of 'performance', and also by the fact it ditches features like WiFi and eMMC which eat up a little more power:

In the end, there's no clear winner for all cases. The GMKtec is the budget option, and supposedly they have a new thermal design that should solve the stability issues I was encountering. The K100 is tiny, uses the least energy, and runs the coolest... but is also the most expensive, and has no built-in eMMC. The Beelink is the most expandable, and is currently cheaper than the K100, but that's a pre-sale price. And the extra drive slots means each drive only taps into one lane of bandwidth instead oftwo.

So if you're in the market for a tiny homelab storage server, pick one based on your own requirements.

For me, I'm leaning towards the K100, but only if I can find a good deal on 4 TB NVMe SSDs, because I need at least 6 TB of usable space in a RAIDZ1 array.

## Further reading

* The (almost) perfect mini NAS for my mini rack
* The Rock 5 B is not a Raspberry Pi killer—yet
* Building a fast all-SSD NAS (on a budget)

homelab

mini rack

nas

linux

video

youtube

storage

reviews

beelink

aiffro

gmktec

* Add new comment


## Comments

I feel for you, must feel awful downgrade like that. Not sure I could live without my movie collection, has helped so many times when internet went out in my life. 4k movies take up alot of space. Thing i'd also miss my 10gb fiber network, and my ability to put home assistant in a VM on my freebsd zfs machine.

* Reply

having no movies to watch if the internet isn't working??how can we possibly survive that?!?

* Reply

My book library fits in ~1GB, and reads fine over 1gb ethernet.

* Reply

Hi Jeff

As always brilliant and definitely an unbiased conversation. But am a bit confused as to why you stuck to intel only products, after all there are many arm boards which could have entered the fight, specifically the cm3588 Nas board from friendly elec. Be interesting to know why that didn't make the cut in this debate.

* Reply

I've been working on full mini PCs lately; the CM3588 is interesting and I hope to test it as well at some point. It would probably be competitive in most aspects to these machines, though I'd like a nice enclosure too.

* Reply

What about a Mac Mini M-series and some (if such a thing exists) board purely for installing M.2 NVMe drives (say 4 or 6) and those two things connected via Thunderbolt 3/4/5?

That way you get the low idle power of Apple's silicon, and the speed from Thunderbolt to the NVMe drives. You're stuck on macOS until/if Thunderbolt drivers for Apple silicon land in Asahi Linux but this setup (if feasible) feels like it could be good no?

* Reply

As a windows desktop user, I desperately want apple to make an apple silicon server that can run linux and has a bunch of pcie slots to be used for NVMes, I would buy the absolute crap out of that. Right now the best case scenario is something like what you suggested with a thunderbolt -> PCIe 3x4 splitter to 4 PCIe 3x1 NVMes, which could mean a reasonably straightforward max capacity of 12 drives via just thunderbolt, which would be incredible.

Honestly I feel like this is one of those situations where it's really frustrating how little competition there is in power efficient high performance ARM silicon. Apple clearly doesn't care about the homelab server market, but their hardware is so much better than everyone else that it's just insanely attractive if you want something that you know will never struggle with anything you throw at it... but actually getting something functional requires you to run MacOS which sucks.

(I am very frustrated by the current state of events if you can't tell)

* Reply

Hooking up external storage feels like just asking for data corruption. Perhaps less so on a desktop like the Mac Mini but does Apple not sleep the Thunderbolt ports? Like what if you aren’t actively using the drive and the port sleeps and unmounts? You’d be forced into continuous unplugging/replugging of the drives.

* Reply

Is the Beelink ME mini *still* on pre-sale? I heard about it for a while.

* Reply

What about a Mac Mini M-series and some (if such a thing exists) board purely for installing M.2 NVMe drives (say 4 or 6) and those two things connected via Thunderbolt 3/4/5?

That way you get the low idle power of Apple's silicon, and the speed from Thunderbolt to the NVMe drives. You're stuck on macOS until/if Thunderbolt drivers for Apple silicon land in Asahi Linux but this setup (if feasible) feels like it could be good no?

* Reply

Hi Jeff, I may have a solution for the K100 boot issue. Back in the heady days of mdraid under Linux I would carve off a small boot partition on each of the RAID drives. With the BIOS set to boot off more than one I would still be able to recover from a first drive failure. A cron job for rsync made sure that the shadow boot partitions remained patched. Sure, you give up a small portion of your usable RAID space, but with Ubuntu being able to fit in 10GB, that isn't much out of a 6TB volume. Certainly less than the marketing departments of drive vendors take by using TB instead of TiB ;-)

P.S. I added this same comment to your YT but I can't see it on other clients so I reposted it here

* Reply

Do any of these (particularly the me mini) support in-band ecc? I know it’s possible with n100/n150 and other similar chips, it’s just rarely enabled and implemented in the bios.

* Reply
