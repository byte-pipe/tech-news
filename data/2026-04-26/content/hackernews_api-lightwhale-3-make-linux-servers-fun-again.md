---
title: 'Lightwhale 3: Make Linux servers fun again!'
url: https://lightwhale.asklandd.dk/
site_name: hackernews_api
content_file: hackernews_api-lightwhale-3-make-linux-servers-fun-again
fetched_at: '2026-04-26T06:00:19.061598'
original_url: https://lightwhale.asklandd.dk/
author: Stephan Henningsen
date: '2026-04-25'
description: Make Linux servers fun again!
tags:
- hackernews
- trending
---

## Lightwhale

is a purpose-built operating system
					designed to run Docker containers effortlessly.
					Itlive-bootsfrom an ISO straight
					into a fully functional Docker Engine,
					eliminating the need for installation or configuration.

The core system is immutable,
					making it inherently maintenance-free while enhancing security.
					Data and customisations are stored entirely segregated on a dedicated device,
					ensuring they never become entangled with core system files.
					This gives transparency and makes backup easier.

Streamlined yet versatile enough for home labs orenterprise,
					bare‑metal or virtualized,
					edge nodes or clusters.

Driven by a minimalistic design philosophy and an emphasis on ease of use,
					Lightwhale lowers the entry barrier,
					removes tedious administration tasks,
					and opens afriction-freepath to productivity,
					and makes you feel awesome!

## Features

Plug and play

						Just download the ISO and live‑boot the server straight into an
						operational Docker Engine,
						with all necessary tools immediately available.
					

Simplicity by design

						The number of moving parts has been reduced to a minimum,
						which makes the system easy to learn and quickly mastered with confidence.
					

Secure and predictable

						With an immutable and stateless core,
						the system provides a minimal attack surface against malware,
						and is equally resilient to unintentional modification.
						Every boot is consistent.
					

Opt-in persistence

						Persistence happens on the 
data filesystem

						which is physically segregated from the immutable root filesystem at all times.
						By default, the data filesystem is located in RAM and volatile.
						However, when 
persistence
 is enabled,
						Lightwhale will automatically detect, partition, format,
						and mount the data filesystem on a separate storage device and persistent changes across reboots.
					

Efficient and eco-conscious

						All unnecessary processes are removed,
						ensuring a minimal footprint that conserves resources and power,
						always getting the most from the hardware.
						Lightwhale extends the life of older or low-end machines,
						reducing environmental impact by leveraging the carbon
						already invested in them.
					

Empowers digital sovereignty

						Lightwhale lets organizations of all sizes self-host with ease,
						break free from Big Tech lock-in,
						and take back privacy and data.
					

## Getting Started

Let's get Lightwhale running on a bare‑metal x86 machine,
					in just a few easy steps.

1. Download Lightwhale

Download thelatest Lightwhale ISO filefrom thedownload sectionor copy, paste, and run this in your terminal:

curl -JOL http://lightwhale.asklandd.dk/download/lightwhale-3.0.0-x86.iso

2. Prepare boot media

Write the Lightwhale ISO file to a USB flash device,
							either using your favoriteISO burner tool,
							or simplyusedd.:

sudo dd bs=4M conv=fsync if=lightwhale-3.0.0-x86.iso of=/dev/sdx

3. Boot Lightwhale

Boot your machine on the newly prepared Lightwhale boot media.
							It may be necessary to disablesafe bootin the BIOS first.

4. Log in

Username:opPassword:opsecret

5. Enable persistence (optional)

Write themagic headerto the desiredstorage device,
						typically an SSD or HDD.
						Write it to theblock device(not apartition);
						for HDD use e.g./dev/sda(not/dev/sda1);
						for NVME use e.g./dev/nvme0n1(not/dev/nvme0n1p1).
						This will in turn erase all existing data on the device.
						On some systems it's necessary to wipe an existing partition table first
						before writing the magic header:

sudo dd if=/dev/zero bs=512 count=1 conv=notrunc of=/dev/nvmeØn1echo "lightwhale-please-format-me" | sudo dd conv=notrunc of=/dev/nvmeØn1

Reboot to let Lightwhale detect the magic header
						and automatically create and mount thedata filesystem.

6. Enable wifi (optional)

sudo setup-wifi --ssid="my wifi name" --password="my wifi secret"

7. Run a container

At this point it's business as usual:

docker run -it --rm busybox ps

8. Change password

Always take adequate security measures before exposing a server to the internet.
							Sinceeveryoneknows the default login and password of your new server, at the very least change that:

passwd op

## Startup Sequence

The Lightwhale ISO can boot on bare‑metal or in a virtual machine,
					supporting both UEFI and classic BIOS.
					It uses a classicsysv‑likeinit system
					that keeps the startup process simple and transparent.

First, the boot loader loads the Linux kernel
					and the root filesystem into memory.
					The kernel initializes the hardware
					and then hands control to/init.

Theinitprocess reads/etc/inittab,
					mounts a standard writabletmpfsfor/tmpand/run,
					and then executes the init scripts in/etc/init.d.

Early during init, the writabledata filesystemis mounted.
					It provides direct storage forDocker dataand upper overlays for/etc,/var,
					and/home.

					This effectively enables you to configure Lightwhale, and install
					and run containers, all on top of the immutable root filesystem.

					By default, the data filesystem is a volatiletmpfs,
					but whenpersistenceis enabled,
					a storage device is used instead.

After all filesystems and overlays are in place,
					the remaining services start,
					and Lightwhale is ready to serve containers.

## Immutability by Design

This is what truly sets Lightwhale apart
					from conventional server operating systems!

The root filesystem is a staticsquashfsimage,
					compressed to save memory, and inherently immutable.
					An immutable kernel and root filesystem instantly brings a number of advantages
					in terms of simplicity, security, and reliability.

### Advantages of Immutability

Zero installation

						Because the kernel and root filesystem cannot be modified,
						all essential software and configuration is pre‑baked.
						The result is a fully self‑contained image that can be
						written to a boot media and live‑booted,
						similar to a video game
						
cartridge
.
						This approach eliminates the tedious installation process
						of partitioning, formatting,
						software selection and copying, and post‑install configuration.
					

Zero maintenance

						With everything preinstalled and configured with sensible defaults,
						there is no need to install additional software or update what already works.
						No more package managers, package dependencies, or race of staying up to date.
						The dreadful operation of 
reinstalling everything
 is effectively accomplished by a simple reboot.
					

Reduced attack surface

						Inherently resilient to both unintentional and malicious modification,
						a file cannot accidentally be deleted from the root filesystem,
						nor modified by a virus.
						In contrast, on a traditional system all files are exposed including
						the kernel and every little part of the underlying operating system, e.g.
						
/bin/sh
,
						
/lib/libc.so.6
,
						of course 
/usr/bin/[
. 
					

No junk

						Long‑running systems tend to accumulate leftover files that
						take up disk space, pollute backups, degrade performance,
						and leave the system messy.
						A read‑only root filesystem prevents this clutter entirely.
					

Experiment freely

						Boot it on a computer or in a local VM,
						so you can experiment right away — and undo everything with a reboot.
					

Relax, it's just a copy

						Lightwhale is a static image written to a boot media.
						It holds absolutely no important information, and immutability ensures it never will.
						Thus, if the device is lost or damaged, you can simply replace it with a new copy,
						and the system is completely restored.
					

## Persistence by Choice

The immutable nature of Lightwhale offers clearadvantages,
					but in order to install, configure, run containers, and write data, a writable filesystem is required.
					And for the system to be genuinely useful,
					such changes must persist across reboots.

### The Data Filesystem

Lightwhale provides bothtemporaryandpersistentwritability 
					through an automated subsystem activated early during startup.
					This mounts thedata filesystemat/mnt/lightwhale-data.

All data written by Lightwhale is kept within a single subdirectory:/mnt/lightwhale-data/lightwhale-state.
					This in turn serves as the writableupper layerin anoverlayfsstack,
					with the immutable root as thelower layer.

By default, Lightwhale mounts a volatiletmpfsas its data filesystem.
					
					When persistence is enabled,
					the data filesystem instead resides on astorage deviceand is mounted accordingly.

### Key Directories

The data filesystem overlay does not cover the entire root filesystem;
					that would defeat thepurposeof immutability
					and Lightwhale altogether.
					Instead, the writable overlays apply only to a few strategic directories:

/etc

						For customizing system configuration,
						including networking, password, and 
sshd
 settings.
					

/var

						For log and other application data.
					

/home

						For user account customization,
						including authorized SSH keys,
						and cloning Git repositories with Docker and Swarm stacks.
					

### Docker Data

Docker is configured with itsdata root directorylocated directly on thedata filesystem,
					where all Docker runtime data is stored,
					including images, containers, volumes, and network state:

/mnt/lightwhale-data/lightwhale-state/docker

### Enable Persistence

Persistence must be enabled explictly
					by writing themagic headerto the storage device to be used,
					e.g./dev/sdx:

echo "lightwhale-please-format-me" | sudo dd conv=notrunc of=/dev/sdx

Multiple storage devices are supported to have a magic header written,
					and will be assembled into a Btrfs RAID1 volume.

The next time Lightwhale boots up,
					it will detect themagic disk,
					format it, and make it thedata filesystem.

### Managing Persistence

Thepersistence subsystemis initiated from/etc/init.d/S11persistence,
					and proceeds through a sequence of detailed steps, executed fully automatically:

1. Find data filesystem

Scan all disks for a partition with the filesystem labellightwhale-data.

If found, use it as thedata filesystemand jump to step 6;
							otherwise proceed to step 2.

2. Find magic disks

Scan all disks for themagic header,
							specifically this exact byte sequence at the very start of the device:lightwhale-please-format-me.

If found, treat each as amagic diskand proceed to step 3;
							otherwise jump to step 6.

3. Create magic partitions

For each magic disk, create a swap partition labeledlightwhale-swap,
							then create a Linux partition that uses the remaining space and label itlightwhale-data.
							Then proceed to step 4.

4. Find magic partitions

Scan all disks for swap partitions labeledlightwhale-swapand Linux partitions labeledlightwhale-data.
							Treat each as amagic swap partitionormagic data partitionand proceed to step 5.

5. Create data filesystem
					

All magic swap partitions are formatted
							and labeledlightwhale-swap.

If only a single magic data partition exists,
							format it withbtrfs --data single --metadata dup.In case of multiple,
							join them into a RAID1 and format withbtrfs --data raid1 --metadata raid1cn.
							Subvolumes are created for@lightwhale-data,@lightwhale-state,
							and@lightwhale-state-snapshots.

Label the data filesystemlightwhale-data,
							so it can be detected in step 1 at next startup.

6. Mount data filesystem and prepare state directory
					

If a data filesystem was created or found,
							mount its subvolume@lightwhale-dataat/mnt/lightwhale-data;
							otherwise mount atmpfsinstead.

7. Mount overlays
					

Prepare the immutablelower layer:
							Bind mount/etcon/run/lightwhale/overlay/lower/etc,
							and mirror the entire directory tree of the immutable root filesystem.

Prepare the writableupper layer:
							If not present, create a directory on the writable data filesystem at/mnt/lightwhale-data/lightwhale-state/overlay/upper/etc.

Finally useoverlayfsto virtually merge
							the two layers and mount theoverlay filesystemat/etc.
							This effectively replaces the immutable directory
							with a writable version!

Repeat for remaining key directories/varand/home.

## FAQ

Frequently asked questions, or future question that someone might be asking at some point.

How do I copy and paste the commands from this guide?

You are right not to try to type all the commands by hand.
							But do review and edit as required before executing,
							particularly when dealing withsudoand device names on the host.

Triple-click to select an entire line in guide and have it copied to your clipboard.
							Triple-click and drag to select a multi-line command.
							Then middle-click to paste it into the terminal.

How do I login on Lightwhale?

Use thedefault loginwith console getty or ssh.

Can I connect Lightwhale to wifi?

Yes.

Should I use Lightwhale at home, school, or work?

Yes.

What hardware is supported?

Only x86‑64, both BIOS and EFI.

Can I run Lightwhale on Raspberry Pi?

No, not currently.
							It's on thebacklog.

Can I run Lightwhale on Apple M‑series chips?

No, not bare‑metal. You can of coursevirtualizeit.

Can I run Lightwhale virtualized in VMWare/ESX/Proxmox/cloud/etc?

Yes,
							Lightwhale includes guest agents for QEMU/KVM (used by Proxmox) and VMware ESXi hypervisors.

Here's a quick and dirty way to boot the Lightwhale ISO in QEMU
							with a virtual disk image to testpersistence:

dd if=/dev/zero of=persistence.img bs=1M count=512echo "lightwhale-please-format-me" | dd conv=notrunc of=persistence.imgqemu-system-x86_64 -m 2G -hda persistence.img -cdrom lightwhale-3.0.0-x86.iso -boot d

How do I install software on Lightwhale?

Only Docker containers can be installed.
							Installing software directly onto the file system isnot possibleand would defeat thevery purposeof Lightwhale.

Wait, what? Is Lightwhale immutable or not?

The core system is immutable and cannot be modified.
							Configuration, customization, containers, etc.are written to memoryby default.
							Optionally, you canenable persistenceand only then are changes preserved across reboots.

How do I change the hostname?

The default hostname includes the machine ID to prevent hostname conflicts
							on the network.
							Changing the hostname takes effect immediately,
							except for the current shell environment,
							so either log out and back in, 
							or replace the shell. e.g:

sudo setup-hostname lightwhaleexec "$SHELL" -l

How am I covered if Lightwhale
						crashes, breaks something, makes me lose data/money/sleep/customers/reputation/spouse/hair/testicle/etc?

There is no warranty.
							Think, take responsibility of your own actions, and use at your own risk.

Can you please add 
wget
, 
nano
, 
$my_fav_app_omg_i_love_it
 to the root filesystem?

No, not likely.

I understand that can be disappointing
							not to have all the tools at your disposal,
							that you are accustomed to on a mainstream Linux system.
							Maybe you're used tonano, and now feel forced tolearnvi.
							But remember,
							this is a minimalisticpurpose-specificserver OS,
							and with that comes some compromises and limitations;
							you get one editor, one http client, and other preselected essentials.
							Everything neededisthere,
							but perhaps not in the shapes and sizesyouprefer.

What's the TL;DR of your Privacy Policy?

The Lightwhale Project doesn't care about your private data.
							That's entirelyyourbusiness.
							We don't want any of it,
							so we go to great lengths not to collect it.

Storing and processingpersonally identifiable informationcomes with serious responsibility:
							it must be protected withstrong security,
							handled with care and respect,
							and is subject to legal obligations under regulations like GDPR.

Taking on that burden for critical data we don't even need makes no sense.
							So we simply don't collect it.

If you opt-in on telemetry,we collectanonymous data only, and you can always review it.

How does Lightwhale comply with age-related regulations?

Lightwhale is an operating system, not an online service.
							It does not serve age-restricted content,
							and it does not identify or track its users.

If you are deploying services that are subject to age-related regulations, you are responsible for implementing appropriate compliance measures.