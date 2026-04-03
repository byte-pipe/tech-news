---
title: Y2K38 bug? Debian switching to 64-bit time for everything • The Register
url: https://www.theregister.com/2025/07/25/y2k38_bug_debian/
site_name: hackernews
fetched_at: '2025-07-29T07:05:16.808961'
original_url: https://www.theregister.com/2025/07/25/y2k38_bug_debian/
author: pseudolus
date: '2025-07-29'
---

#### OSes

# Debian isn't waiting for 2038 to blow up, switches to 64-bit time for everything



## We say everything... just not the oldest hardware. Unix Epochalypse less than 13 years away

Venerable Linux distribution Debian is side-stepping the Y2K38 bug – also known as the Unix Epochalypse – by switching to 64-bit time for everything but the oldest of supported hardware, starting with the upcoming Debian 13 "Trixie" release.

"[We will] use 64-bit time_t on 32-bit architectures to avoid the 'year 2038 problem' when the existing 32-bit signed int rolls over (potentially setting time back to 1900)," the Debian maintainers say of the move and the problem it aims to fix.

## The 'nothing-happened' Y2K bug – how the IT industry worked overtime to save world's computers

READ MORE

"This is now less than 15 years away and plenty of systems that will have problems have already been shipped. We should stop adding to the problem."

Readers of a certain vintage will remember well the "Y2K problem," caused by retrospectively shortsighted attempts to save a couple of bytes by using two-digit years – meaning that "2000" is represented as "00" and assumed to be "1900." While predictions of aircraft falling from the skies and bank balances being wiped out by negative-decades of interest did not, thankfully, come true, that was purely due to the tireless behind-the-scenes work of software developers who were able to patch affected systems before celebrating the turn of the century.

There's another, less well-known clock problem looming, however: theUnix Epochalypse,which affects any systems that measure time the Unix way – in seconds elapsed since January 1, 1970. Come the very precise time of 03:14:07 UTC on January 19, 2038, the number of seconds elapsed will be larger than can be represented by a signed 32-bit integer. This would be fine if the decision hadn't been made all those years ago to store the number of seconds in exactly such a format.

Rather than the last-minute scramble of the Y2K fix, software developers are already working on its upcoming cousin. Any software written for and running on 64-bit hardware is already safe, but Debian – which was launched by founder Ian Murdock back in 1993, and is the second-oldest actively developed Linux distribution behind the one-month-older Slackware – is the distro of choice for older and resource-constrained embedded devices based on 32-bit processors.

"There is quite a lot of cost-sensitive 32-bit computing still out there, and still shipping new devices (automotive, IoT, TVs, routers, plant control, building monitoring/control, cheap Android phones)," the Debian developers explain. "Most such new hardware will be running build-from-source OSes like OpenEmbedded, or Alpine, Android, or Gentoo, but the Debian-based niche is likely to remain for some years, and some stuff built with it is likely to be in use/installed for long enough to hit Jan 2038."

* Y2K quick-fix crick? 1920s come roaring back after mystery blip at UK's vehicle licensing agency
* Need 32-bit Linux to run past 2038? When version 5.6 of the kernel pops, you're in for a treat
* Linux 5.10 to make Year 2038 problem the Year 2486 problem
* Curious tale of broken VPNs, the Year 2038, and certs that expired 100 years ago
* Epoch-alypse now: BBC iPlayer flaunts 2038 cutoff date, gives infrastructure game away

The fix is to move to a 64-bit integer, even when running on 32-bit hardware. It's no small change: Debian's maintainers found the relevant variable, time_t, "all over the place," spread across a total of 6,429 packages. As the move requires a breaking change to the application binary interface (ABI), it also has to happen across all affected libraries simultaneously.

While that was a chunk of work, Debian is confident it is now complete and tested enough that the move will be made after the release of Debian 13 "Trixie" – at least for most hardware.

"The i386 port will be left with the existing 32-bit time_t, as a compatibility architecture for existing x86 binaries," the maintainers say. "A new 'i686' x86 ABI/architecture using 64-bit time, and potentially newer ISA features, could be created if there was sufficient enthusiasm for dragging 32-bit x86 into its now very limited future. The hurd-i386 port is not going to be switched, as its kernel lacks support, and efforts are underway instead to switch to hurd-amd64."

More information, including on how developers can test to see if the shift to 64-bit time breaks their software, is available on theDebian wiki. ®



Get our

Tech Resources

Share

#### More about

* Debian
* Linux
* Y2K

More like these

×

### More about

* Debian
* Linux
* Y2K

### Narrower topics

* Asahi Linux
* CentOS
* Fedora
* GNOME
* Linux Foundation
* One Way Forward
* Ubuntu
* Windows Subsystem for Linux

### Broader topics

* FOSS
* Linus Torvalds
* Operating System
* Vulnerability

#### More about

Share

#### More about

* Debian
* Linux
* Y2K

More like these

×

### More about

* Debian
* Linux
* Y2K

### Narrower topics

* Asahi Linux
* CentOS
* Fedora
* GNOME
* Linux Foundation
* One Way Forward
* Ubuntu
* Windows Subsystem for Linux

### Broader topics

* FOSS
* Linus Torvalds
* Operating System
* Vulnerability

#### TIP US OFF

Send us news
