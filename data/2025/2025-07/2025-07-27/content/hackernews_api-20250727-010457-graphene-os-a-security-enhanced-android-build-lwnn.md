---
title: 'Graphene OS: a security-enhanced Android build [LWN.net]'
url: https://lwn.net/SubscriberLink/1030004/898017c7953c0946/
site_name: hackernews_api
fetched_at: '2025-07-27T01:04:57.720950'
original_url: https://lwn.net/SubscriberLink/1030004/898017c7953c0946/
author: madars
date: '2025-07-25'
description: 'Graphene OS: a security-enhanced Android build'
tags:
- hackernews
- trending
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

 By
Jonathan Corbet
July 24, 2025


People tend to put a lot of trust into their phones. Those devices have
access to no end of sensitive data about our lives — our movements,
finances, communications, and more — so phones belonging to even relatively
low-profile people can be high-value targets. Android devices run free
software, at least at some levels, so it should be possible to ensure that
they are working in their owners' interests. Off-the-shelf Android
installations tend to fall short of that goal. The
GrapheneOS
 Android rebuild is an attempt
to improve on that situation.

GrapheneOS got its start as "CopperheadOS"; it wasreviewed herein 2016. A couple of years
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
into making the security improvements as unobtrusive as possible.No AI slop, all substance: subscribe to LWN todayLWN has always been about quality over quantity; we need your help
to continue publishing in-depth, reader-focused articles about Linux
and the free-software community. Please subscribe today to support our work
and keep LWN on the air; we are offeringa free one-month trial subscriptionto get you started.#### InstallationSome Android rebuilds prioritize supporting a wide range of devices, often
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
 [Link] (1 responses)I like the 'improved user profiles' feature of Graphene OS.For most applications I use most of the time Google umbilical cord is unnecessary. So all of those applications sit in my "owner" profile with no google services support. The majority are installed through the Obtainium app, which allows to manage and update applications directly pulled off the internet; typically apks generated as part of Github releases.But in addition to "Owner" I have "Work" and "Play" user profiles. Both of which use Android apps pulled from Google Play store.For example I bought a Bose noise cancelling headphones and while the Android app is not necessary for important functionality it does allow to manage bluetooth devices that the headphones are aware of and set custom noise cancelling profiles. So that ends up in the "Play" profile. I switch to the profile to configure the headphones and when I am done I shut it down and none of the stuff there remains active.That way I have a degree of control over when these sorts of google related services are active.Overall I am pretty happy with the switch to Graphene. The OS updates are frequent, but it is trivial to manage. It sends a message announcing a new update was downloaded and I need to reboot the phone to finalize the install. And that is it, no drama or brokenness. Pretty solid product in my experience.### Improved user profilesPosted Jul 25, 2025 11:30 UTC (Fri)
 byjcul(subscriber, #171954)
 [Link]It's also useful for having a stripped down "camera" only profile, for when you want to have a digital detox but still take photos.Or having additional google profiles, I manage my wife's grandparents' google devices like this.To be fair stock android allows multiple profiles, but of course not with the option of them being AOSP or Google play.And Graphene allows a lot more profiles.The private space on android is great too, I think it's an android thing and not just graphene specific.But it allows you a bit more overlap between main profile and private profile, like copy / pasting, sharing photos. Except one or the other can be without play services if desired.Same thing for self managed work profile, which can be set up with shelter.https://f-droid.org/en/packages/net.typeblog.shelter/Though I actually do use shelter as a true work profile, so I can switch off slack, work email etc when not working.### Google login?Posted Jul 24, 2025 22:04 UTC (Thu)
 bypabs(subscriber, #43278)
 [Link] (3 responses)Which aspect of the OS/device required a Google login? The article doesn't make it clear. The Aurora Store mentioned in the GrapheneOS docs has allowed me still install apps while avoiding having a Google login, for other Android variants though.https://grapheneos.org/usage#sandboxed-google-play-instal...https://auroraoss.com/### Google login?Posted Jul 24, 2025 22:18 UTC (Thu)
 bycorbet(editor, #1)
 [Link]The Google login was required for the Play Store. I haven't tried Aurora.### Google login?Posted Jul 25, 2025 0:09 UTC (Fri)
 byrjones(subscriber, #159862)
 [Link]If you install and run the "sandboxed play services" then you'll need to log into Google.Aurora depends on logging into Google to get access to the playstore stuff, but using your personal account is optional. It'll use a generic aurora account or something like that by default.It has been a while since I did my Graphene OS install so I don't remember for certain, but I don't think it prompted me for google login on first boot. I didn't give it to it if it did. It isn't required by the OS by default.### Google login?Posted Jul 25, 2025 11:14 UTC (Fri)
 byvimja(subscriber, #91577)
 [Link]I'm running Graphene without a Google Login. You don't need one, really.You can get proprietary apps through Aurora which will use it's own generic login.Just if you have something that really-really needs Play services or if you want to buy apps or download a previously bought app, you'll need a Google account.### GrapheneOS & law enforcementPosted Jul 24, 2025 22:16 UTC (Thu)
 bypabs(subscriber, #43278)
 [Link] (4 responses)Recently GrapheneOS has been smeared by law enforcement in Europe, saying organised crime prefers GrapheneOS on Pixel devices.https://grapheneos.social/@GrapheneOS/114784469162979608https://grapheneos.social/@GrapheneOS/114813613250805804https://www.androidauthority.com/google-pixel-organized-c...https://www.androidauthority.com/why-i-use-grapheneos-on-...### GrapheneOS & law enforcementPosted Jul 25, 2025 4:38 UTC (Fri)
 byraven667(subscriber, #5198)
 [Link]"smeared"? that sounds more like a recommendation ;-)### GrapheneOS & law enforcementPosted Jul 25, 2025 5:02 UTC (Fri)
 bydonald.buczek(subscriber, #112892)
 [Link]> Recently GrapheneOS has been smeared by law enforcement in Europe, saying organised crime prefers GrapheneOS on Pixel devices.That would at least be an indication of its effectiveness if criminal organizations, for whom privacy must be particularly important, were to rely on the system.### GrapheneOS & law enforcementPosted Jul 25, 2025 6:23 UTC (Fri)
 bydanieldk(subscriber, #27876)
 [Link]Smear campaign? More like a quote of a single police official:> As it sounds . The phrase "every time we see a Pixel we think it could be a drug dealer" is as forceful as it is surprising. It comes from a Catalan anti-drug official for the Mossos d'Esquadra (Catalan police) who spoke to DiariAra about the phones they see during their operations. Far from being a Google problem (of course), the reason its phones have become popular among criminal gangs is, paradoxically, one of its greatest virtues for Android enthusiasts: its freedom. A freedom that, combined with the installation of an alternative operating system, makes it an almost infallible communication tool.blown up by some Android news sites to a smear campaign for clicks.Original source:https://www.xatakandroid.com/sociedad/cada-vez-que-vemos-...### GrapheneOS & law enforcementPosted Jul 25, 2025 6:26 UTC (Fri)
 bylunaryorn(subscriber, #111088)
 [Link]Did you read the article?"Law enforcement in Europe"? Hardly so. More like "the regional police in one specific Spanish autonomous region which represents just about 2% of the whole EU population", according to one (machine translated) article in a Spanish internet outlet".Neither the most reliable source nor national news. More like someone was desparately locking for some clickbait... and hugely blown out of proportion.### Attestation requirementsPosted Jul 24, 2025 22:39 UTC (Thu)
 bypabs(subscriber, #43278)
 [Link] (2 responses)Attestation requirements seem like an anti-competitive action to me, I wonder if they are illegal under anti-trust law in some countries?### f-droidPosted Jul 25, 2025 4:37 UTC (Fri)
 byachak(subscriber, #178511)
 [Link]GOS is like a swiss-army-knife for android, it is highly configurable for many use cases and still can be secure and private at certain degrees, no need for another marketplace to deliver and update apps; another f-droid repository could do the job.### Attestation requirementsPosted Jul 26, 2025 13:06 UTC (Sat)
 bykleptog(subscriber, #1183)
 [Link]> Attestation requirements seem like an anti-competitive action to me, I wonder if they are illegal under anti-trust law in some countries?They probably probably could be, if they were used that way.Like how DVD region coding was labelled anti-competitive in Australia because its primary effect was to make the majority of DVD content unavailable to Australians.So, if it turned out that a lot of popular apps started using attestation for inappropriate reasons, you might get some regulatory attention. But the current state I don't think there's likely to be a problem.### UglyPosted Jul 25, 2025 5:06 UTC (Fri)
 bymarcH(subscriber, #57642)
 [Link]> if nothing else, the project's belligerent fediverse presence bears a lot of resemblance to his previous interaction patterns.I just spent 5-10 min looking at some fights between /e/OS and GrapheneOS it was really painful to see. Supposedly, nothing unites like a "common enemy" but no: those guys manage to prove that wrong! I have no issue with "my security is bigger than yours" contests and other comparisons as long as the tone reflects a sane coopetition. But the tone I saw was not friendly at all. I don't have the time to fact-check or even read the technical assertions or verify "who started it" but it does not matter because the situation is very sad in any case.The most mature side (again: I don't know which side it is) should just completely stop engaging on social media with the less mature side until the latter learns the most basic life skills (with most adults: never. Too late.) The former should still deal with any valid bug reported by the latter but they should pretend the report came from somewhere else and never engage directly.Never. Feed. The. Troll. Always, always ignore it.### What about transparency?Posted Jul 25, 2025 6:24 UTC (Fri)
 byacer(subscriber, #156526)
 [Link] (2 responses)How can we trust a project that is not transparent when it comes to development and the internal organisation?### What about transparency?Posted Jul 25, 2025 6:32 UTC (Fri)
 bymarcH(subscriber, #57642)
 [Link]Lesser of many evils?### What about transparency?Posted Jul 25, 2025 13:28 UTC (Fri)
 bymathstuf(subscriber, #69389)
 [Link]So…don't use a smart phone then?### Hostile to rootPosted Jul 25, 2025 7:13 UTC (Fri)
 bywsy(subscriber, #121706)
 [Link] (2 responses)As a grapheneos user, my only complaint is its lack of support for root permission. I have to use a custom build of magisk and keep the bootloader unlocked. I don't think giving device owner root permission weakens the security of the system. With root permission, I can use more tools to monitor and control how apps work.### Hostile to rootPosted Jul 25, 2025 10:15 UTC (Fri)
 bynumgmt(subscriber, #167446)
 [Link] (1 responses)The GrapheneOS developer community vehemently disagrees with the notion that rootful Android does not weaken the security of the system.Notably, without Verified Boot, malware persisting at the lowest levels of the device is possible. It prevents rootkit persistence. Without verified boot, you have no guarantees. This is a compelling reason to have a locked bootloader with verified boot enabled.In fact, it's a big reason why the Pixel is the only device GrapheneOS supports. Few other OEMs produce phones that allow you to re-lock the bootloader.That being said, if GrapheneOS didn't exist, I'd be running rootful LineageOS or whatever the heck would get me a halfway decent experience instead of stock.### Hostile to rootPosted Jul 25, 2025 16:09 UTC (Fri)
 bywsy(subscriber, #121706)
 [Link]Verified Boot does not mean owners can't have root permission. I just want to do whatever I want to 3rd party apps without modifying the system. I do understand most people don't need that. But for me a device without root is not my device.### Graphene + Aurora (but no Google Play) herePosted Jul 25, 2025 8:28 UTC (Fri)
 byvimja(subscriber, #91577)
 [Link]I always though Android w/o Google would be near impossible to use and was only for the very hard core. But then we had a long discussion on the topic in the local hacker space where many people described the positive experiences they've made. This gave me the motivation to try it myself.So not too long ago, I switched to a Google Pixel 9a and installed Graphene. I've been very happy with it ever since. I don't use the Google Play services, not even microG.I still need some proprietary apps, but I get those through the Aurora Store. That way I don't have to login to a Google Account. Without Google Play, some apps have missing functionality, most notable the push notifications which are not working. Also some Apps won't show a map where they should.But with a single exceptions, all the apps I use work. Even banking and credit card apps (of 3 different banks), local public transport app for purchasing tickets on the phone, a local pay-by-phone provider (Twint), and a government provided authentication app all run.Funnily enough, Twint is popping up warnings about the app not working without Play servcies. On every interaction. Twice. But after clicking those away, the app works just fine.Day to day I mostly use Open Source apps and those run very well indeed. Many can use UnifiedPush for push notifications or come, like Threema Libre, with their own push implementation.At the moment, I'm living a Google free and happy life ;)### Corrections/elaborations on some pointsPosted Jul 25, 2025 14:32 UTC (Fri)
 bymatchboxbananasynergy(subscriber, #178520)
 [Link]Hi everyone. GrapheneOS community manager here. We reached out to the author with some comments/corrections and we were encouraged to post them as a comment, as there seems to be a policy to not editing the article after publication in most cases.One is about the history of the project. The open source project has been the same from the beginning. It started as a solo project, was known as CopperheadOS for a time, then later was renamed to GrapheneOS. What is now CopperheadOS is a fork. See the following links:-https://github.com/GrapheneOS/platform_manifest/forks?inc...-https://github.com/GrapheneOS/platform_bionic/forks?inclu...-https://github.com/GrapheneOS-Archive/legacy_bugtracker/i...The above links show forks of our repositories dating back to 2016, which shows that GrapheneOS is the original project, not some spin-off that started later. The third link points to our legacy bugtracker, prior to the rename.Regarding the failed cli install, we're not sure what happened there. Flashing that way works fine. We are aware that some issues can arise in certain cases, like when using OS-provided Fastboot. If you were to try again, we'd suggest making sure you are using the Fastboot mentioned in our install instructions to avoid these sorts of issues.We usually suggest people flash GrapheneOS using the web installer because it's easier for most people. Also, as you found, the cli install is robust but uses more OS-provided functionality so more issues can occur due to bugs in the OS outside of our control especially if using an OS package for fastboot. We're glad you were able to install GrapheneOS easily with the web installer, though.Regarding Play Integrity, it should be noted that there's nothing we can do if apps check for device or strong integrity since Play Integrity responses are signed by Google. The issue isn't one of whether we've implemented something or not. We do have a guide on how apps can add support for GrapheneOS using hardware attestationhttps://grapheneos.org/articles/attestation-compatibility..., which some apps have done, including Yuh and Swissquote.Regarding the network permission, users can install apps without the network permission granted by unchecking the network permission box when installing the app.And for the sensors permission, there is a toggle in Settings where apps can have the sensors permission not granted by default.In the section about fingerprint unlocks and PINs are mentioned, it is worth explaining that the duress feature doesn't brick the device, it wipes keys from the keystore (among other things). After duress is triggered, the device will say it's corrupt, and from there it can be factory reset via Recovery.It is mentioned that after 5 unsuccessful fingerprint attempts, you're locked out for 30 minutes. On GrapheneOS, it is permanent until you input your primary unlock method again. On the stock OS, it locks you out after 5 attempts for a time period and has permanent lockout until you input your primary unlock method again after 20 attempts.A related feature is our 2nd factor fingerprint unlock feature. When using this feature, users can set a very strong alphanumeric password for the primary unlock method and use their enrolled fingerprint + a PIN for added security.The best way to see what the project is prioritizing is by checking the issue tracker. Planned features have priority labels.Development guidelines can be found in the build page that is linked there, under this section:https://grapheneos.org/build#development-guidelines, and if someone wanted to help contribute, they can express interest in our development room, or they can comment on an issue they are interested in contributing to.The project has and is subject to attacks over the years, so most contributors prefer to keep their heads down and maintain anonymity. This way they are less likely to be targeted. We really care about protecting our project members, so we're taking the appropriate measures to do that.This may be why from the outside it looks like Daniel Micay is still the driving force of the project, which makes sense because he's the founder and has always been the public face for the project. Nowadays, other developers do the majority of development work, including reviews. Nonetheless, his expertise remains invaluable to the project.Some other thoughts:- On the stock OS, Android Auto is a privileged app. On GrapheneOS it's sandboxed and only necessary permissions are granted if users toggle them on. Still more access than other apps, but configurable and better than on other OSes.- App compatibility is a priority for the project and we are always working on maintaining/improving that.- From our perspective, running an invasive app on GrapheneOS is much better than running it on a less secure, less private OS that doesn't provide the same amount of control.- It's important to note that if hardening features break apps, there are toggles that can be used to make apps work again.- A correction regarding the timeline for Android 16: the initial upstream release was on June 10th and our initial production release was on June 30. It usually takes us ~2 days, but took longer this time due to upstream dropping some device repositories, so porting took longer than usual. We did backport driver/firmware security patches to Android 15 before finalizing the Android 16 port.- At the beginning of the article, it was said that GrapheneOS is an "Android rebuild". It would be more accurate to call it a fork of the Android Open Source Project (AOSP).### HeliBoard keyboardPosted Jul 25, 2025 15:07 UTC (Fri)
 bymichaelo(subscriber, #23907)
 [Link]Have you tried the HeliBoard keyboard?It's an OpenBoard derivative available in F-Droid. I've been happily using it for 6 months now. At last a Free Software option that doesn't make me miserable (compared to Swiftkey I was using before, which was hard to move away from).### How the project really feels about this articlePosted Jul 25, 2025 18:08 UTC (Fri)
 bycorbet(editor, #1)
 [Link] (4 responses)For the curious, here isthe GrapheneOS project's fediverse responseto this article.### How the project really feels about this articlePosted Jul 25, 2025 19:20 UTC (Fri)
 byDemiMarie(subscriber, #164188)
 [Link]Thank you for linking to that response.### How the project really feels about this articlePosted Jul 25, 2025 19:27 UTC (Fri)
 byexcors(subscriber, #95769)
 [Link] (1 responses)Unfortunately we can no longer see how they really feel, because they deleted the parts of their original response that accused this article of being influenced by LWN's long-standing bias against PaX/grsecurity.(I wouldn't bring that up if they indicated they had changed their mind about the accusation, but I get the impression they just realised they shouldn't have said it out loud because it makes them sound much less reasonable to other readers. The original response certainly backs up the article's comment on the project having a "belligerent fediverse presence".)### How the project really feels about this articlePosted Jul 25, 2025 20:02 UTC (Fri)
 bycorbet(editor, #1)
 [Link]Interesting, they also deleted my responses, before I gave up on it. What's there now is pretty far removed from what that conversation initially looked like. It's tempting to resurrect the whole thing out of my client history ... but I suspect I'll manage to resist.### How the project really feels about this articlePosted Jul 25, 2025 20:30 UTC (Fri)
 bytschoerbi(subscriber, #88015)
 [Link]Graphene OS looks very good on paper, and from what I heard from the few users I know, it hold many of its promises. Sadly, the people behind it don't work well with the communities (FOSS, security, privacy communities). I have been associated with various privacy-oriented projects and whenever anyone from Graphene OS appears, it's but a bad thing. I can't but call what I have seen harassment. Usually coming from someone with a severe superiority complex. Often some long-wound text that can be summarized as "we know it best and everyone disagreeing is an idiot (or worse)."I hoped for the project to become more open over time and for a community forming around. Sadly, this doesn't appear to have happened. For the time being, I'll stay away from it simply as result who is running it. I'd rather not been seen as supporting this kind of behavior, or worse, being associated with it.





Copyright © 2025, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
