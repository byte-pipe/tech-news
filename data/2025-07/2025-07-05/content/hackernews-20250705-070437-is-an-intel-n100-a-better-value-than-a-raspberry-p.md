---
title: Is an Intel N100 a better value than a Raspberry Pi? | Jeff Geerling
url: https://www.jeffgeerling.com/blog/2025/intel-n100-better-value-raspberry-pi
site_name: hackernews
fetched_at: '2025-07-05T07:04:37.877198'
original_url: https://www.jeffgeerling.com/blog/2025/intel-n100-better-value-raspberry-pi
author: transpute
date: '2025-07-05'
---

# Is an Intel N100 a better value than a Raspberry Pi?

tl;dr:it depends.

About one year ago, I bought an Intel N100 mini PC (specifically theGMKtec N100 NucBox G3) andcompared it to the Raspberry Pi 5 8GB.

A year later, and we havea newer $159 16GB version of that mini PCwith a slightly-faster Intel N150, and a new16GB Raspberry Pi 5.

I re-ran all my benchmarks, andthis timecompared like-for-like, installing Linux on the Mini PC. Many people argued comparing the OOTB experience running Windows 11 Pro (which came on the Tiny PC) to Raspberry Pi OS (which I installed on the Raspberry Pi 5) was unfair.

I have a video that goes through everything in this post, embedded below:

If you prefer to read the post instead, please continue:

## N100 PCs are not created equal

In the video, I ran through four myths to test whether they hold water—one of the most difficult to assess is whether the N100 isfasterandmore efficientthan a Pi 5.

Because unlike the Pi, an N100 (or the newer N150) is just the SoC used on dozens (maybehundredsnow?) of boards, from prebuilt Tiny PCs to full-on motherboards. Manufacturers pair the SoC with different types of RAM, IO, and cooling options.

All that to say, if you're comparing an N100 paired with slow DDR4 RAM and a weak laptop fan to one running fast DDR5 RAM with a huge desktop CPU cooler, you're going to have a pretty different experience.

But even the slower DDR4-based systems beat the Pi 5 in raw performance, in my testing.How muchdepends a lot on the thermals and power limits.

On the NucBox G3, with DDR4 RAM and some thermal constraints which required me to pop the top off and place a fan over the back side of the main board, it was between 1.5-2x faster than a Pi 5, depending on the benchmark.

For example, High Performance Linpack saw almost double the performance:

But note theefficiencyscores. Despite the N150 using 'Intel 7' (a 10 nm process node), it gets less work done per watt than the Pi 5 (whose Arm BCM2712 chip uses a 16nm process). So the maxim of "better process node == better efficiency" doesnotapply universally (not to mention comparing different process nodes is a fun experiment these days, because 1nm can mean a lot of different things!).

Architecture, feature sets, and chip design still matters.

I haveallthe dozens of benchmark results (and a log of the full process getting them) for both computers on mySBC Reviews website.

## Used Tiny PCs are Cheaper

In news that should be obvious to anyone who thinks about it for more than half a second:used Tiny PCs are cheaper. Cheaper than both new fully-kitted-out Raspberry Pi 5s, and cheaper than new Tiny PCs.

Because of the massive quantity of leased Tiny/Mini/Micro PCs for business use (every doctor's office and hospital on the planet seems to have a dozen), there's a constant churn of 3-5 year old models, and many end up on eBay.

I acquired a couple old Lenovos this way, with 7th and 8th-gen Intel CPUs. Even though they burn a few more watts at idle, they're an excellent deal if you just need a little PC to run something in a homelab, or for a lightweight desktop.

They usually have more expansion options than a cheap Tiny PC or Pi have.

But newsflash:used is different than new. Just like used gaming consoles are cheaper than new ones... you can't say "Tiny PCs are cheaper than Raspberry Pis" based onusedpricing versusnew.

It's enough to say Tiny PCs are cheaper than Raspberry Pis if comparinglike for likespecs onnewmachines:

The Raspberry Pi 5 16 GB model, with 512 GB of SSD storage, Raspberry Pi's NVMe HAT, an Active Cooler, an RTC battery, a 27W power adapter, and a rubber bumper case, costs $208, compared to the similarly-specced GMKtec NucBox G3 Plus.

But you can't find a new fully-kitted Tiny PC in the $60-80 range that competes with the Pi 5, which starts at $50 for the bare Pi 5 board (for a 2 GB model). The most direct comparison is the Radxa X4 (which is a very close Intel-based replacement for the Raspberry Pi). But that board's pricing is very closely aligned to the Pi, as you need to add on accessories to have a fully functional system.

All of this to say: value is complicated. The Pi 5 ismuchmore compact and slightly more power efficient (especially at idle) compared to the cheapest N1XX Intel systems. The Intel systems are better suited for a desktop use case. The Pi 5 can be run off PoE power, for easier one-cable networking + power. The Intel systems are more compatible with a wider range of software (not the least of which isanything requiring Windows).

The idle power is the difference of maybe $10-20/year of power consumption. So it's notthat big a dealfor most users. But it's substantial if you're running off PoE power for remote use cases, or need to run a computer off solar or battery power.

It's not that useful to say one is cheaper than the other, because it's like saying "a bicycle is cheaper than a car." If you need to transport 4 adults 150 miles as quickly as possible, one choice is obviously better!

## Other Notes

* The NucBox G3 Plus I was sent was ordered through Amazonby GMKtecas a review sample; so it comes from the same stock that's shipping to customers. My unit had a defective power adapter, only supplying 0.14V. Luckily I had my old adapter from the original NucBox G3 that I bought, and it worked fine.
* The fan connector on the NucBox G3 is actually the same JST connector / pitch that the Pi 5 uses; just an interesting observation, as I haven't seen that connector used for fans outside of SBCs like the Pi 5 before.
* DDR5 SO-DIMMs are not compatible with DDR4 SO-DIMM slots—just something I learned on this project... I knew full-size DIMMs were incompatible due to the extra on-stick ECC circuit on DDR5 RAM, I just didn't know the same applied to SO-DIMMs. Obvious in hindsight, but something to keep in mind.
* Ubuntu 24.04 required a kernel update to 6.12 (I used Mainline Kernels to do it) to work with the iGPU on the N150 SoC.

## Further reading

* When did Raspberry Pi get so expensive?
* The (almost) perfect mini NAS for my mini rack
* The Rock 5 B is not a Raspberry Pi killer—yet

intel

n150

mini pc

raspberry pi

gmktec

video

youtube

linux

performance

* Add new comment


## Comments

The biggest drawback of the Pi is its lack of built-in SSD support. If you want a reliable system, you need reliable storage, something SD or eMMC are not.

* Reply

I do agree on having m.2 support built-in, but I have had good luck so far with industrial microSD cards. IIRC the datasheet for the ones I have described them basically having similar wear leveling controls to a full SSD packed into the card. Speed still suffers though, and the only readily available ones I found are 8 and 16 GB. Good for needs but not everyone's

* Reply

There is NVMe HAT

* Reply

How ironic, the pi's biggest innovation was the ability to boot without a HDD, and booting from SSD's are it's biggest weakness!

* Reply

A high quality SD-Card is not that bad. My Pi 4 is now running home assistant with the same card for the last 5 years (with 6+ months in between reboots). I backup plan is mandatory, anyway, and I have the whole setup in ansible so that I can easily recreate the setup when needed.That said, I also prefer NVME whenever possible: There are now very affordable NVME hats for the Pi 5 - Pineboards' Hatdrive Nano is just €10 (only 2230/2242 support but that's enough for me).

* Reply

For anyone interested...

I've designed a simple vertical stand for natural convection, and an active cooling option for a double 40x10mm setup:https://www.printables.com/model/1180105-gmktec-nucbox-g3-plus-vertical…

or a more overly complicated - yet more silent - option for a 120mm fan:https://www.printables.com/model/1174310-gmktec-nucbox-g3-plus-cooling-…

Also available on makerworld, if that's more your cup of tea.

Still quite new to CAD modeling so I'd welcome some feedback for improvement :)

* Reply

Thank you once more for an interesting post.
Two (personal) additions:

1. the fun factor of a Raspberry Pi is priceless, and
2. the forum of Raspberry Pi is huge, up to date and helpful.

* Reply

For me, the lack of GPIO access on NUC is what keeps me firmly in the Pi group.

* Reply

At 10 cents per kWH and 7W difference or so in power draw for normal cpu usage, that calculates out to about $6 per year increased energy cost for a much higher performance box than a pi5 for normal things that don't require GPIO.

Add in the much lower time-value-of-your-blood-pressure cost of running any x86_64 variant of linux and finding docker images to run, given it can be hard to find ARM compatible images, to me the NucBox is an obvious no-brainer win for any kind of reasonable desktop/server use cases.

Raspi for places where you want to tinker or battery power or connect to GPIO - sure - but I just don't see it as a viable desktop/server box any more if you were starting from scratch. Even for things like HomeAssistant that ship their own pi hardware, I'd argue that it runs far better in docker on my ancient i3 NUC than it does on a pi5, or at least that's been my experience.

* Reply

We are running a fleet of Raspberry Pis in production. We are using passiv cooled cases and Kingston industrial microSD cards.There where 2 or 3 defect units in all the years, but hey what system survives a crash with a forklift? None of the industrial SD cards ever died!Reliability is what makes the Rasperry Pi often the first choice, and this point is ignored in the discussion. No moving parts, a lot less components, a lot more systems are out there and with it much more informations, about bugs and problems and how to fix them. And you can order a new Raspberry PI 5 in 10 years. Can you do it with the nuc if it breaks down? How does the fan hold up in 2 - 3 years without cleaning? Can you get spares? Do you need new mounts for other nucs? Can you swap fast from a broken system to a working one? On a Raspberry you can just move the SD card to a new system and you are good to go. Or a software update, take the old SD card out, put the new one in, downtime 1 min.

* Reply

Just a heads-up about bargain basement PCs running Windows 10: two units I purchased in the past year, a refurbished Dell Optiplex and an Evolve Maestro laptop ($79.95 at Micro Center) mysteriously lost their operating systems just days apart. Coincidence? Maybe, but since both are running Linux just fine now I have no immediate plans to sue Microsoft over it.

* Reply

Got a Pi500. Handy and does what I want it to (surfing, Steam Link). Micro SD is fine for me but also the option of NVME. More than happy.

* Reply

Still waiting for a SBC PC with a camera port

* Reply

I tried to find the GMKtec device you tested at that price the day your review came out, and I tried today but unfortunately it is selling for a whole lot more: $249 - $15 (coupon).

* Reply

Hmm... it's $219 - $15 for me on Amazon US right now—I wonder if it's tariff pricing or what. I know they've had prices go up and down a bit in the past, but usually the base models would settle in around $120-160 every few months.

* Reply

The version used in this review (16GB RAM, 512GB SSD) is $146 on AliExpress. There's also a barebones version without the low-tier RAM and SSD for $96.

* Reply

Zimaboard 2 832: 199€RAM 8GBeMMC 32GBLAN 2x2.5GbESATA 2x 3.0USB 2x 3.1PCIe 1x 3.0CPU TDP 10W

* Reply
