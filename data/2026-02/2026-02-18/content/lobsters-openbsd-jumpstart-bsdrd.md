---
title: OpenBSD Jumpstart | bsd.rd
url: https://openbsdjumpstart.org/bsd.rd/
site_name: lobsters
content_file: lobsters-openbsd-jumpstart-bsdrd
fetched_at: '2026-02-18T06:00:34.369088'
original_url: https://openbsdjumpstart.org/bsd.rd/
author: Wesley Mouedine Assaby
date: '2026-02-18'
description: 'Master the OpenBSD bsd.rd kernel: the definitive guide for installation, system upgrades, and disaster recovery. Learn how to boot and use the RAM disk kernel effectively.'
tags: openbsd
---

# Lab: Anatomy of
 bsd.rd — No Reboot Required

System:OpenBSD 7.8 / amd64Time:15 minutesPrerequisites:Root access on a running OpenBSD
 system

## What this lab is about

Every OpenBSD admin has bootedbsd.rdat least once
 — to install, upgrade, or rescue a broken system. But few people
 stop to look at what’s actually inside that file. It turns outbsd.rdis a set of nested layers, and you can take it
 apart on a running system without rebooting anything.

That’s what we’ll do here. We’ll go from the raw gzip file all
 the way down to the miniroot filesystem, exploring each layer with
 standard tools. Everything is documented in the man pages — we’re
 just following the trail.

Man pages we’ll use:rd(4),rdsetroot(8),vnconfig(8),vnd(4),disklabel(8),elf(5)

## Follow the SEE ALSO links

Before you start, take a look at how the man pages chain
 together. Each one points to the next through its SEE ALSO
 section:

rd(4) — ramdisk driver
│ SEE ALSO:
│ ├── elf(5)
│ └── rdsetroot(8) — insert/extract disk image into RAMDISK kernel
│ SEE ALSO:
│ ├── config(8)
│ ├── disklabel(8)
│ └── vnconfig(8) — configure vnode disks
│ SEE ALSO:
│ └── vnd(4) — vnode disk device driver

The developers already built the learning path. We’re just
 walking it.

## Step 1 — What
 does bsd.rd look like on disk?

Start by copying/bsd.rdto a working directory. We
 rename it.gzbecause that’s what it actually is:

# mkdir -p /tmp/lab && cd /tmp/lab
# cp /bsd.rd bsd.rd.gz
# file bsd.rd.gz

bsd.rd.gz: gzip compressed data, max compression, from Unix

So the file on your disk is gzip-compressed. Theboot(8)loader handles decompression
 on the fly — you never see this layer during normal operation.

## Step 2 — Strip the gzip
 layer

# gunzip bsd.rd.gz
# file bsd.rd

bsd.rd: ELF 64-bit LSB executable, x86-64, version 1

Now we can see what’s underneath: a standard ELF binary. Same
 format as/bin/lsor any other executable on the
 system, except this one is a kernel.

## Step 3 — Look at the ELF
 header

# readelf -h bsd.rd

ELF Header:
 Magic: 7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
 Class: ELF64
 Data: 2's complement, little endian
 Version: 1 (current)
 OS/ABI: UNIX - System V
 ABI Version: 0
 Type: EXEC (Executable file)
 Machine: Advanced Micro Devices X86-64
 Version: 0x1
 Entry point address: 0xffffffff81001000
 Start of program headers: 64 (bytes into file)
 Start of section headers: 9900144 (bytes into file)
 Flags: 0x0
 Size of this header: 64 (bytes)
 Size of program headers: 56 (bytes)
 Number of program headers: 5
 Size of section headers: 64 (bytes)
 Number of section headers: 13
 Section header string table index: 10

The first four bytes (7f 45 4c 46) spell out.ELFin ASCII — that’s the magic number every ELF
 binary starts with. Seeelf(5)for the full
 spec.

The entry point at0xffffffff81001000is where the
 CPU jumps after the bootloader loads the kernel into memory. The
 five program headers describe how to map the binary’s segments into
 the address space.

This is what the bootloader sees. Nothing special so far — it
 looks like any other kernel. The interesting part is what’s hidden
 inside.

## Step 4 — How big is
 the embedded ramdisk?

This is whererdsetroot(8)enters
 the picture. The man page says:

The-soption prints the size in bytes of the
 reserved space in the RAMDISK kernel.

# rdsetroot -s bsd.rd

3768320

That’s bytes. If you want something more readable, pipe it
 throughawk(1):

# rdsetroot -s bsd.rd | awk '{printf "%.2f MB\n", $1/1024/1024}'
3.59 MB

About 3.6 MB. That’s the space reserved inside the kernel binary
 for the embedded disk image. It’s there because this kernel was
 compiled withoption RAMDISKandpseudo-device rd— two kernel config directives that
 tell the build system to carve out room for a filesystem image. Therd(4)driver then makes that chunk of
 memory available as a block device at boot time. You can see all the
 kernel options inoptions(4).

## Step 5 — Extract the
 miniroot

Still fromrdsetroot(8):

The-xoption extracts the disk.fs image. The
 disk can be made accessible usingvnconfig(8), filesystems can be
 manipulated, and finally re-inserted into the RAMDISK
 kernel.

That last sentence is important — it means you can modify the
 miniroot and put it back. We’ll get to that later. For now, let’s
 just extract it:

# rdsetroot -x bsd.rd miniroot.fs
# file miniroot.fs

miniroot.fs: Unix Fast File system [v1] (little-endian), last mounted on ,
last written at Sun Oct 12 19:03:07 2025, clean flag 1, number of blocks
7360, number of data blocks 7071, number of cylinder groups 1, block size
4096, fragment size 512, minimum percentage of free blocks 0, rotational
delay 0ms, disk rotational speed 60rps, SPACE optimization

# ls -lh miniroot.fs
-rw-r--r-- 1 root wheel 3.6M Feb 16 18:31 miniroot.fs

That’s an FFS filesystem in a regular file. 3.6 MB, one cylinder
 group, 4096-byte blocks. This is the complete root filesystem that
 gets mounted as/when you bootbsd.rd.

## Step 6 — Mount and
 explore the miniroot

To access the filesystem inside that image file, we need two
 things:vnconfig(8)to attach the file to avnd(4)pseudo-disk device, andmount(8)to mount it.

# vnconfig vnd0 miniroot.fs

Let’s check the partition layout withdisklabel(8):

# disklabel vnd0

# /dev/rvnd0c:
type: vnd
disk: rdrootb
label:
duid: da67acb93404a776
flags:
bytes/sector: 512
sectors/track: 100
tracks/cylinder: 1
sectors/cylinder: 100
cylinders: 73
total sectors: 7360
boundstart: 0
boundend: 0

2 partitions:
# size offset fstype [fsize bsize cpg]
 a: 7360 0 4.2BSD 512 4096 920

One partition, type4.2BSD(FFS), covering the
 entire image. No swap, nothing else. Minimal.

Mount it read-only:

# mount -r /dev/vnd0a /mnt

### What’s inside

# ls -l /mnt

total 159
-rw-r--r-- 1 root wheel 1767 Oct 12 21:03 .profile
lrwxr-xr-x 1 root wheel 11 Oct 12 21:03 autoinstall -> install.sub
drwxr-xr-x 2 root wheel 512 Oct 12 21:03 bin
drwxr-xr-x 2 root wheel 2048 Oct 12 21:03 dev
drwxr-xr-x 5 root wheel 512 Oct 12 21:03 etc
lrwxr-xr-x 1 root wheel 11 Oct 12 21:03 install -> install.sub
-rw-r--r-- 1 root wheel 2942 Oct 12 21:03 install.md
-rwxr-xr-x 1 root wheel 65092 Oct 12 21:03 install.sub
drwxr-xr-x 2 root wheel 512 Oct 12 21:03 mnt
drwxr-xr-x 2 root wheel 512 Oct 12 21:03 mnt2
drwxr-xr-x 2 root wheel 1024 Oct 12 21:03 sbin
drwxrwxrwt 2 root wheel 512 Oct 12 21:03 tmp
lrwxr-xr-x 1 root wheel 11 Oct 12 21:03 upgrade -> install.sub
drwxr-xr-x 6 root wheel 512 Oct 12 21:03 usr
drwxr-xr-x 6 root wheel 512 Oct 12 21:03 var

The first thing that jumps out: three symlinks pointing to the
 same file.

autoinstall -> install.sub
install -> install.sub
upgrade -> install.sub

install.subis a 65 KBksh(1)script. It’s the single script
 that handles install, upgrade, and autoinstall — it checks$0to figure out which mode it was called in. Seeautoinstall(8)for how the auto mode
 works.

### The .profile — where it
 all starts

When the kernel finishes booting and spawns a shell,.profileruns. Here’s the interesting part:

export

VNAME
=
$(
sysctl

-n
 kern.osrelease
)

export

ARCH
=
$(
sysctl

-n
 hw.machine
)

export

OBSD
=
"OpenBSD/
$ARCH

$VNAME
"

It reads the version and architecture fromsysctl(8)at runtime — the same
 miniroot image works across releases because nothing is hardcoded.
 Then it prints the prompt everyone recognizes:

Welcome to the OpenBSD/amd64 7.8 installation program.
(I)nstall, (U)pgrade, (A)utoinstall or (S)hell?

It also calls/upgrade -axearly on to detect if
 there’s already an OpenBSD installation on disk. And if the system
 was PXE-booted or has an/auto_install.conffile, the
 autoinstall timeout kicks in after 5 seconds.

### The toolbox

The miniroot ships with just enough to get a system
 installed:

# ls /mnt/bin

arch chgrp cp dd ed hostname ln mkdir
mv rm sha256 sleep sync cat chmod date
df eject ksh ls mt pax sh sha512
stty tar

# ls /mnt/sbin

bioctl dmesg fsck_msdos init mount_cd9660
mount_nfs ping restore umount chown
fdisk growfs kbd mount_ext2fs mount_udf
ping6 route dhcpleased fsck halt
mknod mount_ffs newfs reboot slaacd
disklabel fsck_ffs ifconfig mount mount_msdos
newfs_msdos resolvd sysctl

# ls /mnt/usr/bin

doas egrep encrypt fgrep ftp grep gunzip gzcat
gzip less more sed signify tee

# ls /mnt/usr/sbin

chroot installboot pwd_mkdb

That’s it.fdisk(8)anddisklabel(8)to partition,newfs(8)to format,ftp(1)to download,signify(1)to verify,installboot(8)to make the disk
 bootable. Everything the installer needs, nothing it doesn’t.

### Devices and config

# ls /mnt/dev

Pre-created device nodes for the most common hardware —sd0,wd0,cd0,rd0(the ramdisk itself),bpffor network
 capture, console, random. Built byMAKEDEV(8).

# ls /mnt/etc

firmware fstab group hosts passwd protocols
pwd.db services signify spwd.db ssl

The bare minimum: user databases, thesignify(1)public keys for verifying
 install sets, and CA certificates inssl/for HTTPS
 downloads. That’s all you need to bootstrap trust.

## Step 7 — Clean up

# cd /tmp
# umount /mnt
# vnconfig -u vnd0
# rm -rf /tmp/lab

## Putting it all together

Here’s what we just took apart, layer by layer:

┌─────────────────────────────────────────────────────┐
│ bsd.rd (as distributed) │
│ └─ gzip compressed ← Step 1-2 │
│ └─ ELF 64-bit executable ← Step 3 │
│ ├─ Kernel code + data │
│ │ option RAMDISK │
│ │ pseudo-device rd ← Step 4 │
│ └─ Embedded FFS image ← Step 5 │
│ ├─ .profile (launches installer) │
│ ├─ install.sub (main script) ← Step 6 │
│ ├─ install → install.sub │
│ ├─ upgrade → install.sub │
│ ├─ autoinstall → install.sub │
│ ├─ bin/ sbin/ (minimal tools) │
│ ├─ dev/ (pre-created devices) │
│ └─ etc/ (signify keys, ssl certs) │
└─────────────────────────────────────────────────────┘

Tools used:file(1),gunzip(1),readelf(1),rdsetroot(8),vnconfig(8),disklabel(8),mount(8)

Man page chain:rd(4)→rdsetroot(8)→vnconfig(8)→vnd(4)

## Going further

You can modify the miniroot and put it back into the kernel.
 Extract, mount read-write, make your changes, unmount, and
 re-inject:

# vnconfig vnd0 miniroot.fs
# mount /dev/vnd0a /mnt
# echo "custom" > /mnt/custom.txt
# umount /mnt
# vnconfig -u vnd0
# rdsetroot bsd.rd miniroot.fs
# gzip -c9n bsd.rd > bsd.rd.new

That gives you a custombsd.rd— still bootable,
 with whatever you added inside.

For more on how the kernel is configured and built:

* options(4)— kernel config options,
 includingRAMDISK
* config(8)— how kernel configs are
 compiled
* boot(8)— the bootloader that loadsbsd.rd
* boot_config(8)— User Kernel Config
 (boot -c)

And if you want to go deeper into the kernel itself:

* intro(9)— section 9 of the manual,
 Kernel Developer’s Manual
* autoconf(9)— device autoconfiguration
 at boot
* boot(9)— kernel-side bootstrap and
 shutdown

Lab tested on OpenBSD 7.8/amd64 — February 2026All output captured from a live system. No reboot was harmed in
 the making of this lab.
