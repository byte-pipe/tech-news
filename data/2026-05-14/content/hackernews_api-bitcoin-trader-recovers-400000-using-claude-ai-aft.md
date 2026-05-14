---
title: Bitcoin trader recovers $400,000 using Claude AI after getting 'stoned' and losing wallet password 11 years ago — bot tried 3.5 trillion passwords before decrypting an old wallet backup | Tom's Hardware
url: https://www.tomshardware.com/tech-industry/cryptocurrency/bitcoin-trader-recovers-usd400-000-using-claude-ai-after-losing-wallet-password-11-years-ago-bot-tried-3-5-trillion-passwords-before-decrypting-an-old-wallet-backup
site_name: hackernews_api
content_file: hackernews_api-bitcoin-trader-recovers-400000-using-claude-ai-aft
fetched_at: '2026-05-14T19:34:58.360339'
original_url: https://www.tomshardware.com/tech-industry/cryptocurrency/bitcoin-trader-recovers-usd400-000-using-claude-ai-after-losing-wallet-password-11-years-ago-bot-tried-3-5-trillion-passwords-before-decrypting-an-old-wallet-backup
author: cednore
date: '2026-05-14'
published_date: '2026-05-14T10:19:56Z'
description: The user apparently changed the password while 'stoned.'
tags:
- hackernews
- trending
---

(Image credit: Getty)

* Copy link
* Facebook
* X
* Whatsapp
* Reddit
* Pinterest
* Flipboard
* Email

Share this article

4

Join the conversation

Follow us

Add us as a preferred source on Google

Newsletter

Subscribe to our newsletter

A Bitcoin holder who changed their wallet password while 'stoned' and then forgot it was finally able to recover their wallet with the help of Claude. According to X user cprkrn, they’d been trying to recover their wallet for more than 11 years. Still, they didn’t give up because that wallet contained 5 BTC; this may not sound much, but it has a value of almost $400,000.

After finding a mnemonic that actually turned out to be their old password a few weeks ago, the user dumped their entire college computer files in Claude in a last-gasp effort. The bot uncovered an old backup wallet file that it successfully decrypted, while also uncovering a bug in the password configuration that was preventing recovery up to that point.

HOLY FUCKING SHIT OMG CLAUDE JUST CRACKED THIS SHIT, THANK YOU @AnthropicAI THANK YOU @DarioAmodei NAMING MY KID AFTER YOU 😍https://t.co/gObNirRDpS https://t.co/ByTdIM4d20 pic.twitter.com/xB5LUJb6PeMay 13, 2026

Cryptocurrency wallets during their early years were completely different beasts. Mnemonic seed phrases back then generated the HD key tree, but wallets often mixed them with non-HD and imported keys. Those cannot be recovered by the seed phrase and are stored in a wallet file that requires a password. This is what happened to cprkrn — they changed the password to the wallet file that contained some specific keys while they were stoned and then completely forgot what password they used. This meant that the Bitcoins tied to those keys were completely inaccessible, and they’ve been trying to find their way back in since then.

Latest Videos From

It seems that the user already had some candidate passwords and multiple wallets stored on their PC. They'd been trying to brute-force their way into the locked file with btcrecover, an open-source Bitcoin wallet recovery tool, but to no success. Their luck changed for the better when they found an old mnemonic seed phrase written in an old college notebook. The HD addresses recovered by the seed phrase matched those of a specific file on their computer, confirming that it was the wallet that held the 5 BTC, but it remained encrypted.

Out of frustration, cprkrn then dumped their whole college computer into Claude. This was when the AI discovered an older backup file of the wallet from December 2019 hidden in cprkrn's data. Claude also discovered an issue where the shared key and passwords that btcrecover was trying weren’t combined properly. With the bug ironed out and an older wallet predating the password change, Claude successfully ran btcrecover and was able to decrypt the private keys, allowing cprkrn to transfer the five “lost” BTC to their current wallet.

This is a happy ending for one user who forgot their wallet password, giving them a massive windfall because of Bitcoin’s massive increase in value during the past few years. And while Anthropic’s Claude did not magically guess the right set of characters to unlock the file that held the private keys, it fixed one critical issue that cprkrn missed out on, allowing him to finally regain his crypto. Before AI LLMs became popular, researchersspent at least half a year cracking open a Bitcoin walletwith a forgotten 20-character password. It was well worth the effort, though, as it contained an estimated $1.6 million in BTC back in 2024. Unfortunately, we cannot say the same thing for this poor guy who lost $780 million in Bitcoin after a 2025court ruling prevented him from attempting to rummage through the local dumpafter his laptop with 8,000 BTC was discarded in the trash.

 

FollowTom's Hardware on Google News, oradd us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

Jowi Morales
Contributing Writer

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.