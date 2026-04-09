---
title: 'Graphene OS: a security-enhanced Android build [LWN.net]'
url: https://lwn.net/SubscriberLink/1030004/898017c7953c0946/
site_name: hackernews
fetched_at: '2025-07-25T16:07:24.315677'
original_url: https://lwn.net/SubscriberLink/1030004/898017c7953c0946/
author: madars
date: '2025-07-25'
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

# Graphene OS: a security-enhanced Android build

## [LWN subscriber-only content]

### Welcome to LWN.netThe following subscription-only content has been made available to you
by an LWN subscriber. Thousands of subscribers depend on LWN for the
best news from the Linux and free software communities. If you enjoy this
article, please considersubscribing to LWN. Thank you
for visiting LWN.net!ByJonathan CorbetJuly 24, 2025People tend to put a lot of trust into their phones. Those devices have
access to no end of sensitive data about our lives — our movements,
finances, communications, and more — so phones belonging to even relatively
low-profile people can be high-value targets. Android devices run free
software, at least at some levels, so it should be possible to ensure that
they are working in their owners' interests. Off-the-shelf Android
installations tend to fall short of that goal. TheGrapheneOSAndroid rebuild is an attempt
to improve on that situation.GrapheneOS got its start as "CopperheadOS"; it wasreviewed herein 2016. A couple of years
later, though, an ugly dispute between the two founders of that project led
to its demise. One of those founders, Daniel Micay, continued the work and
formed what eventually became GrapheneOS, which is, according tothis history page, an
independent, open-source project that "will never again be closely tied
to any particular sponsor or company". Work on GrapheneOS is supported
by a Canada-based foundation created in 2023; there appears to be almost no
public information available regarding this organization, though.At its core, GrapheneOS is an effort to harden Android against a number of
threats and to make Android serve the privacy interests of its users. It
is based on theAndroid Open Source
Project, but removes a lot of code and adds a long list of changes.
Some of those, such as ahardenedmalloc()libraryor the use of additional
control-flow-integrity features, will be mostly invisible to users (unless
they break apps, of course, which has evidently been known to happen).
Others are more apparent, but it is clear that a lot of effort has gone
into making the security improvements as unobtrusive as possible.#### InstallationSome Android rebuilds prioritize supporting a wide range of devices, often
with an eye toward keeping older devices working for as long as possible.
GrapheneOS is not one of those projects. Thelist of supported
hardwareis limited to Google Pixel 6 through Pixel 9
devices, with some trailing-edge support for Pixel 4 and 5
devices. Even then, though, the newer devices are strongly recommended:8th/9th generation Pixels provide a minimum guarantee of 7 years of
	support from launch instead of the previous 5 year minimum
	guarantee. 8th/9th generation Pixels also bring support for the
	incredibly powerful hardware memory tagging security feature as
	part of moving to new ARMv9 CPU cores. GrapheneOS uses hardware
	memory tagging by default to protect the base OS and known
	compatible user installed apps against exploitation, with the
	option to use it for all apps and opt-out on a case-by-case basis
	for the few incompatible with it.My phone had been making it clear for a while that it could not be counted
on in the future, but the prospect of buying a new one inspired a lot of
trepidation. Each new device seems to come with more privacy-hostile
"features" and intrusive AI "assistants"; finding all of the necessary
"disable" switches is a tedious and error-prone task. That, along with thenewsthat Google's "Gemini" feels increasingly entitled to a device-owner's data
regardless of its configuration, inspired the purchase of a Pixel 9
device that would be used to experiment with GrapheneOS to see if it could
replace stock Android for everyday use.Flashing the firmware of an expensive device is always a bit of a nervous
prospect; the GrapheneOS installer is designed to minimize the amount of
fingernail biting involved in the process. There are two installation
methods described in the documentation — a web-based install, and one that
works from the command line. Naturally, I chose the command-line version.The instructionsare
straightforward enough: download the installation image, connect the
device, and run the supplied script. Said script ran to completion and
confidently declared victory at the end, but the device still only booted
into normal Android — a repeatable result, but not quite the intended one.Some investigation turned up the (undocumented) fact that the web
installation method is seen as being rather more reliable than the
command-line version. So I tried that, and it worked as intended; the
GrapheneOS experiment had begun in earnest.#### First impressionsStock Android includes some nice features to make the move to a new device
as easy as possible — unsurprising, given the strong incentive to get
people to make that move often. Most of the data, apps, and configurations
that were on the old device will be automatically moved to the new one.
GrapheneOS has no such feature; a newly installed phone is a blank slate
that must be reconfigured from the beginning. One should expect to spend a
lot of time rediscovering all of those settings that were set just right some
years ago.As can be seen from the screenshot to the right, the initial GrapheneOS
screen is an austere and monochromatic experience. The system handles
color just fine, but color is something for the owner to configure, it seems.A stock Android install comes with a large set of apps out of the box, many
of which the user likely never wanted in the first place, and many of which
often cannot be deleted. GrapheneOS does not have all of that stuff. It
comes with its own versions of the web browser, camera app, PDF viewer, and
app store. Notably, GrapheneOS doesnotinclude the Google Play
store or any apps from there (but keep reading for Google Play). The app
store offers all of 13 apps in total.The web browser is a Chromium fork calledVanadium. It enables
strict site isolation on mobile devices (which Chrome evidently does not)
and adds a number of code-hardening features. The documentation strongly
recommends avoiding Firefox, which is described as "more vulnerable to
exploitation".Thecamera appis said to
be the best available in a writing style that is often encountered with
GrapheneOS:GrapheneOS Camera is far better than any of the portable open
	source camera alternatives and even most proprietary camera apps
	including paid apps. On Pixels, Pixel Camera can be used as an
	alternative with more featuresThe camera app stripsExifmetadata by default, and location metadata must be enabled separately if it
is wanted.#### App storesOne other thing that can be installed from the GrapheneOS store is theAccrescentapp store,
which is an alternative repository that claims a focus on security and
privacy. It provides access to a few dozen more apps, includingOrganic Maps, theMollySignal fork, andIronFox, a hardened
version of
Firefox.With those app stores, one can enable a certain amount of basic phone
functionality, but the sad fact is that many of us will need a bit more
than that. One alternative, of course, isF-Droid, which can certainly be installed
and used on GrapheneOS. Hard-core security-oriented people, including
those in the GrapheneOS community, tend to look down on F-Droid (seethis
articlefor an example), but it is a useful source for (mostly)
free-software apps.In the end, though, it will often come down to using the Google Play store;
an Android device can be nearly useless for many people without the apps
found there. GrapheneOS offersa sandboxed
version of Google Playthat turns it into an ordinary app without the
special privileges that Google Play has on stock Android systems. It
worked without a hitch here; the documentation says that some apps may not
work properly, but I did not encounter any.It is worth noting that Android providesan "integrity
API"that can be used to query the status of the software running on
the device. Among other things, it can attest to whether the secure-boot
sequence was successfully executed, or whether the device is running an
official Android build. GrapheneOS implements this API and, since it uses
the secure-boot machinery, can pass the first test, but it is not an
official image and cannot pass the second. Some apps care about the
results of these queries and may refuse to work if they get an answer they
don't like.GrapheneOS will put up a notification for each use of this API, so it is
easy to see which apps are using it. Most don't, but some definitely do.
I saw a few apps query this API, but did not encounter any that refused to
work; booting securely was good enough for them. Some others are pickier;
there isa
short list of appsthat refuse to run under GrapheneOS available.
Testing any important apps before committing to an alternative build like
GrapheneOS is thus an important bit of diligence. One just has to hope
that a future app update won't make a working app decide to stop
cooperating; this is a definite risk factor associated with using any
alternative Android build.#### Security featuresGrapheneOS includes a number of security and privacy features beyond the
under-the-hood hardening. Many of them are designed to make the device
work as if the owner of the device actually owns it. For example, the
provisioning data included with Android, which tells the device how to work
with carriers around the world, allows those carriers to specify that
features like tethering are not to be made available. GrapheneOS never
quite got around to implementing that part of the system. There is,
instead, an option to prevent the phone from being downgraded to older,
less-secure cellular protocols.Standard Android gives control over some app permissions, but does not let
users deny network access to an app. GrapheneOS does provide that control,
though network access is enabled by default for compatibility reasons. If
network access is disabled, the app in question sees a world where that
access is still available, but, somehow, the device just never finds a
signal. So apps should not refuse to run just because network access is
unavailable (though they may, of course, fail to run correctly).There is a "sensors" permission bit that controls access to any
sensors that are not subject to one of the other permissions; these include
the accelerometer, compass, thermometer, or any other such that may be
present. This permission, too, is enabled by default but can be turned off
by the owner.Thestorage
scopesfeature can put apps into a sandbox where they believe they have
full access to the device's shared storage, but they can only access the
files they have created themselves. There is also acontact scopesfeature that allows apps to believe they have full access to the owner's
contacts, while keeping most or all of that data hidden from those apps.GrapheneOS supports fingerprint unlocking, just like normal Android, with
one difference: after five consecutive failures, the fingerprint feature is
disabled for 30 minutes. An owner being forced to supply a finger to
unlock a device can thus disable that functionality quickly by using an
unrecognized finger. For those whose privacy needs are more stringent, aduress PINcan be
configured; entering that PIN causes the device to immediately wipe all of
its data. Needless to say, this self-destruct feature should be used with
care.There isa special appthat can
audit the state of a GrapheneOS device and, using the hardware security
features, provide an attestation that the device has not been tampered with
or downgraded to an older software version.The project makes frequentreleases, and installed
GrapheneOS systems update aggressively. The project updated to the
Android 16 release in early July, slightly less than one month after
Google released that version. In the default configuration, the device
will automatically reboot after 18 hours of inactivity as a way of
pushing all data to (encrypted) rest; that also has the effect of making
the device run the latest software version.See alsothis
pagecomparing a long list of security features across several
Android-based builds.#### Governance and communityOne potential caveat is that the development community behind GrapheneOS is
somewhat murky. As mentioned, a foundation exists to support this system,
but there is little information about how the foundation operates beyondan impressively long listof ways
to donate. Thepublic registry
informationshows three directors: Micay, Khalykbek Yelshibekov, and
Dmytro Mukhomor, but there is no public information on how directors are
chosen or how the foundation uses its funds.There isa vast set of
repositoriescontaining the project's source, but there is little
information on how one might contribute or what the development community
is up to. Some information can be found onthe build-instructions page. The
project runsa set of chat rooms
and a forum, but they seem to be dominated by user-oriented
conversation rather than development. Participation by the project in the
forums comes from a generic "grapheneos" account.In a response to a private query, the project claimed to have ten active,
paid developers, most of whom are full time. One gets the feeling, though,
that Micay is still the driving force behind GrapheneOS; if nothing else,
the project's belligerentfediverse presencebears a
lot of resemblance to his previous interaction patterns. What would happen
if he were to depart the project is far from clear. There is a potential
risk here that is hard to quantify.#### Overall impressionsSetting up the device with GrapheneOS required a couple of days of work,
much of which was dedicated to reproducing the apps and configuration on
the older device. A certain amount of time must be put into setting the
privacy features appropriately and giving apps the permissions they need to
work. In the end, though, the device works just as well as its
predecessor, with all the needed functionality present, and a lot of
unneeded functionality absent. I have committed willingly to using it, and
have no intention of going back.The system is undoubtedly more secure, even if the invisible
hardening changes do not actually do anything. The sandboxing is tighter,
there is more control over what apps can do, and there is no AI jinni doing
its best to escape its bottle.The remaining problem, of course, is that, for many people, GrapheneOS alone
will not be enough, and it will be necessary to let the nose of proprietary
software into the tent. The documentation says that logging into the Play
Store is not required, but it insisted on a login for me, re-establishing
the umbilical connection to Google that installing GrapheneOS had cut. The
keyboard does not support "swipe" typing; users who want that will likely
end up installing GBoard, which poses privacy risks of its own. The
GrapheneOS messaging app works, but Google's app can filter out some spam,
one might as well toss it on. There are some reasonable,
privacy-respecting weather apps on F-Droid these days, but the proprietary,
privacy-trashing ones have better access to weather alerts (at least in
countries that still have functioning weather agencies) and red-flag
warnings. Android Auto is highly useful, and it works fine in GrapheneOS,
but it requires its own level of special access permissions.Then there is the whole slew of banking apps, ride-share apps, airline
apps, and so on that, seemingly, are indispensable in modern life. Each of
these pokes another hole into the private space that GrapheneOS has so
carefully created. Itispossible to live and thrive without these
tools, and many of us know people who do, but the tools exist and are
popular for a reason. For many, it is simply not possible to get by
without using proprietary software, much of which is known to be watching
our every move and acting in hostile ways.Putting GrapheneOS onto a phone, at least, forces an awareness of each hole
that is being poked, and provides an incentive to minimize those holes as
much as possible. When potentially malicious software has to be allowed
onto a device that contains many of our closest secrets, the system will at
least do its best to keep that software within its specified boundaries and
unable to do anything that it is not specifically allowed to do.
Installing GrapheneOS orients a device more toward the interests of its
owner; that, alone, is worth the price of admission.to post comments



### GrapheneOS also has fixes for vulnerabilities Android does not havePosted Jul 24, 2025 13:51 UTC (Thu)
 byDemiMarie(subscriber, #164188)
 [Link]For instance, TapTrap (https://taptrap.click) is fixed in GrapheneOS but not in other Android-based OSs, and it allows apps to get permissions without user consent. Some of the vulnerabilities GrapheneOS has patched that upstream Android has not are significantly worse than that.### Improved user profilesPosted Jul 24, 2025 16:12 UTC (Thu)
 byrjones(subscriber, #159862)
 [Link]I like the 'improved user profiles' feature of Graphene OS.For most applications I use most of the time Google umbilical cord is unnecessary. So all of those applications sit in my "owner" profile with no google services support. The majority are installed through the Obtainium app, which allows to manage and update applications directly pulled off the internet; typically apks generated as part of Github releases.But in addition to "Owner" I have "Work" and "Play" user profiles. Both of which use Android apps pulled from Google Play store.For example I bought a Bose noise cancelling headphones and while the Android app is not necessary for important functionality it does allow to manage bluetooth devices that the headphones are aware of and set custom noise cancelling profiles. So that ends up in the "Play" profile. I switch to the profile to configure the headphones and when I am done I shut it down and none of the stuff there remains active.That way I have a degree of control over when these sorts of google related services are active.Overall I am pretty happy with the switch to Graphene. The OS updates are frequent, but it is trivial to manage. It sends a message announcing a new update was downloaded and I need to reboot the phone to finalize the install. And that is it, no drama or brokenness. Pretty solid product in my experience.### Google login?Posted Jul 24, 2025 22:04 UTC (Thu)
 bypabs(subscriber, #43278)
 [Link] (2 responses)Which aspect of the OS/device required a Google login? The article doesn't make it clear. The Aurora Store mentioned in the GrapheneOS docs has allowed me still install apps while avoiding having a Google login, for other Android variants though.https://grapheneos.org/usage#sandboxed-google-play-instal...https://auroraoss.com/### Google login?Posted Jul 24, 2025 22:18 UTC (Thu)
 bycorbet(editor, #1)
 [Link]The Google login was required for the Play Store. I haven't tried Aurora.### Google login?Posted Jul 25, 2025 0:09 UTC (Fri)
 byrjones(subscriber, #159862)
 [Link]If you install and run the "sandboxed play services" then you'll need to log into Google.Aurora depends on logging into Google to get access to the playstore stuff, but using your personal account is optional. It'll use a generic aurora account or something like that by default.It has been a while since I did my Graphene OS install so I don't remember for certain, but I don't think it prompted me for google login on first boot. I didn't give it to it if it did. It isn't required by the OS by default.### GrapheneOS & law enforcementPosted Jul 24, 2025 22:16 UTC (Thu)
 bypabs(subscriber, #43278)
 [Link] (2 responses)Recently GrapheneOS has been smeared by law enforcement in Europe, saying organised crime prefers GrapheneOS on Pixel devices.https://grapheneos.social/@GrapheneOS/114784469162979608https://grapheneos.social/@GrapheneOS/114813613250805804https://www.androidauthority.com/google-pixel-organized-c...https://www.androidauthority.com/why-i-use-grapheneos-on-...### GrapheneOS & law enforcementPosted Jul 25, 2025 4:38 UTC (Fri)
 byraven667(subscriber, #5198)
 [Link]"smeared"? that sounds more like a recommendation ;-)### GrapheneOS & law enforcementPosted Jul 25, 2025 5:02 UTC (Fri)
 bydonald.buczek(subscriber, #112892)
 [Link]> Recently GrapheneOS has been smeared by law enforcement in Europe, saying organised crime prefers GrapheneOS on Pixel devices.That would at least be an indication of its effectiveness if criminal organizations, for whom privacy must be particularly important, were to rely on the system.### Attestation requirementsPosted Jul 24, 2025 22:39 UTC (Thu)
 bypabs(subscriber, #43278)
 [Link] (1 responses)Attestation requirements seem like an anti-competitive action to me, I wonder if they are illegal under anti-trust law in some countries?### f-droidPosted Jul 25, 2025 4:37 UTC (Fri)
 byachak(subscriber, #178511)
 [Link]GOS is like a swiss-army-knife for android, it is highly configurable for many use cases and still can be secure and private at certain degrees, no need for another marketplace to deliver and update apps; another f-droid repository could do the job.### UglyPosted Jul 25, 2025 5:06 UTC (Fri)
 bymarcH(subscriber, #57642)
 [Link]> if nothing else, the project's belligerent fediverse presence bears a lot of resemblance to his previous interaction patterns.I just spent 5-10 min looking at some fights between /e/OS and GrapheneOS it was really painful to see. Supposedly, nothing unites like a "common enemy" but no: those guys manage to prove that wrong! I have no issue with "my security is bigger than yours" contests and other comparisons as long as the tone reflects a sane coopetition. But the tone I saw was not friendly at all. I don't have the time to fact-check or even read the technical assertions or verify "who started it" but it does not matter because the situation is very sad in any case.The most mature side (again: I don't know which side it is) should just completely stop engaging on social media with the less mature side until the latter learns the most basic life skills (with most adults: never. Too late.) The former should still deal with any valid bug reported by the latter but they should pretend the report came from somewhere else and never engage directly.Never. Feed. The. Troll. Always, always ignore it.





Copyright © 2025, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
