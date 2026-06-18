---
title: AMD silently removes memory encryption from consumer Ryzen CPUs, leaving users unaware that they may be vulnerable — security feature vanishes after newer AGESA firmware, AMD engineers go radio silent when pressed about the change | Tom's Hardware
url: https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change
site_name: hackernews_api
content_file: hackernews_api-amd-silently-removes-memory-encryption-from-consum
fetched_at: '2026-06-19T01:17:31.972843'
original_url: https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change
author: lompad
date: '2026-06-18'
published_date: '2026-06-17T10:00:00Z'
description: AMD engineer shuts down discussions on the issue
tags:
- hackernews
- trending
---

(Image credit: AMD)

* Copy link
* Facebook
* X
* Whatsapp
* Reddit
* Pinterest
* Flipboard
* Email

Share this article

27

Join the conversation

Follow us

Add us as a preferred source on Google

Newsletter

Subscribe to our newsletter

According to a report byArs Technica, AMD has quietly stripped a criticalsecurityfeature from its lower-end CPUs, leaving unaware users potentially vulnerable to physical attacks. Following a months-long investigation tracked on GitHub, Ben Kilpatrick confirmed that the Transparent Secure Memory Encryption (TSME) feature — which protects CPUs against physical exploits thatsiphon data from connected memory chips— was suddenly no longer available on AMD CPUs outside the company's Pro lineup.

As the exhaustive inquiry, which involved conversations with AMD engineers, board vendors, and other CPU users, was coming to a head, an AMD engineer abruptly cut discussions short, stating, "My apologies, but I don't have any more information to share on this topic." As of this report, AMD has neither officially acknowledged nor explained the disappearance of the security feature.

TSME is a protection feature that encrypts the data stored in memory, making it unusable to physical attackers. AMD initially added this feature to its high-end CPUs, then later extended it to lower-end CPUs. Eventually, the feature became a given, leaving lower-end chip users assured in its availability as part of the chip package. However, without prior notice, AMD appears to have scrapped the security feature in these processors.

Latest Videos From
Watch full video here: 

According to the Ars report, the company's only official reaction to the matter — not counting the GitHub discussions — is an email response stating that TSME "is a security feature only applied to PRO CPUs as part of AMD PRO Technologies," notably the first time the company has publicly stated such a restriction, despite the feature having worked on consumer chips for years. However, it remains unclear whether the disappearance is an intentional policy decision by AMD to reserve TSME for Pro chips or an unintentional regression that was introduced inAGESA1.2.7.0, a newer firmware release.

Another concerning aspect of the removal is that the feature's disappearance is completely undetectable on Windows machines and requires significant technical work to identify on Linux. That means the security feature was removed, leaving users unaware that anything had changed.

Kilpatrick, a self-described "privacy-conscious Linux hobbyist" who first reported the change, was installing a new operating system on his machine running aRyzen 7 9700Xfrom the Zen 5 architecture. To confirm that all his security protections were enabled, he ran Host Security ID (HSI), an auditing feature that evaluates a system's firmware and hardware security configurations. To his surprise, HSI reported that TSME was no longer supported — even though he had enabled it in his BIOS settings all along. The contradiction sent him searching for answers.

His first instinct was to reach out to MSI, his motherboard’s manufacturer, but the company didn't initially provide a definitive explanation. He also filed a bug report on AMD's public engineering GitHub repository, where two AMD engineers eventually responded: Tom Lendacky, an AMD fellow software engineer, and Mario Limonciello, an AMD senior principal software engineer.

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

Interestingly, neither engineer appeared to have a clear answer for why the feature had disappeared. Their advice was basically the same: disable and re-enable the option in the BIOS, and if that didn't work, take it up with the motherboard manufacturer, making it clear that people directly at AMD were just as in the dark as the user reporting it.

It was only after this that Kilpatrick pressed MSI harder, eventually convincing its engineers to run controlled tests. They found that consumer Ryzen chips had TSME enabled under an older firmware version but showed it as "not supported" under a newer one (AGESA 1.2.7.0), while Pro versions of the CPU supported the feature regardless of the firmware or motherboard used.

This leaves the big question of whether AMD deliberately restricted TSME to its Pro chips, or whether the change was an accidental regression — a firmware bug introduced in that newer AGESA version. Either way, the silicon appears to have been capable of running the feature. The difference is whether users are looking at a bug that AMD should fix or a quiet product-segmentation decision that AMD has not properly explained.

Kilpatrick took these MSI findings back to the AMD engineers and resumed the discussion six weeks later. MSI's product marketing team, he reported, had been told directly by AMD that TSME is exclusively supported on Pro series processors. He also relayed MSI's test results: an internal AGESA flag that controls whether TSME activates during boot returned FALSE on consumer chips regardless of the BIOS setting, but TRUE on Pro processors when the feature was enabled.

Kilpatrick then brought up something especially awkward. He reminded Lendacky of a comment that the engineer had made back in 2020, confirming that a Ryzen 3700X, a consumer CPU, “should support TSME.” In a later 2025 comment in the same discussion, Lendacky again recommended using TSME, while noting that the motherboard BIOS provider had to expose the option. So there it was, AMD's own engineer, years earlier, acknowledging the feature working on exactly the kind of lower-end chip now stripped of it, proving that Ryzen support was not some fantasy users invented.

After some more back-and-forth, Kilpatrick asked bluntly whether the flag being set to FALSE on consumer chips was a silicon-level limitation or a firmware policy decision — since one is permanent and the other is potentially reversible. Limonciello’s reply effectively closed the chapter. “My apologies, but I don’t have any more information to share on this topic,” he wrote.

To be fair to AMD, there is no clear indication that the company ever publicly advertised TSME as a consumer Ryzen feature. AMD has long said that a related memory protection, Secure Memory Encryption (SME), is available only in the Pro andEPYCCPU tiers. SME is OS-managed, using a single key and allowing the OS to selectively encrypt individual memory pages. TSME, by contrast, is firmware-managed, encrypting all RAM with no OS involvement. When active, it guards against physical attacks such as cold-boot exploits,DRAMinterface snooping, and memory module removal, and it activates silently once enabled in the BIOS, making it the more practically useful of the two protections.

For now, AMD has said nothing official. It hasn't confirmed what happened, why it happened, whether anything actually changed, or what users of its consumer chips should now expect. Given the years of TSME quietly doing its job on these lower-cost processors — and the AMD engineers' supposed own past comments treating it as supported — users had every reason to regard it as part of the package.

For most consumer Ryzen users, the practical impact of the change is narrow. TSME protects against physical attacks, meaning scenarios in which someone has physical access to the machine or its memory hardware and attempts to extract secrets directly from RAM. The feature is more important for people carrying sensitive laptops, handling confidential work, relying on full-disk encryption, or operating in environments where seizure, theft, or hardware tampering is a realistic concern. Anyone who genuinely needs memory encryption on AMD hardware now appears to need a Ryzen Pro or EPYC system, unless AMD clarifies the situation or restores support.

 

FollowTom's Hardware on Google News, oradd us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

Etiido Uko
News Contributor

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.