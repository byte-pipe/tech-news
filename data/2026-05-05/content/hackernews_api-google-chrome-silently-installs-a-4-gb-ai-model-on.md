---
title: Google Chrome silently installs a 4 GB AI model on your device without consent. At a billion-device scale the climate costs are insane. — That Privacy Guy!
url: https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/
site_name: hackernews_api
content_file: hackernews_api-google-chrome-silently-installs-a-4-gb-ai-model-on
fetched_at: '2026-05-05T11:59:34.781989'
original_url: https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/
author: john-doe
date: '2026-05-05'
published_date: '2026-05-04T00:00:00.000Z'
description: Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.
tags:
- hackernews
- trending
---

### Image generation details

Model
Flux.1 Dev (q8p)

Architecture
Flux DiT (Diffusion Transformer) + T5-XXL + CLIP-L text encoders · 12B (DiT) + 4.7B (T5-XXL) + 0.4B (CLIP-L)

Text encoders
T5-XXL + OpenAI CLIP ViT-L/14

VAE
Flux VAE (f16)

Sampler
EulerA · 20 steps · guidance 4

Resolution
1344×768

Seed
37565907

Clip skip
1

Generator
DrawThings (Flux.1 Dev q8p) via TPG Blog Pipeline

Hardware
Apple M1 Ultra · 20 cores (16 performance + 4 efficiency) · 48 cores GPU · 128 GB unified

OS
macOS 26.3 (build 25D125)

Author
Alexander Hanff

#### Prompt

A vast scorched cracked desert landscape, deep dry fissures splitting the orange-brown earth across the foreground, glowing embers visible deep in the cracks, hazy dark red sky thick with smoke and ash, blackened skeletal dead trees scattered on the horizon, broken silicon circuit boards motherboards and torn server racks half-buried in the cracked ground, low afternoon sun, photorealistic, shallow depth of field.

(c) Hanff & Co. AB - CC BY-NC-SA 4.0
 ·https://www.thatprivacyguy.com/

This could be you

Reach privacy, DP, security and AI leaders

~100k monthly readers — CPOs, DPOs, general counsel, CISOs, compliance teams. No tracking, no ad tech, no auction. Direct deal only.

Get in touch

# Google Chrome silently installs a 4 GB AI model on your device

Two weeks ago I wrote about Anthropic silently registering a Native Messaging bridge in seven Chromium-based browsers on every machine where Claude Desktop was installed [1]. The pattern was: install on user launch of product A, write configuration into the user's installs of products B, C, D, E, F, G, H without asking. Reach across vendor trust boundaries. No consent dialog. No opt-out UI. Re-installs itself if the user removes it manually, every time Claude Desktop is launched.

This week I discovered the same pattern, executed by Google. Google Chrome is reaching into users' machines and writing a 4 GB on-device AI model file to disk without asking. The file is namedweights.bin. It lives inOptGuideOnDeviceModel. It is the weights for Gemini Nano, Google's on-device LLM. Chrome did not ask. Chrome does not surface it. If the user deletes it, Chrome re-downloads it.

The legal analysis is the same one I gave for the Anthropic case. The environmental analysis is new. At Chrome's scale, the climate bill for one model push, paid in atmospheric CO2 by the entire planet, is between six thousand and sixty thousand tonnes of CO2-equivalent emissions, depending on how many devices receive the push. That is the environmental cost of one company unilaterally deciding that two billion peoples' default browser will mass-distribute a 4 GB binary they did not request.

This is, in my professional opinion, a direct breach of Article 5(3) of Directive 2002/58/EC (the ePrivacy Directive) [2], a breach of the Article 5(1) GDPR principles of lawfulness, fairness, and transparency [3], a breach of Article 25 GDPR's data-protection-by-design obligation [3], and an environmental harm of a magnitude that would be a notifiable event under the Corporate Sustainability Reporting Directive (CSRD) for any in-scope undertaking [4].

## What is on the disk and how it got there

On any machine that has Chrome installed, in the user profile, sits a directory whose name isOptGuideOnDeviceModel. Inside it is a file calledweights.bin. The file is approximately 4 GB. It is the weights file for Gemini Nano. Chrome uses it to power features Google has marketed under names like "Help me write", on-device scam detection, and other AI-assisted browser functions.

The file appeared with no consent prompt. There is no checkbox in Chrome Settings labelled "download a 4 GB AI model". The download triggers when Chrome's AI features are active, and those features are active by default in recent Chrome versions. On any machine that meets the hardware requirements, Chrome treats the user's hardware as a delivery target and writes the model.

The cycle of deletion and re-download has been documented across multiple independent reports on Windows installations [5][6][7][8] - the user deletes, Chrome re-downloads, the user deletes again, Chrome re-downloads again. The only ways to make the deletion stick are to disable Chrome's AI features throughchrome://flagsor enterprise policy tooling that home users do not generally have, or to uninstall Chrome entirely [5]. On macOS the file lands as mode 600 owned by the user (so it is deletable in principle) but Chrome holds the install state inLocal Stateafter the bytes are written, and as soon as the variations server next tells Chrome the profile is eligible, the download fires again - the architecture is the same, only the file permissions differ.

## How I verified this on a freshly created Apple Silicon profile

Most of the existing reporting on this behaviour is from Windows users who noticed their disk filling up - useful, but Google could (and probably will) try to characterise those reports as anecdotes from non-representative configurations. So I went looking for a clean witness on a different platform.

The witness I found is macOS itself. The kernel keeps a filesystem event log called.fseventsd- it records every file create, modify and delete at the OS level, independent of any application logging. Chrome cannot edit it, Google cannot remotely reach it, and the page files that record the events survive the deletion of the files they reference.

I created a Chrome user-data directory on 23 April 2026 to run an automated audit (one of the WebSentinel 100-site privacy sweeps). The audit driver is fully Chrome DevTools Protocol - it loads a page, dwells for five minutes with no input, captures events, closes Chrome between sites - and the profile had received zero keyboard or mouse input from a human at any point in its existence. Every "AI mode" surface in Chrome was untouched - in fact every UI surface in Chrome was untouched, the audit driver only interacts with the document via CDP and the omnibox is never reached. By 29 April the profile contained 4 GB ofOptGuideOnDeviceModelweights - and I knew it because a routinedu -shof the audit-profile directory caught it during a cleanup pass.

I went back to.fseventsdto ask exactly when those 4 GB landed. macOS gave me the answer, byte-precise, in three sequential page files:

* 24 April 2026, 16:38:54 CEST (14:38:54 UTC)- Chrome creates theOptGuideOnDeviceModeldirectory in the audit profile (page file0000000003f7f339).
* 24 April 2026, 16:47:22 CEST (14:47:22 UTC)- three concurrent unpacker subprocesses spawn temporary directories in/private/var/folders/.../com.google.Chrome.chrome_chrome_Unpacker_BeginUnzipping.*/. One of them (5xzqPo) writesweights.bin,manifest.json,_metadata/verified_contents.jsonandon_device_model_execution_config.pb. The second writes a Certificate Revocation List update. The third writes a browser preload-data update. Chrome batched a security update, a preload refresh and a 4 GB AI model into the same idle window, as if they were equivalent (page file00000000040c8855).
* 24 April 2026, 16:53:22 CEST (14:53:22 UTC)- the unpackedweights.binis moved to its final location atOptGuideOnDeviceModel/2025.8.8.1141/weights.binalong withadapter_cache.bin,encoder_cache.bin,_metadata/verified_contents.jsonand the execution config. Concurrently four additional model targets (numbered 40, 49, 51 and 59 in Chrome's optimization-guide enum) register fresh entries inoptimization_guide_model_store- these are the smaller text-safety and prompt-routing models that pair with the LLM. None of these targets existed in the profile before this moment (page file00000000040d0f9c).

Total install time, from directory creation to final move:14 minutes and 28 seconds. Total human action against the profile during that window:none. The audit driver was either dwelling on a third-party home page or transitioning between sites - the unpacker fired in the background while a tab waited for a five-minute timer to expire.

The naming inside that fseventsd record is, if anything, the most damning detail. The temp directory iscom.google.Chrome.chrome_chrome_Unpacker_BeginUnzipping.5xzqPo- that prefixcom.google.Chrome.chrome_chrome_*is the bundle ID and subprocess naming convention Google Chrome itself uses. It is notcom.google.GoogleUpdater.*and it is notcom.google.GoogleSoftwareUpdate.*. The writer is Chrome - the browser process the user has installed and trusts to load web pages - reaching into the user's filesystem on its own initiative and laying down a 4 GB ML binary while the foreground tab does something completely unrelated.

Three further pieces of corroborating evidence sit elsewhere on the same machine:

1. Chrome's own Local State JSONfor the audit profile contains anoptimization_guide.on_deviceblock withmodel_validation_result: { attempt_count: 1, result: 2, component_version: "2025.8.8.1141" }. Chrome ran the model. Thecomponent_versionmatches the version string the fseventsd events recorded as the path component. Two independent witnesses, same artefact. The same block reportsperformance_class: 6, vram_mb: "36864"- Chrome characterised my hardware (read the GPU, read the unified memory total) to decide whether I was eligible for the model push, before any user-facing AI feature surfaced.
2. Chrome'sChromeFeatureStatefor the audit profile listsOnDeviceModelBackgroundDownload<OnDeviceModelBackgroundDownloadandShowOnDeviceAiSettings<OnDeviceModelBackgroundDownloadin theenable-featuresblock. The first flag is what triggers the silent download. The second flag is what reveals the on-device AI section inchrome://settings. Both are gated by the same rollout flag - which means that by Chrome's own architecture, the install beginsbeforethe user has any settings UI in which to refuse it. The settings page that would let you discover the feature exists is enabled in lockstep with the install - it is design, not oversight.
3. The GoogleUpdater logsrecord the on-device-model control component (appid{44fc7fe2-65ce-487c-93f4-edee46eeaaab}) being downloaded fromhttp://edgedl.me.gvt1.com/edgedl/diffgen-puffin/%7B44fc7fe2-65ce-487c-93f4-edee46eeaaab%7D/...- a 7 MB compressed control file that arrived on 20 April 2026, three daysbeforethe audit profile in question was created. That is the upstream control plane: it is profile-independent, it is launched automatically by a LaunchAgent that fires every hour, and the URL is plain HTTP (the integrity is verified by the CRX-3 signature inside the package, not by transport security). The control component gives Chrome the manifest pointing at the actual weights, and Chrome's in-processOnDeviceModelComponentInstaller- a separate code path from GoogleUpdater - then fetches the multi-GB weights direct from Google's CDN.

So we now have a four-way evidence chain - macOS kernel filesystem events, Chrome's own per-profile state, Chrome's runtime feature flags, and Google's component-updater logs - all four agreeing on the same conduct, and the conduct is: a 4 GB AI model arrived on this user's disk without consent, without notice, on a profile that received zero human input, in a window of 14 minutes and 28 seconds, on a Tuesday afternoon.

Reports of theOptGuideOnDeviceModeldirectory and theweights.binfile have been circulating in community forums for over a year - what is new in 2026 is the scale and the verifiability. Chrome's market share has held above 64% globally [9][10], Chrome's user base is between 3.45 billion and 3.83 billion individuals worldwide depending on which 2026 estimate you trust [9][11], and Google has been rolling Gemini features into Chrome with increasing aggression. The behaviour is no longer affecting a minority of power users on a minority of platforms - it is affecting hundreds of millions of devices, on every desktop OS Chrome ships against.

## The Anthropic comparison, point for point

The same dark-pattern playbook. I am repeating my categorisation from the Claude Desktop article [1] because the patterns are identical and that is the point.

1. Forced bundling across trust boundaries.Anthropic installed Claude Desktop, then wrote into Brave, Edge, Arc, Vivaldi, Opera, and Chromium. Google installs Chrome, then writes a 4 GB AI model under the user's profile directory without authorisation. The binary is not Chrome. It is a separately-trained machine-learning model, with a separate purpose, a separate data-protection profile, and a separate consent footprint.

2. Invisible default, no opt-in.No dialogue at first launch. No checkbox in Settings. The model is downloaded; the user finds out about it months later when their disk fills up [5][6][7].

3. More difficult to remove than install.Adding the file took zero clicks. Removing it requires (a) discovering the file exists, (b) understanding what it is, (c) navigating into a hidden user profile path, (d) deleting it (and on Windows, also clearing the read-only attribute first), and (e) accepting that Chrome will silently re-download it on next eligible window unless the user also navigateschrome://flags, enterprise policy, or platform-specific configuration tooling to disable the underlying Chrome AI feature [5]. None of those steps is documented in the place a normal user looks - none of them is even hinted at in default Chrome.

4. Pre-staging of capability the user has not requested.The Nano model exists on the user's disk so that Chrome features that use it can run instantly when the user invokes them. The user has not invoked any of those features. The model still sits there, taking 4 GB.

5. Scope inflation through generic naming.OptGuideOnDeviceModelis internal Chrome jargon for "OptimizationGuide on-device model storage". A user looking at their disk usage, even one who knows roughly what they are looking at, would not matchOptGuideOnDeviceModel/weights.binto "Gemini Nano LLM weights". Accurate naming would beGeminiNanoLLM/weights.bin. Google chose to obfuscate the name.

6. Registration into resources the user has not configured.A user who has not opened Chrome's AI features still gets the model. A user who has opened them once and decided they were not interested still gets the model. The file's presence is decoupled from the user's actual use of any feature it powers.

7. Documentation gap.Google's user-facing documentation about Chrome's AI features does not, with the prominence proportionate to a 4 GB silent download, tell the user that the cost of the feature being available is a 4 GB file appearing on their device. The behaviour is documented in places a curious admin will find. It is not documented in the place a regular user looks before installing Chrome or before Chrome decides to begin pushing the model.

8. Automatic re-install on every run.Same as Claude Desktop. Delete the file, Chrome re-creates it. The user's deletion is treated as a transient state to be corrected, not as a directive to be respected.

9. Retroactive survival of any future user consent.If Google in future starts asking users "would you like Chrome to download a 4 GB AI model", that prompt does not retro-actively legitimise the silent installs that have already happened on hundreds of millions of devices. The damage to the trust relationship is done. The bytes have moved. The atmosphere has been written to.

10. Code-signed, shipped through the normal release channel.This is not test build behaviour. It is Chrome stable.

## The "AI Mode" pill is the cherry on top

Here is the part that should make every privacy lawyer in the audience put their coffee down. When Chrome 147 launches against an eligible profile, the omnibox - the address bar at the top of the window, the most visible piece of real estate in the entire browser - renders an "AI Mode" pill to the right of the URL field. A reasonable user, seeing "AI Mode" sitting in their browser's most prominent UI element in 2026, with the well-publicised existence of on-device LLMs in Chrome and a 4 GB Gemini Nano binary already silently installed on their disk, is going to draw what feels like an obvious inference - that the visible AI Mode is using the on-device model, that their queries stay on the device, that the local model is what powers the local-looking surface.

Every part of that inference is wrong. The AI Mode pill in the Chrome 147 omnibox is a cloud-backed Search Generative Experience surface - every query the user types into it is sent over the network to Google's servers for processing by Google's hosted models. The on-device Nano model is not invoked by the AI Mode UI flow at all. They are entirely separate code paths - the most visible AI affordance in the browser does not use the local model the user has been silently given, and the features thatdouse the local model (Help-Me-Write in<textarea>, tab-group AI suggestions, smart paste, page summary) are buried in textarea-context menus and tab-group right-click menus that the average user will discover, on average, never.

Think about what that arrangement actually is. The user pays the storage cost of the silent install (4 GB on disk, plus the bandwidth of the silent download). The user's most visible AI experience - the pill they actually see and click - delivers no on-device benefit at all because it routes to Google's servers regardless. The on-device model is therefore a sunk cost imposed on the user, with no offsetting transparency benefit at the surface where transparency would matter most. To put it another way - if the on-device install had given the user a clear "your AI Mode queries stay on your device" property, the install would have a defensible privacy framing (worse storage, better data flow). It does not - the install gives Google a future-options resource (the model can be invoked by other Chrome subsystems without further server round-trips) at the user's disk-and-bandwidth expense, while the headline AI surface continues to send the user's queries to Google as before. The local model is a Google-side asset positioned on the user's device - it is not a user-side asset and one could argue it is nothing but sleight-of-hand to hide that actually, the visible AI mode is NOT using the local model.

That arrangement, on its own, engages at least three of the deceptive design pattern families catalogued in EDPB Guidelines 03/2022 [20]. It ismisleading informationbecause the visible label "AI Mode" creates a false impression about where processing occurs - the label does not say "cloud-backed" or "queries sent to Google", and a reasonable user with knowledge of on-device AI will infer locality from the proximity of an on-device 4 GB model on their disk. It isskippingbecause the user is not given a moment to choose between local-only and cloud-backed AI surfaces - both are switched on by the same upstream rollout, with no per-feature consent. And it ishinderingbecause turning AI Mode off does not also remove the on-device install, and removing the on-device install does not turn AI Mode off - the two are separately controlled, and discovering both controls requires knowing about bothchrome://flagsandchrome://settings/ai, neither of which is obvious in default Chrome.

So: not just a non-consented install, but a non-consented install that doubles as cover for a parallel cloud-backed surface that misrepresents to the user where their typing is being processed. Both layers compound the consent problem.

## Why this is unlawful in the EEA and the UK

Article 5(3) of Directive 2002/58/EC (the ePrivacy Directive) prohibits the storing of information, or the gaining of access to information already stored, in the terminal equipment of a subscriber or user, without the user's prior, freely-given, specific, informed, and unambiguous consent, except where strictly necessary for the provision of an information-society service explicitly requested by the user [2]. The 4 GB Gemini Nano weights file is information stored in the user's terminal equipment. The user did not consent. The user has not requested any service that strictly requires a 4 GB on-device LLM. Chrome is functional without the file. The Article 5(3) breach is direct.

Article 5(1) GDPR requires processing of personal data to be lawful, fair, and transparent to the data subject [3]. Where the user's hardware is profiled to determine eligibility for the model push, where the install events are logged on Google's servers, and where the on-device features the model powers process user prompts (whether or not those prompts leave the device), the lawfulness, fairness, and transparency of all of that processing depend on the user being told, in plain language, what is happening. They are not.

Article 25 GDPR requires the controller to implement appropriate technical and organisational measures to ensure that, by default, only personal data that are necessary for each specific purpose are processed [3]. Pre-staging a 4 GB AI model on a user's disk, against a contingency that the user might in future invoke an AI feature, is the architectural opposite of by-default minimisation and the profiling of the device to determine whether or not to push the model is not different to the profiling used to track you online and as such that profile contains personal data and if the AI model is used, will process personal data, so the GDPR arguments are in scope and valid.

Under the UK GDPR and the Privacy and Electronic Communications Regulations 2003, the analysis is the same. Under the California Consumer Privacy Act, the absence of a notice-at-collection covering this specific category of pre-staged software puts Google's CCPA notice posture in question [12].

Then there are the criminal-law violations under various national computer-misuse statutes - which again cannot be overstated.

## ESG: the climate cost of the silent push

The Anthropic case I wrote about was a desktop application installing a 350-byte JSON manifest in seven directories. The bandwidth and energy cost of that, summed across all Claude Desktop users, was negligible. The Chrome case is different. Chrome is pushing a 4 GB binary across hundreds of millions of devices. That has a measurable, quantifiable, and frankly alarming environmental footprint.

I am calculating this using the same methodology our WebSentinel audit platform applies to website environmental analysis [13]:

* Energy intensity of network data transfer:0.06 kWh per GB, the mid-band of Pärssinen et al. (2018) "Environmental impact assessment of online advertising",Science of The Total Environment[14]. The paper reports a 0.04-0.10 kWh/GB range depending on the share of fixed-line vs mobile transfer and inclusion of end-user device energy. 0.06 is a defensible mid-point.
* Grid emissions factor:0.25 kg CO2e per kWh, the EEA / IEA composite EU-27 electricity-supply factor for 2024 reporting [15]. Globally the figure varies from ~0.10 kg/kWh on mostly-renewable grids to over 0.70 kg/kWh on coal-heavy grids; 0.25 is mid-band for a global push and is the figure WebSentinel uses by default.

### Per-device cost of one Nano push

* Bandwidth: 4 GB
* Energy: 4 × 0.06 =0.24 kWhper device per push
* CO2: 0.24 × 0.25 =0.06 kg CO2eper device per push

That is per device, per push. A single download of the model. It does not include re-downloads triggered by the user trying and failing to delete the file. It does not include subsequent updates to the model. It does not include the on-device inference energy when the model is actually used. It is just the one-time delivery cost to one device.

### Aggregated cost across the deployment

Google does not publish how many devices receive the Nano push. The eligibility criteria gating the push (a hardware "performance class" that Chrome computes from CPU class, GPU class, system RAM and available VRAM - typically ~16 GB unified memory or better on Apple Silicon, ~16 GB RAM and a discrete or integrated GPU with sufficient VRAM on Windows and Linux) carve out the very low end of the consumer install base, but the qualifying population is still enormous. I will use three illustrative deployment bands so the reader can pick whichever they consider closest to reality. None of these bands is implausibly large for a feature that ships in default-on Chrome.

Devices receiving the push

Total bytes pushed

Total energy

Total CO2e

100 million (low band: ~3% of Chrome users)

400 petabytes

24 GWh

6,000 tonnes CO2e

500 million (mid band: ~15% of Chrome users)

2 exabytes

120 GWh

30,000 tonnes CO2e

1 billion (high band: ~30% of Chrome users)

4 exabytes

240 GWh

60,000 tonnes CO2e

To compare those numbers to what an ESG report could compare to:

* 24 GWh(low band) is roughly the annual electricity consumption of about 7,000 average UK households [16].
* 120 GWh(mid band) is roughly the annual electricity consumption of about 36,000 average UK households, or the annual output of a 14 MW wind turbine running at typical UK capacity factor.
* 240 GWh(high band) is roughly the annual electricity consumption of about 72,000 average UK households, or the annual output of about 28 MW of installed wind capacity.
* 6,000 tonnes CO2e(low band) is roughly the annual emissions of 1,300 average passenger cars in the EU [17].
* 30,000 tonnes CO2e(mid band) is roughly the annual emissions of 6,500 cars, or one return flight from London to Sydney for about 8,000 passengers in economy.
* 60,000 tonnes CO2e(high band) is roughly the annual emissions of 13,000 cars.

These are thedelivery-onlynumbers. They count the bytes traversing the network exactly once. They do not count:

* The roughly 4 GB × N devices of disk-storage cost, sustained, on user hardware. SSDs have a per-GB embodied carbon cost of approximately 0.16 kg CO2e per GB of NAND manufactured [18]; for 1 billion devices × 4 GB that is around 640,000 tonnes CO2e of embodied SSD allocated to a use case the user did not consent to. This is a one-off manufacturing-carbon impact, but the storage burden is borne in perpetuity by user devices that could otherwise have used the space for user data.
* The on-device inference energy when Nano is invoked. Per inference this is small. At 2 billion daily Chrome users it is no longer small.
* The re-download cycle for users who try to delete the file. Each successful re-trigger of the download is another 4 GB × 0.06 kWh × 0.25 kg = 0.06 kg CO2e per device per re-download.
* The future model updates. Gemini Nano is not a one-shot artefact; it is an evolving model with periodic weight refreshes. Each refresh repeats the calculation.

In ESG-reporting language, the one-time push of the current model is a Scope 3 Category 11 ("use of sold products") emission against Google, attributable to the user-side delivery of a binary the user did not request, in the operation of a free product Google distributes [4].

### Why the bandwidth side matters in its own right

In addition to the carbon cost, the network-bandwidth cost is paid by ISPs, by mobile network operators, by users on metered connections, and by every piece of network infrastructure that has to carry an unwanted 4 GB payload to a destination that did not ask for it. Per the Pärssinen reference, around 50% of that delivery energy is in the access network and CDN edge, around 30% is in user-side equipment (router, modem, NIC), and the remainder is in the core. None of that infrastructure exists for free. Every byte Chrome pushes is a byte that competes with bytes the user actually wanted.

For users on capped mobile data plans, particularly in regions where smartphone-as-only-internet is dominant (much of Africa, much of South and Southeast Asia, most of Latin America), 4 GB of unrequested download is on the order of a month's data allowance, vapourised by Chrome on the user's behalf. Google has not, to my knowledge, published any analysis of the welfare impact of this on the populations whose internet access is metered.

Keep in mind that mobile data plans (4G and 5G) are used by many households who do not have access to fiber, cable or adsl and are used for desktop devices as well as mobile - so the argument that Google won't push this to mobile devices (although I have not found anything official to support that argument anyway) will not fly.

## What Google should have done

This is not a hard list. It is the same list I gave Anthropic in the Claude Desktop article, applied to Google.

1. Ask.First time Chrome is about to download the Nano model, pop a dialogue. "Chrome would like to download a 4 GB AI model file to your device to power the following features. Allow, or skip and decide later." Two buttons. Done.
2. Pull, not push.Trigger the download as a downstream consequence of the user invoking an AI feature for the first time. Let the feature itself be the consent event. Do not pre-stage on a contingency.
3. Surface it.Inchrome://settings/, list the AI model files Chrome has downloaded, their size, the features they power, and a "Remove and stop downloading" button per model. Make removal persistent, not a transient state Chrome corrects on next launch.
4. Document it.Tell the user, plainly, in the Chrome description on the Microsoft Store, in the Chrome installer, on the Google Chrome download page, that Chrome will download additional model files of substantial size on supported hardware. Currently, this is essentially undocumented to a normal user.
5. Respect deletion.If the user deletesweights.bin, do not re-create it. If the user has a strong preference about what is on their disk, the application is not in a position to override that preference because the application thinks it knows better.
6. Disclose at scale.Publish, in Google's annual ESG report, the aggregate bandwidth and carbon footprint of all AI-feature model pushes to user devices, broken down by region. Treat it as the Scope 3 Category 11 emission it is. Account for it.
7. Notify retrospectively.Users who already received the model without consent should, on next Chrome launch, be told what happened, shown the file, and offered a one-click revoke + uninstall. This is the same retrospective-consent step Anthropic should also have taken.

## Closing

Both of these episodes, the Anthropic Claude Desktop manifest install I wrote about two weeks ago and the Google Chrome Gemini Nano push I am writing about today, share the same underlying decision. An engineering team at a large AI vendor decided that the user's machine is a deployment surface to be optimised for the vendor's product roadmap, not a personal device whose owner is the legal authority on what runs there.

The Anthropic case put a pre-authorisation for browser automation on around three million Claude Desktop user devices [19]. The Google case puts 4 GB of AI weights on, by my mid-band estimate, around 500 million Chrome user devices, with proportionally larger ePrivacy, GDPR, and environmental exposure.

Both companies have a public posture of caring about safety, ethics, and responsible AI. Both companies, in the silent installation behaviours documented here, have undermined the foundational consent on which the legitimacy of any of those positions depends. The fact that the bytes are AI bytes does not exempt them from the law that governs every other byte that gets written to a user's device without permission. The fact that the bytes are "small" relative to the user's disk does not exempt the cumulative carbon footprint from being a real, measurable, ongoing harm to the climate.

If Google's next Chrome update silently removes the unconsented installs and replaces the behaviour with an explicit opt-in, we will know the company can read the room. If it does not, we will know what the company's published positions on responsible AI and sustainability are actually worth.

In light of what is increasingly becoming default behaviour, one has to ask a very simple question. When will the Regulators and Public Prosecutors start to enforce the law which has been in place since 2002 - or are global tech corporations exempt from criminal and civil statutes?

## References

[1] Hanff, A. "Anthropic secretly installs spyware when you install Claude Desktop",That Privacy Guy!, 18 April 2026.https://thatprivacyguy.eu/blog/anthropic-spyware

[2] European Parliament and Council. Directive 2002/58/EC on privacy and electronic communications (ePrivacy Directive), Article 5(3).https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02002L0058-20091219

[3] European Parliament and Council. Regulation (EU) 2016/679 (GDPR), Articles 5(1), 25.https://eur-lex.europa.eu/eli/reg/2016/679/oj

[4] European Parliament and Council. Directive (EU) 2022/2464 amending Regulation (EU) No 537/2014, Directive 2004/109/EC, Directive 2006/43/EC and Directive 2013/34/EU as regards corporate sustainability reporting (CSRD).https://eur-lex.europa.eu/eli/dir/2022/2464/oj

[5] Pure Infotech. "Stop Chrome from silently downloading Gemini Nano AI model on Windows 11".https://pureinfotech.com/stop-chrome-gemini-nano-download-windows-11/

[6] Dhavale, V. "Chrome Installed a 4GB LLM on My Machine. Here's What I Found Out."https://www.vishwamdhavale.com/blog/chrome-gemini-nano-on-device

[7] WinAero. "Google Chrome Secretly Downloads Huge Local AI Models".https://winaero.com/google-chrome-secretly-downloads-huge-local-ai-models/

[8] AIBase. "Google Chrome Exposed for Forcing 4GB AI Model Installation".https://www.aibase.com/news/25955

[9] StatCounter. "Browser Market Share Worldwide".https://gs.statcounter.com/browser-market-share

[10] Wikipedia. "Usage share of web browsers".https://en.wikipedia.org/wiki/Usage_share_of_web_browsers

[11] DemandSage. "How Many People Use Google Chrome (Updated 2026 Data)".https://www.demandsage.com/chrome-statistics/

[12] State of California. California Consumer Privacy Act of 2018, Cal. Civ. Code § 1798.100 et seq.https://oag.ca.gov/privacy/ccpa

[13] Hanff, A. "WebSentinel ESG Considerations chapter methodology". WebSentinel report template, Chapter 08. (Source: this article's author's audit platform, code at /backend/lib/transparency/esg-calculator.js.)

[14] Pärssinen, M., Kotila, M., Cuevas, R., Phansalkar, A., Manner, J. "Environmental impact assessment of online advertising",Science of The Total Environment, 2018.https://www.sciencedirect.com/science/article/pii/S0195925517303505

[15] European Environment Agency. "Greenhouse gas emission intensity of electricity generation".https://www.eea.europa.eu/en/analysis/indicators/greenhouse-gas-emission-intensity-of-1

[16] Ofgem. "Average gas and electricity usage". (UK average household electricity consumption: ~2,700 kWh/year, "low" TDCV 2024.)https://www.ofgem.gov.uk/

[17] European Environment Agency. "Average CO2 emissions from new passenger cars" (EU-27, 2024 reporting baseline ~109 g/km × ~12,000 km/year ≈ 1.3 t/year per average car).https://www.eea.europa.eu/

[18] Tannu, S., Nair, P. J. "The dirty secret of SSDs: embodied carbon",ACM SIGENERGY Energy Informatics Review, 2023.https://dl.acm.org/doi/10.1145/3630614.3630618

[19] Anthropic. Reported Claude Desktop install base estimates from Q1 2026 disclosures. (Estimate; Anthropic does not publish exact figures.)https://www.anthropic.com/

[20] European Data Protection Board. "Guidelines 03/2022 on deceptive design patterns in social media platform interfaces", version 2.0, adopted 14 February 2023.https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-032022-deceptive-design-patterns-social-media_en

Forensic web audit

### Run this audit on your own property.

WebSentinel is the forensic audit platform behind articles like this one. Every tracker, every cookie, every library, every consent boundary — evidenced, timestamped, court-ready.

* CRITTracking pixels firing before consent
* HIGHThird-party data flows under-disclosed in the privacy notice
* MEDCookie banner non-compliance with Article 7(3) withdrawal
* INFOJS library SBOM with integrity hashes & change detection

See WebSentinel

Talk to us