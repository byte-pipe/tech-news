---
title: using Sun Ray thin clients in 2025 » catstret.ch
url: https://catstret.ch/202506/sun-ray-shenanigans/
site_name: lobsters
fetched_at: '2025-07-02T23:06:35.870553'
original_url: https://catstret.ch/202506/sun-ray-shenanigans/
date: '2025-07-02'
tags: retrocomputing
---

i’ve used thin clients at home for quite a while - both for theirintendeduse (remotely accessing a desktop of another system); and in the sense of “modern thin clients are x86 boxes that are wildly overpowered for what they run, so they make good mini servers.”

recently, i saw a bulk lot of Sun Ray thin clients pop up on Trade Me (NZ’s eBay-like auction site) - and with very little idea of how many clients were actually included in this lot, i jumped on it. after a 9 hour round-trip drive (on some of the worst roads i’ve seen!), i returned home with the back of my car completely packed with Sun Rays. time for some interesting shenanigans!

## sections

* cataloguing the haul
* setting up the Sun Ray Server Softwaregetting SRSS installed on OpenIndianagetting the Sun Ray firmware in place
* getting SRSS installed on OpenIndiana
* getting the Sun Ray firmware in place
* kiosk sessionsRDPbrowser sessions
* RDP
* browser sessions
* where to from here?

## cataloguing the haul

when picking all of these up from the seller, i had guesstimated there was maybe 30 clients in total. turns out i was off by quite a bit.

i ended up bringing home:

* 12xSun Ray 2
* 12xSun Ray 2FS
* 11xSun Ray 3
* 4xSun Ray 3+
* 3xSun Ray 270- 17” (1280x1024) LCD screens with integrated Sun Ray clients
* 4xIncarta Uvo- 24” 1080p LCD screens with integrated clientsi can’t find any info about these other than the linked page on the Wayback Machine - if you know more about these, please send me an email!
* i can’t find any info about these other than the linked page on the Wayback Machine - if you know more about these, please send me an email!
* about 40 smart cards, for authentication/hotdesking
* a small pile of Sun Type 7 USB keyboards, and some Sun-branded optical mice

so that’s46clients all up!

a few days prior to picking all this up, i rented a storage unit in a local facility, and put some garage shelving units in there - and boy howdy i’m glad i did!

## setting up the Sun Ray Server Software

looking at the Oracle (eugh.) documentation for the Sun Ray Server Software, it appeared there were two options: run it on ancient Linux, or run it on ancient Solaris. Oracle dropped support for the Sun Rays in 2014, as part of extinguishing everything Sun Microsystems stood for after the 2010 acquisition. i didn’treallywant to have a RHEL 6 box kicking around, nor did i want to deal with trying to make Solaris 10 work in a VM on my home Proxmox cluster, so i did some digging.

enterillumos- well, in my case, OpenIndiana. illumos is, essentially, a fork of the pre-Oracle-acquisition OpenSolaris codebase. OpenIndiana is one of many illumosdistributions(in a very similar sense to Linux distributions), and OpenIndiana is more suited for desktop use than most other illumos distributions. the OpenIndiana documentation hasa section on setting up the Sun Ray Server Software on OpenIndiana, but even with that in hand there was a lot of pieces to figure out on my own!

### getting SRSS installed on OpenIndiana

this is mostly a copy of the docs from the OpenIndiana handbook, with some adjustments to fix things i ran into. i did this on top of a text-only install -OpenIndiana Hipster 2025.04 Text Install DVD (64-bit x86)was the install media i used (fromhttps://www.openindiana.org/downloads/).

to get the desktop environment installed:

# pkg install mate_install

unlocking the dependencies for SRSS:

# pkg change-facet facet.version-lock.gnome/gnome-session=false
# pkg change-facet facet.version-lock.gnome/gnome-settings-daemon=false
# pkg change-facet facet.version-lock.system/display-manager/gdm=false
# pkg change-facet facet.version-lock.library/gnome/libgnomekbd=false
# pkg change-facet facet.version-lock.gnome/window-manager/metacity=false
# pkg change-facet facet.version-lock.library/desktop/gnome-desktop=false
# pkg change-facet facet.version-lock.cde/cde-runtime=false
# pkg change-facet facet.version-lock.library/motif=false
# pkg change-facet facet.version-lock.library/tooltalk=false
# pkg change-facet facet.version-lock.compatibility/packages/SUNWxwplt=false

setting up the package source, and installing the SRSS dependencies:

# pkg set-publisher --search-before=openindiana.org -g http://pkg.toc.de/sunray sunray
# pkg set-publisher --non-sticky openindiana.org
# pkg install sunray-essential

after unpacking the Sun Ray Server Software installers (both the Solaris and Linux versions) into/root, i ran theupdate_dhcp_dependencyscript from the OI Handbook, then tried to install SRSS, which bombed out spectacularly with package manager rejections of theThis version is excluded by installed incorporation consolidation/userland/userland-incorporation@...sort. so here’s the correct (read: “worked for me!”) steps:

# /root/update_dhcp_dependency /root/srs_5.4.0.0-Solaris_11plus.i386/IPS.i386/
# pkg set-publisher -g /root/srs_5.4.0.0-Solaris_11plus.i386/IPS.i386/ sunray
# pkg uninstall entire userland-incorporation
# pkg install SUNWut-srss SUNWut-srwc SUNWuti

the
update_dhcp_dependency
 script, for posterity

update_dhcp_dependency

raw

#!/bin/ksh

# set -x

if

[

-z

$1

]

||

[

!

-d

$1

]
;

then

echo

"usage:
$0
 repodirectory"


exit

fi

if

[[

$1

!=
 /
*

]]
;

then

repo
=
$(
pwd
)
/
$1

else

repo
=
$1

fi

republish
=
"republish
$$
"

mkdir

${
republish
}

for
p
in
SUNWutr SUNWuto
;

{

(
cd

${
republish
}

 pkgrecv
-d

.

--raw

-s

$repo

$p

||

exit
2

for
d
in

$(
ls

$p
)
;

{


(
cd

$p
/
$d


sed

-i
 s#service/network/dhcp#service/network/dhcp/isc-dhcp# manifest
 pkgrepo
-s

$repo
 remove
$p

 pkgsend publish
-s

$repo

-d

.
 manifest

)


}

)
;

}

rm

-r

${
republish
}

to make SRSS happy with isc-dhcp:

# rpm2cpio /root/srs_5.4.0.0-Linux.i386/Components/10-SRSS/Content/Sun_Ray_Core_Services_4.5/Linux/Packages/SUNWuto-4.5-44.i386.rpm | bsdtar -C /root -xf - ./opt/SUNWut/lib/dhcp/
# sed 's#$UTDHCPDIR | sort#$UTDHCPDIR | gsort#g' -i.bak /root/opt/SUNWut/lib/dhcp/isc/dhcp_config_linux
# cp -R /root/opt/SUNWut/lib/dhcp/isc /opt/SUNWut/lib/dhcp/
# cp /opt/SUNWut/lib/dhcp/isc/dhcp_config_linux /opt/SUNWut/lib/dhcp/isc/dhcp_config_solaris
# ln -s /opt/SUNWut/lib/dhcp/isc /etc/opt/SUNWut/dhcp

then apply the needed patch to/opt/SUNWut/sbin/utadm:

openindiana-srss-utadm.patch

raw

From a1072acfffd91457d91cd6d202a988d88bc3fb8a Mon Sep 17 00:00:00 2001
From: Carsten Grzemba <cgrzemba@opencsw.org>
Date: Mon, 3 Feb 2020 10:58:31 +0100
Subject: [PATCH] apply changes for:

* change the dhcp config file name
* different ipadm argument names
* name IP interface utadm to refer to the IP address creator
* do not use /etc/hostname.<if>

---

 utadm | 41 +++++++----------------------------------
 1 file changed, 7 insertions(+), 34 deletions(-)

diff --git a/utadm b/utadm
index cffac27..448c171 100644

--- a/utadm

+++ b/utadm

@@ -116,7 +116,7 @@
 UTDHCPSERVICE_SUCCESS=0
 UTDHCPSERVICE_DISABLED=3

 SVCADM="/usr/sbin/svcadm"

-DHCP_FMRI="svc:/network/dhcp-server:default"

+DHCP_FMRI="svc:/network/dhcp-server:ipv4"

 UTLIB="/opt/SUNWut/lib"
 UTSBIN="/opt/SUNWut/sbin"

@@ -207,6 +207,7 @@
 function SetPlatformDependencies {
 IFCONFIG_KEY_NETMASK="netmask"
 if [ -x /usr/sbin/ipadm ]; then
 IPADM_CONF=true

+ DHCPCONFIG="/etc/dhcp/dhcpd.conf"

 fi

 ;; # end case SunOS

@@ -1783,14 +1784,6 @@
 function DoAddNetworkConfig {
 DHCPONLY="N"
 for test in ${INTF_ALL}; do
 if [ "${INTF}" = "${test}" -a -f "${HOSTNAME_C}${INTF}" ]; then

- #
- # Need to catch the case where hostname.<intf> exists but the hostname
- # defined in the file may not be configured locally in the hosts file.
- #
- if [ ! -f ${HOSTNAME_C}${INTF} ]; then
- print -u2 "Error: missing \"${HOSTNAME_R}${INTF}\" file."
- return 1
- fi

 if [[ $OS == "SunOS" ]]; then
 NAME=`getIfname ${INTF}`
 if [ -z "${NAME}" ]; then

@@ -2567,9 +2560,9 @@
 should an auth server be located by broadcasting on the network?" "Y"
 fi
 # Clear any pre-existing state on interface, then create
 # new persistent configuration

- ipadm delete-ip ${INTF} 2>/dev/null
- ipadm create-ip ${INTF}
- ipadm create-addr -T static -a local=${IPADDR}/${MASKBITS} ${INTF}/v4static

+ ipadm delete-if ${INTF} 2>/dev/null
+ ipadm create-if ${INTF}
+ ipadm create-addr -T static -a local=${IPADDR}/${MASKBITS} ${INTF}/v4utadm

 else
 # ifconfig the new interface
 ifconfig ${INTF} plumb >/dev/null 2>&1 ;

@@ -2710,7 +2703,7 @@
 function DoList {
 if [[ $BLOCKTYPE = "interface" ]] ; then
 if Intf=${UT_DHCP_INTERFACE} ; then
 if [[ ! -s ${HOSTNAME_R}.${Intf} ]]; then

- IntfAddr=""*MISSING*""

+ IntfAddr=`ipadm show-addr -p -o ADDR ${Intf}/ | awk '{split($1,a,"/"); print a[1]}'`

 else
 typeset H=`getIfname ${Intf}`
 IntfAddr=`getent hosts $H | awk '{ print $1 }'`

@@ -3151,14 +3144,6 @@
 function DoPrint {

 INTF=${UT_DHCP_INTERFACE}

- #
- # Need to catch the case where hostname.<intf> exists but the hostname
- # defined in the file may not be configured locally in the hosts file.
- #
- if [ ! -f ${HOSTNAME_R}.${INTF} ]; then
- print -u2 "Error: missing \"${HOSTNAME_R}.${INTF}\" file."
- return 1
- fi

 H=`getIfname ${INTF}`
 if [ -z "${H}" ]; then
 print -u2 "Error: interface ${INTF} is partially configured. Hostname not" \

@@ -3452,19 +3437,7 @@
 function getIfname {
 awk '{print $1 ; exit}' "${HOSTNAME_R}.$1"
 return
 else

- # With ipadm, there's no way to create a persistent
- # configuration without it immediately being reflected in the
- # runtime configuration, nor does ipadm provide any convenient
- # way to find the IPv4 addrobj for the interface, so just
- # check runtime configuration via ifconfig.
- IPADDR=$(ifconfig $1 | awk '
- /[ ]inet /{
- for (i = 1; i < NF; ++i) {
- if ($i == "inet") {
- print $(i+1)
- }
- }
- }')

+ IPADDR=`ipadm show-addr -p -o ADDR $1/ | awk '{split($1,a,"/"); print a[1] }'`

 if [ -z "$IPADDR" ]; then
 print -u2 "Error in parsing of ifconfig addresses"
 exit 2

--

2.23.0

now, get the ancient JRE in place:

# cd /root/srs_5.4.0.0-Solaris_11plus.i386/Supplemental/Java_Runtime_Environment/Solaris
# ./jre-6u41-solaris-i586.sh
# mv ./jre1.6.0_41 /opt/
# ln -s /opt/jre1.6.0_41 /etc/opt/SUNWut/jre

and, since i wanted the web administration tools to work too:

# bsdtar -C /opt -xf /root/srs_5.4.0.0-Solaris_11plus.i386/Supplemental/Apache_Tomcat/apache-tomcat-5.5.36.tar.gz
# ln -s /opt/apache-tomcat /opt/apache-tomcat-5.5.36

i then configured the Sun Ray server:

# /opt/SUNWut/sbin/utconfig
# /opt/SUNWut/sbin/utpolicy -a -z both -g -M
# /opt/SUNWut/sbin/utadm -L on
# /opt/SUNWut/sbin/utstart -c

and…

it fuckin’ worked!

### getting the Sun Ray firmware in place

since i was using version 5.4.x of the Sun Ray Server Software, the client firmware wasn’t part of the install - from version 5.3 onwards, you had to have an Oracle support contract to get firmware updates. sigh.

thankfully, getting a 5.2.x release (with the firmware included!) wasn’t hard. i grabbed a 5.2.x release for Linux, found the RPM with the firmware in it (SUNWutfw04.3-50.i386.rpm), and extracted that withrpm2cpio.

the Solaris version of SRSS wants to find the firmware in a different place than the Linux version it seems - the Linux versions put it in/opt/SUNWut/lib/firmware, but on Solaris/OpenIndiana, it needs to be in/opt/SUNWutdfw/lib/firmware. easy enough.

once in place, this was all it took to set up the TFTP server, and make SRSS populate the right places with the firmware:

# mkdir /tftpboot
# cd /tftpboot
# ln -f -s . tftpboot
# /opt/SUNWut/sbin/utfwadm -AaV -G force

## kiosk sessions

i wanted to use some of the integrated-into-screens Sun Rays to replace some of the Raspberry Pis (and old iMacs) around the house showing Home Assistant dashboards. i also wanted to set up the Sun Ray server so that when i inserted a particular smart card into a client, it would bring up an RDP session to my existing “desktop” (a Fedora VM running Xrdp).

these both turned out to be… interesting to get working.

### RDP

the Sun Ray Server Software has a built-in method for connecting to Microsoft RDP servers - the Sun Ray Windows Connector, also known asuttsc.
as you might have guessed, it’s broken as fuck on OpenIndiana, even putting aside the fact that the newest RDP server it knows how to handle would be in the Windows Server 2003 era.

so, let’s hack something together with XFreeRDP!

i wanted to be able to specify what RDP server each token would connect to. this was a fairly common use case back in the day, and some people wrote helpers to allow things like that - one of which beingDaniel Cifuentes’ meta-kiosk, which i borrowed some ideas from.

after much trial and error, i got something working!

/etc/opt/SUNWkio/sessions/freerdp.conf

raw

KIOSK_SESSION_EXEC
=
$KIOSK_SESSION_DIR
/freerdp

KIOSK_SESSION_LABEL
=
"FreeRDP session"

/etc/opt/SUNWkio/sessions/freerdp/freerdp

raw

#!/bin/sh

openbox
--replace
 &
/opt/SUNWut/bin/utscreenresize
-s
 all
-l
 &

REG_OTHER
=
`
/opt/SUNWut/sbin/utuser
-p

$SUN_SUNRAY_TOKEN
 |
grep

"Other Info"
 |
cut

-f2

-d
=
`

if

[

"
$REG_OTHER
"

=

""

]

then

zenity
--error

--text
=
"freerdp: idk what you want me to do!
$SUN_SUNRAY_TOKEN
"


exit
1

fi

exec
xterm
-e
 xfreerdp /cert:tofu /f
-toggle-fullscreen
 /dynamic-resolution /gfx +gfx-thin-client /smartcard /bpp:24
$REG_OTHER

after throwing those in place, install the dependencies and configure the session:

# pkg install openbox freerdp
# printf "KIOSK_SESSION=freerdp\n" | /opt/SUNWut/sbin/utkiosk -i FreeRDP

then it’s just a matter of adding the needed data to each token, and assigning the tokens to the FreeRDP session:

# /opt/SUNWut/sbin/utkioskoverride -s kiosk -r OpenPlatform.47905167523905788499 -c FreeRDP

upon inserting that token into a client…

success!

### browser sessions

with much the same setup as the RDP sessions, it’s pretty easy to start a kiosk-mode Firefox, pulling the URL to open from the token data:

/etc/opt/SUNWkio/sessions/kiosk-browser.conf

raw

KIOSK_SESSION_EXEC
=
$KIOSK_SESSION_DIR
/kiosk-browser

KIOSK_SESSION_LABEL
=
"Kiosk Browser"

/etc/opt/SUNWkio/sessions/kiosk-browser/kiosk-browser

raw

#!/bin/sh

openbox
--replace
 &
/opt/SUNWut/bin/utscreenresize
-s
 all
-l
 &

# get rid of the cursor

cat

<<-
EOF
 | xrdb -merge -
Xcursor.theme: InvisibleCursor

EOF

# disable screen blanking

xset s off
xset s noblank
xset
-dpms

REG_OTHER
=
`
/opt/SUNWut/sbin/utuser
-p

$SUN_SUNRAY_TOKEN
 |
grep

"Other Info"
 |
cut

-f2

-d
=
`

if

[

"
$REG_OTHER
"

=

""

]

then

zenity
--error

--text
=
"kiosk-browser: No browser URL provided!
$SUN_SUNRAY_TOKEN
"


exit
1

fi

firefox
--new-instance

--kiosk

--private-window

"
$REG_OTHER
"

i needed to hide the mouse cursor, anduncluttersimplydoes notwork in Sun Ray sessions, so i went with an invisible cursor theme -https://github.com/l-theanine/invisible-cursor-themeworks well.

a problem, though. Firefox would show its first-run “Welcome to Firefox” popup… every time. Sun Ray kiosk sessions run as a random user namedutkuXX(whereXXis a number), and after the kiosk session ends the home directory of the kiosk user gets fully deleted, so the user can be recycled for other sessions. given i wanted to use this with some always-on Sun Rays, with no input devices attached…

thankfully, Firefox policies allow turning that off! throwing this hunk of JSON into/etc/firefox/policies/policies.jsonfixed that:

/etc/firefox/policies/policies.json

raw

{


"policies"
:

{


"DontCheckDefaultBrowser"
:

true
,


"SkipTermsOfUse"
:

true
,


"Preferences"
:

{


"browser.startup.upgradeDialog.enabled"
:

{


"Value"
:

false
,


"Status"
:

"locked"


},


"browser.startup.homepage_override.mstone"
:

{


"Value"
:

"ignore"
,


"Status"
:

"locked"


}


}


}

}

and with that, i could create a token for an individual client (the tokens for this arepseudo.<MAC>, where the MAC is all lower-case), set that token’s “Other Info” field to the URL to show, and assign the kiosk session to that pseudo-token the same way as with smart card tokens.

## where to from here?

this was a lot of fun to get working. i need to take a break from reading the Sun Ray Administration Guide though, so here’s my thinking for a potential part 2:

* i want to see how well the multi-head stuff works in SRSS - which joins multiple physical clients together into one desktop session, using the peripherals connected to the “primary” client. unfortunately the Xinerama support is weird (Xinerama and xrandr are mutually exclusive…), but if i can make it play ball it could be a neat thing to use.
* i want to try and find a newer firmware package too, but that might be a little bit of a lost cause, given i refuse to give Oracle a bunch of money.
* maybe i’ll set up another OpenIndiana VM and configure the HA failover in SRSS?

for now, though… that’s all.
