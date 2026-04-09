---
title: Claude Code Can Debug Low-level Cryptography
url: https://words.filippo.io/claude-debugging/
site_name: hackernews
fetched_at: '2025-11-02T11:08:21.056226'
original_url: https://words.filippo.io/claude-debugging/
author: Bogdanp
date: '2025-11-02'
published_date: '2025-11-01T18:10:13.968231Z'
description: Surprisingly (to me) Claude Code debugged my new ML-DSA implementation faster than I would have, finding the non-obvious low-level issue that was making Verify fail.
---

1 Nov 2025

# Claude Code Can Debug Low-level Cryptography

Over the past few days I wrote a new Go implementation of ML-DSA, a post-quantum signature algorithm specified by NIST last summer. Ilivecodedit all over four days, finishing it on Thursday evening. Except… Verify was always rejecting valid signatures.

$ bin/go test crypto/internal/fips140/mldsa
--- FAIL: TestVector (0.00s)
 mldsa_test.go:47: Verify: mldsa: invalid signature
 mldsa_test.go:84: Verify: mldsa: invalid signature
 mldsa_test.go:121: Verify: mldsa: invalid signature
FAIL
FAIL crypto/internal/fips140/mldsa 2.142s
FAIL

I was exhausted, so I tried debugging for half an hour and then gave up, with the intention of coming back to it the next day with a fresh mind.

On a whim, I figured I would let Claude Code take a shot while I read emails and resurfaced from hyperfocus. I mostly expected it to flail in some maybe-interesting way, or rule out some issues.

Instead, it rapidly figured out a fairly complex low-level bug in my implementation of a relatively novel cryptography algorithm. I am sharing this because it made me realize I still don’t have a good intuition for when to invoke AI tools, and because I think it’s a fantastic case study for anyone who’s still skeptical about their usefulness.

Full disclosure: Anthropic gave me a few months of Claude Max for free. They reached out one day and told me they were giving it away to some open source maintainers. Maybe it’s a ploy to get me hooked so I’ll pay for it when the free coupon expires. Maybe they hoped I’d write something like this. Maybe they are just nice. Anyway, they made no request or suggestion to write anything public about Claude Code. Now you know.

## Finding the bug

I started Claude Code v2.0.28 with Opus 4.1 and no system prompts, and gave it the following prompt (typos included):

I implemented ML-DSA in the Go standard library, and it all works except that verification always rejects the signatures. I know the signatures are right because they match the test vector.

YOu can run the tests with “bin/go test crypto/internal/fips140/mldsa”

You can find the code in src/crypto/internal/fips140/mldsa

Look for potential reasons the signatures don’t verify. ultrathink

I spot-checked and w1 is different from the signing one.

To my surprise, it pinged me a few minutes later witha complete fix.

Maybe I shouldn’t be surprised! Maybe it would have been clear to anyone more familiar with AI tools that this was a good AI task: a well-scoped issue with failing tests. On the other hand, this is a low-level issue in a fresh implementation of a complex,relatively novelalgorithm.

It figured out that I had mergedHighBitsandw1Encodeinto a single function for using it from Sign, and then reused it from Verify whereUseHintalready produces the high bits, effectively taking the high bits of w1 twice in Verify.

Looking atthe log, it loaded the implementation into the context and thenimmediatelyfigured it out, without any exploratory tool use! After that it wrote itself a cute little test that reimplemented half of verification to confirm the hypothesis, wrote a mediocre fix, and checked the tests pass.

Ithrew the fix awayand refactoredw1Encodeto take high bits as input, and changed the type of the high bits, which is both clearer and saves a round-trip through Montgomery representation. Still, this 100% saved me a bunch of debugging time.

## A second synthetic experiment

On Monday, I had also finished implementing signing with failing tests. There were two bugs, which I fixed in the following couple evenings.

The first one was due tosomehow computing a couple hardcoded constants (1 and -1 in the Montgomery domain) wrong. It was very hard to find, requiring a lot of deep printfs and guesswork. Took me maybe an hour or two.

The second one was easier:a value that ends up encoded in the signature was too short (32 bits instead of 32 bytes). It was relatively easy to tell because only the first four bytes of the signature were the same, and then the signature lengths were different.

I figured these would be an interesting way to validate Claude’s ability to help find bugs in low-level cryptography code, so I checked out the old version of the change with the bugs (yay Jujutsu!) and kicked off a fresh Claude Code session with this prompt:

I am implementing ML-DSA in the Go standard library, and I just finished implementing signing, but running the tests against a known good test vector it looks like it goes into an infinite loop, probably because it always rejects in the Fiat-Shamir with Aborts loop.

You can run the tests with “bin/go test crypto/internal/fips140/mldsa”

You can find the code in src/crypto/internal/fips140/mldsa

Figure out why it loops forever, and get the tests to pass. ultrathink

It spentsome time doing printf debugging and chasing down incorrect values very similarly to how I did it, and then figured out and fixed the wrong constants. Took Claude definitely less than it took me. Impressive.

It gave up after fixing that bug even if the tests still failed, so I started a fresh session (on the assumption that the context on the wrong constants would do more harm than good investigating an independent bug), and gave it this prompt:

I am implementing ML-DSA in the Go standard library, and I just finished implementing signing, but running the tests against a known good test vector they don’t match.

You can run the tests with “bin/go test crypto/internal/fips140/mldsa”

You can find the code in src/crypto/internal/fips140/mldsa

Figure out what is going on. ultrathink

It took a couple wrong paths, thought for quite a bit longer, and then found this one too. I honestly expected it to fail initially.

It’s interesting how Claude found the “easier” bug more difficult. My guess is that maybe the large random-looking outputs of the failing tests did not play well with its attention.

The fix it proposed was updating only the allocation’s length and not its capacity, but whatever, the point is finding the bug, and I’ll usually want to throw away the fix and rewrite it myself anyway.

Three out of three one-shot debugging hits with no help isextremely impressive. Importantly, there is no need to trust the LLM or review its output when its job is just saving me an hour or two by telling me where the bug is, for me to reason about it and fix it.

As ever, I wish we had better tooling for using LLMs which didn’t look like chat or autocomplete or “make me a PR.” For example, how nice would it be if every time tests fail, an LLM agent was kicked off with the task of figuring out why, and only notified us if it did before we fixed it?

For more low-level cryptographybugsimplementations, follow me on Bluesky at@filippo.abyssdomain.expertor on Mastodon at@filippo@abyssdomain.expert. I promise I almost never post about AI.

## The picture

Enjoy the silliest floof. Surely this will help redeem me in the eyes of folks who consider AI less of a tool and more of something to be hated or loved.

My work is made possible byGeomys, an organization of professional Go maintainers, which is funded bySmallstep,Ava Labs,Teleport,Tailscale, andSentry. Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in theGeomys announcement.)
Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing.Teleport Identityis designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We atAva Labs, maintainer ofAvalancheGo(the most widely used client for interacting with theAvalanche Network), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.
