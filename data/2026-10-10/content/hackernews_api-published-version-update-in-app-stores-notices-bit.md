---
title: Published version update in app stores - Notices - Bitwarden Community Forums
url: https://community.bitwarden.com/t/published-version-update-in-app-stores/102750
site_name: hackernews_api
content_file: hackernews_api-published-version-update-in-app-stores-notices-bit
fetched_at: '2026-10-10T22:14:14.790147'
original_url: https://community.bitwarden.com/t/published-version-update-in-app-stores/102750
author: Cider9986
date: '2026-10-10'
published_date: '2026-10-09T15:04:03+00:00'
description: Hello everyone! Starting in the next release, the Bitwarden apps published to the various stores will be the commercially licensed builds. No action is needed, and the apps will work exactly as they do today. Bitwarde…
tags:
- hackernews
- trending
---

# Published version update in app stores

Announcements

Notices

app:all

RyanL

 October 9, 2026, 3:04pm
 

1

Hello everyone!

Starting in the next release, the Bitwarden apps published to the various stores will be the commercially licensed builds. No action is needed, and the apps will work exactly as they do today.

* Bitwarden remains committed to open source security and transparency
* The GPLv3 OSS licensed version continues to be updated and published on GitHub
* All current features are available in both versions
* License details are onGitHub
* Bitwarden remains committed to a robust, free forever plan for everyone

If you have any questions, please ask them in this thread. Thanks all!

EDIT:You can still read, audit, and contribute to the codebase on GitHub, and that isn’t changing. The apps we release are built from the code in those repositories.

* Bitwarden is not going closed-source
* You can still fork Bitwarden
* No change to self-hosting, the licensing change affects those who are repackaging and reselling Bitwarden
* The free plan is here to stay permanently

1 Like

grb

 October 9, 2026, 3:16pm
 

2

Will thePortable Desktop App linkon Bitwarden’sDownload Pagedownload a build that is commercially licensed or OSS licensed?

Whatdifferenceswill exist between the two parallel versions?

RyanL

 October 9, 2026, 3:20pm
 

4

Some future components will be published under the commercial license and will exist only in that build. Newly developed features will be evaluated on a case-by-case basis for which license applies to them.

1 Like

RyanL

 October 9, 2026, 3:28pm
 

5

That’s a great question. I’ll work to get that information.

Edit: The download page will also direct link to the commercial license.

grb

 October 9, 2026, 3:33pm
 

6

Ahhh, so the word “current” is doing someheavy liftingin the following statement:

But will the new features (those excluded from the GPLv3 OSS licensed builds) still beopen source?

1 Like

grb

 October 9, 2026, 3:40pm
 

7

@RyanLGiven that there are already many features that are only unlocked for Premium subscriptions, will there now be up tofourlevels of functionality (as shown in the table below), and if so, will there be up to four different pricing tiers (including at least one “Free” option)?

Relative Cost

GPLv3 License

Commercial License

Non-Premium

Free

???

Premium

  $

$$$

RyanL

 October 9, 2026, 3:41pm
 

8

Direct downloads from theDownload the Bitwarden Password Manager App for iPhone, Android, Chrome, Safari, and More | Bitwardenpage will also be under the commercial license.

Yes, Bitwarden continues development of open source code under GPLv3. Code under the commercial license is just as viewable and transparent on GitHub. This licensing model provides additional legal protection for select features.

3 Likes

davidmayr

 (David Mayr)
 

 October 9, 2026, 6:52pm
 

9

This concerns me quite a bit tbh. It feels like the standard: Open Source → Semi Opensource → Open Source discontinued Rugpull quite a few companies have been doing lately. I especially got hit by this with MinIO, so I’m quite careful what I use now because MinIO has been a huge pain and switching from Bitwarden would be too.

I both pay for Bitwarden (although I don’t use any premium features. I got it to support Bitwarden so it can continue being an open source project. With the price increase I was already considering cancelling as I don’t use the premium stuff and with this it gives me even more reason to do so) but I also have Vaultwarden instances self-hosted for various projects to work in teams. Both are essential to me and I want both to work equally well. I currently neither plan to switch my personal Bitwarden to self hosted nor would I ever consider moving my self hosted instances to your servers.

So my questions are:

* Are there any new features coming to the OSS version, or is it staying as is with everything new being in the commercial version?
* What would I lose out on by not using the commercial version now or in the future?
* How are you guaranteeing that self-hosting will remain effortless and will it remain possible for third-party teams like Vaultwarden to continue to use the protocol?
* What version does the Linux Flatpak store receive? Will it remain the open source version or the commercial one?
* Will e.g. a commercial browser addon remain compatible with a open source client? (E.g. With the biometric thingy?)
* How are you guaranteeing to us that such a Rugpull will not happen now or in the future?

In any case Bitwarden will now be put on the list of things I will need to watch its development more closely in case this goes south.

Edit: I just saw in the comments that it was noted that it will be decided on case by case basis on what gets developed. Thats good for now I guess, yet the other questions remain open. (Ig it implicitly answers some other questions e.g. the self-hosting one too, but think of them more in the long run)

6 Likes

Lexx

 October 9, 2026, 6:52pm
 

10

While this might seem benign, Bitwarden would be well advised to review in detail what happened with the recent Coinkite fiasco. The security playing field is basically identical and the extremely real (and dramatically realized) risk is basically identical.

In summary: CoinKite ColdCard was also published open software but without a FOSS license. This, in turn, eliminated any possibility and motivation for the community to fork, audit, and review their software. This, in turn, allowed a, frankly, idiotic bug to fester. This in turn led to users’/customers’ loss of a few million dollars of value to an almost trivial exploit that can’t even be classified as a proper hack. Besides insane value loss, Coinkite is effectively dead as an enterprise and its principles doxed and will remain shunned the rest of their lives (deservedly so; I accidentally know one of them as a previous work colleague — not a bad guy, but this is deserved).

This is exactly where Bitwarden is heading now.

5 Likes

zfJames

 October 9, 2026, 7:16pm
 

11

This seems like a great reason for me to discontinue my Bitwarden subscription. Bitwarden is easily the best platform out there for password management but this is the obvious result of venture capital influence and attorneys.

What would keep me subscribed as a user if I have the requirement that I must be able to self-host a platform in order to keep using it (even if I am not currently self-hosting, which I am not)?

6 Likes

dwbit

 October 9, 2026, 7:18pm
 

12

Hey@zfJamesthere is no requirement to self-host and you can continue using the clients from the app storefronts as normal.

zfJames

 October 9, 2026, 7:21pm
 

13

Thank you for your reply! I think my question was worded confusingly.

My requirement for a password manager is: It must give me the option to self host if I choose to do so.

That is a safeguard against my passwords and data getting locked in a box that I cannot get out of. With this new license and policy, it is clear to me that Bitwarden now does not meet my requirements. An unnamed list of “features” will now be developed entirely apart from what I can host that may or may not end up being critical for security.

Can you confirm if this is correct?

1 Like

dwbit

 October 9, 2026, 7:22pm
 

14

That is incorrect, there is no change to the ability to self-host with a Bitwarden subscription.

Nail1684

 October 9, 2026, 7:28pm
 

15

I see no sign yet that vault export is getting removed. Quite the contrary, theCredential Exchange Protocol/Format (CXP/CXF)was added recently to the mobile apps.

1 Like

zfJames

 October 9, 2026, 7:29pm
 

16

Thank you for clarifying! That does not change my negative stance on this change but does help clarify operation.

dwbit

 October 9, 2026, 7:39pm
 

17

For your question on third-party community servers, there is no change, they can continue to choose which features to support and build out on their server.

1 Like

Wreckage

 October 9, 2026, 8:37pm
 

18

Not a great look, this seems a lot like openwashing. How can we trust that this is not the first step in a rug pull out of FOSS?

Can you clarify if commercial license exclusive features will be available for self hosted users? Are self hosted users now second class citizens?

dwbit

 October 9, 2026, 8:59pm
 

19

@Wreckageno change to self-hosting. This only affects those who are repackaging and reselling Bitwarden.

grb

 October 9, 2026, 9:34pm
 

20

@dwbitCould you please look into my unanswered question from above and see if some clarity can be provided?

1 Like

Wreckage

 October 9, 2026, 9:35pm
 

21

I understand, but I worry more about the future. Will all future features still be available for self hosters? Or should we expect that some future features will not be available for self hosters?

While I have been happy to be a paying subscriber, self hosting capabilities is very important to me as it is my exit strategy if something goes wrong.

next page →