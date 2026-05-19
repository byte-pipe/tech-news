---
title: OpenBSD 7.9
url: https://www.openbsd.org/79.html
site_name: hnrss
content_file: hnrss-openbsd-79
fetched_at: '2026-05-19T19:37:16.552640'
original_url: https://www.openbsd.org/79.html
date: '2026-05-19'
description: OpenBSD 7.9
tags:
- hackernews
- hnrss
---

## OpenBSD7.9

Released May 19, 2026. (60th OpenBSD release)

Copyright 1997-2026, Theo de Raadt.

7.9 Song: "
Diamond in the Rough
"

Artwork by Lyra Henderson.

* See the information onthe FTP pagefor
 a list of mirror machines.Go to thepub/OpenBSD/7.9/directory on
 one of the mirror sites.Have a look atthe 7.9 errata pagefor a list
 of bugs and workarounds.See adetailed log of changesbetween the
 7.8 and 7.9 releases.signify(1)pubkeys for this release:openbsd-79-base.pub:RWTSdNN9A3yvWNn7mUjXwv9DOCOUnyfuV+mq1iGPIfD+NhN8EYnEQ1atopenbsd-79-fw.pub:RWQdmBb/OCe1hXE08xCj5VLnBpGpphy7kYPdU3oWyfnrwswjtl8K385Eopenbsd-79-pkg.pub:RWSw1kDLJJy6OYgnayEMReLV57z2rzx5jYNCghO+2ARwqd6KuwGFWSn7openbsd-79-syspatch.pub:RWTJmz/ur68S9e26/JVRr7T88lAPZIF3YgZ3w2lDnf/frAxTerC/DrZ6
* Go to thepub/OpenBSD/7.9/directory on
 one of the mirror sites.Have a look atthe 7.9 errata pagefor a list
 of bugs and workarounds.See adetailed log of changesbetween the
 7.8 and 7.9 releases.signify(1)pubkeys for this release:openbsd-79-base.pub:RWTSdNN9A3yvWNn7mUjXwv9DOCOUnyfuV+mq1iGPIfD+NhN8EYnEQ1atopenbsd-79-fw.pub:RWQdmBb/OCe1hXE08xCj5VLnBpGpphy7kYPdU3oWyfnrwswjtl8K385Eopenbsd-79-pkg.pub:RWSw1kDLJJy6OYgnayEMReLV57z2rzx5jYNCghO+2ARwqd6KuwGFWSn7openbsd-79-syspatch.pub:RWTJmz/ur68S9e26/JVRr7T88lAPZIF3YgZ3w2lDnf/frAxTerC/DrZ6
* Have a look atthe 7.9 errata pagefor a list
 of bugs and workarounds.See adetailed log of changesbetween the
 7.8 and 7.9 releases.signify(1)pubkeys for this release:openbsd-79-base.pub:RWTSdNN9A3yvWNn7mUjXwv9DOCOUnyfuV+mq1iGPIfD+NhN8EYnEQ1atopenbsd-79-fw.pub:RWQdmBb/OCe1hXE08xCj5VLnBpGpphy7kYPdU3oWyfnrwswjtl8K385Eopenbsd-79-pkg.pub:RWSw1kDLJJy6OYgnayEMReLV57z2rzx5jYNCghO+2ARwqd6KuwGFWSn7openbsd-79-syspatch.pub:RWTJmz/ur68S9e26/JVRr7T88lAPZIF3YgZ3w2lDnf/frAxTerC/DrZ6
* See adetailed log of changesbetween the
 7.8 and 7.9 releases.signify(1)pubkeys for this release:openbsd-79-base.pub:RWTSdNN9A3yvWNn7mUjXwv9DOCOUnyfuV+mq1iGPIfD+NhN8EYnEQ1atopenbsd-79-fw.pub:RWQdmBb/OCe1hXE08xCj5VLnBpGpphy7kYPdU3oWyfnrwswjtl8K385Eopenbsd-79-pkg.pub:RWSw1kDLJJy6OYgnayEMReLV57z2rzx5jYNCghO+2ARwqd6KuwGFWSn7openbsd-79-syspatch.pub:RWTJmz/ur68S9e26/JVRr7T88lAPZIF3YgZ3w2lDnf/frAxTerC/DrZ6

All applicable copyrights and credits are in the src.tar.gz,
sys.tar.gz, xenocara.tar.gz, ports.tar.gz files, or in the
files fetched viaports.tar.gz.

### What's New

This is a partial list of new features and systems included in OpenBSD 7.9.
For a comprehensive list, see thechangelogleading to 7.9.Platform-specific improvements:arm64:Enabledice(4)on arm64.Added support for the RK3588 and RK3576 SoCs with new or additions to existing drivers.Added support for the Genesys Logic GL9755 SDHC controller
	(which includes the SDHC controller on some of the Apple Silicon
	laptops) tosdmmc(4).amd64:Added SMU support toamdpmc(4). The SMU is a
	microcontroller buried deep in the bowels of AMD SoCs and needs to be
	tickled in order to reach the lowest power states in suspend.Disabled Panel Self Refresh (PSR) in amdgpu to avoid a potential hang on a ThinkPad X13 gen 6.Increased MAXCPUs on amd64 to 255.On amd64, we now zero the DM PTE/PDE pages before use. This fixes a bug on machines with more than 512GB RAM.Mitigated floating point state leakage observed on AMD Zen/Zen+ (Zen 1).luna88k:Switched luna88k compiler to gcc4.Switched luna88k to PIE (Position Independent Executables) by default.riscv64:Systems with a SpacemiT K1 SoC gained support with the following (and more) changes:Addedsmtclock(4), a driver for the clock/reset controller on the SpacemiT K1 SoC.Added many more drivers to support the SpacemiT K1 SoC.Implemented support for the Zicbom (Cache-Block Management) and Svpbmt (Page-Based Memory Types) extensions.Added the SpacemiT K1 device trees onto the riscv64 miniroot making them accessible during installation.Made "Instruction access fault" (EXCP_FAULT_FETCH) traps being treated as PROT_EXEC. This fixes random SIGSEGV on the SpacemiT X60 cores.Added SpacemiT K1 support todwpcie(4).Otherarchitectures:Fixed various errors on big-endian systems inice(4)to make it work on sparc64.Changedpowerpc64memory barriers to "sync".Reworked and improved TLB shootdown onalpha.Hoisted mips64 CPU accounting to get multiple softnet threads on MP systems.Made sure to initialize all FPU registers on sparc64 to all 1 (or -NaN), and not only the lower 32 registers.Fixed parking mutex on sun4u sparc64 cpus.More platform-specific changes can be found in thehardware supportsection below.Various kernel improvements:Introduced a mechanism to manage CPU cores with different speeds
	in the scheduler. Thesysctl(8)variable
	"hw.blockcpu" takes a sequence of 4 letters: S (for SMT), P (regular
	performance CPU), E (efficient CPU, generally 80% to 50% as fast), and
	L (lethargic CPU) which are even slower. Set this to select CPUs to
	kick out of the scheduler (SL by default). Currently works on amd64 and arm64.Replaced the cas spinlock in kernel mutexes with a "parking" lock.Stopped forcing the page daemon to sleep when there are outstanding paging requests.Implemented addb(4)stop command that sends a SIGSTOP to the specified pid.Madeddb(4)output visible when entering ddb from X on amdgpu.Added infrastructure to allow future support of up to 52 partitions per disk.Made changes to avoid memory allocation from within the swapencrypt path of the
	pagedaemon by pre-allocating 32 swapclusters up-front.Changed the strategy by which the pagedaemon creates free memory
	by overshooting the creation of inactive and free pages, in order to
	defragment memory.Refuse to load a binary without a PT_LOAD exec segment.Suspend/Hibernate Support:Implemented delayed hibernation:In order to prevent running out of battery while suspended, this
	feature wakes up a suspended system after a configurable time to then
	immediately perform a hibernation. Themachdep.hibernatedelaysysctl(2)is used to
	configure the number of seconds after which the system will wake up
	from suspend and hibernate itself.SMP Improvements:Unlockedsocket splicing.Unlocked icmp6_sysctl().Unlocked the IGMP slow timeout.Enabled parallel fault handling on amd64 and arm64.Madebse(4)interrupts mp-safe.Protected the IGMP and MLD6 fast timers with an rwlock.Direct Rendering Manager and graphics drivers:Updateddrm(4)to
	Linux 6.18.22.VMM/VMD and virtualization improvements:Adopted PCI-based semantics for reading unsupported or invalid registers by returning all 1's. Newer Linux kernels have started using 128-bit feature spaces.Addedsysctl(8)machdep.vmmode to indicate status as a host or guest (and SEV mode).Added vmboot, a tiny kernel that allowssysupgrade(8)to work forvmd(8)VMs.Allowedcd(4)/vioscsi(4)on a VM
	to use confidential computing methods, e.g. AMD SEV.Fixed a segfault invmd(8)during vmmci timeout firing.Enabled 32-bit direct kernel launch for both amd64 and i386 in vmd(8).Fixed a race invmd(8)vm pause barrier usage.Fixed a race in vmm(4) vm termination path.Added emulation of AMD SysCfg MSR in vmm(4).Made OpenBSD work on Apple Virtualization.Only exposepvclock(4)invmm(4)if tsc frequency is known.Reducedvmd(8)lowmem area in the memory map to help Linux guest reboot issues.Preventedvmd(8)pause deadlock when vcpu doesn't halt.Fixed timer emulation-related OpenBSD-i386 VM hangs when using the i8254 hardware timecounter withvmm(4).Madevio(4)recover from missed RX interrupts.Fixedvmd(8)vionet reset race leading to broken networking.Various new userland features:Dynamically determine the possible partition names to show in thedisklabel(8)editor
	a(dd) command help message.Allow thedisklabel(8)'d'elete
	editor command to zero out FS_UNUSED partitions despite current value
	of d_npartitions.Added display of the close-on-fork flag as 'f' in R/W column tofstat(1).Added support for the XDG_RUNTIME_DIR environment variable inlogin(1)andxenodm(1)vialogin_cap(3). Set it by default, pointing to/tmp/run/user/${uid}which gets created if needed.More bugfixes and tweaks in userland:Madelibsndiorestart the audio(4) device upon underrun.Enable fall-back audio devices by default insndiod(8).Simplified the Unix socket binding code insndiod(8).Simplified cookie handling inlibsndio.Enabled recording and monitoring at the same time insndiod(8).In theLLVM compiler, fixed x86 frame lowering for -msave-args.Madepthread_set_name_np(3)succeed with long thread names instead of silently failing.Handle calls to libc'sfreeaddrinfo(3)function with a NULL argument, instead of crashing, and improve the manpage.Madepcidump(8)print PCI bridge windows when they are "open".Fixed aneditline(3)bug that truncates completion candidates when the input wraps to a new line.Addedfile(1)support for PSF2 fonts detection.Addedfile(1)support for Web Open Font Format (WOFF) detection.Fixedmg(1)replace-regexp issues.Improved handling ofstrdup(3)failures inmg(1).Improved the "No changes need to be saved" check inmg(1).Dropped the initialization ofcurseswhenksh(1)is
	not started interactively. This avoids opening and parsing of theterminfo(3)file.Addedecho(1)-eto
	process escape sequences and support for multiple groups of dash args
	like ksh's echo.Increased the length of arguments that can be given topkill(1). This allows
	matching of commands with longer command line arguments.Made the-0option override-Einxargs(1).SetmetaSendsEscapeby default inxterm(1).Fixed leap year detection innewsyslog(8).Fixedless(1)crash on reading an invalid tags file.Fixed a memory leak onsensorsd(8)configuration reload.Improved hardware support and driver bugfixes, including:Tweaked PCI device power management such that drivers can change their own power state. Letxhci(4)power itself down
	such that its companion USB4 controller can go to sleep in its DVACT_POWERDOWN implementation.Addednhi(4), a driver for USB4 controllers.Added anaudio(9)driver interface to expose the hardware's display name.Changedenvy(4)anduaudio(4)devices to return the product name as the display name.Handleuaudio(4)devices with a single clock exposed in multiple domains.Fixed unintended truncation ofuaudio(4)device names when printing them in libsndio applications.Improvedacpi(4)handling of PCI bridges.Implemented "StorageD3Enable" support inacpi(4).Stoppedacpi(4)from calling the PCI function when an AML node has neither _ADR nor _HID, and avoid a panic on the ThinkPad X40.Addediasuskbd(4)support for special keys on the ASUS I2C laptop keyboards.Addedsgmsi(4), a driver for the MSI controller implementation on Sophgo SG2042 SoCs.Addedcdpcie(4), a driver for the Cadence PCIe controller, supporting the variant found on the Sophgo SG2042 SoC.Addeddwpcie(4)Qualcomm SC7280 support.Addedqcuart(4), a driver for Qualcomm GENI UART serial consoles.Addedsmtgpio(4), a driver for the GPIO controller found on SpacemiT K1 SoCs.Addedrkusbdpphy(4), a driver for the USB DP Combo PHY on Rockchip SoCs.Added support for blocking reads tofuse(4).Added basic implementation of the low-level FUSE API sufficient to compile and run lowntfs-3g.Alloweduhidev(4)to attach to and work with devices that don't have an input interrupt endpoint.Added theispi(4)driver for Intel LPSS SPI controller.Added an Apple variant to the "de" keyboard encoding forwskbd(4).Addedacpihid(4), a driver for the Generic Buttons Device defined by the ACPI specification.Madeviogpu(4)viogpu_wsmmap() return a physical address viabus_dmamem_mmap(9).Added support for "Apple Inc. Virtual USB Digitizer", to expose the touchpad on Apple Virtualization.Added support for the PSP found on the AMD EPYC 9005 topsp(4).Added support for the AlphaSmart Dana touvisor(4)as a PALM4 device.Added support for more line speeds touplcom(4).Added support for the RK3528 SoC to thedwmshc(4)eMMC controller driver.Inwscons(4)disallowed loading if mapchar emulops require a question mark character that is missing.New or improved network hardware support:Fixed memory leaks inbnxt(4).Inumb(4), made uplink and downlink speeds visible throughkstat(4).Added support for Quectel EC200A LTE modems toumsm(4).Addedrge(4)support for RTL8126 chip revision 0x64a00000.Turned on SoftLRO by default onbnxt(4)andice(4).Fixed theice(4)"too many data commands" error on TSO packets.Increased theurndis(4)buffer size to 16k.Fixed an issue wheredwqe(4), e.g. on aveb(4), doesn't recover when the link is down but packets are bridged.Made the output ofbse(4)mp-safe.Enabled 64-bit DMA transfers onaq(4),em(4),rge(4),re(4),iavf(4),ix(4),ixv(4),ixl(4),igc(4),ice(4)andiwx(4).Added support for BCM575xx devices (also known as Thor or P5) tobnxt(4).Addedsmte(4), a
	driver for the ethernet interfaces of the SpacemiT K1 SoC.IEEE 802.11 wireless stack improvements and bugfixes:Fixed association to access points which have all 802.11b rates disabled.Updatedieee80211_classify()to RFC8325 to prioritize interactive SSH sessions correctly, and
	rate-limit high-prio QoS packets.Initialized TIDs 4-7 to improve QoS behaviour during Tx aggregation.Added basic 802.11ax support.Added support for a 160 MHz window at 5 GHz and enabled it oniwx(4).Added or improved wireless network drivers:Improved chances ofqwx(4)receiving the initial WPA handshake message.Reinitialized theqwx(4)HAL state when resuming from suspend.Enablediwx(4)on i386.Added PMF (Protected Management Frames) support toiwm(4),iwx(4), andqwx(4), and add support for
	802.11 AKM SHA256-PSK toifconfig(8)and enable
	it by default if the driver supports PMF.Fixediwx(4)issues related to roaming and PMF and firmware crypto keys.Set the assoc ID field iniwx(4)firmware commands correctly.Added support for BZ devices with WiFi 6e radio toiwx(4).Made iwx(4) not load incomplete firmware images and report a proper error instead.Fixediwn(4)setting of DMA base addresses of Tx rings 17 and beyond.Added powersave support toiwx(4)and enable by default.Added support for 160 MHz channel width toiwx(4).Increased the VHT frame aggregation size limit from 64k to 1024k oniwx(4).Alignediwx(4)antenna patterns and STBC with iwlwifi.Installer, upgrade, bootloader, and pkg-tools improvements:Allowinstallboot(8)to finish, even ifefi(4)can't be accessed.Made sysupgrade fail ifdf /usrsays the filesystem is over 90% full, rather than potentially completely breaking the system.Scan both dmesg.boot anddmesg(8)output for devices withfw_update(8).On amd64, added support for loading files (kernels) from the EFI system
	partition. This means one can put the OpenBSD boot loader and bsd.rd
	on the EFI boot partition and run the installer that way. This already works on arm64.Improvedkeydisk partitiondetection in the installer.Addedaggr(4)support to arm64 RAMDISK and i386/amd64 RAMDISK_CD.Increased the auto-allocated partition size of/usr/objindisklabel(8).Floppy install users on i386/amd64 may findfw_update(8)for some
	drivers will not work because pci strings in the kernel have become
	too large.Security improvements:Stop allowing root to bypass the effects ofbpf(4)BIOCLOCK.
 BIOCLOCK is intended to remove the ability to reconfigure
 a BPF descriptor, but root processes were not subject to
 this revocation of privileges. No software relied on root
 being able to reconfigure a BPF descriptor, so this exemption
 was been removed.Retired thepledge(2)'tmppath'
	promise. The use ofunveil/tmp rwc,unveil / ror similar together withpledge "rpath wpath cpath"replaces all use cases of 'tmppath' in a safer way.Introduced the__pledge_open(2)system call, allowing libc to open a small set of tightly controlled
	internal files even when pledge(2) and unveil(2) would otherwise
	disallow direct access. File descriptors obtained this way are
	restricted to read-only use and cannot be used with write(2),
	chmod(2), chflags(2), chown(2), ftruncate(2), or fdpassing. This lets
	libc handle required devices, pledge-dependent files, and zoneinfo
	data without preserving the old pledge_namei() shortcut that allowed
	non-libc code to open the same special files.In pledged processes, made/etc/localtimeand/usr/share/zoneinfoscans much stricter.Indig(1), fixed
	pledge/unveil issues relating to manual opening of/etc/resolv.conf.Fixedunveil(2)to
	handle a filesystem that is mounted on a mount point that is itself
	the root of another filesystem.Startfork(2)'ed children without apgrpset (i.e. NULL) and update the
	pgrp pointer late to fix a potential race.Do not expose p_addr kernel address throughsysctl(2)unless root.For sysctl({CTL_KERN, KERN_TTY, KERN_TTY_INFO), only export the
	t_session kernel address pointer if the caller is root.New features in the network stack:Made the Virtual Ethernet Bridgeveb(4)a VLAN-aware
	bridge.Ports in veb(4) now have a PVID (port VLAN identifier)
	used to determine which VLAN untagged packets get associated with, and
	a bitmap of allowed VIDs (VLAN IDs) that say what VLANs tagged traffic
	can interact with. Ports can be configured as "access" ports by only
	configuring a pvid but with no entries in the vid map, or as a "trunk"
	by disabling the pvid and adding entries to the vid map, or a "hybrid"
	port by configuring both a pvid and entries in the vid map. To
	maintain compatibility with existing (simple) setups, veb defaults to
	using pvid 1 on ports added to the bridge.Added a LOCKED flag toveb(4)ports that are added
	to abridge(4). This
	makes sure that the source MAC address of frames received by these
	ports has an entry in the fib/address cache pointing at the same
	interface.InIPFIX/Netflow
	v10, added a NAT template with post-NAT source and destination IP
	address and ports, allowing use of pflow to track internal to external
	translations.Enabled IPv6 autoconf (SLAAC) by default.Further changes and bugfixes in the network stack:Implemented "checksum offload" betweenrport(4)pairs. This allows
	the kernel to skip ip/tcp/udp checksum calculation for packets between
	rdomains.Implemented IFCAP_TSO inrport(4). This allows
	the stack to pass large tcp frames between rdomains.Inrport(4), made changes to use
	multiple txqs to spread traffic handling over softnet threads.Fixed a panic when autodial (link1) onpppoe(4)tries to run.Allowedbpf(4)in
	tun_dev_read to see VLAN tags when IFCAP_VLAN_HWTAGGING is enabled.Added XOR and MOD operations tobpf(4).Madetpmr(4)work
	with ether_offload_ifcap likeveb(4)andbridge(4).Added Private VLAN support to veb(4) as per RFC 5517.Allowed VLAN tags (and therefore VLAN interfaces) on top of vports.Made use of per-CPU refs in the input path instead of doing one refcnt per port
	to improve performance ontpmr(4),veb(4)andaggr(4).Removed lacp support fromtrunk(4), now better
	supported byaggr(4).Introduced a global interface queue limit.
	Limit all multiqueue network interfaces to common IF_MAX_VECTORS.
	Currently it is set to 8. One global limit helps to find an optimal
	value, stops wasting interrupt vectors, and clarifies what the
	actual hardware or driver limitations are.Updated codel implementation to comply with RFCs 8289 and 8290.Improvedvio(4)feature negotiation for Large Receive Offload/TCP Segmentation Offload.Prevented false ELOOP error in socket splicing withSO_SPLICE.Made the network stack ignore TCP SACK packets with invalid sequence numbers to prevent potential kernel crash.The following changes were made to thepf(4)firewall:Introduced source and state limiters inpf(4). See theSource Limiterssection inpf.conf(5).Extendedpf(4)limiters so an administrator can specify the action the rule executes when limit is reached.Inpfctl(8), changed default limiter action from no-match to block.Havepf(4)state and source limiter state cleanup assert on the right lock.Fixedpfctl(8)with-nvf ...option to provide output which matches pfctl
	grammar for rules that use source/state limiters.Print both nat-to and rdr-to inpfctl(8)show rules.Routing daemons, network services and other userland network programs saw the following improvements:Do not log an error whendhcp6leased(8)cannot
	add a route because it already exists.Indhcpleased(8), do not
	pass pointers over process privilege boundaries via imsg, only data.Do not log an error whenslaacd(8)cannot
	add a route because it already exists.Fixed a buffer overflow reachable via rogue router advertisements inslaacd(8).Prevented potentialslaacd(8)crash if an
	attacker on the same layer 2 network sends rogue router
	advertisements.Changedospf6d(8)rc.d script to disallow reload, since ospf6d does not support it.Fixedsmtpd(8)dying
	if a malformed imsg is sent on the local socket.Improved the logging of filter processing insmtpd(8).Changed the default "tagged" operation forifconfig(8)to add VLAN
	IDs rather than replace them.Allowed theifconfig(8)andbrconfig(8)"tagged"
	operation to accept multiple VIDs and/or ranges of VIDs.Added support for non-default config file paths tounbound(8)rc.d script.Inunwind(8),
	allow one to configure forced resolvers outside of preference blocks.Added a "no banner" option to suppress the Server header inhttpd(8).Restoredhttpd(8)server_http_time() use of GMT.Madehttpd(8)error out on presence of Content-Length and Transfer-Encoding headers
	for GET, HEAD and other methods that should have no body.Made relayd(8) and httpd(8) use the same internal log functions as bgpd(8) (and several other daemons).Restoredrelayd(8)relay_http_time() use of GMT.Addedrelayd(8)support for PROXY protocol in TCP relays.Set a User-Agent in HTTP health checks sent byrelayd(8).Fixed a race condition inrelayd(8)that could cause a crash during configuration reload.Maderelayd(8)support TLS with multiple listeners.Fixedftp(1)http_time() to use GMT, not UTC, per RFC 9110.Report success inftp(1)when a file is fully retrieved.Madetcpdump(8)show the 802.11 QoS TID with -v.Added printing of NetBIOS and DNS servers in IPCP totcpdump(8).Extendedtcpdump(8)for printing of DHCPv6 information.Made sure that internal counters do not go out of bounds if the-nor-Atraceroute(8)options
	are specified more than once.Raisedrad(8)lifetimes for the router, DNS and NAT64 to 60 minutes and lower the
	prefix valid lifetime to 60 minutes. It does not make sense for one piece of
	information to time out before another when these are transmitted in one router
	advertisement packet.Fixed a hang inrad(8)andslaacd(8)when they
	receive an RA from the local network with an ND option of length zero.acme-client(1)saw several changes:Madeacme-client(1)only display port numbers in Host headers when the port is not 443.Added support for IP Address certificates inacme-client(1).Made changes to use ASN1_STRING_* accessor functions instead of reaching into ASN1_STRING objects directly.Inbgpd(8):Rewrote the Adj-RIB-Out handling to be more memory efficient and
	faster. For large IXP route server deployments a reduction in memory
	usage of more than 50% should be feasible.Process UPDATE messages in two phases: first update Adj-RIB-In,
	Loc-RIB, and FIB, then process all the Adj-RIB-Out tables. This
	significantly reduces the latency since updating all the Adj-RIB-Out
	tables could take a fair amount of time.Introduced CH hash tables - a scalable hash map implementation
	that boosts performance through improved cache locality.Introduce new metrics that track the amount of time spent in
	various parts of the main event loop of the route decision engine.Fixed various non-critical things uncovered by Coverity scanner.Improved outbound filter performance by storing the rules in
 an array and also deduplicate equal filters across peers.
 This and the filter_set change reduce the initial sync duration of
 large route servers by more than 25%.Improved performance of filter_sets processing in the RDE process
 by moving to a linear array of set objects to reduce cache misses.Added better logging for attribute parse errors which cause a
 session reset via UPDATE ATTRLIST error notification.Introduced various additional memory metrics which are part
 of the 'show rib memory' command. Some values are also tracked
 per-neighbor and visible via 'show neighbor'.Fixed logic error when handling per-peer and per-group MRT message
 dump configurations.Inrpki-client(8):The Canonical Cache Representation underwent a breaking change after the
 adoption ofdraft-ietf-sidrops-rpki-ccras a SIDROPS working group item. Apart from several CMS-related cosmetics,
 it now uses an IANA-assigned content type. As a result, rpki-client 9.7
 cannot parse rpki-client 9.6's .ccr files and vice versa.Support for Ghostbusters Record objects (RFC 6493) has been removed.
 Nobody showed interest in deploying this and there are other, widely
 supported ways of exchanging operational contact information such as
 RDAP. RFC 6493 is undergoing a status review to be marked as historic:status-change-rpki-ghostbusters-record-to-historicPrepare the code base for the opaque ASN1_STRING structure in OpenSSL 4.Fixed two reliability issues: one where a malicious RPKI Certification
 Authority can trigger a crash, one where a malicious Trust Anchor can
 provoke memory exhaustion. Thanks to Xie Yifan for reporting.Various refactoring for improved compatibility with various libcrypto
 implementations and in CA/BGPsec certificate handling.Fixed an accounting issue in HTTP gzip compression detection.Added a warning in extra verbose mode (-vv) about standards
 non-compliant Issuer and Subject ASN.1 string encodings.Added a check for canonical encoding of ASPA eContent in alignment
 withdraft-ietf-sidrops-aspa-profile-22.Ensure that a repository timeout correctly stops repository
 processing. Thanks to Fedor Vompe from Deutsche Telekom for reporting.Fixed a defect in Canonical Cache Representation ROAIPAddressFamily
 sort order. As a result, rpki-client 9.8 cannot parse rpki-client
 9.7's .ccr files and vice versa. Thanks to Bart Bakker from RIPE NCC
 for reporting.Fixed an issue in the parser for the locally configured constraints.
 Thanks to Daniel Anderson.A malicious RRDP Publication Server can cause a NULL dereference.
 Thanks to Daniel Anderson for reporting.A malicious RPKI Publication Server can cause an incorrect error exit.
 Thanks to Yuheng Zhang, Qi Wang, Jianjun Chen from Tsinghua University,
 and Teatime Lab for reporting.tmux(1)improvements and bug fixes:Fixed the logic of the no-detached case for detach-on-destroy option.Support case-insensitive search intmux(1)modes in the same
	way as copy mode (like emacs, so all-lowercase means case
	insensitive).Added-lflag totmux(1)command-prompt to
	disable splitting into multiple prompts.Allowedshow-messagesto work without a client.Added seconds totmux(1)clock mode.Madetmux(1)clock mode seconds synchronized to the second.Added support for synchronized output mode (DECSET 2026).Added a focus-follows-mouse option.Reduced request timeout to 500 milliseconds to match the extended escape time and discard palette requests if receiving a reply for a different index.Added an-eflag totmux(1)command-promptto close if empty.Fixed window-size=latest not resizing on switch-client in session groups.Made tmux respond to DECRQM 2026.Break out the sorting code into a common file so formats and modes use the same code and add-Ofor sorting to the list commands.Added sorting (-O flag) and a custom format (-F) to list-keys.Fixed several memory leaks.Allow copy mode to work for readonly clients, except for copy commands.Avoid a crash by checking for NULL before dereferencing.Make -c (shell command) work with new-session -A.Draw message as one format, allowing prompts and messages to occupy only
	a portion of the status bar, overlaying the normal status content rather
	than replacing the entire line.Add a short built-in help text for each mode accessible with C-h.Add extkeys feature totmux(1)itself so nested tmux works.Add -C flag totmux(1)command-prompt to match display-message -C.LibreSSL version 4.3.0:Portable changesRework portable assembly handling withLIBRESSL_USE_ASSEMBLYAdd SHA assembly for elf-aarch64Add definition of ssize_t to cms.h for WindowsFix posix_open() implementation so it properly signals failureFixSIGALRMhandler for openssl speed on WindowsInternal improvementsRemove the unused sequence number fromX509_REVOKED.Replace a call to atoi(3) with strtonum(3) in nc(1) and replace a
 misleading use of ntohs(3) with htons(3).openssl(1) speed now usesHMAC-SHA256for its hmac benchmark.Reimplemented only use of ASN1_PRINTABLE_type() in openssl(1) ca.
 The API will be removed in an upcoming release.Add curve NID toEC_POINTobjects so the library has a clue on which
 curve a givenEC_POINTis supposed to live.Use curve NID to check for compatibility between group and points
 in various EC API. This isn't 100% failsafe but good enough for sane
 uses.Require SSE in order to use gcm_{gmult,ghash}_4bit_mmx().
 On rare i386 machines supporting MMX but not SSE this could result
 in an illegal instruction.Cleaned up asn1t.h to make it somewhat readable and more robust by
 using C99 initializers in particular.Further assembly macro improvements for -portable.Add fast path for well-known DH primes in DH_check(3) (including
 those from RFC 7919). Some projects still fiddle with this in 2025.Rewrite ec_point_cmp() for readability and robustness.Improve EVP_{Open,Seal}Init(3) internals. This is legacy API that
 cannot be removed since one scripting language still exposes it.ASN1_BIT_STRING_set_bit(3) now trims trailing zero bits itself rather
 than relying on i2c_ASN1_BIT_STRING(3) to do that when encoding.Fix and add workarounds to libtls to improve const correctness and
 to avoid warnings when compiling with OpenSSL 4.PrefixEC_KEYmethods with ec_key_ to avoid problems in
 some static links.Removemac_packet, a leftover from accepting SSLv2 ClientHellos.Removessl_server_legacy_first_packet().In addition to what was done in LibreSSL 4.0 for the version
 handling, disable TLSv1.1 and lower also on the method level.Remove workaround for SSL 3.0/TLS 1.0 CBC vulnerability.Refactorocsp_find_signer_sk()to avoid neglecting the ASN.1's
 semantics by directly reaching into deeply nested OCSP structures.Compatibility changesExpose X509_VERIFY_PARAM_set_hostflags(3) as a public symbol.Provide SSL_SESSION_dup(3).BIGNUMs now use the C99 types uint64_t/uint32_t for the word width.
 Fixes long-standing issues with 32-bit longs on 64-bit Windows.Many unused BN_* macros with incomprehensible names were removed:BN_LONG,BN_BITS{,4},BN_MASK2{,l,h,h1},BN_TBIT,BN_DEC_CONV,BN_{DEC,HEX}_FMT{1,2}, ...openssl(1) cms no longer accepts the unsupported-compressand-uncompressswitches.AddedPKCS7_NO_DUAL_CONTENTflag/behavior. This is
 incorrect legacy behavior but some language bindings decided to
	rely on it in 2025.RemoveSTABLE_FLAGS_MALLOCbut keepSTABLE_NO_MASKbecause there is still one user...FixASN1_ADB_ENDmacro to have compatible signature
 with OpenSSL. Theadb_cb()argument is currently ignored.UnexportASN1_LONG_UNDEF.New featuresSupport forMLKEM768_X25519keyshare in TLS.AddedML-KEMbenchmarks to openssl(1) speed.Added support for starttls protocolsieve.Add support forRSASSA-PSSwith pubkey OIDRSASSA-PSSto libssl.Bug fixesEnsure the group selected by a TLSv1.3 server for a
 HelloRetryRequest is not one for which the client has
 already sent a key share.Plug memory leak in CMS_EncryptedData_encrypt(3).Plug possible memory leak and double free innref_nos().Removed always zero test results for some no longer available
 legacy primitives in openssl(1) speed.List SHA-3 digests in openssl(1) help output.Fix encoding of bit strings with trailing zeroes on whichASN1_STRING_FLAG_BITS_LEFTis not set.Add missing NULL pointer check to PKCS12_item_decrypt_d2i(3).Avoid type confusion leading to 1-byte read at address 0x00-0xff
 in PKCS#12 parsing.Fix type confusion in timestamp response parsing for v2 signing
 certs.Fix EVP_SealInit(3) to return 0 on error, not -1.Replace incorrect strncmp(3) with strcmp(3) in CRL distribution point
 config parsing.openssl x509 -textwrites its output to the file
 specified by-outlike all other openssl(1) subcommands.Stop Delta CRL processing in the verifier if the cRLNumber is
 missing. This is flagged on deserialization, but nothing checks
 that flag. This can lead to aNULLdereference if the
	verification has enabled Delta CRL checking by settingX509_V_FLAG_USE_DELTAS.FixNULLdereference that can be triggered with malformed
 OAEP parameter encoding for CMS decryption.Add missing length checks before BIO_new_mem_buf(3) in libtls.Improve libtls error reporting consistency, avoid reporting
 unrelated errnos.Fix SAN dNSName constraints: instead of substring matching,
 match exactly and allow zero or more components in front of
 the candidate.Reliability fixFix off-by-one error in the X.509 verifier depth checking. This can
 lead to a 4-byte overwrite on heap allocated memory for clients
 talking to a malicious server or for servers that have client
 certificate verification enabled. In addition, the maximum depth
 must be set to the maximum allowed value of 32.Testing and proactive securityPort Wycheproof tests totestvectors_v1and improve
 coverage and correctness. Add tests for ML-KEM in particular.OpenSSH 10.3:Security fixes:ssh(1): validation of shell
 metacharacters in user names supplied
 on the command-line was performed too late to prevent some
 situations where they could be expanded from %-tokens in
 ssh_config. For certain configurations, such as those that use a
 "%u" token in a "Match exec" block, an attacker who can control
 the user name passed tossh(1)could potentially execute arbitrary
 shell commands. Reported by Florian Kohnhäuser.

 We continue to recommend against directly exposingssh(1)and
 other tools' command-lines to untrusted input. Mitigations such
 as this cannot be absolute given the variety of shells and user
 configurations in use.sshd(8): when matching
 an authorized_keys principals="" option
 against a list of principals in a certificate, an incorrect
 algorithm was used that could allow inappropriate matching in
 cases where a principal name in the certificate contains a
 comma character. Exploitation of the condition requires an
 authorized_keys principals="" option that lists more than one
 principal *and* a CA that will issue a certificate that encodes
 more than one of these principal names separated by a comma
 (typical CAs strongly constrain which principal names they will
 place in a certificate). This condition only applies to user-
 trusted CA keys in authorized_keys, the main certificate
 authentication path (TrustedUserCAKeys/AuthorizedPrincipalsFile)
 is not affected. Reported by Vladimir Tokarev.scp(1): when downloading
 files as root in legacy (-O) mode and
 without the -p (preserve modes) flag set, scp did not clear
 setuid/setgid bits from downloaded files as one might typically
 expect. This bug dates back to the original Berkeley rcp program.
 Reported by Christos Papakonstantinou of Cantina and Spearbit.sshd(8): fix incomplete
 application of PubkeyAcceptedAlgorithms
 and HostbasedAcceptedAlgorithms with regard to ECDSA keys.
 Previously if one of these directives contains any ECDSA algorithm
 name (say "ecdsa-sha2-nistp384"), then any other ECDSA algorithm
 would be accepted in its place regardless of whether it was
 listed or not. Reported by Christos Papakonstantinou of Cantina
 and Spearbit.ssh(1): connection
 multiplexing confirmation (requested using
 "ControlMaster ask/autoask") was not being tested for proxy mode
 multiplexing sessions (i.e. "ssh -O proxy ..."). Reported by
 Michalis Vasileiadis.Potentially incompatible changes:ssh(1),sshd(8): remove bug
 compatibility for implementations
 that don't support rekeying. If such an implementation tries to
 interoperate with OpenSSH, it will now eventually fail when the
 transport needs rekeying.sshd(8): prior to this
 release, a certificate that had an empty
 principals section would be treated as matching any principal
 (i.e. as a wildcard) when used via authorized_keys principals=""
 option. This was intentional, but created a surprising and
 potentially risky situation if a CA accidentally issued a
 certificate with an empty principals section: instead of being
 useless as one might expect, it could be used to authenticate as
 any user who trusted the CA via authorized_keys. [Note that this
 condition did not apply to CAs trusted via thesshd_config(5)TrustedUserCAKeys option.]

 This release treats an empty principals section as never matching
 any principal, and also fixes interpretation of wildcard
 characters in certificate principals. Now they are consistently
 implemented for host certificates and not supported for user
 certificates.ssh(1): the -J and
 equivalent -oProxyJump="..." options now
 validate user and host names for ProxyJump/-J options passed
 via the command-line (no such validation is performed for this
 option in configuration files). This prevents shell injection in
 situations where these were directly exposed to adversarial
 input, which would have been a terrible idea to begin with.
 Reported by rabbit.New features:ssh(1),sshd(8): support IANA-assigned
 codepoints for SSH agent
 forwarding, as per draft-ietf-sshm-ssh-agent. Support for the new
 names is advertised via the EXT_INFO message. If a server offers
 support for the new names, then they are used preferentially.

 Support for the pre-standardisation "@openssh.com" extensions for
 agent forwarding remains supported.ssh-agent(1):
 implement support for draft-ietf-sshm-ssh-agent
 "query" extension.ssh-add(1): support
 querying the protocol extensions via the
 agent "query" extension with a new -Q flag.ssh(1): support multiple
 files in ssh_config and sshd_config RevokedHostKeys directive.bz3918ssh(1): add a ~I escape
 option that shows information about the current SSH connection.ssh(1): add an "ssh
 -Oconninfo user@host" multiplexing command that shows connection
 information, similar to the ~I escapechar.ssh(1): add anssh -O
 channels user@hostmultiplexing command to
 get a running mux process to show information about what channels
 are currently open.sshd(8): addinvaliduserpenalty to PerSourcePenalties, which is
 applied to login attempts for usernames that do not match real
 accounts. Defaults to 5s to match 'authfail' but allows
 administrators to block such attempts for longer if desired.sshd(8): add a
 GSSAPIDelegateCredentials option for the server,
 controlling whether it accepts delegated credentials offered by
 the client. This option mirrors the same option in ssh_config.ssh(1),sshd(8): support the VA DSCP
 codepoint in the IPQoS directive.sshd(8): convert
 PerSourcePenalties to using floating point time,
 allowing penalties to be less than a second. This is useful if you
 need to penalise things you expect to occur at >=1 QPS.ssh-keygen(1):
 support writing ED25519 keys in PKCS8 format.Support the ed25519 signature scheme via libcrypto.Bugfixes:sshd(8): make IPQoS
 first-match-wins in sshd_config, like other configuration directives.bz3924sshd(8): fix potential
 crash when MaxStartups is set to a single
 argument (i.e. not using the MaxStartups x:y:z form) with a value
 below 10.bz3941sshd(8): fix a potential
 hang during key exchange if needed DH
 group values were missing from /etc/moduli.ssh-agent(1): fix
 return values from extensions to be correct with respect to
 draft-ietf-sshm-ssh-agent: extension requests should indicate
 failure using SSH_AGENT_EXTENSION_FAILURE rather than the generic
 SSH_AGENT_FAILURE error code. This allows the client to discern
 between "the request failed" and "the agent doesn't support this
 extension".ssh(1): use fmprintf for
 showing challenge-response name and info
 to preserve UTF-8 characters where appropriate.scp(1): when uploading a
 directory using SFTP (e.g. during a recursive transfer), don't
 clobber the remote directory permissions unless either we created the
 directory during the transfer or the -p flag was set.bz3925All: implement missing pieces of FIDO/webauthn signature support,
 mostly related to certificate handling and enable acceptance of this
 signature format by default.bz3748sshd_config(5):
 make it clear that DenyUsers/DenyGroups overrides
 AllowUsers/AllowGroups. Previously we specified the order in which
 the directives are processed but it was ambiguous as to what
 happened if both matched.ssh(1): don't try to match
 certificates held in an agent to
 private keys. This matching is done to support certificates that
 were loaded without their private key material, but is
 unnecessary for agent-hosted certificates, which always have
 private key material available in the agent. Worse, this matching
 would mess up the request sent to the agent in such a way as to
 break usage of these keys when the key usage was restricted in
 the agent.bz3752sftp(1): if editline has
 been switched to vi mode (i.e. via "bind -v" in .editrc), set up a
 keybinding so that command mode can be entered.ssh(1),sshd(8): improve performance
 of keying the sntrup761 key agreement algorithm.ssh(1),sshd(8): enforce maximum
 packet/block limit during pre-authentication phase.sftp(1): don't misuse the
 sftp limits extension's open-handles
 field. This value is supposed to be the number of handles a
 server will allow to be opened and not a number of outstanding
 read/write requests that can be sent during an upload/download.sshd(8): don't crash at
 connection time if the main sshd_config
 lacks any subsystem directive but one is defined in a Match block.bz3906sshd_config(5): add
 a warning next to the ForceCommand directive
 that forcing a command doesn't automatically disable forwarding.sshd_config(5): add
 a warning that TOKENS are replaced without filtering or escaping and that
 it's the administrator's responsibility to ensure they are used safely in
 context.scp(1): correctly quote
 filenames in verbose output for local->local copies.bz3900sshd(8): don't mess up the
 PerSourceNetBlockSize IPv6 mask if sscanf didn't decode it.ssh-add(1): when
 loading FIDO2 resident keys, set the comment to the FIDO application
 string. This matches the behaviour of ssh-keygen -K.sshd(8): don't strnvis()
 log messages that are going to be logged
 by sshd-auth via its parent sshd-session process, as the parent
 will also run them through strnvis(). Prevents double-escaping of
 non-printing characters in some log messages.bz3896ssh-agent(1): escape
 SSH_AUTH_SOCK paths that are sent to the shell as setenv commands.
 Unbreaks ssh-agent for home directory paths that contain whitespace.bz3884All: Remove unnecessary checks for ECDSA public key validity.sshd(8): activate
 UnusedConnectionTimeout only after the last
 channel has closed. Previously UnusedConnectionTimeout could fire
 early after a ChannelTimeout. This was not a problem for the
 OpenSSH client because it terminates once all channels have
 closed but could cause problems for other clients (e.g. API
 clients) that do things differently.bz3827All: fix PKCS#11 key PIN entry problems introduced in
 openssh-10.1/10.2.bz3879scp(1): when using the
 SFTP protocol for transfers, fix implicit destination path selection
 when source path ends with "..".bz3871sftp(1): when
 tab-completing a filename, ensure that the completed
 string does not end up mid-way through a multibyte character, as
 this will cause a fatal() later on.ssh-keygen(1): fix
 crash at exit (visible via ssh-keygen -D) when multiple keys loaded.scp(1)/sftp(1): correctly display
 bandwidths greater than 2 GBps in the progress meter.Ports and packages:Many pre-built packages for each architecture:aarch64: 12883amd64: 13044arm: XXXi386: 10631mips64: 9309powerpc: XXXpowerpc64: 9507riscv64: XXXsparc64: 10079Some highlights:Asterisk 16.30.1, 18.26.4, 20.19.0 and 22.9.0Audacity 3.7.7CMake 4.2.3Chromium 147.0.7727.101Emacs 30.2FFmpeg 8.0.1GCC 15.2.0GHC 9.10.3GNOME 49Go 1.26.2JDK 11.0.30, 17.0.18, 21.0.10 and 25.0.2KDE Applications 25.12.3KDE Frameworks 6.23.0KDE Plasma 6.6.4Krita 5.2.16LLVM/Clang 19.1.7, 20.1.8 and 21.1.8LibreOffice 26.2.2.2Lua 5.1.5, 5.2.4, 5.3.6 and 5.4.8MariaDB 11.4.10Mono 6.14.1Mozilla Firefox 150.0 and ESR 140.10.0Mozilla Thunderbird 140.10.0Mutt 2.3.1 and NeoMutt 20260406Node.js 22.22.2OCaml 4.14.2OpenLDAP 2.6.13PHP 8.2.30, 8.3.30, 8.4.20 and 8.5.5Postfix 3.5.25 and 3.11.1PostgreSQL 18.3Python 2.7.18 and 3.13.13Qt 5.15.18 (+ kde patches) and 6.10.2R 4.5.2Ruby 3.3.11, 3.4.9 and 4.0.2Rust 1.94.1SQLite 3.51.3Shotcut 26.2.26Sudo 1.9.17p2Suricata 7.0.7Tcl/Tk 8.5.19, 8.6.17 and 9.0.3TeX Live 2025Vim 9.2.0357 and Neovim 0.12.1Vulkan 1.4.341.0Wayland 1.24.0 with compositors Labwc, Mango, Niri, Sway and WayfireXfce 4.20.0As usual, steady improvements in manual pages and other documentation.The system includes the following major components from outside suppliers:Xenocara (based on X.Org 7.7 with xserver 21.1.21 + patches,
 freetype 2.14.2, fontconfig 2.17.1, Mesa 25.0.7, xterm 406,
 xkeyboard-config 2.20, fonttosfnt 1.2.4 and more)LLVM/Clang 19.1.7 (+ patches)GCC 4.2.1 (+ patches)Perl 5.42.2 (+ patches)pkgconf 2.4.3NSD 4.14.2Unbound 1.24.2Ncurses 6.4Binutils 2.17 (+ patches)GDB 6.3 (+ patches)Awk 20250116Expat 2.7.5zlib 1.3.2 (+ patches)

### How to install

Please refer to the following files on the mirror site for
extensive details on how to install OpenBSD 7.9 on your machine:.../OpenBSD/7.9/alpha/INSTALL.alpha.../OpenBSD/7.9/amd64/INSTALL.amd64.../OpenBSD/7.9/arm64/INSTALL.arm64.../OpenBSD/7.9/armv7/INSTALL.armv7.../OpenBSD/7.9/hppa/INSTALL.hppa.../OpenBSD/7.9/i386/INSTALL.i386.../OpenBSD/7.9/landisk/INSTALL.landisk.../OpenBSD/7.9/loongson/INSTALL.loongson.../OpenBSD/7.9/luna88k/INSTALL.luna88k.../OpenBSD/7.9/macppc/INSTALL.macppc.../OpenBSD/7.9/octeon/INSTALL.octeon.../OpenBSD/7.9/powerpc64/INSTALL.powerpc64.../OpenBSD/7.9/riscv64/INSTALL.riscv64.../OpenBSD/7.9/sparc64/INSTALL.sparc64

Quick installer information for people familiar with OpenBSD, and the use of
the "disklabel-E" command.
If you are at all confused when installing OpenBSD, read the relevant
INSTALL.* file as listed above!### OpenBSD/alpha:If your machine can boot from CD, you can writeinstall79.isoorcd79.isoto a CD and boot from it.
Refer to INSTALL.alpha for more details.### OpenBSD/amd64:If your machine can boot from CD, you can writeinstall79.isoorcd79.isoto a CD and boot from it.
You may need to adjust your BIOS options first.If your machine can boot from USB, you can writeinstall79.imgorminiroot79.imgto a USB stick and boot from it.If you can't boot from a CD, floppy disk, or USB,
you can install across the network using PXE as described in the included
INSTALL.amd64 document.If you are planning to dual boot OpenBSD with another OS, you will need to
read INSTALL.amd64.### OpenBSD/arm64:Depending on your hardware, you can writeinstall79.isoorcd79.isoto a CD and boot from it, or write a system specific
miniroot to an SD card and boot from it after connecting to the serial
console. Refer to INSTALL.arm64 for more details.### OpenBSD/armv7:Write a system specific miniroot to an SD card and boot from it after connecting
to the serial console. Refer to INSTALL.armv7 for more details.### OpenBSD/hppa:Boot over the network by following the instructions in INSTALL.hppa or thehppa platform page.### OpenBSD/i386:If your machine can boot from CD, you can writeinstall79.isoorcd79.isoto a CD and boot from it.
You may need to adjust your BIOS options first.If your machine can boot from USB, you can writeinstall79.imgorminiroot79.imgto a USB stick and boot from it.If you can't boot from a CD, floppy disk, or USB,
you can install across the network using PXE as described in
the included INSTALL.i386 document.If you are planning on dual booting OpenBSD with another OS, you will need to
read INSTALL.i386.### OpenBSD/landisk:Writeminiroot79.imgto the start of the CF
or disk, and boot normally.### OpenBSD/loongson:Writeminiroot79.imgto a USB stick and boot bsd.rd from it
or boot bsd.rd via tftp.
Refer to the instructions in INSTALL.loongson for more details.### OpenBSD/luna88k:Copy 'boot' and 'bsd.rd' to a Mach or UniOS partition, and boot the bootloader
from the PROM, and then bsd.rd from the bootloader.
Refer to the instructions in INSTALL.luna88k for more details.### OpenBSD/macppc:Burn theinstall79.isoimage from a mirror site to a CDROM,
and power on your machine while holding down theCkey until
the display turns on and showsOpenBSD/macppc boot.Alternatively, at the Open Firmware prompt, enterboot cd:,ofwboot
/7.9/macppc/bsd.rd### OpenBSD/octeon:After connecting a serial port, boot bsd.rd over the network via DHCP/tftp.
Refer to the instructions in INSTALL.octeon for more details.### OpenBSD/powerpc64:To install, writeinstall79.imgorminiroot79.imgto a
USB stick, plug it into the machine and choose theOpenBSD
installmenu item in Petitboot.
Refer to the instructions in INSTALL.powerpc64 for more details.### OpenBSD/riscv64:To install, writeinstall79.imgorminiroot79.imgto a
USB stick, and boot with that drive plugged in.
Make sure you also have the microSD card plugged in that shipped with the
HiFive Unmatched board.
Refer to the instructions in INSTALL.riscv64 for more details.### OpenBSD/sparc64:Burn the image from a mirror site to a CDROM, boot from it, and typeboot cdrom.If this doesn't work, or if you don't have a CDROM drive, you can writefloppy79.imgorfloppyB79.img(depending on your machine) to a floppy and boot it withboot
floppy. Refer to INSTALL.sparc64 for details.Make sure you use a properly formatted floppy with NO BAD BLOCKS or your install
will most likely fail.You can also writeminiroot79.imgto the swap partition on
the disk and boot withboot disk:b.If nothing works, you can boot over the network as described in INSTALL.sparc64.

### How to upgrade

If you already have an OpenBSD 7.8 system, and do not want to reinstall,
upgrade instructions and advice can be found in theUpgrade Guide.

### Notes about the source code

src.tar.gzcontains a source archive starting at/usr/src.
This file contains everything you need except for the kernel sources,
which are in a separate archive.
To extract:#mkdir -p /usr/src#cd /usr/src#tar xvfz /tmp/src.tar.gzsys.tar.gzcontains a source archive starting at/usr/src/sys.
This file contains all the kernel sources you need to rebuild kernels.
To extract:#mkdir -p /usr/src/sys#cd /usr/src#tar xvfz /tmp/sys.tar.gzBoth of these trees are a regular CVS checkout. Using these trees it
is possible to get a head-start on using the anoncvs servers as
describedhere.
Using these files
results in a much faster initial CVS update than you could expect from
a fresh checkout of the full OpenBSD source tree.

### Ports Tree

A ports tree archive is also provided. To extract:#cd /usr#tar xvfz /tmp/ports.tar.gzGo read theportspage
if you know nothing about ports
at this point. This text is not a manual of how to use ports.
Rather, it is a set of notes meant to kickstart the user on the
OpenBSD ports system.Theports/directory represents a CVS checkout of our ports.
As with our complete source tree, our ports tree is available viaAnonCVS.
So, in order to keep up to date with the -stable branch, you must make
theports/tree available on a read-write medium and update the tree
with a command like:#cd /usr/ports#cvs -d anoncvs@server.openbsd.org:/cvs update -Pd -rOPENBSD_7_9[Of course, you must replace the server name here with a nearby anoncvs
server.]Note that most ports are available as packages on our mirrors. Updated
ports for the 7.9 release will be made available if problems arise.If you're interested in seeing a port added, would like to help out, or just
would like to know more, the mailing listports@openbsd.orgis a good place to know.