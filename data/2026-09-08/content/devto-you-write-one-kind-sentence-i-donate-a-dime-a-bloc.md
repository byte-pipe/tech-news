---
title: You write one kind sentence. I donate a dime. A blockchain makes sure I do. - DEV Community
url: https://dev.to/nazar-boyko/you-write-one-kind-sentence-i-donate-a-dime-a-blockchain-makes-sure-i-do-f5o
site_name: devto
content_file: devto-you-write-one-kind-sentence-i-donate-a-dime-a-bloc
fetched_at: '2026-09-08T21:34:49.089421'
original_url: https://dev.to/nazar-boyko/you-write-one-kind-sentence-i-donate-a-dime-a-blockchain-makes-sure-i-do-f5o
author: Nazar Boyko
date: '2026-09-06'
description: 'This is a submission for the DEV Weekend Challenge: Generosity Edition. What I... Tagged with devchallenge, weekendchallenge, solana, go.'
tags: '#devchallenge, #weekendchallenge, #solana, #go'
---

DEV Weekend Challenge: Generosity Edition Submission 💜

This is a submission for theDEV Weekend Challenge: Generosity Edition.

## What I Built

Kindness Chain is one page. You write one sentence about a kind thing you did or will do today, add your name if you want, and click "Add my link". Your sentence appears in the feed, then flips to "confirmed" with a link to Solana Explorer, because it was just written to the Solana devnet as an SPL Memo transaction. Every memo carries the signature of the memo before it, so the feed is a chain anyone can walk with a block explorer. For every confirmed link I donate ten cents to the International Institute of Minnesota, up to fifty dollars. The pledge itself is link #0, written on the chain before anything else, and the count of links after it is the number I owe.

No signup, no wallet, no cookies. The visit takes thirty seconds.

The why is personal. My family arrived in Minnesota in 2023. We landed in Newark on February 28, 2023 and were in Minnesota the next day. We did not have an apartment of our own until March 20. For those first three weeks a family we had never met before gave us rooms, drove us to appointments, and explained things nobody writes down: which documents to carry, how the school bus works, which store is worth the trip. Nobody was paid for any of it. Organisations like the International Institute of Minnesota, which resettles refugees and helps immigrants with language, jobs and legal questions, are the difference between a family that lands and a family that stays lost for a year. I wanted the challenge weekend to send them something, and I wanted the sending to be checkable rather than a promise in a post. So the money is tied to what strangers write, and the writing is on a public ledger that I cannot quietly edit.

## Demo

Try it:https://kindness-chain.fly.dev

The pledge is link #0:3q5P2tY6kc2Y7tSMUcb9q5WcDZmaZPhv73PDWK2a3mAWBLVYHgvUXHjaFZcTFi99sdiLyVYhxru2h43ErYri5W54. Open it and read the memo: the sentence is the promise, worded from the same configuration that draws the counter on the page. Every memo the signer account ever wrote is listed onits address page, which is the whole audit: count the memos after #0.

### Verify it without my site

One command walks the chain from the head back to the pledge using only the RPC node, checks that everyprevmatches, and prints what I owe:

go run ./cmd/walkchain

Enter fullscreen mode

Exit fullscreen mode

#4 Nazar Made a small public promise to refugees in Minnesota, and b… 4Pc7xziBVEKrzs4oZVJWzaPZYKhcvKMgEr2M2okRKbfGk4wKpfk6Gh3ceK31KYsSTK4ncRpX9Ty8Hg7cDo5Cpdbx
#3 ++ Walked a stranger at the grocery store to the aisle they co… NDLUQocnFQJMZBQxZzhWUBetFZ9kBdytKwT2qNqehrMP9TWN9Bo4hyyPsY4VLXC7xMessRRx6JGmG4tEdqEdzzi
#2 Anonymous Ran the full deploy check on this chain from the command li… 2FcFZPEWZ3GKYiaVzV4y8bPgN48FyfMTfc3zWcivC9UmsQPgeVpCGmUy1d5ar1HvEfLXciGpX6XKCQ6B89vjZEE1
#1 Nazar Spent the last few months helping a friend's small company … 394BGKjQGMSdwHFEVx8dC1fA6e1txYSHCGiFBeD2WEf5umr3YuczZxRVGJHRHChJCYNpQBmNah28bRPzB284KE7w
#0 Nazar I, Nazar, pledge $0.10 for every link added to this chain, … 3q5P2tY6kc2Y7tSMUcb9q5WcDZmaZPhv73PDWK2a3mAWBLVYHgvUXHjaFZcTFi99sdiLyVYhxru2h43ErYri5W54

4 links after the pledge, $0.40 owed of $50 at $0.10 per link
every prev matched: yes, the chain runs back to the pledge at #0
the site reports 4 confirmed links, the same

Enter fullscreen mode

Exit fullscreen mode

If that number and the counter on the page ever disagree, the chain is right and I am wrong.

## Code

## nazboyko/kindness-chain

# Kindness Chain

One sentence from you. One dime from me. Verified on-chain.

Live:https://kindness-chain.fly.dev

Anyone can add one sentence about a kind thing they did or will do today, with no signup and no wallet. Each sentence becomes a link on Solana devnet: an SPL Memo transaction whose JSON carries the signature of the link before it, so the whole chain can be walked and counted by anyone. For every confirmed link I donate $0.10 to theInternational Institute of Minnesota, up to $50, and the chain is the receipt.

## Verify the chain yourself

go run ./cmd/walkchain

That reads the chain head and the pledge terms from the live site, then talks only to a Solana RPC node: it fetches each memo, followsprevback togenesis, prints one line per link, and adds up what I owe. Pass a signature to start from a different link,-rpc…

View on GitHub

Go standard library for the server, one SQLite file, React for the page, one binary on one Fly.io machine. Everything was written between Saturday night and Sunday evening; the tag v0.1.0-challenge marks the exact state at the deadline. 10 commits inside the window, 94 Go tests, all of them against a fake ledger so the suite never touches the network.

## How I Built It

The chain is sequential on purpose.A memo can only point at a signature that exists, so links have to be written one after another. There is one worker goroutine. It takes links in order, reads the signature of the last confirmed link, builds the memo, sends one SPL Memo v2 transaction, waits for the cluster to report it confirmed, and only then records the signature and moves on. Confirmation on devnet takes one to two seconds, which is also how long "confirming on-chain" shows in the feed before it flips.

The memo is the row.Six fields in a fixed order, andtis the moment the visitor added the link, not the moment the worker got to it:

{
"v"
:
1
,
"n"
:
2
,
"act"
:
"Ran the full deploy check on this chain from the command line, so every link after this one lands where it should."
,
"by"
:
""
,
"prev"
:
"394BGKjQGMSdwHFEVx8dC1fA6e1txYSHCGiFBeD2WEf5umr3YuczZxRVGJHRHChJCYNpQBmNah28bRPzB284KE7w"
,
"t"
:
"2026-09-06T05:13:32Z"
}

Enter fullscreen mode

Exit fullscreen mode

Because the bytes are a pure function of the stored row,/api/verify/{n}can fetch the transaction, decode the memo instruction and compare it with the database field by field. The Verify button on every link does exactly that and shows both sides. A memo has to fit one instruction, 566 bytes, and a 200 character sentence in a wide script plus JSON escaping can get there, so the size is checked at submission time and refused with a sentence, not discovered by the worker later. One number I did not expect: a 440 byte memo transaction used 109,096 of 200,000 compute units, because the memo program logs what it writes.

SQLite is the truth, Solana is the proof.The database holds every link, its status, and the memo that was sent. That split is what makes failure boring. A send that fails for network reasons keeps the link pending and retries with a growing delay; after three failures in a row the page shows the chain as paused, and nothing is lost. A transaction the cluster rejects for good marks that one link failed and the next link chains to the last one that did land. A restart re-queues every pending link. And when the machine is asked to stop, a memo in flight is allowed to finish, because a memo that reached the cluster but was never recorded would be sent again on the next start.

Anti-abuse without accounts.There is no login, so seven small layers do the work: sentence rules (10 to 200 characters, no URLs, a short blocklist), a honeypot field that gets a convincing fake 202, proof of work in the browser, duplicate detection, three links an hour per address, ten links a minute chain-wide, and a queue that refuses beyond a thousand waiting links. The proof of work is the interesting one.GET /api/challengehands out a seed; the page finds a nonce so that SHA-256 of seed, nonce and sentence starts with 18 zero bits, with the Web Crypto API and no library. That is about 262,000 hashes on average, half a second on a laptop and a second or two on a phone, behind a "Sealing your link" message most people will not have time to read. The honest part: a script solves the same puzzle in a fraction of a second, so the proof of work is a speed bump and the throttles are the wall. The pledge cap is the financial backstop. Past 500 confirmed links the chain keeps growing and the donation stops at $50, so the worst a spammer can do is cost me fifty dollars and fill a feed that shows every sentence to everyone.

Live without polling.One server-sent event stream per open tab. It sends the current stats on connect, then alinkevent and astatsevent after every confirmation, with a comment every 25 seconds to keep proxies from closing it. The browser reconnects by itself and refetches the first page after a gap, so a phone that was in a pocket for an hour shows the right numbers the moment it wakes. I added link #1 from a phone on LTE and watched it land on the desktop feed.

The whole page on a phone, down to the newest link.

Verify reads the memo back from the cluster and shows both sides.

The page.I wanted it to look like a ledger, because that is what it is. The paper is the pale green that accounting ledger paper was printed on, the sentences are set in Alegreya, the counts and signatures in IBM Plex Mono, and the feed is a numbered thread with a line running from the newest link down to the pledge. One accent colour. The counter rolls when a link confirms, and nothing moves for people who asked their system for reduced motion. The JavaScript bundle is 66 KB gzipped and the fonts are split by script, so Cyrillic glyphs only load when someone writes in Cyrillic.

### What I cut and why

* Accounts and wallet sign-in.The whole point is that a person with no crypto knowledge can add a link in thirty seconds. A server-side key signs everything, and the cost of that choice is trust in me, which is why every memo is public and comparable.
* Mainnet.Devnet is free and instant, and this is a proof of concept of a ledger, not a contract. Devnet can be reset by Solana at any time; if it is, older explorer links stop resolving, the database keeps every link, and verify says so. I would rather say that plainly than pay for permanence on a weekend.
* Relay mechanics, likes, comments, leaderboards.The feed is the product. Anything that ranks sentences turns kindness into a contest.
* Moderation by a model.A whole-word blocklist, duplicate detection and human eyes on a public feed. A model deciding what counts as kind would be a stranger deciding, and a slow one.
* A second keypair for tests.The signer account carries one smoke-test memo from before link #0. The chain starts at #0, withprevset togenesis, and I wrote that down instead of hiding it.

### Dependencies and credits

Go 1.26 standard library,modernc.org/sqlitefor a pure Go SQLite, andsolana-gofor the RPC client, transaction building and the SPL Memo instruction.React19,Vite8,TypeScript7 andTailwind CSS4 on the page.AlegreyaandIBM Plex, self-hosted through Fontsource.Fly.iofor one machine and one volume. The tagv0.1.0-challengemarks the repository at the deadline; anything after it is listed in the README.

## Prize Categories

Best Use of Solana.The chain is not decoration on a donation page. It is the ledger the donation is computed from. Each link is an SPL Memo transaction whose JSON names the previous link's signature, the pledge is link #0, and the signer's address page lists every memo ever written, so anyone can count the links and hold me to the number without trusting my database or my counter. The verify endpoint closes the loop in the other direction: it reads a memo back from the cluster and compares it with what was stored, field by field, and the page shows both. Solana is what makes the promise checkable by a stranger, and devnet is what made it free to try on a weekend.

## What happens next

After the deadline I will make the donation and post the receipt from the International Institute of Minnesota as an update to this post, with the final count of links. The chain will keep accepting sentences after the cap; the donation stops at $50 and the feed does not.

If you have thirty seconds, add a link:https://kindness-chain.fly.dev. Write the small thing. It counts.

Thanks for reading! English isn't my first language, so I use AI to polish the grammar.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse