---
title: F-Droid and Google's Developer Registration Decree | F-Droid - Free and Open Source Android App Repository
url: https://f-droid.org/2025/09/29/google-developer-registration-decree.html
site_name: hackernews_api
fetched_at: '2025-09-29T11:08:31.120257'
original_url: https://f-droid.org/2025/09/29/google-developer-registration-decree.html
author: gumby271
date: '2025-09-29'
description: For the past 15 years1, F-Droid has provided a safe and securehaven for Android users around the world to find and install free and opensource apps. When con...
tags:
- hackernews
- trending
---

For the past 15 years1, F-Droid has provided a safe and secure
haven for Android users around the world to find and install free and open
source apps. When contrasted with the commercial app stores — of which the
Google Play store is the most prominent — the differences are stark: they
are hotbeds of spyware and scams, blatantly promoting apps that prey on
their users through attempts to monetize their attention and mine their
intimate information through any means necessary, including trickery and
dark patterns.[^spyware1]

https://f-droid.org/2025/09/04/twif.html[^spyware1]: “Spyware maker caught distributing malicious Android apps for
years”:https://techcrunch.com/2025/02/13/spyware-maker-caught-distributing-malicious-android-apps-for-years

F-Droid is different. It distributes apps that have been validated to workforthe user’s interests, rather than for the interests of the app’s
distributors. The way F-Droid works is simple: when a developer creates an
app and hosts the source code publicly somewhere, the F-Droid team reviews
it, inspecting it to ensure that it is completely open source and contains
no undocumentedanti-featuressuch as advertisements or
trackers2. Once it passes inspection, the F-Droid build
service compiles and packages the app to make it ready for distribution. The
package is then signed either with F-Droid’s cryptographic key, or, if the
build is reproducible[^reproducible], enables distribution using the
original developer’s private key. In this way, users can trust that any app
distributed through F-Droid is the one that was built from the specified
source code and has not been tampered with.

https://f-droid.org/docs/Anti-Features/[^reproducible]: F-Droid Reproducible Builds Introduction:https://f-droid.org/docs/Reproducible_Builds/

Do you want a weather app that doesn’t transmit your every movement to a
shadowy data broker3? Or a scheduling assistant that doesn’t
siphon your intimate details into an advertisement
network[^surveillance-ads]? F-Droid has your back. Just as sunlight is the
best disinfectant against corruption, open source is the best defense
against software acting against the interests of the user.

https://www.howtogeek.com/884233/your-weather-app-is-spying-on-you-heres-what-to-do/#why-are-weather-apps-such-a-privacy-nightmare[^surveillance-ads]: “Online Behavioral Ads Fuel the Surveillance
Industry—Here’s How”:https://www.eff.org/deeplinks/2025/01/online-behavioral-ads-fuel-surveillance-industry-heres-how

### Google’s move to break free app distribution

The future of this elegant and proven system was put in jeopardy last month,
when Google unilaterally decreed4that Android developers everywhere
in the world are going to be required to register centrally with Google. In
addition to demanding payment of a registration fee and agreement to their
(non-negotiable and ever-changing) terms and conditions, Google will also
require the uploading of personally identifying documents[^regid], including
government ID, by the authors of the software, as well as enumerating all
the unique “application identifiers” for every app that is to be distributed
by the registered developer.[^regappid]

require all apps to be registered by verified developers in order to be
installed by users on certified Android devices.”https://android-developers.googleblog.com/2025/08/elevating-android-security.html[^regid]: Android developer verification: “You will need to provide and
verify your personal details, like your legal name, address, email address,
and phone number. You may also need to upload official government ID.”:https://developer.android.com/developer-verification#verify-your-identity[^regappid]: Android developer verification: “You’ll need to prove you own
your apps by providing your app package name and app signing keys.”:https://developer.android.com/developer-verification#register-your-apps

The F-Droid project cannot require that developers register their apps
through Google, but at the same time, we cannot “take over” the application
identifiers for the open-source apps we distribute, as that would
effectively seize exclusive distribution rights to those applications.

If it were to be put into effect, the developer registration decree will end
the F-Droid project and other free/open-source app distribution sources as
we know them today, and the world will be deprived of the safety and
security of the catalog of thousands of apps that can be trusted and
verified by any and all. F-Droid’s myriad users5will be left
adrift, with no means to install — or even update their existing installed —
applications.

because we don’t track users or have any registration. “No user accounts, by
design”:https://f-droid.org/2022/02/28/no-user-accounts-by-design.html

### The Security Canard

While directly installing — or “sideloading”6— software can be
construed as carrying some inherent risk, it is false to claim that
centralized app stores are the only safe option for software
distribution. Google Play itself has repeatedly hosted
malware[^playmal1][^playmal2], proving that corporate gatekeeping doesn’t
guarantee user protection. By contrast, F-Droid offers a trustworthy and
transparent alternative approach to security: every app is free and open
source, the code can be audited by anyone, the build process and logs are
public, and reproducible builds ensure that what is published matches the
source code exactly. This transparency and accountability provides astrongerbasis for trust than closed platforms, while still giving users
freedom to choose. Restricting direct app installation not only undermines
that choice, it also erodes the diversity and resilience of the open-source
ecosystem by consolidating control in the hands of a few corporate players.

came up with; it means “installing software without our permission,” which
we used to just call “installing software” (because you don’t need a
manufacturer’s permission to install software on your computer).’ —
Pluralistic:Darth Android:https://pluralistic.net/2025/09/01/fulu/[^playmal1]: “224 malicious apps removed from the Google Play Store after ad
fraud campaign discovered”:https://www.malwarebytes.com/blog/news/2025/09/224-malicious-apps-removed-from-the-google-play-store-after-ad-fraud-campaign-discovered[^playmal2]: “Malware-ridden apps made it into Google’s Play Store, scored
19 million downloads”:https://www.theregister.com/2025/08/26/apps_android_malware/

Furthermore, Google’s framing that they need to mandate developer
registration in order to defend against malware is disingenuous because theyalreadyhave a remediation mechanism for malware they identify on a
device: the Play Protect service7that is enabled on all
Android Certified devices already scans and disables apps that have been
identified as malware, regardless of their provenience. Any perceived risks
associated with direct app installation can be mitigated through user
education, open-source transparency, and existing security measures without
imposing exclusionary registration requirements.

harmful behavior”:https://support.google.com/googleplay/answer/2812853

We do not believe that developer registration is motivated by security. We
believe it is about consolidating power and tightening control over a
formerly open ecosystem.

### The Right to Run

If you own a computer, you should have the right to run whatever programs
you want on it. This is just as true with the apps on your Android/iPhone
mobile device as it is with the applications on your Linux/Mac/Windows
desktop or server. Forcing software creators into a centralized registration
scheme in order to publish and distribute their works is as egregious as
forcing writers and artists to register with a central authority in order to
be able to distribute their creative works. It is an offense to the core
principles of free speech and thought that are central to the workings of
democratic societies around the world.

By tying application identifiers to personal ID checks and fees, Google is
building a choke point that restricts competition and limits user
freedom. It must find a solution which preserves user rights, freedom of
choice, and a healthy, competitive ecosystem.

### What do we propose?

Regulatory and competition authorities should look carefully at Google’s
proposed activities, and ensure that policies designed to improve security
are not abused to consolidate monopoly control. We urge regulators to
safeguard the ability of alternative app stores and open-source projects to
operate freely, and to protect developers who cannot or will not comply with
exclusionary registration schemes and demands for personal information.

If you are a developer or user who values digital freedom, you can
help. Write to your Member of Parliament8,
Congressperson[^congressperson] or other representative, sign petitions in
defense of sideloading, and contact the European Commission’s Digital
Markets Act (DMA) team9to express why preserving open
distribution matters. By making your voice heard, you help defend not only
F-Droid, but the principle that software should remain a commons, accessible
and free from unnecessary corporate gatekeeping.

https://www.europarl.europa.eu/meps/en/home[^congressperson]: Find Your Representativehttps://www.house.gov/representatives/find-your-representative

https://digital-markets-act.ec.europa.eu/contact-dma-team_en

1. “For fifteen more”:↩
2. F-Droid Anti-Features overview:↩
3. “Your Weather App Is Spying on You, Here’s What to Do”:↩
4. Android Developers Blog: “Starting next year, Android will↩
5. How many F-Droid users are there, exactly? We don’t know,↩
6. ‘“Sideload” is a weird euphemism that the mobile duopoly↩
7. “Google Play Protect checks your apps and devices for↩
8. Members of the European Parliament↩
9. Contact the DMA team:↩
