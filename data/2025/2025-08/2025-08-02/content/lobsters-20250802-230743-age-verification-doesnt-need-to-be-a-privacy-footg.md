---
title: Age Verification Doesn’t Need to Be a Privacy Footgun - Dhole Moments
url: https://soatok.blog/2025/07/31/age-verification-doesnt-need-to-be-a-privacy-footgun/
site_name: lobsters
fetched_at: '2025-08-02T23:07:43.443447'
original_url: https://soatok.blog/2025/07/31/age-verification-doesnt-need-to-be-a-privacy-footgun/
date: '2025-08-02'
published_date: '2025-07-31T18:40:08+00:00'
description: '"Won''t someone think of the poor children?" they say, clutching their pearls as they enact another stupid law that will harm the privacy of every adult on Earth and create Prior Restraint that inhibits the freedom of speech in liberal democracies. Art: CMYKat If you''re totally ignorant of how things work, the proposal of "verifying…'
tags: cryptography, privacy
---

“Won’t someone think of the poor children?” they say, clutching their pearls as they enact another stupid law that will harm the privacy of every adult on Earth and create Prior Restraint that inhibits the freedom of speech in liberal democracies.

Art:
CMYKat

If you’re totally ignorant of how things work, the proposal of “verifying you’re an adult” before you access adult content sounds, superficially, like a reasonable thing to do. But it’s a patently stupid idea at every level.

## Age Verification Makes The Internet Less Secure

In meatspace, if you wanted to go to the adult section of a movie store, you would need to show a clerk your government issued photo ID. They would check that your date of birth was before (current date – 18 years), and if so, they would admit you. This is the sort of experience that people who do not understand technology use to build an intuition for how laws like this operate.

The Internet is not like meatspace.When you supply your government ID to a website in order to verify your identity, at least two of the following security and privacy risks introduced at once:

1. The website stores your credential (whether by design or by hacker intervention).
2. The mechanism websites use to prove that the credential is authentic could track who is visiting which adult website in order to build a profile for your tastes and interests for marketing and/or blackmail purposes.
3. Your device (phone, computer, etc.) could have malware installed that pilfers whatever credential you provided in order to e.g. commit identity theft.

That’s a lot of risk for the public to take on. But what are they getting in exchange for it?

CMYKat

Well, a lot fewer adults will choose to share their photo ID to look at pornography, which will likely increase sexual aggression sincepornography use by adults inversely correlates with sexual assaultin every society science has observed.

(…) the increasing availability of pornography appears to be associated with a decline in rape.

Part of this is deliberate: The anti-porn lobby is largely christofascists and they’re all following the same playbook as the authors ofProject 2025. Y’know, the same clowns thatwant to ban sex education.

Art by
AJ

The Christian nationalists behind these movementsalso wantto classify all forms of queer expression as sexual,and therefore pornographic, to force us back into the closet (lest we be prosecuted as sexual predators for daring to be visibly queer “in front of children”).

Transgender people are at the top of their target list, but make no mistake, they hate cisgender gay and lesbian Americans just as much.

Sometimes what can be explained by stupidity is better explained with malice. This is doubly so with right-wing politics.The cruelty is the point.

This is not a uniquely American problem: Puritanical attitudes towards sex have penetrated every society. TheUK’s Online Safety Actaims to accomplish the same end goals as the fascists across the pond. The recent ban waves of adult content on Steam and itch.io were caused by an Australian “feminist” group that usedextralegal pressure through payment processors to achieve their goals.

Needless to say, the attempts to control adult content have been a complete clusterfuck.

## Protecting User Privacy

If it wasn’t clear already, the anti-porn laws are stupid, wrong, and harmful. You should absolutely call your representatives and get these stupid laws overturned if you live in an affected jurisdiction.

But they are, nonetheless, the law in those jurisdictions.

Until they can be repealed by a more competent electorate, we have to operate on the assumption that “age verification” will be a stupid thing we have to live with.

To that end, cryptography actually provides us with an interesting tool for limiting the risks of age verification. They’re calledzero-knowledge proofs.

### Clueless About Zero-Knowledge Proofs

I will not mince words: zero-knowledge proofs straddle the line between genius and madness.

Sure, you can grok the basic idea of them pretty easily: You can prove that you have knowledge without revealingwhat that knowledge is. There have been lots of YouTube videos that explain this pretty intuitively. Here’s one from Numberphile:

But then you get into the art of turning interactive proofs (as described in the video) into non-interactive proofs. This usually involves a Fiat-Shamir transform,which comes with many subtle footguns.

The most basic kind of non-interactive proof you’re likely to run into in the real world is an Schnorr proof–which is the basis for Ed25519 signatures. The signatures are succinct proofs of knowledge of a particular secret number (the private key).

But then you have the madness: Algebraic circuits, polynomial commitments, trusted setups versus recursive proofs,motherfuckingzero-knowledge VMs!

If you stare atthe introductory material for zero-knowledge proofsfor long enough, you will come to appreciate Plato’s account of Socrates in a new light.

I am the wisest man alive, for I know one thing, and that is that I know nothing.

Your brain on zero knowledge

Why am I describing zero-knowledge proofs this way? Because I want you to appreciate how much they are a departure from the simple world of “should I use AES-GCM or ChaCha20-Poly1305 here?” level cryptography protocol design that most developers find themselves in.

CMYKat

Look, I cansort ofexplain my job to strangers, even if they have no technical expertise. It usually goes something like, “Y’know that padlock icon in your browser when you connect to your bank’s website? Well, I test the padlocks.”

That analogy works way better than having to explain for the 10,000th time that I do not work in blockchain.

Nobody knows what “crypto” is, but they think it involves speculative investment. Thanks for nothing, blockchainiacs.

I cannot explain “encode your program as a polynomial and use it in this algebraic circuit” to a mere mortal. And until I’m able to do so, I will always feel like I do not adequately understand this topic within cryptography.

I generally wouldn’t wish this sort of complexity on anyone unsuspecting, but I’m going to make an exception for the governments that pass these privacy-averse age verification laws.

## Privacy-Preserving Age Verification

Google recentlypublished an open source library that proves a user’s age in a way that preserves privacy. This library is undergoing two independent security reviews, but should be production-ready in the near future.

If we’re going to force websites to implement some kind of age verification for adult content, we should demand the governments that pass these laws provide the zero-knowledge proof technologies to satisfy the law.

After all, they’re the entities that vend identity credentials (passports, driver’s licenses, and other photo IDs) in the first place.

If this technology must exist, then let the governments own the risk of this technology, not individual website operators or Internet users.

If nothing else, elected officialsstruggling to articulatePLONK vs R1CS would make for some excellent blooper reels.

#### Consider PrivacyPass

Earlier this year, the paid search engineKagi adopted PrivacyPass(see also: this set ofIETF RFCs and other documents) so they can verify that users are allowed to submit queries (i.e., they’re paying customers) without their backend service being able to know which customer is performing the query.

This involves vending buckets of single-use tokens constructed out of blind signatures to their users.

We could do something similar here for verifying that a user is 18 or older. We would need existing identity verification services (e.g., ID.me in the USA) to vend PrivacyPass tokens that can be redeemed on third party websites.

Then, the onus is on those services to verify your identity. Later, when a porn site inevitably gets hacked, this will not give the attacker any information about users’ real identities.

This is a much more robust approach than outsourcing the identity document verification to a third-party company and hoping for the best.

## Closing Thoughts

Although I keep the art on this blog 100% worksafe, I do not buy into the false narratives about pornography’s supposed harms.

(Also:porn addiction isn’t a real thing, and anyone who calls themselves a “porn addict” is either misinformed or outright lying because that’s not how addiction works.Further reading.)

If we’re going to require adult content be gatekept by some age verification mechanism, we should at least implement it securely in a way that respects user privacy.

Reject any technology that doesn’t respect user privacy.VPN services aren’t a real security tool like their marketing claims imply them to be, but they can be useful for circumventing these regional restrictions.

However, I will not recommend any in particular, and no VPN company on Earth could possibly pay me enough money to endorse them.

I refuse to monetize this blog.

Header art byCMYKat.

* Tagsage verification,anti-porn censorship,cryptography,Politics,Society,Technology,UK Online Safety Act,zero-knowledge,zero-knowledge proofs



## By Soatok

Security engineer with a fursona. Ask me about dholes or Diffie-Hellman!

			View Archive
→
