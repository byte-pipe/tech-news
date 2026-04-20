---
title: Do Not Turn Child Protection Into Internet Access Control
url: https://news.dyne.org/child-protection-is-not-access-control/
site_name: hackernews_api
content_file: hackernews_api-do-not-turn-child-protection-into-internet-access
fetched_at: '2026-03-22T11:09:46.043631'
original_url: https://news.dyne.org/child-protection-is-not-access-control/
author: smartmic
date: '2026-03-21'
published_date: '2026-03-20T17:08:25.000Z'
description: Age verification turns the open internet into a permission system and pushes control away from families, schools, and users.
tags:
- hackernews
- trending
---

Age verification is no longer a narrow mechanism for a few adult websites.Across Europe, the USA, the UK, Australia, and elsewhere, it is expanding into social media, messaging, gaming, search, and other mainstream services.

The real question is no longer whether age checks will spread. It is what kind of internet they are turning into.

The common framing says these systems exist to protect children. That concern is real. Children are exposed to harmful content, manipulative recommendation systems, predatory behavior, and compulsive platform design. Even adults are manipulated, quite succesfully, with techniques that can influence national elections.

Democracy at risk: media warfare and the role of technology in modern elections - Friends of Europe
The think tank for a more inclusive Europe
Friends of Europe
EPIC

But from a technical and political point of view, age verification is not just a child-safety feature. It is an access control architecture. It changes the default condition of the network from open access to permissioned access. Instead of receiving content unless something is blocked,users increasingly have to prove something about themselves before a service is allowed to respond.

That shift becomes clearer when age assurance moves down into the operating system. In some US proposals, the model is no longer a one-off check at a website. It becomes a persistentage-status layer maintained by the OSand exposed to applications through a system-level interface. At that point, age verification stops looking like a limited safeguard and starts looking like a general identity layer for the whole device.

This is no longer only a proprietary-platform story either. Even the Linux desktop stack is beginning to absorb this pressure.systemd has reportedly added an optionalbirthDatefield touserdbin response to age-assurance laws. Regulation is beginning to shape the data model of personal computing, so that higher-level components can build age-aware behavior on top.

The main conceptual mistake in the current debate is simple. It confuses content moderation with guardianship. Those are not the same problem.

Content moderation is about classification and filtering. It asks whether some content should be blocked, labeled, delayed, or handled differently.Guardianship is something else. It is the contextual responsibility of parents, teachers, schools, and other trusted adults to decide what is appropriate for a child, when exceptions make sense, and how supervision should evolve over time.Moderation is partly technical. Guardianship is relational, local, and situated in specific contexts.

I am also a parent. I understand the fear behind these proposals because I live with it too. Children do face real online risks. But recognizing that does not oblige us to accept any solution placed in front of us, least of all one thatweakens privacy for everyone while shifting responsibility away from families, schools, and the people who actually have to guide children through digital life.

Age-verification laws collapse these two questions into one centralized answer. The result is predictable. A platform, browser vendor, app store, operating-system provider, or identity intermediary is asked to enforce what is presented as a child-protection policy, even though no centralized actor can replace the judgment of a parent, a school, or a local community.

This is the wrong abstraction. It treats an educational and social problem as if it were only an authentication problem.

It also fails on its own terms. Thebypasses are obvious: VPNs, borrowed accounts, purchased credentials, fake credentials, and tricks against age-estimation systems. A control that is easy to evade but expensive to impose is not a serious compromise: it is an error or, one may say, acorporate data-grab.

I traced $2 billion in nonprofit grants and 45 states of lobbying records to figure out who's behind the age verification bills. The answer involves a company that profits from your data writing laws that collect more of it.
 by

u/Ok_Lingonberry3296
 in

linux

A sprawling OSINT investigation arguing that parts of the US age-verification push are being shaped by corporate lobbying and opaque advocacy networks, while pushing surveillance down into the operating system layer.

The price is high and paid by everyone. More identity checks. More metadata. More logging. More vendors in the middle. More friction for people who lack the right device, the right papers, or the right digital skills. This is not a minor safety feature. It is anew control layer for the network.

And once that layer exists, it rarely stays confined to age. Infrastructure built for one attribute is easily reused for others: location, citizenship, legal status, platform policy, or whatever the next panic demands. This is howa limited check becomes a general gate.

The solution is simple: moderate content close to the endpoint, in the browser, on the device, on the school network, or through trusted local lists.

Keep guardianship where it belongs: with parents, teachers, schools, and communities that can make contextual decisions, authorize exceptions, and adjust over time.

The operating system can helphere, but only as alocal policy surfaceunder the control of users and guardians. It should not become a universal age-broadcasting layer for apps and remote services. That is the architectural line that matters.

Most of the harms invoked in this debate do not come from the mere existence of content online. They come from recommendation systems, dark patterns, addictive metrics, and business models that reward amplification without responsibility. If the goal is to protect minors, that is where regulation should bite.

Children need protection.
The internet does not need a permission system.

If we are serious about reducing harm, we should stop asking how to identify everyone and start asking how to strengthen local control without turning the network into a checkpoint.

## Chronology

It is encouraging to see this article circulating widely, as it may contribute to a shift in how policymakers approach the issue. Given its growing visibility, I will keep a concise record here of the sequence of its coverage across media outlets, as well pilot implementations across the world.

My first account on the problem emerged from a dialogue with Brave's developerKyle den Hartogat acypherpunk retreat in Berlin. It was right after facilitating the digital identity track of the event that I published a rather technical piece on the topic.

Age Verification for Humans
Europe’s age‑verification pilots conflate censorship with guardianship. This essay argues for a decentralised approach that separates technical filtering from social responsibility.
News From Dyne
Jaromil

Later, as age verification measures began to take hold, and in alignment with our community facilitators at the Dyne.org foundation,we decided to discontinue Discord as a channel for participation, as the platform moved to impose age verification.

This decision to leave Discord was received positively across the community, a clear indication that privacy is valued above outreach.

Then the systemd dispute unfolded, and I found myself, as founder of the project, as the first distro maintainer stating that we would not implement age verification inDevuan GNU/Linux, a Debian fork without systemd that has, since 2016, shown fewer bugs and security advisories. The tech journalist Lunduke picked it up immediately, setting off a wave of similar declarations across the distribution maintainer community.

Founder of@DevuanOrg(a Systemd-free fork of Debian) has declared that Devuan Linux "will remove age verification" that they inherit from projects they base upon.pic.twitter.com/fIN4lmDjUn

— The Lunduke Journal (@LundukeJournal)
March 19, 2026

That was the moment I realised the need to set out, in clear terms, the reasons behind this choice, and the grounds for a form ofconscientious objection should such laws ever be enforced on our projects at Dyne.org. I then wrote a piece for Wired Italy, in Italian, my mother tongue, which is due to be published by the magazine in the coming days (link TBD).

While awaiting publication in Wired, I translated the article and published it here, in English, through our think and do tank. The piece you have just read quickly reached the front page of Hacker News, drawing nearly 400 comments from concerned readers and technical experts, a valuable body of material to build on.

Do Not Turn Child Protection into Internet Access Control | Hacker News
Hacker News

As the discussion gains momentum, I am engaging with colleagues at the City of Lugano and thePlan₿ Foundation, where I have recently taken on the role of Scientific Director. The proposal is to move from analysis to action by establishing a city-wide pilot that explores technologies for locally managed guardianship, offering a constructive example for Switzerland.

draft lip-ageverif: local child protection without internet age verification by jaromil · Pull Request #1 · LuganoPlanB/LIPs
Inspired by https://news.dyne.org/child-protection-is-not-access-control/
This PR adds a new draft proposal in lip-ageverif.md for a Lugano approach to child protection that does not rely on mandat…
GitHub
LuganoPlanB

We are approaching this with confidence and preparing for a rollout for Lugano within the next two years. At the same time, within the Swiss Confederation there are signs of a more grounded direction, as reflected in "The Internet Initiative" placing responsibility on Big Tech and bringing together representatives from all major Swiss political parties.

Startseite - Internet-Initiative
https://www.internet-initiative.ch/wp-content/uploads/Untitled.mp4
Internet Initiative
lazysloth

My next steps include reaching out to contacts in Europe to help broaden the discussion and contribute to a more balanced public debate, in the face of sustained pressure from corporate lobbies advancing data-extractive measures.

And you can play a meaningful role as well: engage with the issue, bring your technical and political understanding to it, and help sustain attention so that those who make up the internet are not excluded from decisions that affect it. I hope this material and the reasoning behind it can be useful in that direction. Do let us at Dyne.org know if we can assist in making visible successful local pilots that implement child protection in a sound and proportionate way.

### Who am I, and further reading

If you like to read further, I've written more about the problems of European Digital Identity implementation plans and architecture.

The Seven Sins of European Digital Identity (EUDI)
EUDI as is today presents big problems and disregards criticism, warnings, and requests to review technical details, with results that harm the fairness of the system and the privacy of its participants, also limiting infrastructure security and scalability.
News From Dyne
Jaromil

I've been working on privacy and identity technology for over a decade, primarily inprojects funded by the European Commission.Among my efforts aredecodeproject.euandreflowproject.eu, various academic papers, includingSD-BLS, recently published by IEEE. Additionally, with our team atThe Forkbomb Companywe've developed digital identity products asDIDROOM.comandCREDIMI.io.
