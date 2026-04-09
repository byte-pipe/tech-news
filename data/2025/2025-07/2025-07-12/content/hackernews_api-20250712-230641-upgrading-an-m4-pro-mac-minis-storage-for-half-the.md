---
title: Upgrading an M4 Pro Mac mini's storage for half the price | Jeff Geerling
url: https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price
site_name: hackernews_api
fetched_at: '2025-07-12T23:06:41.612305'
original_url: https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price
author: speckx
date: '2025-07-11'
description: Upgrading an M4 Pro Mac mini's storage for half the price
tags:
- hackernews
- trending
---

# Upgrading an M4 Pro Mac mini's storage for half the price

A few months ago, Iupgraded my M4 Mac mini from 1 to 2 TB of internal storage, using a then-$269 DIY upgrade kit from ExpandMacMini.

At the time, there was no option for upgrading the M4 Pro Mac mini, despite italsousing auser-replaceable, socketed storage drive.

But the folks atM4-SSDreached out and asked if I'd be willing to test out one of their new M4 Pro upgrades, in this case, upgrading the mini I use at the studio for editing from a stock 512 GB SSD to4 TB.

I said yes, and here we are!

I documented the entire upgrade—along with taking my old M4 mini 1TB SSD and putting it in myDad'sM4 mini—in today's video:

But please continue reading, if you prefer text over video, like I do :)

Theupgrade processitself is straightforward (if you've ever worked on laptop hardware before, at least), though removing the rear plastic cover (which also has the power button attached) is a bit annoying.

There are four metal pegs that are retained in clips in the bottom metal cover, and you have to slide a thin piece of metal / pry tool into the very minimal gap between the plastic bottom cover and the aluminum case, then pry it up. And if you're not careful on that step, you'll not only scratch the aluminum (and maybe crack the plastic bottom), but there's a good chance you rip the fragile (and tiny) power button connector too!

Besides that, it's a matter of removing a number of small torx screws; all the bits I needed were present in the cheapest iFixit assortment I have at my desk.

The only substantial difference between the M4 and M4 Pro mini SSD is the size and relative location—the M4 Pro has a much longer slot, a little more than a standard 2242-size NVMe SSD, while the M4 has a shorter slot, closer to a 2230.

## DFU Restore

Speaking of standards... youhaveto do a full DFU (Device Firmware Update) restore, because unlike conventional M.2 NVMe storage, the M4 uses a proprietary connector, a proprietary-sized slot, and splits up the typical layout—the card that's user-replaceable is actually just flash chips and supporting power circuits, while the storage controller (the NVMe 'brains') is part of the M4 SoC (System on a Chip). Apple could use standard NVMe slots, but they seem to think the controller being part of the SoC brings better security... it certainly doesn't bring any cost savings, resiliency in terms of quick recovery from failure in the field, or performance advantage!

Since DFU restore is necessary, in my earlier video, I suggested you need an Apple Silicon mac (M1 or later) as the other computer.

But I was corrected by my viewers, who mentioned you can use many Intel Macs as well—I believe as long as a T2 chip is present, you're good to go. Just connect to themiddleThunderbolt port on the rear of the Mac mini, then press and hold the power button while plugging it into AC power. The other Mac should pop up an 'Allow this device to connect?' dialog and then you can proceed to theDFU processfrom there.

As far as I'm aware, no Hackintosh or other computer can be made to do a DFU restore.

I've done three upgrades (two on M4 minis, one on an M4 Pro mini), and all three were easy. The second one, I thought I had an issue, but it was just a confirmation dialog that wound upbehindthe active window.

## Performance

I decided to also use an external Thunderbolt 5 NVMe enclosure from M4-SSD along with my (rather expensive) 8TB Sabrent Rocket Q SSD, and do a performance comparison.

See the video at the beginning of this post for some more detail (like all the numbers fromAmorphousDiskMarkandBlackmagic Disk Speed Test), but here are the raw numbers for large file copy performance:

The upgraded 4TB module performed noticeably better in writes, likely because it has more flash chips on it to spread out the write activity. Reads were pretty close to the same, with minor variance in performance across different file sizes and access patterns.

The external TB5 drive was the laggard, but is still ridiculously fast (by my standards, editing 4K video). And it would likely be faster if I used a good PCIe Gen 4x4 drive (the Rocket Q is Gen 3x4).

But the internal storage on these Mac minis is very fast, and even better, veryconsistentlyfast. The external Thunderbolt drive would slow down briefly every minute or so, after 100+ GB were copied—and I verified both withsmartctlandmy thermal camerathat the drive was not overheating.

This is likely due to the internal DRAM cache on the NVMe SSD not being able to keep up with the high transfer speeds over long periods of time.

## Conclusion

I was provided the$699 M4 Pro 4TB SSD upgradeby M4-SSD. It's quite expensive (especially compared tonormal4TB NVMe SSDs, which range from $200-400)...

But it's not nearly as expensive as Apple's own offering, which at the time of this writing is$1,200!

## Further reading

* Don't pay $800 for Apple's 2TB SSD upgrade
* Qualcomm Snapdragon Dev Kit for Windows Teardown (2024)
* Mini NASes marry NVMe to Intel's efficient chip

m4

mac

mini

mac mini

youtube

video

upgrade

ssd

* Add new comment


## Comments

Hi Jeff,Actually, any computer running macOS with USB-C ports (including a Hackintosh) should be able to be the host computer performing a DFU mode restore on another Mac (with Apple Silicon, or with a T2 controller).

When you put one of those Mac computers into DFU mode, it effectively is functioning as a USB device (i.e., “USB gadget mode” on Linux). The host computer performing the restore merely needs to be able to connect to it physically, speak USB, and run the Apple Configurator software.

Don’t quote me on this, but it PROBABLY would also work just fine with a standard USB-A to USB-C cable like you’d use for an external hard drive. Just plug the C port into the DFU port on the restore target, and the A port into the host. You probably can even do it over just USB 2.0, but I don’t want to imagine how long that would take!

* Reply

Interesting; I've heard from a couple people a Hackintosh will work too. That's good to hear! Just wish you could do it from something like a Raspberry Pi... or any PC.

* Reply

Hi, there's idevicerestore which allows you to DFU restore from Linux. Don't even need a Mac.

* Reply

This looks to be the project in question:https://libimobiledevice.org

Seems pretty useful. :)

* Reply

Are there currently any commercially available SSD replacements for the M2 Mac studio? Seems there was an option, but no longer available?

* Reply

Not sure if there is a delay on posting comments or my earlier comment didn't save, but I answered my own question about Smart Control. I see now it is Smartctrl which is part of the smartmontools package available athttps://www.smartmontools.org/

* Reply

Easiest to install via homebrew :)

* Reply

> if you prefer text over video, like I do :)

Love this :)

* Reply
