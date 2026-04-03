---
title: Privacy Badger
url: https://privacybadger.org/
site_name: hackernews_api
fetched_at: '2025-09-30T11:08:55.194194'
original_url: https://privacybadger.org/
author: doener
date: '2025-09-28'
description: Privacy Badger is a free browser extension made by EFF to stop spying
tags:
- hackernews
- trending
---

Language


English

Deutsch

Español

Français

Русский

Svenska

Türkçe

中文（中国）

* English
* Deutsch
* Español
* Français
* Русский
* Svenska
* Türkçe
* 中文（中国）

Privacy Badger is a free browser extension made by the leading digital rights nonprofit
EFF
 to stop companies from spying on you online.

### Browser Not Supported

Privacy Badger is not supported in this browser (more info).

 Add to Chrome


 Add to Firefox


 Add to Firefox for Android


 Add to Edge


 Add to Edge for Android


 Add to Opera


 Add to Chrome


 Add to Firefox


 Add to Firefox for Android


 Add to Edge


 Add to Edge for Android


 Add to Opera


* Other browsers
* Alternative installation options

Release notes for v2025.9.5

## Frequently Asked Questions

* What is Privacy Badger?
* How is Privacy Badger different from other blocking extensions?
* Who makes Privacy Badger?
* How does Privacy Badger work?
* What is a third party tracker?
* What do the red, yellow and green sliders in the Privacy Badger menu mean?
* Why does Privacy Badger block ads?
* Why doesn't Privacy Badger block all ads?
* What is Global Privacy Control (GPC)?
* What about tracking by the sites I actively visit, like NYTimes.com or Facebook.com?
* Does Privacy Badger contain a list of blocked sites?
* How was the cookie blocking yellowlist created?
* Does Privacy Badger prevent fingerprinting?
* Does Privacy Badger consider every cookie to be a tracking cookie?
* Will you be supporting any other browsers besides Chrome, Firefox, Edge and Opera?
* Can I download Privacy Badger directly from eff.org?
* I run a domain that uses cookies or other tracking. How do I stop Privacy Badger from blocking me?
* Where can I find general information about Privacy Badger that I can use for a piece I'm writing?
* As an administrator, how do I configure Privacy Badger on my managed devices?
* What is the Privacy Badger license? Where is the Privacy Badger source code?
* How can I support Privacy Badger?
* How does Privacy Badger handle social media widgets?
* How do I uninstall/remove Privacy Badger?
* Is Privacy Badger compatible with other extensions, including adblockers?
* Is Privacy Badger compatible with Firefox's built-in privacy protections?
* Why does my browser connect to fastly.com IP addresses on startup after installing Privacy Badger?
* Why does Privacy Badger need access to my data for all websites?
* Why aren't videos loading on YouTube? Why isn't Privacy Badger blocking ads on YouTube?
* I need help! I found a bug! What do I do now?

### What is Privacy Badger?

Privacy Badger is a browser extension that stops advertisers and other third-party trackers from secretly tracking where you go and what pages you look at on the web. If an advertiser seems to be tracking you across multiple websites without your permission, Privacy Badger automatically blocks that advertiser from loading any more content in your browser. To the advertiser, it’s like you suddenly disappeared.

### How is Privacy Badger different from other blocking extensions?

Privacy Badger was born out of our desire to be able to recommend a single extension that would:

* Automatically analyze and block any tracker or ad that violated the principle of user consent
* Function well without any settings, knowledge, or configuration by the user
* Use algorithmic methods to decide what is and isn’t tracking
* Be produced by an organization that is unambiguously working for its users rather than for profit

As a result, Privacy Badger differs from traditional ad-blocking extensions in two key ways. First, while most other blocking extensions prioritize blocking ads, Privacy Badger doesn’t block ads unless they happen to be tracking you; in fact, one of our goals is to incentivize advertisers to adopt better privacy practices.

Second, most other blockers rely on a human-curated list of domains or URLs to block. Privacy Badger is an algorithmic tracker blocker – we define what “tracking” looks like, and then Privacy Badger blocks or restricts domains that it observes tracking in the wild. What is and isn’t considered a tracker is entirely based on how a specific domain acts, not on human judgment.

Privacy Badger sends theGlobal Privacy Controlsignal to opt you out of data sharing and selling, and theDo Not Tracksignal to tell companies not to track you. If trackers ignore these signals, Privacy Badger will learn to block them.

Beyond this, Privacy Badger comes with other advantages like cookie blocking,click-to-activate placeholdersfor potentially useful tracker widgets (video players, comments widgets, etc.), and outgoing link click tracking removal onFacebookandGoogle.

By using Privacy Badger, you support theElectronic Frontier Foundationand help fight for a better Web for everybody.

### Who makes Privacy Badger?

Privacy Badger was created by theElectronic Frontier Foundation, a nonprofit organization that protects your privacy and free expression online. We make free tools like Privacy Badger, publish educational guides, testify before lawmakers about technology, and fight for the public interest in court—all thanks to support from EFF’s members. If you want a better internet and a strong democracy,join the fightagainst creepy online surveillance.

### How does Privacy Badger work?

When you view a webpage, that page will often be made up of content from many different sources. For example, a news webpage might load the actual article from the news company, ads from an ad company, and the comments section from a different company that’s been contracted out to provide that service.

Privacy Badger keeps track of all of this. If the same source seems to be tracking across different websites, then Privacy Badger springs into action, telling the browser not to load any more content from that source. And when your browser stops loading content from a source, that source can no longer track you. Voila!

At a more technical level, Privacy Badger keeps track of the “third party” domains that embed images, scripts and advertising in the pages you visit. Privacy Badger looks for tracking techniques like uniquely identifying cookies, local storage “supercookies,” and canvas fingerprinting. If it observes the same third-party host tracking on three separate sites, Privacy Badger will automatically disallow content from that third-party tracker.

By default, Privacy Badger receivesperiodic learning updatesfromBadger Sett, our Badger training project. This “remote learning” automatically discovers trackers present on thousands of the most popular sites on the Web.

### What is a third party tracker?

When you visit a webpage parts of the page may come from domains and servers other than the one you asked to visit. This is an essential feature ofhypertext. On the modern Web, embedded images and code often use cookies and other methods to track your browsing habits — often to display advertisements. The domains that do this are called “third party trackers”, and you can read more about how they workhere.

### What do the red, yellow and green sliders in the Privacy Badger menu mean?

Red means that content from this third party domain has been completely disallowed.

Yellow means that the third party domain appears to be trying to track you, but it is on Privacy Badger’s cookie-blocking “yellowlist” of third party domains that, when analyzed, seemed to be necessary for Web functionality. In that case, Privacy Badger will load content from the domain but will try to screen out third party cookies and referrers from it.

Green means “no action”; Privacy Badger will leave the domain alone.

### Why does Privacy Badger block ads?

Actually, nothing in the Privacy Badger code is specifically written to block ads. Rather, it focuses on disallowing any visible or invisible “third party” scripts or images that appear to be tracking you even though you specifically denied consent by sendingDo Not TrackandGlobal Privacy Controlsignals. It just so happens that most (but not all) of these third party trackers are advertisements. When you see an ad, the ad sees you, and can track you. Privacy Badger is here to stop that.

### Why doesn't Privacy Badger block all ads?

Because Privacy Badger is primarily a privacy tool, not an ad blocker. Our aim is not to block ads, but to prevent non-consensual invasions of people’s privacy because we believe they are inherently objectionable. We also want to create incentives for advertising companies to do the right thing. Of course, if you really dislike ads, you can also install a traditional ad blocker.

### What is Global Privacy Control (GPC)?

Global Privacy Control (GPC)is a new specification that allows users to tell companies they’d like to opt out of having their data shared or sold. By default, Privacy Badger sends the GPC signal to every company you interact with alongside the Do Not Track (DNT) signal.

What’s the difference? Do Not Track is meant to tell companies that you don’t want to be tracked in any way (learn more about what we mean by “tracking”here). Privacy Badger gives third-party companies a chance to comply with DNT by adoptingour DNT policy, and blocks those that look like they’re tracking you anyway.

When DNT was developed, many websites simply ignored users’ requests not to be tracked. That’s why Privacy Badger has to act as an enforcer: trackers that don’t want to comply with your wishes get blocked. Today, users in many jurisdictions have the legal right to opt out of some kinds of tracking. That’s where GPC comes in.

GPC is meant to be a legally-binding request to all companies in places with applicable privacy laws. For example,the California Consumer Privacy Actgives California residents the right to opt out of having their data sold. By sending the GPC signal, Privacy Badger is telling companies that you would like to exercise your rights.

The CCPA and other laws arenot perfect, which is why Privacy Badger uses both approaches. It asks websites to respect your privacy, and it blocks known trackers from loading at all.

### What about tracking by the sites I actively visit, like NYTimes.com or Facebook.com?

At present, Privacy Badger primarily protects you against tracking by third party sites. As far as privacy protections for “first party” sites (sites that you visit directly), Privacy Badger removes outgoing link click tracking onFacebookandGoogle. We plan on adding more first party privacy protections in the future.

We are doing things in this order because the most scandalous, intrusive and objectionable form of online tracking is that conducted by companies you’veoften never heard ofand have no relationship with. First and foremost, Privacy Badger is there to enforce Do Not Track against these domains by providing the technical means to restrict access to their tracking scripts and images. The right policy for whether nytimes.com, facebook.com or google.com can track youwhen you visit that site– and the technical task of preventing it – is more complicated because often tracking is interwoven with the features the site offers.

### Does Privacy Badger contain a list of blocked sites?

Unlike other blocking tools, we have not made decisions about which sites to block, but rather about which behavior is objectionable. Domains will only be blocked if Privacy Badger observes the domain collecting unique identifiers after it was sent Do Not Track and Global Privacy Control signals.

Privacy Badgerdoescontain a “yellowlist” of some sites that are known to provide essential third party resources; those sites show up as yellow and have their cookies blocked rather than being blocked entirely. This is a compromise with practicality, and in the long term we hope to phase out the yellowlist as these third parties begin toexplicitly commit to respecting Do Not Track. The criteria for including a domain on the yellowlist can befound here.

### How was the cookie blocking yellowlist created?

The initial list of domains that should be cookie blocked rather than blocked entirely was derived from aresearch projecton classifying third party domains as trackers and non-trackers. We will make occasional adjustments to it as necessary. If you find domains that are under- or over-blocked, pleasefile a bugon GitHub.

### Does Privacy Badger prevent fingerprinting?

Browser fingerprinting is an extremely subtle and problematic method of tracking, which we documented with theCover Your Tracks project. Privacy Badger can detectcanvas-based fingerprinting, and will block third party domains that use it. Detection of other forms of fingerprinting and protections against first-party fingerprinting are ongoing projects. Of course, once a domain is blocked by Privacy Badger, it will no longer be able to fingerprint you.

### Does Privacy Badger consider every cookie to be a tracking cookie?

No. Privacy Badger analyzes the cookies from each site; unique cookies that contain tracking IDs are disallowed, while “low entropy” cookies that perform other functions are allowed. For instance a cookie like LANG=fr that encodes the user’s language preference, or a cookie that preserves a very small amount of information about ads the user has been shown, would be allowed provided that individual or small groups of users’ reading habits could not be collected with them.

### Will you be supporting any other browsers besides Chrome, Firefox, Edge and Opera?

We are working towardsSafari on macOSsupport.Safari on iOSseems to lack certain extension capabilities required by Privacy Badger to function properly.

Chrome on Android does not support extensions. To use Privacy Badger on Android, installFirefox for Android.

Privacy Badger does not work withMicrosoft Edge Legacy. Please switch to the newMicrosoft Edgebrowser.

### Can I download Privacy Badger directly from eff.org?

If you use Google Chrome, you have to install extensions from Chrome Web Store. To install Privacy Badger in Chrome, visitPrivacy Badger’s Chrome Web Store listingand click the “Add to Chrome” button there.

Otherwise, you can use the following links to get the latest version of Privacy Badger directly from eff.org:

* Firefox:https://www.eff.org/files/privacy-badger-latest.xpi
* Chromium:https://www.eff.org/files/privacy_badger-chrome.crx

### I run a domain that uses cookies or other tracking. How do I stop Privacy Badger from blocking me?

One way is to stop tracking users who have turned on Global Privacy Control or Do Not Track signals (i.e., stop collecting cookies, supercookies or fingerprints from them). Privacy Badger will stop learning to block that domain. The next version of Privacy Badger to ship with an updated pre-trained list will no longer include that domain in the list. Most Privacy Badger users will then update to that list.

You can also unblock yourself by promising to meaningfully respect the Do Not Track signal. To do so, post averbatimcopy ofEFF’s Do Not Track policyto the URLhttps://example.com/.well-known/dnt-policy.txt, where “example.com” is replaced by your domain. Posting EFF’s DNT policy on a domain is a promise of compliance with EFF’s DNT Policy by that domain.

If your domain is compliant with EFF’s DNT policy and declares this compliance, most Privacy Badgers will see this declaration the next time they encounter your domain. Also, the next version of Privacy Badger to ship with an updated pre-trained list will probably include your declaration of compliance in the list.

Note that the domain must support HTTPS, to protect against tampering by network attackers. The path contains “.well-known” perRFC 5785. Also note that you must post a copy of the policy at each compliant subdomain you control. For example, if you wish to declare compliance by both sub1.example.com and sub2.example.com, you must post EFF’s DNT policy on each domain.

### Where can I find general information about Privacy Badger that I can use for a piece I'm writing?

Glad you asked! Check out thisdownloadable press kitthat we’ve put together.

### As an administrator, how do I configure Privacy Badger on my managed devices?

Please see ourenterprise deployment and configurationdocument.

### What is the Privacy Badger license? Where is the Privacy Badger source code?

Privacy Badger’ssource codeis licensed underGPLv3+. This website’ssource codeis licensed underAGPLv3+.

### How can I support Privacy Badger?

Thanks for asking! Individual donations make up about half of EFF’s support, which gives us the freedom to work on user-focused projects. If you want to support the development of Privacy Badger and other projects like it, you canthrow us a few dollars here. Thank you.

If you want to help directly with the project, we appreciate that as well. Please seePrivacy Badger’s CONTRIBUTING documentfor ways to get started.

### How does Privacy Badger handle social media widgets?

Social media widgets (such as the Facebook Like button) often track your reading habits. Even if you don’t click them, the social media companies often see exactly which pages you’re seeing the widget on. When blocking social buttons and other potentially useful (video, audio, comments) widgets,Privacy Badger can replace themwith click-to-activate placeholders. You will not be tracked by these replacements unless you explicitly choose to click them.

### How do I uninstall/remove Privacy Badger?

Firefox: See theDisable or remove Add-onsMozilla help page.

Chrome: See theInstall and manage extensionsChrome Web Store help page.

Edge: See theAdd or remove browser add-ons, extensions, and toolbarsMicrosoft help page.

### Is Privacy Badger compatible with other extensions, including adblockers?

Privacy Badger should be compatible with other extensions.

While there is likely to be overlap between the various manually-edited advertising/tracker lists and Privacy Badger, unlike adblockers, Privacy Badger automatically learns to block trackers based on their behavior. This means that Privacy Badger may learn to block trackers your adblocker doesn’t know about.

### Is Privacy Badger compatible with Firefox's built-in privacy protections?

It’s fine to use Firefox’s built-in content blocking (Enhanced Tracking Protectionor ETP) and Privacy Badger together. While there is overlap between Firefox’s tracker lists and Privacy Badger, Privacy Badger automatically learns to block trackers based on their behavior. This means that Privacy Badger’s automatically-generated and regularly updated blocklist contains trackers not found in Firefox’s human-generated lists. Additionally,Firefox does not fully block “tracking content”in regular (non-“private”) windows by default.

What about Firefox’sTotal Cookie Protection(dynamic First Party Isolation or dFPI)? Total Cookie Protection works by keeping third-party cookies isolated to the site they were set on. However, if unblocked, trackers can still use techniques likefirst-party cookie syncingandbrowser fingerprinting. They can track your IP address, or they can use some combination of these techniques. Trackersharvest sensitive information, andserve as vectors for malware. Not to mention, unblocked trackers slow down websites and waste your bandwidth.

Keep in mind that Privacy Badger isnot just a tracker blocker.

### Why does my browser connect to fastly.com IP addresses on startup after installing Privacy Badger?

EFF uses Fastly to host EFF’s Web resources: Fastly is EFF’s CDN. Privacy Badger pings the CDN for the following resources to ensure that the information in them is fresh even if there hasn’t been a new Privacy Badger release in a while:

* https://www.eff.org/files/pbconfig.json

EFF does not set cookies or retain IP addresses for these queries.

### Why does Privacy Badger need access to my data for all websites?

When you install Privacy Badger, your browser warns that Privacy Badger can “access your data for all websites” (in Firefox), or “read and change all your data on the websites you visit” (in Chrome). You are right to be alarmed. You should only install extensions made by organizations you trust.

Privacy Badger requires these permissions to do its job of automatically detecting and blocking trackers on all websites you visit. We are not ironically (or unironically) spying on you. For more information, see ourPrivacy Badger extension permissions explainer.

Note that the extension permissions warnings only cover what the extension has access to, not what the extension actually does with what it has access to (such as whether the extension secretly uploads your browsing data to its servers). Privacy Badger will never share data about your browsing unless you choose to share it (by filing a broken site report). For more information, see EFF’sPrivacy Policy for Software.

### Why aren't videos loading on YouTube? Why isn't Privacy Badger blocking ads on YouTube?

Is YouTube not working? Trydisabling Privacy Badgeron YouTube. If that resolves the issue, see if re-enabling Privacy Badger breaks YouTube again. If YouTube goes back to not working, pleasetell usso we can look into what’s going on.

Are you surprised that ads aren’t being blocked on YouTube? Privacy Badger is primarily a privacy tool,not an ad blocker. When youvisit YouTube directly, Privacy Badger does not block ads on YouTube because YouTube does not use“third party” trackers. If you really dislike ads, you can also install a traditional ad blocker.

### I need help! I found a bug! What do I do now?

If a website isn’t working like it should, you can disable Privacy Badger just for that site, leaving Privacy Badger enabled and protecting you everywhere else. To do so, navigate to the site with the problem, click on Privacy Badger’s icon in your browser toolbar, and click the “Disable for this site” button in Privacy Badger’s popup. You can also let us know about broken sites using the “Report broken site” button.

To get help or to report bugs, please emailextension-devs@eff.org. If you have a GitHub account, you can use ourGitHub issue tracker.

You can also find us onMastodonandBluesky.

Back to questions ▲
