---
title: Anubis v1.20.0 is now available! | Anubis
url: https://anubis.techaro.lol/blog/release/v1.20.0/#no-js-challenge
site_name: lobsters
fetched_at: '2025-07-11T23:06:39.431364'
original_url: https://anubis.techaro.lol/blog/release/v1.20.0/#no-js-challenge
date: '2025-07-11'
published_date: '2025-06-27T00:00:00.000Z'
description: Hey all!
tags: release, web
---

Hey all!

Today we releasedAnubis v1.20.0: Thancred Waters. This adds a lot of new and exciting features to Anubis, including but not limited to theWEIGHaction, custom weight thresholds, Imprint/impressum support, and a no-JS challenge. Here's what you need to know so you can protect your websites in new and exciting ways!

## Sponsoring the product​

If you rely on Anubis to keep your website safe, please consider sponsoring the project onGitHub SponsorsorPatreon. Funding helps pay hosting bills and offset the time spent on making this project the best it can be. Every little bit helps and when enough money is raised,I can make Anubis my full-time job.

I am waiting to hear back from NLNet on if Anubis was selected for funding or not. Let's hope it is!

## Deprecation warning:DEFAULT_DIFFICULTY​

Anubis v1.20.0 is the last version to support theDEFAULT_DIFFICULTYflag in the exact way it currently does. In future versions, this will be ineffectual and you should use thecustom threshold systeminstead.

If this becomes an imposition in practice, this will be reverted.

## Chrome won't show "invalid response" after "Success!"​

There were a bunch of smaller fixes in Anubis this time around, but the biggest one was finally squashing the"invalid response" after "Success!" issuethat had been plaguing Chrome users. This was a really annoying issue to track down but it was discovered while we were working on better end-to-end / functional testing:Chrome randomizes theAccept-Languageheaderso that websites can't do fingerprinting as easily.

When Anubis issues a challenge, it grabsinformation that the browser sends to the userto create a challenge string. Anubis doesn't store these challenge strings anywhere, and when a solution is being checked it calculates the challenge string from the request. This means that they'd get a challenge on one end, compute the response for that challenge, and then the server would validate that against a different challenge. This server-side validation would fail, leading to the user seeing "invalid response" after the client reported success.

I suspect this was why Vanadium and Cromite were having sporadic issues as well.

## New Features​

The biggest feature in Anubis is the "weight" subsystem. This allows administrators to make custom rules that change the suspicion level of a request without having to take immediate action. As an example, consider the self-hostable git forgeGitea. When you load a page in Gitea, it creates a session cookie that your browser sends with every request. Weight allows you to mark a request that includes a Gitea session token aslesssuspicious:

-

name
:
 gitea
-
session
-
token

action
:
 WEIGH

expression
:

all
:

# Check if the request has a Cookie header

-

'"Cookie" in headers'

# Check if the request's Cookie header contains the Gitea session token

-
 headers
[
"Cookie"
]
.contains("i_love_gitea=")

# Remove 5 weight points

weight
:

adjust
:

-5

This is different from the past where you could only allow every request with a Gitea session token, meaning that the invention of lying would allow malicious clients to bypass protection.

Weight is added and removed whenever aWEIGHrule is encountered. When all rules are processed and the request doesn't match anyALLOW,CHALLENGE, orDENYrules, Anubis usesweight thresholdsto figure out how to handle that request. Thresholds are defined in thepolicy filealongside your bot rules:

thresholds
:

-

name
:
 minimal
-
suspicion
# This client is likely fine, its soul is lighter than a feather

expression
:
 weight <= 0
# a feather weighs zero units

action
:
 ALLOW
# Allow the traffic through

# For clients that had some weight reduced through custom rules, give them a

# lightweight challenge.

-

name
:
 mild
-
suspicion

expression
:

all
:

-
 weight
>
 0

-
 weight < 10

action
:
 CHALLENGE

challenge
:

# https://anubis.techaro.lol/docs/admin/configuration/challenges/metarefresh

algorithm
:
 metarefresh

difficulty
:

1

report_as
:

1

# For clients that are browser-like but have either gained points from custom rules or

# report as a standard browser.

-

name
:
 moderate
-
suspicion

expression
:

all
:

-
 weight
>
= 10

-
 weight < 20

action
:
 CHALLENGE

challenge
:

# https://anubis.techaro.lol/docs/admin/configuration/challenges/proof-of-work

algorithm
:
 fast

difficulty
:

2

# two leading zeros, very fast for most clients

report_as
:

2

# For clients that are browser like and have gained many points from custom rules

-

name
:
 extreme
-
suspicion

expression
:
 weight
>
= 20

action
:
 CHALLENGE

challenge
:

# https://anubis.techaro.lol/docs/admin/configuration/challenges/proof-of-work

algorithm
:
 fast

difficulty
:

4

report_as
:

4

note

If you don't have thresholds defined in your Anubis policy file, Anubis will default to the "legacy" behaviour where browser-like clients get a challenge at the default difficulty.

This lets most clients through if they pass a simpleproof of work challenge, but any clients that are less suspicious (like ones with a Gitea session token) are given the lightweightMeta Refreshchallenge instead.

Threshold expressions are likeBot rule expressions, but there's only one input: the request's weight. If no thresholds match, the request is allowed through.

### Imprint/Impressum Support​

European countries like Germanyrequire an imprint/impressumto be present in the footer of their website. This allows users to contact someone on the team behind a website in case they run into issues. This also must generally have a separate page where users can view an extended imprint with other information like a privacy policy or a copyright notice.

Anubis v1.20.0 and laterhas support for showing imprints. You can configure two kinds of imprints:

1. An imprint that is shown in the footer of every Anubis page.
2. An extended imprint / privacy policy that is shown when users click on the "Imprint" link. For example,here's the imprint for the website you're looking at right now.

Imprints are configured inthe policy file:

impressum
:

# Displayed at the bottom of every page rendered by Anubis.

footer
:

>
-
 This website is hosted by Zombocom. If you have any complaints or notes
 about the service
,
 please contact
 <a href="mailto
:
contact@zombocom.example"
>
contact@zombocom.example</a
>
 and
 we will assist you as soon as possible.

# The imprint page that will be linked to at the footer of every Anubis page.

page
:

# The HTML <title> of the page

title
:
 Imprint and Privacy Policy

# The HTML contents of the page. The exact contents of this page can

# and will vary by locale. Please consult with a lawyer if you are not

# sure what to put here.

body
:

>
-

<p>Last updated
:
 June 2025</p
>
 <h2
>
Information that is gathered from visitors</h2
>
 <p
>
In common with other websites
,
 log files are stored on the web server
 saving details such as the visitor's IP address
,
 browser type
,
 referring
 page and time of visit.</p
>
 <p
>
Cookies may be used to remember visitor preferences when interacting
 with the website.</p
>
 <p
>
Where registration is required
,
 the visitor's email and a username
 will be stored on the server.</p
>
 <
!--

...

-
-
>

If this is insufficient, pleasefile an issuewith a link to the relevant legislation for your country so that this feature can be amended and improved.

### No-JS Challenge​

One of the first issues in Anubis before it was moved to theTecharoHQ orgwas a requestto support challenging browsers without using JavaScript. This is a pretty challenging thing to do without rethinking how Anubis works from a fundamentally low level, and with v1.20.0,Anubis finally has support for running without client-side JavaScriptthanks to theMeta Refreshchallenge.

When Anubis decides it needs to send a challenge to your browser, it sends a challenge page. Historically, this challenge page isan HTML templatethat kicks off some JavaScript, reads the challenge information out of the page body, and then solves it as fast as possible in order to let users see the website they want to visit.

In v1.20.0, Anubis has a challenge registry to holddifferent client challenge implementations. This allows us to implement anything we want as long as it can render a page to show a challenge and then check if the result is correct. This is going to be used to implement a WebAssembly-based proof of work option (one that will be way more efficient than the existing browser JS version), but as a proof of concept I implemented a simple challenge usingHTML<meta refresh>.

In my testing, this has worked with every browser I have thrown it at (including CLI browsers, the browser embedded in emacs, etc.). The default configuration of Anubis does use themeta refresh challengeforclients with a very low suspicion, but by default clients will be sent aneasy proof of work challenge.

If the false positive rate of this challenge turns out to not be very high in practice, the meta refresh challenge will be enabled by default for browsers in future versions of Anubis.

### robots2policy​

Anubis was created because crawler bots don't respectrobots.txtfiles. Administrators have been working on refining and crafting theirrobots.txtfiles for years, and one common comment is that people don't know where to start crafting their own rules.

Anubis now ships with arobots2policytoolthat lets you convert yourrobots.txtfile to an Anubis policy.

robots2policy -input https://github.com/robots.txt

note

If you installed Anubis froman OS package, you may need to runanubis-robots2policyinstead ofrobots2policy.

We hope that this will help you get started with Anubis faster. We are working on a version of this that will run in the documentation via WebAssembly.

### Open Graph configuration is being moved to the policy file​

Anubis supports readingOpen Graph tagsfrom target services and returning them in challenge pages. This makes the right metadata show up when linking services protected by Anubis in chat applications or on social media.

In order to test the migration of all of the configuration to the policy file, Open Graph configuration has been moved to the policy file. For more information, please readthe Open Graph configuration options.

You can also set default Open Graph tags:

openGraph
:

enabled
:

true

ttl
:
 24h

# If set, return these opengraph values instead of looking them up with

# the target service.

#

# Correlates to properties in https://ogp.me/

override
:

# og:title is required, it is the title of the website

"og:title"
:

"Techaro Anubis"

"og:description"
:

>
-
 Anubis is a Web AI Firewall Utility that helps you fight the bots
 away so that you can maintain uptime at work
!

"description"
:

>
-
 Anubis is a Web AI Firewall Utility that helps you fight the bots
 away so that you can maintain uptime at work
!

## Improvements and optimizations​

One of the biggest improvements we've made in v1.20.0 is replacingSHA-256 with xxhash. Anubis uses hashes all over the place to help with identifying clients, matching against rules when allowing traffic through, in error messages sent to users, and more. Historically these have been done withSHA-256, however this has been having a mild performance impact in real-world use. As a result, we now usexxhashwhen possible. This makes policy matching 3x faster in some scenarios and reduces memory usage across the board.

Anubis now usesbartfor doing IP address matching when you specify addresses in aremote_addresscheck configuration or when you are matching againstadvanced checks. This uses the same kind of IP address routing configuration that your OS kernel does, making it very fast to query information about IP addresses. This makes IP address range matches anywhere from 3-14 times faster depending on the number of addresses it needs to match against. For more information and benchmarks, check out@JasonLovesDoggo's PR:perf: replace cidranger with bart for significant performance improvements #675.

## What's up next?​

v1.21.0 is already shaping up to be a massive improvement as Anubis addsinternationalizationsupport, allowing your users to see its messages in the language they're most comfortable with.

So far Anubis supports the following languages:

* English (Simplified and Traditional)
* French
* Portugese (Brazil)
* Spanish

If you want to contribute translations, pleasefile an issuewith your language of choice or submit a pull request tothelib/localization/localesfolder. We are about to introduce features to the translation stack, so you may want to hold off a hot minute, but we welcome any and all contributions to making Anubis useful to a global audience.

Other things we plan to do:

* Move configuration to the policy file
* Support reloading the policy file at runtime without having to restart Anubis
* Detecting if a client is "brand new"
* AValkey-backed store for sharing information between instances of Anubis
* Augmenting No-JS support in the paid product
* TLS fingerprinting
* Automated testing improvements in CI (FreeBSD CI support, better automated integration/functional testing, etc.)

## Conclusion​

I hope that these features let you get the same Anubis power you've come to know and love and increases the things you can do with it! I've been really excited to shipthresholdsand the cloud-based services for Anubis.

If you run into any problems, pleasefile an issue. Otherwise, have a good day and get back to making your communities great.
