---
title: 'EU Age Control: The trojan horse for digital IDs – Juraj Bednar'
url: https://juraj.bednar.io/en/blog-en/2026/04/17/eu-age-control-the-trojan-horse-for-digital-ids/
site_name: hackernews_api
content_file: hackernews_api-eu-age-control-the-trojan-horse-for-digital-ids-ju
fetched_at: '2026-04-26T19:44:48.348384'
original_url: https://juraj.bednar.io/en/blog-en/2026/04/17/eu-age-control-the-trojan-horse-for-digital-ids/
author: gasull
date: '2026-04-26'
published_date: '2026-04-17T20:47:57+02:00'
description: 'EU Age Control: The trojan horse for digital IDs'
tags:
- hackernews
- trending
---

Most people think EU Age Control apps are about identifying users. The sales pitch is all zero-knowledge proofs of age. You prove you’re over 18 without the site learning your name, exact birthday or anything that can link one proof to another.

Before going further, it is worth laying out three separate problems this post is worried about. They are easy to blur but they are very different. First: the DSA fallback — platforms don’t actually need the privacy-preserving wallet; the rules let them use a normal KYC provider instead. Second: attestation lock-in — Google and Apple decide what software runs on the phones that can use this system. Third: the system itself is weaker than advertised — the cryptography the reference app actually ships is not the cryptography the marketing describes, unlinkability depends on wallet behavior not math, and there is a whole class of relay attacks the protocol cannot stop. When commentators wave away “the hacks,” they usually mean bugs in the mock-up.

It is also worth askingwhenthis app started being described as “just a reference implementation” or a “white-label demo.” The README tells a story. On 12 May 2025, a disclaimer appeared framing the project as an “Age Verification Solution Toolbox” that Member States are expected to build on. On 31 July 2025, further softening was added — language explicitly calling the app a white-label reference for countries to adapt — and in the exact same edit, the earlier, blunter disclaimer (which said this was an initial version not intended for production) was quietly removed. In any case, it was always presented as a toolbox that countries should adapt into their apps – so judging the app by itself does not make much sense, it depends on how these techniques are implemented in each country’s verification app. There will be no single EU app, despite what the honchos of EU say.

## The DSA fallback nobody talks about

Big platforms must verify age for certain content. Theycanuse the fancy EU wallet with its privacy features.They can also just plug in a normal KYC providerthat scans your full passport, runs liveness checks and sees everything. Which path do you think most companies will actually take when the “privacy-preserving” option requires integrating with systems that barely exist yet across 27 countries?

It’s marketing sleight of hand. They push the privacy angle hard while the rules quietly allow the non-private fallback. The privacy part is optional. (I think they mainly know the apps will not be ready by the end of the year).

KYC companies have been avoiding real electronic IDs for years. I have a Slovak eID chip that’s been in my wallet forever. It has proper cryptographic keys and can prove who I am far more cleanly than a photo of my driver’s license plus video call. Yet almost every KYC provider still does the bitmap and liveness routine. The reason is simple. Integrating with 27 different national eID systems is a nightmare. Maintaining a database of what every country’s physical ID looks like is cheaper and works everywhere. The cryptographic route doesn’t — in practice, not in theory.

So the EU solution only “works” if platforms decide to do all that integration work themselves.Right now the official trusted list has zero production apps.The reference implementation is still half-baked.Believing this turns into clean interoperability across all EU countries by the end of 2026 is wishful thinking.

## How verification actually works

The main high-assurance path in the reference app uses an NFC passport. You scan the MRZ code at the bottom of the photo page; it gives the keys to read and decrypt the data on the NFC chip. That chip contains signed data including a JPEG photo of the holder. The design calls for a live photo to be taken and matched locally against the chip’s JPEG — this is intended to stop a kid scanning a parent’s passport to get a credential for themselves.

The app is open-source so you can read every line. But changing even one bit would break the hardware attestationonce attestation is actually enforced by national deployments. In the current reference code, attestation verification is not wired up on the server side — it is a promise national deployments would need to add. The binary must ultimately match exactly what Google or Apple signed. No GrapheneOS, no custom Linux phones.

Attestation locks it down. It is the same EU that hates these American corporations and wants EU alternatives for everything — yet no one can make a phone usable for age verification without the blessing of Google (or Apple, who does not certify third-party devices for iOS at all). Bought a Huawei phone that does not pass Play Integrity? Sorry. Note: Huawei phones can produce hardware attestation via their factory key chain, but they cannot pass Google’s Play Integrity verdict — the sameapplies to GrapheneOS, Linux phones, and anything outside the Google blessing. Use a Daylight computer that doesn’t wreck your circadian rhythm? Back to the office.

There is a simpler MRZ-only path in the reference app where you photograph an ID card with no NFC read or face match. Real national apps may not support it, and the reference recommends the high-assurance path. Countries will probably force the chip-based route. It’s a trojan horse to digital ID anyway.

## The marketed crypto and the shipped crypto are not the same thing

The public story is built around zero-knowledge proofs. The reference Android app doesn’t actually use zero-knowledge crypto in the flow that runs. It uses an older ISO standard (ISO 18013-5 mdoc with ES256) where each attribute is signed in advance and the wallet reveals only the ones asked for, hiding the rest using salted-digest commitments. A ZK library is pulled in, but nothing in the presentation path ever calls it. So when people cite “ZK age proofs” as the innovation, they are citing something that is in the repo but is not switched on. Whether national apps eventually turn it on is an open question. Today’s reference is plain signatures.

The cryptographycouldbe solid — zero-knowledge proofs over passport signatures are a real and tractable thing. But the crypto actually shipping in the current reference is the older plain-signature format with disposable-batch unlinkability, not ZK. So when people defend “the math works,” they are defending math that is not turned on. Although if you use each signed attestation only once, it only reveals that you are over 18 and maybe from the signature who issued the attestation. There’s no unique identifier.

## What’s private and what isn’t

The overall flow is local-first, but still needs a server to issue credentials. Scanning and initial checks happen on the phone. Because the app is (or would be) attested, the issuing server can be reasonably confident what exact code actually executed. The server verifies the document signatures and issues a signed credential. That credential can then be used to produce a proof of age when talking to websites.

From the verifier’s (say, a porn site or social media platform) point of view itlooksunlinkable — as long as the wallet behaves. The design is not “the math guarantees two proofs can’t be correlated.” The design is “the wallet hands out a pile of disposable credentials, uses each one once, then asks for more.” If the wallet obeys that rule, two verifiers see two different signatures and can’t tie them together. If the wallet cheats, or if a proof is replayed, the two verifiers see the same signature bytes, and the linkage is trivial. This is an important nuance — the usual “ZK = math = unlinkable forever” pitch doesn’t apply here. The property holds because the wallet issupposedto rotate credentials, not because the cryptography makes reuse impossible. Real cryptographic unlinkability schemes like BBS+ or CL signatures would produce uncorrelated proofs even on reuse. This is not that.

From the issuer’s point of view — they issue credentials when you present your ID. The issuer doesn’t know what you’ll use the credential for, or how many times you’ll use it — the one-use rule lives inside the wallet, not on the server. So if the wallet is modified, or if proofs are captured and replayed, nobody upstream sees it. Any “rate limit” you might imagine is a limit on how many credentials you mint, not on how many times a credential is used in the wild.

They can of course infer that you are an EU country citizen. But they can’t (under normal wallet behavior) tell which accounts are yours or link your activity across sites.

## What about relay attacks?

Here’s a scenario the spec doesn’t really answer. Suppose a child wants to get into an age-gated site. A service pops up — call it Grandma-as-a-Service — that offers to verify on their behalf for a few euros. The child opens the site, gets a QR code or a link, and instead of scanning it themselves they paste it into the proxy service. The proxy forwards it to a real adult somewhere with a real, government-issued wallet on a clean phone. The adult approves. The adult’s wallet produces a cryptographically perfect “over 18” proof. The site sees a valid proof and lets the child in.

Nothing failed. Every signature is real, every attestation is real, the adult really is over 18, the wallet really is running unmodified on a genuine Android. The catch is that the protocol binds the proof to “some wallet somewhere said yes,” not to “the human at this browser right now.” There is no proximity check. The browser-side Digital Credentials API partially closes this — but only when the user verifies on the same phone they’re browsing from. QR codes and deep links, which work across devices, are wide open.

People assume Google’s Play Integrity would stop this. It doesn’t. Play Integrity attestswhat code is running on what device. It says nothing aboutwho is in front of itorwhere the device is. In the proxy flow, the adult’s phone is a real phone and every attestation is real. The relay — the web service the child talks to — isn’t being attested; it’s just moving bytes.

And once an adult is enrolled, the resale version gets ugly. The wallet has thirty disposable credentials, refreshed on a short interval. The issuer never sees how those get used. So the proxy operator can reuse each credential across many children; nothing upstream raises an alarm. The “one-time use” rule is an honor-system rule inside the wallet software, not something the issuer can enforce after the fact. This is not a bug that production apps will “fix.” It’s inherited from the shape of the protocol, so it will be present in all 27 national apps.

## The Trojan Horse

In any case, this is the trojan horse. Start with “protect the children from porn and scary social media.” Create enough friction that people reach for the convenient attested wallet. The app itself must be attested — which in practice means Google or Apple decide what runs. The credential can be killed by the issuer.

The reference app leaks face photos, although only locally. Twenty-seven countries will each build their own version. With their own privacy bugs.

Then you get the Hawthorne effect. Every controversial site that makes you pull out the wallet creates self-censorship, even if the proof is supposedly anonymous. Governments have a terrible track record protecting this data. Any data. History is full of examples.

(Want to watch porn? Criticize a politician? Are you really going to open the EU country’s ID app to verify that you are over 18 and believe it’s unlinkable ZK proof — even if it really is?)

Later they link it to Digital Euro and everything else. Suddenly a big chunk of your life can be switched off remotely. Didn’t pay a parking ticket on time? Let’s temporarily revoke your credentials — when you can’t log in anywhere, you will come and pay the ticket.

The architecture and politics are the usual control layer with fresher paint. We don’t need revocable digital IDs as the price of entry to the internet. We were doing just fine.

## Are the published hacks real?

It’s worth splitting the reported problems into two piles. Pile one: “bugs in the mock-up” — leaked files, unchecked MRZ scans, Chrome-extension demos hitting a placeholder backend. These are fixable and will be fixed per country. Pile two: structural properties that fall out of the protocol itself — no proximity binding, client-side one-time-use, unlinkability that breaks on reuse. These are not bugs. They’ll be present in every national implementation that follows the spec. When commentators wave away “the hacks,” they usually mean pile one. Pile two is what this post is actually about.

There have been several “hacks,” mostly by people who don’t understand how this is supposed to work. Leaving files on disk in the reference app is something that will be fixed, and does not really matter. The reference app will not be used by any country directly — they will have their own bugs. It’s for countries to know how to generate the proofs and stay interoperable. It doesn’t even matter that you can fool it into giving you a test credential, because the primary verification path will be countries’ own eID systems, not their mock-up of unchecked MRZ scanner.

There was a “hack” that created a custom Chrome extension. That would fail app attestation once attestation is enforced. The MRZ path also does not connect to a real backend, because there’s no real EU-side backend — the registries of valid documents are the competence of individual countries.

I’m 99% sure that even though I consider EU completely incompetent, these particular mock-up hacks won’t work in production apps. So this “haha, I hacked the app with my Claude Max subscription” doesn’t mean anything. They’re hacking a mock-up showing the use of a library. Yes, Frau Ursula called it “EU Age Verification app,” but there will not be an EU app — there will be a Slovak app, a Hungarian app, a German app, a Dutch app, a French app…

## But Why?

Many of us naturally ask why people want this. I think it’s a mistake to think they don’t. There is demand for this. The internet is scary, parents think they can’t protect their children from many bad things happening, and someone came to provide a “solution.” Doesn’t matter that I am sure the kids will go around it easily. The clients (the voters) are not the children being protected, but their parents, feeling good.

I think a very good and deep explanation is in my novel Tamers of Entropy. Have a look. It is very cypherpunk/lunarpunk and explains also the psychology behind these dystopias — and a way outside. Plus it’s fun to read. Check it out attamersofentropy.net. The charactersalso have Nostr accounts.

## Conclusion

The EU fancy ZK apps will not be ready. Platforms will use normal KYC providers, AI face age estimators and other means.

When done according to spec, the age verification app has meaningful privacy properties — the platforms don’t know your identity or link your accounts. But those properties rest on wallet behavior, not cryptographic guarantees. The ZK math that would make unlinkability a hard guarantee is in the repo and not switched on.

The apps will not work unless you have a Google or Apple approved device. Forget Linux, GrapheneOS, Huawei, after-market firmwares. It’s part of the security model.

And relay attacks — children using adult proxies to get into age-gated sites — are not fixable bugs. They are a structural property of the protocol that will ship in all 27 national apps.

The privacy theater hides the wolf. The wolf is still there.