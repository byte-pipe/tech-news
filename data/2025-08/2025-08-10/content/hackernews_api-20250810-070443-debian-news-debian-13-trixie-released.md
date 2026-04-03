---
title: Debian -- News -- Debian 13 "trixie" released
url: https://www.debian.org/News/2025/20250809
site_name: hackernews_api
fetched_at: '2025-08-10T07:04:43.334892'
original_url: https://www.debian.org/News/2025/20250809
author: ducktective
date: '2025-08-10'
description: Debian 13 "Trixie"
tags:
- hackernews
- trending
---

# Debian 13trixiereleased

August 9th, 2025

After 2 years, 1 month, and 30 days of development, the Debian
project is proud to present its new stable version 13 (code nametrixie).

trixiewill be supported for the next 5 years thanks to the
combined work of theDebian Security teamand theDebian Long Term Supportteam.

Debian 13trixieships with several desktop environments, such as:

* GNOME 48,
* KDE Plasma 6.3,
* LXDE 13,
* LXQt 2.1.0,
* Xfce 4.20

This release contains over14,100new packages for a total count of69,830packages, while over8,840packages have been removed
asobsolete.44,326packages were updated in this release.
The overall disk usage fortrixieis403,854,660 kB (403 GB), and
is made up of1,463,291,186lines of code.

Thanks to our translators who have made theman-pages fortrixieavailable in multiple languages.

The manpages-l10n project has contributed many improved and new translations
for manual pages. Especially Romanian and Polish translations are greatly
enhanced since bookworm.
All architectures other than i386 now use a 64-bit time_t ABI, supporting dates
beyond 2038.
Debian contributors have made significant progress towards ensuring package
builds produce byte-for-byte reproducible results. You can check the status for
packages installed on your system using the new package debian-repro-status, or
visit
reproduce.debian.net
 for
Debian's overall statistics for trixie and newer.

Debian 13trixieincludes numerous updated software packages
(over 63% of all packages from the previous release), such as:

* Apache 2.4.64
* Bash 5.2.37
* BIND DNS Server 9.20
* Cryptsetup 2.7
* curl/libcurl 8.14.1
* Emacs 30.1
* Exim (default email server) 4.98
* GNUcash 5.10
* GNU Compiler Collection 14.2
* GIMP 3.0.4
* GnuPG 2.4.7
* Inkscape 1.4
* the GNU C Library 2.41
* LibreOffice 25.2
* Linux kernel 6.12 LTS series
* LLVM/Clang toolchain 19 (default), 17 and 18 available
* MariaDB 11.8
* Nginx 1.26
* OpenJDK 21
* OpenLDAP 2.6.10
* OpenSSH 10.0p1
* OpenSSL 3.5
* Perl 5.40
* PHP 8.4
* Postfix 3.10
* PostgreSQL 17
* Python 3, 3.13
* Rustc 1.85
* Samba 4.22
* Systemd 257
* Vim 9.1

With this broad selection of packages and its traditional wide
architecture support, Debian once again stays true to its goal of beingThe Universal Operating System. It is suitable for many different
use cases: from desktop systems to netbooks; from development servers to
cluster systems; and for database, web, and storage servers. At the same
time, additional quality assurance efforts like automatic installation and
upgrade tests for all packages in Debian's archive ensure thattrixiefulfills the high expectations that users have of a stable Debian release.

This release for the first time officially supports the riscv64
architecture, allowing users to run Debian on 64-bit RISC-V hardware and
benefit from all Debian 13 features. A total of seven architectures are officially supported fortrixie:

* 64-bit PC (amd64),
* 64-bit ARM (arm64),
* ARM EABI (armel),
* ARMv7 (EABI hard-float ABI, armhf),
* 64-bit little-endian PowerPC (ppc64el),
* 64-bit little-endian RISC-V (riscv64),
* IBM System z (s390x)

i386 is no longer supported as a regular architecture: there is no official
kernel and no Debian installer for i386 systems. The i386 architecture is now
only intended to be used on a 64-bit (amd64) CPU. Users running i386 systems
should not upgrade to trixie. Instead, Debian recommends either reinstalling
them as amd64, where possible, or retiring the hardware.

trixiewill be the last release for the armel architecture. See5.1.3.
Last release for armelin the release notes for more information on our ARM
EABI support.

The Debian Cloud team publishestrixiefor several cloud computing
services:

* Amazon EC2 (amd64 and arm64),
* Microsoft Azure (amd64),
* OpenStack (generic) (amd64, arm64, ppc64el),
* PlainVM (amd64, arm64, ppc64el),
* NoCloud (amd64, arm64, ppc64el)

The genericcloud image should be able to run in any virtualised environment,
and there is also a nocloud image which is useful for testing the build process.

Cloud images provide automation hooks via ``cloud-init`` and prioritize
fast instance startup using specifically optimized kernel packages and
grub configurations.

### Want to give it a try?

If you simply want to try Debian 13trixiewithout installing it,
you can use one of the availablelive imageswhich load and run the complete operating system in a read-only state via your
computer's memory.

These live images are provided for theamd64andarm64architectures and are available for DVDs, USB sticks,
and netboot setups.
The user can choose among different desktop
environments to try: GNOME, KDE Plasma, Cinnamon, MATE, LXDE, LXQt, and Xfce.
Debian Livetrixiehas a standard live image, so it is also possible
to try a base Debian system without any of the graphical user interfaces.

Should you enjoy the operating system you have the option of installing
from the live image onto your computer's hard disk. The live image
includes the Calamares independent installer as well as the standard Debian
Installer. More information is available in therelease notesand thelive install imagessections of the Debian
website.
Multi-architecture Debiantrixiecontainer images are also available onDocker Hub. In addition to the
standard images, aslimvariant is available to reduce disk usage.
The Debian Installer and Debian Live Images can now be booted usingHTTP Booton supported UEFI and U-Boot firmware.

To install Debian 13trixiedirectly onto your computer's storage
device you can choose from a variety of installation media types toDownloadsuch as: Blu-ray Disc, DVD, CD, USB stick, or via a network connection.
See theInstallation Guidefor more details.

Debian can now be installed in 78 languages, with most of them available
in both text-based and graphical user interfaces.

The installation images may be downloaded right now viabittorrent(the recommended method),jigdo, orHTTP; seeDebian on CDsfor further information.trixiewill soon be available on physical DVD, CD-ROM, and Blu-ray Discs from
numerousvendorstoo.

### Upgrading Debian

Upgrades to Debian 13trixiefrom the previous release, Debian 12bookworm, are automatically handled by the APT package
management tool for most configurations.

Before upgrading your system, it is strongly recommended that you make a
full backup, or at least back up any data or configuration information you
can't afford to lose. The upgrade tools and process are quite reliable, but
a hardware failure in the middle of an upgrade could result in a severely
damaged system.

The main things you'll want to back up are the contents of /etc,
/var/lib/dpkg, /var/lib/apt/extended_states and the output of:

$ dpkg --get-selections '*' # (the quotes are important)

We welcome any information from users related to the upgrade frombookwormtotrixie. Please share information by filing a bug in theDebian
bug tracking systemusing theupgrade-reportspackage with your results.

There has been a lot of development on the Debian Installer since its previous
official release with Debian 12, resulting in improved hardware support and
some very useful new features such asImproved hardware and software support for speech synthesisInitial and restricted support for rescuing Debian installed to a btrfs subvolumeChanged default unit from MB to GB when partitioning disksDisabled cdrom sources if installation medium is not a real CD (USB stick, SD card, ISO file), because APT cannot use it after the installationPlus support for secure boot with systemd-boot

It is advisable to remove bookworm-backports entries from APT source-list
files before the upgrade; after the upgrade consider addingtrixie-backports.

If your APT configuration also involves pinning orAPT::Default-Release,
it is likely to require adjustments to allow the upgrade of packages to the new
stable release. Please considerdisabling APT pinning.

Under some circumstances, issues might arise during the upgrade process, or
while runningtrixie.

For instance, the TLS support in the OpenLDAP clientlibldap2and serverslapdis now provided by OpenSSL instead of GnuTLS. This affects the available
configuration options, as well as their behavior. If no TLS CA
certificates are specified, the system default trust store will now be loaded automatically. If you do not want
the default CAs to be used, you must configure
the trusted CAs explicitly. For more information about LDAP client configuration,
see theldap.conf.5man page.

We have documented this and other possible issues at5. Issues to be aware
of for trixiein the release notes. You're advised to read that before upgrading.

As always, Debian systems may be upgraded painlessly, in place,
without any forced downtime, but it is strongly recommended to read
therelease notesas
well as theinstallation
guidefor possible issues, and for detailed instructions on
installing and upgrading. The release notes will be further improved and
translated to additional languages in the weeks after the release.

## About Debian

Debian is a free operating system, developed by
thousands of volunteers from all over the world who collaborate via the
Internet. The Debian project's key strengths are its volunteer base, its
dedication to the Debian Social Contract and Free Software, and its
commitment to provide the best operating system possible. This new
release is another important step in that direction.

## Contact Information

For further information, please visit the Debian web pages athttps://www.debian.org/or send mail to
<press@debian.org>.
