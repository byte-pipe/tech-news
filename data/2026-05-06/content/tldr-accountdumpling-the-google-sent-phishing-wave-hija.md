---
title: '"AccountDumpling" – The Google-Sent Phishing Wave Hijacking 30k Facebook Accounts'
url: https://guard.io/labs/accountdumpling---hunting-down-the-google-sent-phishing-wave-compromising-30-000-facebook-accounts
site_name: tldr
content_file: tldr-accountdumpling-the-google-sent-phishing-wave-hija
fetched_at: '2026-05-06T12:27:31.304140'
original_url: https://guard.io/labs/accountdumpling---hunting-down-the-google-sent-phishing-wave-compromising-30-000-facebook-accounts
date: '2026-05-06'
description: Hunting Down the Google-Sent Phishing Wave Compromising 30,000+ Facebook Accounts
tags:
- tldr
---

Start for Free

Home

Labs

# "AccountDumpling"Hunting Down the Google-Sent Phishing Wave Compromising 30,000+ Facebook Accounts

Shaked Chen
April 29, 2026
•
14
min read
Table of Contents

Heading 2
TLDR

30,000 Facebook accounts have been compromised by phishing emails Google itself delivers. Authenticated, signed, and never blocked. We call this ”AccountDumpling”: a Vietnamese-linked operation that turns Google AppSheet into a phishing relay, then sells the stolen accounts back through a storefront run by the same hands.

Pulling on that thread led us through Netlify-hosted Facebook clones, Vercel-hosted reward traps, Google Drive-hosted PDFs, and recruiter-style social engineering, all riding the same Google-authenticated relay and feeding the same Telegram bot infrastructure. We mapped roughly 30,000 victims and traced the operation back to a Vietnamese name embedded in a Canva-generated PDF the attackers forgot to scrub. We also recovered enough victim data to reach out directly to many of them, telling them they had been compromised and helping them act before more damage was done.

What we found wasn't a single phishing kit. It was a living operation with real-time operator panels, advanced evasion, continuous evolution and a criminal-commercial loop that quietly feeds on the same accounts it helps steal back.

## The Email Gmail Will Never Block

In the last month, many Facebook Business account owners woke up to an email like this sent from Google:

"Your Facebook account has been flagged for a policy violation. Case ID: 6480258166. Failure to respond within 24 hours will result in permanent disablement"

Your email client shows the usual trust indicators. Nothing is flagged. SPF, DKIM, DMARC all good! This email actually came from Google! It's safe!? Well, not even close...

Email phishing used to rely on spoofing, shady SMTP infrastructure, and just enough broken authentication to slip through the cracks. This case starts from the opposite premise: the email is real, the authentication is clean, and the delivery comes through Google’s own AppSheet, the no-code app builder's notification system.

Over the past few weeks, we tracked waves of emails aimed at Facebook users, page admins, and operators, almost all wrapped in some version of a Meta-related panic. Account disabled. Copyright complaint. Page locked. Blue badge review. Executive recruitment. Different lures, different post-click paths, same destination: people controlling accounts with real financial value.

What stood out first was not just the volume, but the trust inversion. These messages were sent fromnoreply@appsheet.comand delivered throughappsheet.bounces.google.com. In practical terms, SPF, DKIM, and DMARC all aligned exactly the way defenders expect - in this case, can you imagine Google blocking an email that a Google system sent? A green result, as usual, proved only that the sending platform was legitimate, not that the message itself was.

Attackers have noticed this too. They always do.

AppSheet itself is a legitimate Google no-code platform designed to automate workflows and notifications, typically used to send app-driven alerts and internal updates. In this case, attackers abused AppSheet’s notification mechanism to deliver convincing phishing emails impersonating popular brands at scale. There was no need for spoofing, no reliance on compromised Google accounts, just a service doing exactly what it was built to do.

A fully authenticated email proves only that the platform sent it, not that the message itself is trustworthy.

What initially appeared to be a narrow phishing attempt quickly expanded into something much broader. Following this thread did not lead to a single phishing kit or an isolated actor experimenting with a no-code tool, but to a multi-actor, Vietnamese-linked Facebook account hijacking ecosystem spanning Netlify, Vercel, Google Drive, Telegram, and a set of monetization endpoints that look less like a campaign and more like a business. A grim one, but a business all the same.

## Four Lures, One Trap

Starting with an examination of the different AppSheet-originated emails by their call-to-action (CTA) targets, four distinct clusters emerged. The narratives shifted, the infrastructure varied, and the evasion techniques evolved, but the target remained consistent: Facebook accounts with real-world value. Are those different attackers with the same tricks? Or just a single attacker doing some dark side of risk management?

### Cluster A: Netlify-hosted Facebook Help Center

Cluster A was the blunt instrument of the operation: fake Facebook Help Center and account-disablement notices hosted on Netlify. Victims received alarming AppSheet emails about DMCA violations, trademark issues, or permanent disablement, then landed on Facebook-themed appeal pages designed to collect everything needed for account takeover.

These pages did not stop at usernames and passwords. They requested date of birth, phone number, and government-issued ID photos — effectively collecting the full recovery package needed to bypass platform safeguards. This wasn’t just credential theft. It was identity capture.

What made Cluster A especially effective was not just the page design, but the way it was deployed. In many waves, each victim was sent to a unique Netlify subdomain, neatly sidestepping URL blocklists by ensuring there was rarely a shared link worth blocking for long. By the time a URL could be reported or flagged, its job was already done.

In later waves, traces of the build process remained. HTTrack, an open-source website cloning tool, appeared directly in the page source, exposing part of the pipeline. Some pages were cloned from Vercel-hosted templates and redeployed to Netlify as static copies, in one case using a stolen template branded as “Northstar Cloud,” while others mirrored Meta pages directly. Industrialized phishing tends to leave assembly marks. In this case, the attackers didn’t bother to hide them.

Cluster A also evolved. In a more advanced variant observed in early April ‘26, the lure shifted from generic policy violations to a fake Facebook login alert like “Did you just log in near Guilin on a new device?” and routed victims through a two-hopshorten.tvchain before loading the Netlify phishing page inside a full-screen iframe. The browser address bar never revealed the real destination. The victim saw a shortened URL and a familiar Facebook-themed interface.

It’s a simple trick, but it works.

Technically, this variant also improved its exfiltration model. Earlier kits exposed Telegram bot tokens directly in client-side JavaScript. The newer Netlify version moved that logic server-side, posting victim data to /.netlify/functions/send, where a serverless function forwarded it to Telegram using environment variables.

For defenders, that shift matters. The signals don’t disappear, but they become harder to observe, and reverse engineering becomes less straightforward. The data is still flowing to the same place, just with fewer visible traces along the way.

### Cluster B: The Blue Badge You’ll Never Get

Cluster B applied a different social engineering tactic. It replaced fear with the promise of reward.

Instead of threatening account loss, these lures offered something desirable: Blue Badge evaluation, advertiser rewards, or opportunities for account verification. The emails read less like warnings and more like invitations, guiding victims toward Vercel-hosted “Security Check” or “Meta | Privacy Center” pages.

The pages looked polished. Familiar. Convincing enough to keep the flow moving. Many opened with a fake reCAPTCHA or a countdown timer, just enough friction to feel legitimate before transitioning into a staged collection flow: contact details, business information, an initial password entry, a forced retry, and up to three rounds of 2FA codes.

The evasion stack in Cluster B was the most layered we saw at the email stage. Sender display names were padded with invisible hair spaces (unicode invisible character). Body text broke words mid-word to interfere with NLP-based detection. Footer branding used Cyrillic homoglyphs that looked identical to Latin characters.

In one sample, the preheader used Unicode mathematical Fraktur characters - the same character block we later saw in the naming of one of the Telegram bots (𝓢𝓒𝓐𝓝_𝓥𝓘𝓟𝓟𝓡𝓞). Small detail, but not a coincidence. The same hand showed up in both places and later leading us to even more attribution directions.

The landing pages themselves were not static forms. The newer Vercel kit introduced random per-victim URLs, language localization across 30+ languages, anti-debugging scripts, and encrypted local storage. More importantly, the flow was designed not just to collect credentials, but to confirm them while the victim was still interacting with the page.

Before credentials were even requested, the kit collected a full victim profile: personal details, business information, and contact data. That information serves two purposes. It supports immediate account takeover, and it makes recovery significantly harder if the victim tries to regain access.

### Cluster C: A PDF for Human Operator Live Control

Cluster C was by far the most advanced. At first glance, the email looked familiar. Another business-page warning. Another urgent Meta notice. But the click path didn’t go straight to a phishing page. It went somewhere safer. Or at least, something that looked safer - A Google Drive link.

The victim opened a PDF hosted on Google Drive. Inside, a single Canva-designed image posed as a Meta notification, clean and minimal, convincing enough to pass a quick glance. The real payload sat behind it: an embedded link annotation that redirected to a Socket IO-based phishing panel.

That panel gave the operator something the other clusters didn’t: control. We captured live WebSocket traffic showing session identifiers, screen-switch commands, incorrect-password responses, and state changes moving back and forth between the operator and the victim in real time.

The kit could collect passwords, 2FA codes, government ID photos, and even browser screenshots through html2canvas. But more importantly, it could react. The operator could decide what the victim saw next while the victim was still interacting with the page.

Behind the scenes, the attacker has a live window to test all the victim's inputs against a real Facebook login, request additional steps, or push the victim further through the flow. A human in the loop.

### Cluster D: The Fake Job Offer

Cluster D appeared simpler, but the underlying play was just as effective. These emails impersonated recruiters from WhatsApp, Meta, Adobe, Pinterest, Apple, Coca-Cola, Threads, and Ray-Ban Meta. The pitch followed a familiar pattern: a personalized outreach, a senior role, and a vague but enticing opportunity. Instead of directing victims to a phishing page, they pushed for a rapid shift into a live interaction, typically asking them to join a call or continue the process off-platform, sometimes through attacker-controlled sites.

The only consistent technical signal sat in the sender display name. Cyrillic homoglyphs replaced Latin characters in brand names, making them visually identical to a human reader while evading simple string-based detection.

It’s a small trick. But it doesn’t need to be complex to work. Cluster D relies on something older and harder to detect: conversation. Once the victim replies, the attack leaves the inbox and moves to a controlled channel. Trust is built gradually, not extracted in a single click. It feels almost low-tech compared to the other clusters, until you remember how often it still works.

### Many Clusters, Shared Intent, Single Actor?

The broader point matters, as AppSheet wasn’t abused for a single phishing kit. It became a shared entry point for a much bigger operation. And across Clusters A and B, one pattern kept resurfacing:Telegram bots.

Victim data pushed into private channels in real time, where operators could watch it arrive and act on it immediately. That was one of the clearest signs that these weren’t just isolated phishing pages. Once we traced that layer, the noise collapsed into a well-orchestrated structure.

## Inside the operation’s Telegram C2

Once Telegram started appearing in the kits, the investigation accelerated. In Cluster B, the Vercel pages loaded obfuscated JavaScript configuration files that hid bot tokens, chat IDs, and secret keys behind hex-escaped constants and custom encoding.

const
 CONFIG = {

 
'\x54\x45\x4c\x45\x47\x52\x41\x4d\x5f\x42\x4f\x54\x5f\x54\x4f\x4b\x45\x4e'
: a0_0x33cef0(
0x13d
),

 
// "TELEGRAM_BOT_TOKEN" (hex decoded)

 
'\x54\x45\x4c\x45\x47\x52\x41\x4d\x5f\x43\x48\x41\x54\x5f\x49\x44'
: 
'-100368*******'
,

 
'\x53\x45\x43\x52\x45\x54\x5f\x4b\x45\x59'
: 
'QJXP************'
,

};

We deobfuscated the code and recovered the raw configuration, reminding us that a phishing page is just the front end. The data itself moves elsewhere, flowing through Telegram bots and, in some cases, real-time channels like WebSockets.

We identified four bots tied to the credential exfiltration pipeline across Clusters A and B, with one already rotated out by the time we reached it. Two of them immediately stood out.

The first was@haixuancau_bot, displayed asVT張太海宣VT- a name blending Vietnamese initials with Chinese characters used phonetically. It did not read like a disposable alias. It read like a personal handle.

The second was@globalglobalglobalbot_bot, displayed as𝓢𝓒𝓐𝓝_𝓥𝓘𝓟𝓟𝓡𝓞. The styling mattered. The same Unicode Fraktur character set appeared in one of the phishing emails, linking the lure design to the exfiltration layer behind it. That kind of overlap is rarely accidental. It usually reflects operator habits.

When Bot-2 was revoked, it was replaced by@globalglobalglobalbot, which carried the same naming pattern but pointed to a new exfiltration channel. A fourth bot,@tichxanhglobal_bot, appears to have supported the Blue Badge flow directly.Tích Xanhtranslates to “blue checkmark” in Vietnamese, which fits the lure it was servicing.

Following the bots into their channels and pulling administration data revealed two recurring identities:Big Bosssand@mansinblack. Both had administrative access to the channels receiving stolen data, which makes a difference. It draws a direct line between the phishing kits and the people actively monitoring the results.

The data flowing into those channels was extensive. Intercepting the exfiltration request shows exactly how each victim is packaged and delivered to the operator in real time:

The use of Telegram bots for exfiltration gave us an opportunity to learn even more about what exactly happened by pulling some advanced OSINT techniques. We estimated roughly 30,000 victim records: about 2,900 from Bot-1, about 11,000 from Bot-3, about 4,000 from Bot-4, and about 12,000 from the revoked Bot-2 channel. Note that new records were still arriving during the investigation, making it clear this was not historical data but an active operation, so numbers are much higher than the 30k we found on current active infrastructure.

Interestingly, in this case, we were even able to recover more metadata of the hijacked accounts using some advanced tricks. This allowed us to learn more about the geographic distribution of this attack. In the Bot-1 dataset alone, 1,988 of 2,898 victims, or 68.6%, were located in the United States, followed by Italy, Canada, the Philippines, India, Spain, Australia, the UK, Brazil, and Mexico, with more than 50 countries represented overall. The targeting was global, but the primary market was clear.

We took this very seriously and decided to initiateoutreach to some of the affected organizations or individualswe could identify, letting them know they had fallen victim to this operation and urging them to take immediate action, if it is not too late.

Follow-ups helped us validate the impact beyond telemetry. Some victims experienced account lockouts, while others reported suspicious activity and business disruptions. Many suffered from more side effects, including credit card abuse and serious financial loss, proving that those attackers are not only targeting Facebook pages and accounts, but probably continue to circulate stolen PII to more dark markets, monetizing even more on their victims.

By this point, the shape of the operation was difficult to ignore. Which leaves one question: Who built this system, and did they leave behind enough to connect the dots? And how do we stop them?

‍

## The Threat Actor's Calling Card

Attribution in phishing investigations is usually a game of narrowing possibilities and looking for human errors, not collecting confessions. In our case, the first real break came from an unlikely place: a Google Drive PDF.

Cluster C’s email links to this PDF on Drive, which looks like just another fake Meta notice until we pulled its metadata. Looks like this is a Canva generated file, which automatically embeds the user account as well as name and attribution to the file! And indeed, the/Authorfield contained a real Vietnamese name:PHẠM TÀI TÂN

From there we quickly found a Facebook profile at facebook.com/phamtaitan.vn, a public-facing website atphamtaitan.vn, and a business persona openly advertising Facebook-related services, including account "unlocking" and “security” help. Circumstantial? Combined with the phishing infrastructure, it became much harder to dismiss.

The PDF metadata lists Phạm Tài Tân directly, while the campaign timing aligns with Vietnam Standard Time working hours. Vietnamese-language developer comments appear across Cluster A HTML and Cluster B JavaScript, and the same reCAPTCHA gating pattern shows up in both the phishing kits and the storefront. The public persona advertises services that align with the monetization layer, and even the bot's naming carries Vietnamese phonetic traces.

The phishing kits collect credentials and recovery data -> Accounts are taken over -> A public-facing service offers to “recover” access. Taken together, they form a consistent picture of a large, Vietnamese-based, mega operation. Even data recovered from those Telegram Bots across campaign clusters provided clear evidence when initial messages sent with test data (by the Bot creators) provided proof of their origin:

The attribution boundary matters, and we are keeping it explicit. Clusters A, B, and C show strong to direct linkage through shared Vietnamese-language code artifacts, overlapping infrastructure, and the PDF author trail, with Cluster C directly attributed by name through document metadata.

Cluster D is a bit different. It shares the same AppSheet delivery mechanism and timing, but lacks the same code-level fingerprints. It may be part of the same operation, an affiliate, or a separate actor using the same technique. At this stage, the evidence is insufficient to support a direct attribution.

Oh, and there was also another name in the margins:Gatto Sazio.One of the newer Netlify serverless variants carried this signature in its HTML source. This likely points to a separate kit developer, suggesting the tooling may be reused or distributed across operators.

All this fits the broader pattern, as this ecosystem is quite modular:

* One actor builds the kit.
* Another runs the campaign.
* A third monetizes the outcome.

And it's not static as well. It adapts all the time. During the same investigation window, we observed adjacent activity from Vietnamese-linked actors targeting business users through different channels. Not only AppSheet-driven. The techniques varied, but the objective remained the same: gain access, retain control, and extract value.

Here at Guardio Labs, we keep track of those operations, investigating leads and mapping more and more techniques used by those threat actors and similar ones. While writing these words, we have already identified additional interesting techniques and attack vectors used by those and similar groups, and will update as soon as possible.

## From Phishing Campaign to Access Economy

This investigation started with a single email. It expanded into something much larger: a system that harvests access and feeds it into a market where compromised accounts are reused and resold at scale.

This campaign is bigger than a single AppSheet abuse. It's a window into the dark market around stolen Facebook assets, where access, business identity, ad reputation, and even account recovery have all become tradable commodities. Another entry in the pattern we keep surfacing: trusted platforms repurposed as delivery, hosting, and monetization layers.

What we mapped looks less like a campaign and more like a supply chain. Access is harvested, accounts are taken over, and recovery itself gets sold back. Each stage feeds the next. Hijacked trust becomes the product.

And that's the real problem. Social platforms were built on the assumption that accounts represent real people, real businesses, real brands. That assumption no longer holds. Stolen pages don't just enable account takeover, they power disinformation, fake endorsements, fraudulent storefronts, and identity laundering at scale. Once an account is compromised and resold, it becomes infrastructure for the next layer of abuse. Trust stopped being a signal. It's inventory now.

And a final note: We focused here on four attack clusters, but they are only part of the bigger picture. Additional operations are already tied to the same infrastructure with similar or identical attribution and will be covered in upcoming publications, so stay tuned!

‍

‍

## IOCs

** Netlify

* https://nammoi2bnewyer.netlify.app

* https://incomparable-otter-61efbb.netlify.app

* https://magical-malabi-ec587a.netlify.app

* https://kaleidoscopic-youtiao-5e7b9e.netlify.app

* https://neon-zabaione-4c8494.netlify.app

* https://melodic-lebkuchen-9daf83.netlify.app

* https://magenta-granita-bdfa90.netlify.app

* https://tranquil-basbousa-0d24ed.netlify.app

* https://loquacious-starburst-d9a91e.netlify.app

* https://adorable-kheer-028a6f.netlify.app

* https://melodic-smakager-a2ef78.netlify.app

* https://tiny-kelpie-b9e835.netlify.app

* https://classy-treacle-731cfd.netlify.app

* https://courageous-seahorse-e3da15.netlify.app

* https://heroic-tarsier-be3643.netlify.app

* https://gregarious-flan-5135c9.netlify.app

* https://quiet-liger-f19f43.netlify.app

* https://jazzy-pixie-6e536e.netlify.app

* https://soft-crumble-b64e31.netlify.app

* https://roaring-crepe-63dc91.netlify.app

* https://gorgeous-dodol-df7959.netlify.app

* https://effervescent-horse-9f123e.netlify.app

* https://glistening-bublanina-62beaa.netlify.app

* https://delicate-sunshine-eb1f86.netlify.app

* https://starlit-bienenstitch-3bb17d.netlify.app

⸻

** Vercel

* https://h22a6ev34i-064ddfc747.vercel.app

* https://3jgq759wnd-bc592a5ce4.vercel.app

* https://4wxaghebok-10b01c9f86.vercel.app

* https://dhx33sb5so-564d88b6cd.vercel.app

* https://id09ewyodo-b4f17d4da8.vercel.app

* https://vxfg8h5f41-ffa279e45a.vercel.app

* https://9v21kpz0u8-959533e567.vercel.app

* https://1vw2ixjrti-3e9b5281ce.vercel.app

* https://jd8rxwmgwh-0735eebe2f.vercel.app

* https://vy6w6itqm8-2996498a9e.vercel.app

* https://msjprqs3jx-2c59da0405.vercel.app

* https://0kqj4h2pgv-adcf79cfa0.vercel.app

* https://exo5fnd4ho-56848d8c13.vercel.app

* https://e41pul71wi-0880265f81.vercel.app

* https://wnyqc5k66u-21f44bc213.vercel.app

* https://v0-northstar-cloud-landing-page.vercel.app

⸻

** Google Drive

* https://drive.google.com/file/d/18xr8p05iNDQuDfDxHchHx24p2854H2eo

* https://drive.google.com/file/d/1R1XIwXGtZ4GrC2m0SP79mguS5NxZjl_R

⸻

** Shorten.tv

* https://shorten.tv/NvII9

* https://shorten.tv/facebook-meta-password_and_security_change-pass

⸻

** Threat Actor Attributed

* https://phamtaitan.vn/

* https://dichvufbgiare.com/

⸻

** Reply-To / Scam Domains

* wajobfocus.com

* ExecutiveTeamtalent.com

* meetpinterestrecruiters.com

* mtarecruitglobal.com

* adobejobexplorer.com

* futureadobeworks.com

* adobecareerstrategy.com

* talentresourceadobe.com

* mtaworkmatch.com

* mtaworkfuture.com

* mtacareercommunity.com

* applejobcareer.com

* careercommunitycola.com

* hiringcontactpinterest.com

* jobseekermatchingmt.com

* wajobspot.com

* jobchannelpinteres.com

* page-deleted.metaverifiedprofilepage.com

* metaverifiedprofilepage.com

* deleted.protechpagemeta.com

⸻

** Emails

* noreply@appsheet.com

* phamtaitanads@gmail.com

‍

{{component-quote-box}}

{{component-tips}}

{{component-block-quote}}
{{component-sidenote}}

This is some sitenote text
Header 1
Header 2
Header 3
Phishing and social engineering
Attackers manipulate individuals into divulging sensitive information or granting access to systems through deceptive emails, messages, or calls.
Endpoints, user accounts, email systems
Malware and ransomware
Malicious software is deployed to compromise systems, encrypt files, or exfiltrate data, often demanding ransom payments.
Cloud workloads, databases, storage systems
Credential theft and brute force attacks
Attackers steal or guess login credentials through phishing, keylogging, or automated brute-force attempts.
User accounts, IAM systems, cloud management consoles
Article sources

FAQs
No items found.
About the Author
Shaked Chen
Cyber Security Researcher
Shaked Chen is a security researcher at Guardio focused on investigating web threats and emerging attacker techniques.

Jan 15
13
min read

### “MyFlaw” — Cross Platform 0-Day RCE Vulnerability Discovered in Opera’s Browser

Learn More
-->
Oct 23
10
min read

### “Dormant Colors”: Live Campaign With Over 1M Data Stealing Extensions Installed

Learn More
-->
Dec 16
17
min read

### “DeceptionAds” — Fake Captcha Driving Infostealer Infections and a Glimpse to the Dark Side of Internet Advertising

Learn More
-->
It couldn't be easier to protect yourself online

"It blocked every single verified phishing fraud, for a perfect 100% score."
PC MAG
Start for Free
Start for Free