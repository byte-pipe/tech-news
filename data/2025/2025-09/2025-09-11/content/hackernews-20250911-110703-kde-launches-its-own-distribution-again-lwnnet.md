---
title: KDE launches its own distribution (again) [LWN.net]
url: https://lwn.net/SubscriberLink/1037166/caa6979c16a99c9e/
site_name: hackernews
fetched_at: '2025-09-11T11:07:03.825236'
original_url: https://lwn.net/SubscriberLink/1037166/caa6979c16a99c9e/
author: Bogdanp
date: '2025-09-11'
---

LWN
.net

News from the source






User:


Password:



 |


 |


Subscribe
 /

Log in
 /

New account

# KDE launches its own distribution (again)

## [LWN subscriber-only content]

### Welcome to LWN.netThe following subscription-only content has been made available to you
by an LWN subscriber. Thousands of subscribers depend on LWN for the
best news from the Linux and free software communities. If you enjoy this
article, please considersubscribing to LWN. Thank you
for visiting LWN.net!ByJoe BrockmeierSeptember 10, 2025AtAkademy 2025, the
KDE Projectreleasedan
alpha version ofKDE Linux, a
distribution built by the project to "include the best
implementation of everything KDE has to offer, using the most advanced
technologies". It is aimed at providing an operating system
suitable for home use, business use, OEM installations, and more
"eventually". For now there are many rough edges and missing
features that users should be aware of before taking the plunge; but
it is an interesting look at the kind of complete Linux system that
KDE developers would like to see.#### Development and goalsKDE contributor Nate Graham wrote anannouncement
blog poston September 6 to accompany the release of KDE
Linux. Harald Sitter had introduced the project as "Project Banana"
during a talk (video,slides)
atAkademy in 2024, and has
been leading its development along with major contributions from Hadi Chokr, Lasath Fernando,
Justin Zobel, Graham, andothers.KDE Linux is an immutable distribution that uses Arch Linux
packages as its base, but Graham notes that it is "definitely not
an 'Arch-based distro!'" Pacman is not included, and Arch is used
only for the base operating system. Everything else, he said, is
either compiled from source usingKDE Builderor installed
using Flatpak.Some may wonder why another Linux distribution is needed; Graham
said that he has expressed that sentiment himself in the past
regarding other distributions, but he thinks that KDE Linux is justified:KDE is a huge producer of software. It's awkward for us to not have
our own method of distributing it. Yes, KDE produces source code that
others distribute, but we self-distribute our apps on app stores like
Flathub and the Snap and Microsoft stores, so I think it's a natural
thing for us to have our own platform for doing that distribution too,
and that's an operating system. I think all the major producers of
free software desktop environments should have their own OS, and many
already do:Linux MintandElementaryOSspring to mind, andGNOME is working on one too.Besides, this matter was settled 10 years ago with the creation of
KDE neon, our first bite at the "in-house OS" apple. The sky did not
fall; everything was beautiful and nothing hurt.Speaking ofneon, Graham points
out that it is "being held together by a heroic volunteer"
(singular) and that no decision has been made as of yet about its
future. Neon has "served admirably for a decade", he said, but
it "has somewhat reached its limit in terms of what we can do with
it" because of its Ubuntu base. According to thewiki
page, neon's Ubuntu LTS base is built on old technology and
requires "a lot of packaging busywork". It also becomes less
stable as time goes on, "because it needs to be tinkered with to
get Plasma to build on it, breaking the LTS promise".#### Architecture and plansKDE Linux, on the other hand, is designed to be a greenfield
project that allows KDE to make use of newer technologies and more
modern approaches to a Linux distribution unhampered by the needs of a
general-purpose distribution. If KDE Linux's technology choices are
not appealing, Graham says, "feel free to ignore KDE Linux and
continue using the operating system of your choice. There are plenty
of them!"KDE Linux is Wayland-only; there is no X.org session and no plan
to add one. Users with some of the older NVIDIA cards will need tomanually
configure the systemto work properly with KDE Linux. The
distribution also only supports UEFI systems, and there are no plans
to add support for BIOS-only systems.The root filesystem (/) is a read/write Btrfs
volume, while/usris a read-onlyEnhanced
Read-Only File System(EROFS) volume backed by a single file. The
system is updated atomically by swapping out the EROFS volume;
currently KDE Linux caches up to five of the files to allow users to
roll back to previous versions if the most recent updates are
broken.The files have names likekde-linux_202509082242.erofsand
are stored in/system. The most recent releases are about
4.8GB in size. The project usessystemd-sysupdateunder the hood, whichdoes not have
support for delta updatesyet. Users should expect to set aside at least 30GB
just to cache the EROFS files for now.Unlike Fedora's image-basedAtomic Desktops,
KDE Linux does not supply a way for users to add packages to the base
system. So, for example, users have no way to add packages with
additional kernel modules. Userscanadd applications packaged as
Flatpaks using KDE's Discover graphical software manager; the
Snap format is also supported, but it is not integrated with
Discover—thesnapcommand-line
utility can be used to do install Snaps for now. KDE Linux also includesDistrobox, which allows users to set
up a container with the distribution of their choice and install
software in the container that is integrated with the system. LWNtouched onDistrobox in
our coverage of the Bluefin image-based operating system in December
2023.Unfortunately, itlooks
like users are not set up correctlyfor Podman, which Distrobox
needs, on KDE Linux; trying to set up a new container gives a
"potentially insufficient UIDs or GIDs available in user namespace"
error when trying to test Distrobox on the latest KDE Linux build.This
commentin the Podman repository on GitHub set me on the right
path to fix the problem. This kind of bug is to be expected in an
alpha release; no doubt it will be ironed out in the coming weeks or
months.System updates are also performed using Discover: when a new system
image is available, it will show up in the Updates tab and can be
installed from there. (Or using "sudo updatectl update" from
the command line, for those who prefer doing it that way.) Likewise,
installed Flatpaks with updates will show up in the Updates tab. For
now, at least, users will have to manually manage any applications
installed in a Distrobox container.The default software selection is a good start for a desktop
distribution; it includes the Gwenview image viewer, Okular document
viewer, Haruna media player, Kate text editor, and Konsole for
terminal emulation. Firefox is the only prominent non-KDE application
included with the default install. The base system currently includes
GNU Bash 5.3.3, curl 8.15, Linux 6.16.5, GCC 15.2.1, Perl 5.42, Python 3.13.7, Vim
9.1, and wget 1.25. It does not include some utilities users might
want or expect, such as GNU Screen, Emacs, tmux, pip, or alternate shells like Fish.KDE Linux's base packages are not meant to be user-customizable,
but it should be possible to create custom images using systemd'smkositool, which is what is used
by the project itself. Themkosi.conf.ddirectory in the KDE Linux repository contains the various
configuration files for managing the packages included in the system image.#### Development and what's nextThe plan, longer term, is to have three editions of KDE Linux: the
testing edition, which is what is available now, an enthusiast
edition, and a stable edition. The testing edition is meant for
developers and quality assurance folks; it is to be built daily from
Git and to be similar in quality to KDE neon's unstable release. The
enthusiast edition will include beta or released software, depending
on the status of a given application at the time; this edition is
aimed at "KDE enthusiasts, power users, and influencers". The
stable edition, as the name suggests, will include only released
software that meets quality metrics (which are not yet defined),
indicating it's ready for users not in the other categories.KDE Linux can beinstalled
on bare metalor in avirtual
machineusingvirt-manager. Support
for UEFI Secure Boot is currently missing. Since KDE Linux uses a lot
of space for cached images, users should provision more disk space for
a virtual machine than they might ordinarily; I allocated 50GB, but
probably should have gone with 75GB or more.Those wishing to follow along with KDE Linux development can check
out the milestone trackers for theenthusiastandstableeditions. All of themilestoneshave been reached for the testing edition. There are quite a few items
to complete before KDE Linux reaches beta status; for example, the
project is currently using packages from the Arch User Repository (AUR) but
the plan is tomove
away from using AURsoon. The project also needs tomove
production to official KDE infrastructurerather than depending on
Sitter's personal systems.At the moment, the project does not have a security announcement mailing
list or other notification mechanism; those using KDE Linux for more
than testing should keep an eye onArch's security trackerandKDE security advisories.
Since KDE Linux is an immutable derivative of Arch Linux, with no
way to immediately pull updated Arch packages, users should remember
that they will be at a disadvantage when there are security
vulnerabilities in the base operating system. Any security update would
need to be created by Arch Linux, pushed out as an Arch package, and
then incorporated into a build for KDE Linux. Conservatively, that
will add at least a day for any security updates to reach KDE Linux
users.One of the downsides of having no package manager is that there is
no easy way to take stock of what is installed on the system. Normally,
one might do an inventory of software using a package manager's query
tools; a quick "rpm -qa" shows all of the system software on
my desktop's Fedora 42 install. There is no such mechanism for
KDE Linux, and it's not clear that there are any plans for that type
of feature long term. To be suitable for some of the target audiences,
KDE Linux will need (for example) ways to manage the base operating
system and easily query what is installed.The project's governance isdescribed
asa "'Council of elders' model with major contributors being
the elders". Sitter has final decision-making authority in cases
of disagreement.Obviously the team working on KDE Linux wants the project to
succeed, but it has put some thought into what will happen if the
distribution is put out to pasture at some point. There is anend-of-life
contingency planto "push a final update shipping an OS image
that transforms the system into a completely different
distro". The successor distribution has not been chosen yet; it
would be picked based on the KDE Linux team's relationship with the other
distribution and its ability to take on all of the new users.Part of the rationale for KDE Linux is to satisfy an impulse that
is common to many open-source developers: the desire to ship software
directly to users without an intermediary tampering with it.
The process of creating and refining KDE Linux will satisfy
that for KDE developers, but it may also serve another purpose: to
demonstrate just how difficult it is to create and maintain a
desktop distribution for widespread use. Whether KDE Linux succeeds as a
standalone distribution or not, it may be a useful exercise to
illustratewhyprojects like Debian, Fedora, openSUSE, Ubuntu,
and others make choices that ultimately frustrate application
developers.to post comments



### Not using pre-existing immutable tools?Posted Sep 10, 2025 21:09 UTC (Wed)
 bypauldoo(subscriber, #124140)
 [Link] (1 responses)I haven’t looked super closely but it sounds like KDE Linux isn’t using existing solutions for delivering an immutable Linux, such as bootc, ABRoot, or ostree, but has built something new here..Is there a reason for that? Is what KDE Linux has done better suited than those tools in some way?### Not using pre-existing immutable tools?Posted Sep 11, 2025 2:23 UTC (Thu)
 bysalvesefu(guest, #179283)
 [Link]According to this presentation [1], they choose to use systemd-sysupdate [2] for system image management.[1]https://conf.kde.org/event/6/contributions/202/attachment...[2]https://www.freedesktop.org/software/systemd/man/latest/s...### HmmmPosted Sep 10, 2025 23:53 UTC (Wed)
 bygerdesj(subscriber, #5446)
 [Link]"Whether KDE Linux succeeds as a standalone distribution or not, it may be a useful exercise to illustrate why projects like Debian, Fedora, openSUSE, Ubuntu, and others make choices that ultimately frustrate application developers."

I've used all of the components of this thing at one time or another but I would not use them like this as a whole. I remember when KDE (around 1998) compiled and ran on my Slackware effort. Time has moved on.

This beast starts off with Arch - fine choice of rolling distro. No pacman ... hmm we are off piste now ... OK. It has an unusual partitioning scheme involving Butter Fuss and something-else-fs (EROFS). Arch is not normally deployed on that sort of combo but it probably has been done because Archers are prettyweirdadventurous.

Then it gets cute and immutable and all that stuff.

I hope it works out but I don't think that what I might charitably call a Window Manager flogger, should be fiddling with the rest of the OS. Stick with what you do well and leave the OS floggers to do their thing. A demo OS build is obviously a great way to advertise your wares.

For starters this distro will never be a corporate thing which is sad. I can get Kubuntu (int al) through all audits - ISO 9000, 27000, UK - Cyber Essentials and Essentials+.

*sigh*### Very nice articlePosted Sep 11, 2025 8:27 UTC (Thu)
 bynadir(subscriber, #154506)
 [Link]I could write this more often, but I found this article to be particularly pleasant to read.### Package manager.Posted Sep 11, 2025 10:14 UTC (Thu)
 byNN(subscriber, #163788)
 [Link]I'm really surprised at the absence of a package manager. I guess it's understandable, since if e.g., they picked pacman then this would look more like KDE Arch than its own thing... I guess I just hadn't considered that not having its own package manager was an option at all.





Copyright © 2025, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
