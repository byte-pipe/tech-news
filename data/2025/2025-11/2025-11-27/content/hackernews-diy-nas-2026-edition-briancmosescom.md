---
title: 'DIY NAS: 2026 Edition - briancmoses.com'
url: https://blog.briancmoses.com/2025/11/diy-nas-2026-edition.html
site_name: hackernews
fetched_at: '2025-11-27T19:06:39.438558'
original_url: https://blog.briancmoses.com/2025/11/diy-nas-2026-edition.html
author: sashk
date: '2025-11-27'
description: An 8-bay DIY NAS with 10GbE networking, TrueNAS 25.10.0.1, an Intel N355 CPU, 32GB of DDR5 RAM, and a smallish form factor that occupies less than 20 liters of your office space.
---

Fourteen years ago, my storage needs outpaced my capacity and I began to look into building a network attached storage server. I had a few criteria in mind and was curious to see if anyone had _ recently_ shared something similar, but I couldn’t find anything that was relevant.

In fact, I found that the communities I was looking for answers in were actively hostile towards what I wanted to do. This resulted in my decisionto build my own DIY NASand share that as one of my very first blogs.

Much to my surprise, people were very interested in that blog! Ever since, I’ve been building a similar DIY NAS machine almost every year, trying to satisfy the curiosity of other prospective DIY NAS builders.

Here are those criteria:

1. Small form factor: It’s not the case for me anymore, but at the time the space was limited in my office. I always assume that space in everybody’s office is limited. As a result, I want my DIY NAS builds to occupy as little of that office space as I can.
2. At least six drive bays: Back when I built my NAS, it took about four drives’ worth of storage to meet my storage needs. Plus, I desired two empty drive bays for future use. However, in the years since, hard drive capacities have increased dramatically. At some point in the future, I may reduce this to four drive bays.
3. An integrated, low-power CPU: I intend my DIY NAS to run 24 hours a day, 7 days a week, and 52 weeks a year. When it comes to power consumption, that can do some damage on your electric bill! Thankfully, our electricity here isn’t as expensive as others’ in the United States, or even further outside its borders, but I try and keep power consumption in mind when picking components for a DIY NAS build.
4. Homelab potential: It does not take up a lot of CPU horsepower for a NAS to serve up files, which means that on modern hardware there’s a lot of untapped potential in a DIY NAS for virtual machines and/or containers to self-host services.

It’s important to remember thatthese are my criteria, and not necessarily yours. Every DIY NAS builder should be making their own list of criteria and reconcile all of their component purchases against the criteria that’s important to them.

## Is it even a good time to build a NAS?

As I prepared to build this NAS, component prices disappointed me. Hard drives, SSDs, and RAM prices were all rising. Based on what I’ve been told, I expect Intel CPU prices to increase as well. My contact at Topton has been encouraging me to stock up on motherboards while they still have some in inventory. Based on what’s been explained to me, I expect the motherboards’ prices to rise and for their availability to potentially dwindle.

In short, the economy sucks, and the price of DIY NAS components is a pretty good reflection of just how sucky things are becoming. I briefly considered not publishing a DIY NAS build this year, hoping that things would improve a few months down the road. But then I asked myself, “What if it’s even worse in a few months?”

I sure hope things get better, but I fear and expect that they’ll get worse.

## Motherboard and CPU

I builtmy first DIY NAS with a Topton motherboard in 2023. Each DIY NAS since then has also featured a Topton motherboard. My only complaint about the motherboards has been that buying them from one of the Chinese e-tail sites like AliExpress is considered problematic by some. With every DIY NAS build, I try and go through all the motherboards that I can find while searching for something with a better value proposition, but for each of the past three years I’ve landed on the latest offering from Topton.

For theDIY NAS: 2026 Edition, I chose theTopton N22 motherboardwith theIntel Core 3 N355CPU. The motherboard is similar to last year’sTopton N18but has incrementally more compelling features, particularly the extra 2 SATA ports, the PCI-e x1 slot, and the N355 CPU!

* Mini-ITX Form Factor
* Intel® Processor Core 3 N3558 cores / 8 threads / Max Turbo 3.9GHz15 W TDPIntegrated GPU with Intel Quick Sync Video
* 8 cores / 8 threads / Max Turbo 3.9GHz
* 15 W TDP
* Integrated GPU with Intel Quick Sync Video
* 1 x DDR5 SO-DIMM
* 8 x SATA 3.0 Ports (Asmedia ASM1164)
* 2 x M.2 NVMe Slots (PCIe 3.0 x1)
* 1 x 10Gbps NIC (Marvell AQC113C)
* 2 x 2.5Gbps NICs (Intel i226-V)
* 1 x PCI-e x1 or M.2 E-Key slot

I opted for the motherboard with theIntel Core 3 N355CPU. This makes the server a more capable homelab machine than prior years’ DIY NAS builds. The extra cores and threads come in handy for streaming media, replacing your cloud storage, facilitating home automation, hosting game servers, etc.

## Case

Just like Topton has been making great motherboards for DIY NAS machines, JONSBO has been steadily releasing great cases for DIY NAS machines. This year SilverStone Technology, released a new case, theCS383(specs), which I wasvery interestedin buying for theDIY NAS: 2026 Edition. Unfortunately, it carries a pretty hefty price tag to go along with all of its incredible features!

TheJONSBO N4(specs) is a third of the price, adheres to my “smaller footprint” criteria, and it is rather impressive on its own. It’s atinybit larger case than last year’s DIY NAS, but I really like that it has drive bays for six 3.5” drives and two 2.5” drives.

It’s peculiar in that two of the 3.5” drive bays (and the two 2.5” drive bays) aren’t attached to a SATA backplane and can’t be swapped anywhere as easily as the other four 3.5” bays. However, this peculiar decision seems to have caused the JONSBO N4 to sell for a bit less ($20–$40) than similar offerings from JONSBO. At its price, it’s a compelling value proposition!

### Case Fan

In the past, I’ve found that the fans that come with JONSBO cases are too noisy. They’ve been noisy for two reasons: The design and quality of the fans make them loud, and the fans are constantly running at their top speed because of the fan header they’re plugged into on the cases’ SATA backplanes.

I anticipated that fan efficiency and noise would be a problem, so I picked out theNoctua NF-A12x25 PWMto solve it. Firstly, swapping in a high-quality fan that pushes more airandgenerates less noise–especially at its top speed–is a good first step. Secondly, I’d address the problem by plugging the fan into the motherboard’sSYS_FANheader instead of on the SATA backplane. This provides the opportunity to tune the fan’s RPMs directly in the BIOS and generate far less noise.

## RAM

The first time I first asked myself, “Should I even build theDIY NAS: 2026 Edition?” came as I was checking prices on DDR5 memory. Thankfully for me, I had leftover RAM after purchasing DDR5 4800MHz SODIMMs for theDIY NAS: 2025 Edition,the Pocket Mini NAS, and then again for theDIY NAS that I built and gave away at 2025’s Texas Linux Fest. I was personally thankful that I had one brand-new 32GB DDR5 4800MHz SODIMM lying around, but I was wildly disappointed for everybody who will try and follow this build when I saw the price of those same SODIMMs.

Regardless, I felt aCrucial 32GB DDR5 4800MHz SODIMM(specs) was the right amount of RAM to get started with for a DIY NAS build in 2025. Whether you just need storage or you wish to also host virtual machines, you will benefit from having more than the bare minimum recommendation of RAM. I really wanted to buy a48GB DDR5 4800MHZ SODIMMfor this DIY NAS build, but I couldn’t talk myself into spending the $250–$300 that it would’ve wound up costing.

## Storage

A quick disclaimer about all the drives that I purchased for theDIY NAS: 2026 Edition:, I already had all of them! I tend to buy things when I see them on sale, and as a result, I have a collection of brand-new parts for machines in my homelab or for upcoming projects. I raided that collection of spare parts for theDIY NAS: 2026 Edition.

### Boot Drive

If you ranked the drives in your DIY NAS in order of importance, the boot drive should be the least-important drive. That isnotsaying that boot drive isn’t performing an important function, but I am suggesting that you shouldn’t invest a bunch of energy and money into picking the optimal boot drive.

Because theJONSBO N4has a pair of 2.5” drive bays, I decided that a 2.5” SATA SSD would be ideal for the boot drives. As a rule of thumb, I try and spend less than $30 per boot drive in my DIY NAS builds.

Ultimately I selected a pair of128GB Silicon Power A55 SSDs(specs). I’ve used these before, I’d use them again in the future, and I even have four of their higher-capacity (1TB) SSDs in a pool in my own NAS.

### App and Virtual Machine NVMe SSDs

Using your DIY NAS to host containers and virtual machines has really exploded in the past few years. The developers of NAS appliances have all made it much easier, and the self-hosted products themselves have become as good–or often better–than things you’re probably subscribing to today. Because of that, I saved the highest-performing storage options on theTopton N22 motherboardfor apps and VMs.

However, it’s important to point out that these M.2 slots are PCI-e version 3 and capped at a single PCI-e lane. This is a consequence of the limited number of PCI-e lanes available for each of the CPU options available for theTopton N22 motherboard(N100, N150, N305, and N355).

I opted for a NVMe drive that was a good value rather than a high performer and chose two of theSilicon Power 1TB M.2 NVMe SSDs (SP001TBP34A60M28)(specs).

### Bulk Storage Hard Disk Drives

Thanks to rising prices, I opted to do like I’ve done with past DIY NAS builds and skip buying hard drives for theDIY NAS: 2026 Edition.

When planning your DIY NAS, it is good to always remember thatstorage will ultimately be your costliest and most important expense.

Here are a few things to consider when buying hard drives:

1. Determine your hardware redundancy preferences. I recommend having two hard disk drives’ worth of redundancy (RAIDZ2, RAID6, etc.)
2. Focus on price-per-terabyte when comparing prices of drives.
3. Do someburn-in testingof your hard drives before putting them to use.
4. When buying new drives of the same model, try and buy them from multiple vendors to increase the chances of buying drives manufactured in separate batches.
5. Plan ahead! Understand the rate that your storage grows so that you can craft a strategy to grow your storage down the road.
6. Being cheap today can and will paint you into a corner that’s quite expensive to get out of.
7. Understand that RAID is not a backup!

Thankfully, I’ve collected a bunch of my own decommissioned hard drives which I used to thoroughly test this DIY NAS build.

## SATA Cables

One of the under-the-radar features of theTopton N22 motherboardmight be one of my favorite features! The motherboard’s Asmedia ASM1164 SATA controllers sit behind two SFF-8643 connectors. These connectors provide two advantages for these motherboards:

1. Save room on the motherboard’s PCB.
2. SFF-8643 to 4x SATA breakout cablesreduce the amount of cable management hassle.

## Power Supply

The one thing that I have routinely disliked about building small form factor DIY NAS machines is the price tag that accompanies a small form factor power supply (SFX) like is required with theJONSBO N4.

I wound up choosing theSilverStone Technology SX500-G(specs) which I had used earlier in the year for theDIY NAS I gave away at Texas Linux Fest. Its 500W rating exceeds the needs of all the components that I’d picked out for theDIY NAS: 2026 Edition. Plus, the power supply’s80 Plus Goldrating aligns well with my criteria for power efficiency.

## TrueNAS Community Edition

Regardless of whether it was called FreeNAS, TrueNAS, TrueNAS CORE, TrueNAS SCALE, or nowTrueNAS Community Edition, the storage appliance product(s) from iXSystems have always been my go-to choice. For each yearly DIY NAS build, I wander over to theTrueNAS Software Status pageand look at the state of the current builds.

I’m conservative with my personal NAS setup. However, for these blog builds, I typically choose Early Adopter releases. This year that’sTrueNAS 25.10.0.1 (aka Goldeye). I enjoy being able to use these DIY NAS builds as a preview to the latest and greatest that TrueNAS has to offer.

I repeatedly choose TrueNAS because it’s become an enterprise-grade storage product, which is exactly the quality of solution that I want my data depending on. At the same time, it does not feel like you need a specialized certification and a truckload of enterprise storage experience to set up a NAS that exceeds your needs at home.

Many times I have been asked, “Why not<insert NAS appliance or OS here>?” My answer to that question is, TrueNAS has always done everything that I need it to, and they haven’t given me any reason to consider anything else. As a result, there’s never been a need for me to evaluate something else.

## Final Parts List

Component

Part Name

Qty

Cost

Motherboard

Topton N22 (w/ N355 CPU) NAS Motherboard

specs

1

$446.40

CPU

Intel Core 3 N355

specs

1

N/A

Memory

Crucial RAM 32GB DDR5 4800MHz SODIMM (CT32G48C40S5)

specs

1

$172.96

Case

JONSBO N4

specs

1

$121.59

Case Fan

Noctua NF-A12x25 PWM chromax.Black.swap

specs

1

$37.95

Power Supply

SilverStone 500W SFX Power Supply SST-SX500-G)

specs

1

$142.34

Boot Drive

Silicon Power 128GB A55 SATA SSD

specs

2

$21.97

Apps/VM Drives

Silicon Power 1TB - NVMe M.2 SSD (SP001TBP34A60M28)

specs

2

$99.99

SATA Cables

OIKWAN SFF-8643 Host to 4 X SATA Breakout Cable

N/A

2

$11.99

Price
without
 Storage:

$989.36

Total Price:

$1,189.34

## Hardware Assembly, BIOS Configuration, and Burn-In

### Hardware Assembly

I always want the smallest possible DIY NAS. TheJONSBO N4case initially felt too large since it accommodates Micro ATX motherboards. However, I grew to accept its slightly larger footprint. However, putting theTopton N22 motherboardinto the case felt roomy and luxurious. Building theDIY NAS: 2026 Editioncompared to prior years’ felt a lot like coming home to put on sweatpants and a T-shirt after wearing a suit and tie all day long.

I wasn’t too fond of the cable management of the power supply’s cables. The layout of the case pretty much makes the front of the power supply inaccessible once it is installed. One consequence of this is that the power cable which powered the SATA backplane initially prevented the 120mm case fan from spinning up. That issue was relatively minor and was resolved with zip ties.

Overall, I felt pretty good about the assembly of theDIY NAS: 2026 Edition, but things would take a turn for the worse when I decided to fill all the 3.5-inch drive bays up with some of my decommissioned 8TB HDDs. Now this is probably my fault, I wouldn’t be surprised at all that the manual of theJONSBO N4warned me against this, but putting the drives in last turned out to be a major pain in the neck for each of the four drive bayswithouta SATA backplane.

I had wrongly guessed that you accessed those drives’ power and data ports from the front of the case. I worked really hard to route the cables and even managed to install all of the drives before realizing my error and learning my lesson. I’m understanding now why theJONSBO N4is cheaper than all of its siblings: Partly because there’s a missing SATA backplane, but also because those other 4 drive bays’ layout is frustrating.

Don’t let my last couple paragraphs sour you on theJONSBO N4, though. I still really like its size; it feels big when you’re working in it with a Mini ITX motherboard. If you wind up deciding to use the JONSBO N4, then I suggest that you put those four drives and their cables in first before you do anything else. That would’ve made a world of difference for me. Looking at the documentation before getting started might have saved me quite a bit of aggravation, too!

If I have ruined the JONSBO N4 for you, then check out theJONSBO N3. Itseight3.5-inch drive bays pair up really nicely with theTopton N22 motherboard. You can see what I thought of the JONSBO N3 by reading theDIY NAS: 2024 Editionblog.

### BIOS Configuration

Generally speaking, I do as little as I possibly can in the BIOS. Normally, I strive to only set the time and change the boot order. However, I did a bit more for theDIY NAS: 2026 Editionsince I’m using theSYS_FANheader for the fan responsible for cooling the hard drives. Here are the changes that I made in the BIOS:

1. Set theSystem DateandSystem Timeto Greenwich Mean TimeAdvancedHardware Monitor ( Advanced)SetSYS SmartFan ModetoDisabled.Set theManual PWM Setting(forSYS_FAN) to 180.SetPWRON After Power LosstoAlways OnBootSetBoot Option #1to the TrueNAS boot device.
2. AdvancedHardware Monitor ( Advanced)SetSYS SmartFan ModetoDisabled.Set theManual PWM Setting(forSYS_FAN) to 180.
3. Hardware Monitor ( Advanced)SetSYS SmartFan ModetoDisabled.Set theManual PWM Setting(forSYS_FAN) to 180.
4. SetSYS SmartFan ModetoDisabled.
5. Set theManual PWM Setting(forSYS_FAN) to 180.
6. SetPWRON After Power LosstoAlways On
7. BootSetBoot Option #1to the TrueNAS boot device.
8. SetBoot Option #1to the TrueNAS boot device.

I’m not at all interested in venturing into the rabbit’s hole of trying to completely minimize how much power the NAS uses. However, I imagine there are some opportunities for power savings lurking in the BIOS. I didn’t go looking for them myself, but if you’re intrepid enough to do so, here are a few suggestions that I have for saving some additional power:

* Disable the onboard audio.
* Disable any network interfaces that you don’t wind up using.
* Tinker with the CPU settings.
* Got other suggestions?Share them in the comments!

### Burn-In

Because all of the hardware is brand-new to me and brand-new components are not guaranteed to be free of defects, I always do a little bit of burn-in testing to establish some trust in the hardware that I’ve picked out for each DIY NAS build. While I think doingsomeburn-in testing is critically important, I also think the value of subsequent burn-in testing drops the more that you do. Don’t get too carried away, and do your own burn-in testing in moderation!

#### Memtest86+

Ialwaysuse Memtest86+ to burn-in the RAM. I always run at least 3+ passes of Memtest86+. Typically, I run many more passes because I tend to let the system keep running additional passes overnight. Secondarily, running these many passes gives the CPU a little bit of work to do and there’s enough information displayed by Memtest86+ to give me confidence in the CPU and its settings.

#### Hard Drives

The failure rate of hard drives is highest when the drives are new and then again when they’re old. Regardless of type of hard drives that I buy or when I buy them, I always do some disk burn-in. I tend to runSpearfoot’s Disk Burn-in and Testing scripton all of my new drives. However, executing this script against all of the drives can take quite a long time, even if you use something liketmuxto run the tests in parallel.

## Initial TrueNAS CE Setup

There’s always a little bit of setup that I do for a new TrueNAS machine. This isn’t intended to be an all-inclusive step-by-step guide for all the things you should do with your DIY NAS. Instead, it’s more of a list of things I kept track of while I made sure that theDIY NAS: 2026 Editionwas functional enough for me to finish writing this blog. That being said, I do think your NAS would be rather functional if you decided to do the same configuration.

1. Updated the hostname todiynas2026Note: This is only to avoid issues with another NAS on my network.
2. Note: This is only to avoid issues with another NAS on my network.
3. Updated the time zone.
4. Enabled the following services and set them to start automatically.SMBSSHNFS
5. SMB
6. SSH
7. NFS
8. Enabled password login for thetruenas_adminuser.* Note: If I were planning to use this DIY NAS long-term, I wouldn’t have done this. Using SSH keys for authentication is a better idea.
9. Edited the TrueNAS Dashboard widgets to reflect the 10Gb interface (enp1s0).
10. Created a pool namedflashwhich consisted of mirrored vdev using theTeamgroup MP44 1TB NVMe SSDs.
11. Created a pool namedrustwhich consisted of a single RAID-Z2 vdev using eight hard drives that I had sitting on my shelf after they were decommissioned.
12. Configured the Apps to use theflashpool for the apps’ dataset.
13. Made sure that the System Dataset Pool was set toflash.
14. Confirmed that there were Scrub Tasks set up for theflashandrustpools.
15. Created a dataset on each pool for testing:flash-testandrust-test.
16. Installed theScrutinyapp found in the App Catalog.

If I were planning to keep this NAS and use it for my own purposes, I would also:

1. Set up aLet’s Encrypt certificate.
2. Hook up the NAS toa compatible UPS, enable the UPS service, and configure the UPS service to shut down the NAS before the battery runs out of juice.
3. Set up system email alert service.
4. Createreplication tasksto back up critical data to myoff-site NAS.
5. Add the new NAS to my Tailscale tailnet using theTailscale app from the official catalog.
6. As the NAS is seeded with data, create and maintain a suite ofsnapshot taskstailored to the importance of the different data being stored on the NAS.
7. Set up S.M.A.R.T. tests for all of the drives:Weekly Short TestMonthly Long Test
8. Weekly Short Test
9. Monthly Long Test

## Benchmarks

Just about every year, I benchmark each DIY NAS build and almost always come to the same conclusion: The NAS will outperform your network at home. Your first bottleneck is almost always going to be the network, and the overwhelming majority of us have gigabit networks at home–but that’s slowly changing since 2.5Gbps and 10Gbps network hardware has started to get reasonably affordable lately.

Even though I always come to the same conclusion, I still like to do the benchmarks for two reasons:

1. It helps me build confidence that theDIY NAS: 2026 Editionworks well.
2. People tend to enjoy consuming benchmarks,andit’s fun for me to see the DIY NAS’ network card get saturated during the testing.

### Throughput

I like to do three categories of tests to measure the throughput of the NAS:

1. Useiperf3to benchmark throughput between my NAS and another machine on my network.
2. Benchmark the throughput of the pool(s) locally on the NAS usingfio.
3. Set up SMB shares on each of the pools and then benchmark the throughput when using those shares.

Every year I try and mention that Tom Lawrence fromLawrence Systemspublisheda great video about benchmarking storage with FIOand sharedthe FIO commands from his video in their forums. I use these FIO commands constantly as a reference point forwh I am testing ZFS pools’ throughput. More importantly I’d like to point out that, in that same video, Tom says something very wise:

There are lies, damn lies, and then there are benchmarks!

Tool

Pool

Test
Size

Random
Write
IOPS

Random
Read
IOPS

Sequential
Write
(MB/s)

Sequential
Read
(MB/s)

FIO

flash

4G

1906.00

2200.00

548.00

1214.00

FIO

flash

32G

2132.00

3012.00

544.00

1211.00

FIO

rust

4G

1352.00

108.00

367.00

530.00

FIO

rust

32G

1474.00

326.00

368.00

544.00

CrystalDiskMark

flash

4GiB

5858.89

50409.91

1104.64

956.70

CrystalDiskMark

flash

32GiB

4193.36

31047.36

635.42

946.20

CrystalDiskMark

rust

4GiB

5226.50

46239.01

756.23

655.32

CrystalDiskMark

rust

32GiB

3794.43

12809.33

759.38

677.02

What do I think these benchmarks and my use of theDIY NAS: 2026 Editiontell me? In the grand scheme of things, not a whole lot.

However, these benchmarks do back up what I expected: TheDIY NAS: 2026 Editionis quite capable and more than ready to meet my storage needs. I especially like that the CrystalDiskMark benchmarks of the SMB shares wereboth faster than a SATA SSD, and the throughput to the share on theflashpool practically saturated the NAS’ 10GbE network connection.

#### FIO Tests

Every time I benchmark a NAS, I seem to either be refining what I tried in prior years or completely reinventing the wheel. As a result, I wouldn’t recommend comparing these results with results that I shared in prior years’ DIY NAS build blogs. I haven’t really put a ton of effort into developing a standard suite of benchmarks. Things in my homelab change enough between DIY NAS blogs that trying to create and maintain an environment for a standard suite of benchmarks is beyond what my budget, spare time, and attention span will allow.

I’m going to paste thesefiocommands here in the blog for my own use in future DIY NAS build blogs. If you wind up building something similar, thesemightbe helpful to measure your new NAS’ filesystem’s performance and compare it to mine!

## Random Write IOPS
fio --randrepeat=1 --ioengine=libaio --direct=1 --name=test --filename=test --bs=128k --size=4G --readwrite=randwrite --ramp_time=10
fio --randrepeat=1 --ioengine=libaio --direct=1 --name=test --filename=test --bs=128k --size=32G --readwrite=randwrite --ramp_time=10

## Random Read IOPS
fio --randrepeat=1 --ioengine=libaio --direct=1 --name=test --filename=test --bs=128k --size=4G --readwrite=randread --ramp_time=10
fio --randrepeat=1 --ioengine=libaio --direct=1 --name=test --filename=test --bs=128k --size=32G --readwrite=randread --ramp_time=10

## Sequential Write (MB/s)
fio --randrepeat=1 --ioengine=libaio --direct=1 --name=test --filename=test --bs=4M --size=4G --readwrite=write --ramp_time=10
fio --randrepeat=1 --ioengine=libaio --direct=1 --name=test --filename=test --bs=4M --size=32G --readwrite=write --ramp_time=10

## Sequential Read (MB/s)
fio --randrepeat=1 --ioengine=libaio --direct=1 --name=test --filename=test --bs=4M --size=4G --readwrite=read --ramp_time=10
fio --randrepeat=1 --ioengine=libaio --direct=1 --name=test --filename=test --bs=4M --size=32G --readwrite=read --ramp_time=10

### Power Consumption

One not-so-obvious cost of running a DIY NAS is how much power it consumes. While I specifically tried to pick items that were efficient in terms of power consumption, it’s also important to realize that all the other bells and whistles on the awesomeTopton N22 NAS motherboardconsume power, too, and that the biggest consumer of power in a NAS is almost always the hard disk drives.

Thanks to my tinkering withhome automation, I have a plethora ofsmart outletswhich are capable of power monitoring. I used those smart outlets for most of my power monitoring. But I also have aKill a Watt P400that I also use for some of the shorter tests:

* Power consumed during a handful of specific tasks:Idle while running TrueNASRAM Burn-in (~14 passes of Memtest86+)An 8-hour throughput benchmark copying randomly sized files to the NAS using SMB.
* Idle while running TrueNAS
* RAM Burn-in (~14 passes of Memtest86+)
* An 8-hour throughput benchmark copying randomly sized files to the NAS using SMB.
* Total consumed during the build, burn-in, and use of theDIY NAS: 2026 Edition.

Task

Duration

Max Wattage

Avg. Wattage

Total Consumption

Boot

10 min.

200.00 W

120.00 W

0.02 kWh

Idle

3 hr.

90.00 W

66.67 W

0.20 kWh

RAM Burn-in

18 hr.

104.00 W

91.67 W

1.65 kWh

SMB Benchmark of HDDs

8 hr.

107.00 W

85.00 W

0.68 kWh

Total

108 hr.

237.80 W

66.49 W

7.17 kWh

## What about an EconoNAS?

Shortly before prices skyrocketed, I decided I wasn’t very interested in doing separate EconoNAS builds any longer. Several months ago, I realized that there were several off-the-shelf NAS machines that were more than capable of running TrueNAS, and they were selling at economical prices that couldn’t be topped by a DIY approach. I will dive deeper into this in a future blog, eventually …maybe?

All that being said, it’d be incredibly easy to make some compromises which result in theDIY NAS: 2026 Editionbecoming quite a bit more economical. Here’s a list of changes that I would consider to achieve a more budget-friendly build:

* Different motherboard/CPU combo:N18 w/ N100 CPU(-$224),N18 w/ N150 CPU(-$214), orN22 w/ N150 CPU(-$180)
* 16GB of DDR5 RAM(-$39) instead of 32GB.
* Thermal Right TL-C12015 Slim Faninstead of the Noctua NF-A12x25 (-$26)
* Apevia SFX-AP500W Power Supply(-$104)
* Skip the redundancy for the boot pool (-$22)

Altogether, these savings could add up to more than $400, which is pretty considerable! If you made all of these changes, you’d have something that’s going to be nearly equivalent to theDIY NAS: 2026 Editionbut at a fraction of the price.

## What am I going to do with the DIY NAS: 2026 Edition?!

My DIY NAS is aging quite gracefully, but I’ve recently been wondering about replacing it. Shortly before ordering all the parts for theDIY NAS: 2026 Edition, I briefly considered using this year’s DIY NAS build to replace my personal NAS. However, I decided not to do that. Then prices skyrocketed and I shelved the idea of building a replacement for my own NAS and I nearly shelved the idea of a DIY NAS in 2026!

So that begs the question, “What is Brian going to do with theDIY NAS: 2026 Edition?”

I’m going to auction it off on thebriancmosesdotcom store on eBay! Shortly after publishing this blog, I’ll list it on eBay. In response to skyrocketing prices for PC components, I’m going to do a no-reserve auction. At the end of the auction, the highest bidder wins, and hopefully they’ll get a pretty good deal!

## Final Thoughts

Overall, I’m pleased with theDIY NAS: 2026 Edition. TheTopton N22 motherboardis a significant improvement over last year’sTopton N18 motherboard, primarily due to its extra two SATA ports. This provides 33.3% more gross storage capacity.

While testing, I found theIntel Core 3 N355 CPUsomewhat excessive for basic NAS functions. However, the substantial untapped CPU horsepower offers luxurious performance potential. This makes the build compelling for anyone planning extensive self-hosting projects.

I have mixed feelings about theJONSBO N4 case. The four right-side drive bays lack SATA backplane connectivity. Without creative cabling solutions, individual drive replacement becomes challenging. However, the case’s ~$125 price point compensates for this inconvenience. I anticipate that those the cost savings will justify the compromise for most builders. If I were to build theDIY NAS: 2026 Editionall over again, I’d be tempted to use theJONSBO N3 caseor even theJONSBO N6which isn’t quite obtainable, yet.

The DIY NAS: 2026 Edition delivers excellent performance and superior specifications. In my opinion, it represents better value than off-the-shelf alternatives:

* QNAP TS-832PX-4G($880)
* Asustor Lockerstor 8 AS6508T($960)
* UGREEN NASync DXP8800($1200)

Building your own NAS provides significant advantages. Years later, you can upgrade RAM, motherboard, case, or add PCI-e (x1) expansion cards. These off-the-shelf alternatives offer severely limited upgrade paths.

Is 2026 finally the year that you decide to build your DIY NAS? I hope that it is! Share your experience building your NAS in the comments below, or come tell us about it in the#diynas-and-homelab channel on the Butter, What?! Discord server!
