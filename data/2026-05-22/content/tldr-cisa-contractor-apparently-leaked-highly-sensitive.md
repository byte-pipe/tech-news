---
title: CISA contractor apparently leaked 'highly sensitive' government AWS keys on Github | TechRadar
url: https://www.techradar.com/pro/security/cisa-contractor-apparently-leaked-highly-sensitive-government-aws-keys-on-github
site_name: tldr
content_file: tldr-cisa-contractor-apparently-leaked-highly-sensitive
fetched_at: '2026-05-22T11:58:14.833998'
original_url: https://www.techradar.com/pro/security/cisa-contractor-apparently-leaked-highly-sensitive-government-aws-keys-on-github
date: '2026-05-22'
published_date: '2026-05-19T15:20:00Z'
description: One of the most egregious government data leaks in recent history
tags:
- tldr
---

(Image credit: Image: Generated with Google Gemini)

* Copy link
* Facebook
* X
* Whatsapp
* Reddit
* Pinterest
* Flipboard
* Threads
* Email

Share this article

0

Join the conversation

Follow us

Add us as a preferred source on Google

Newsletter

Subscribe to our newsletter

* A public GitHub repository called “Private‑CISA” exposed highly sensitive internal credentials and systems used by the US Cybersecurity and Infrastructure Security Agency
* Security researchers confirmed the authenticity of the leak, describing it as one of the worst government data exposures they had ever seen
* The repository, maintained by contractor Nightwing, was eventually locked down, with CISA pledging safeguards to prevent future incidents

Researchers have revealed details on what they called, “one of the most egregious government data leaks in recent history” involving some potentially incredibly sensitive US government information.

Security researcher Guillaume Valadon reached out toKrebsOnSecurityto help contact a person in charge of a public GitHub repository.

This person, who was not responding to messages, was operating a GitHub repository called “Private-CISA” which contained, among other things:

Latest Videos From
* AWS GovCloud administrative credentials for three accounts
* AWS access keys
* AWS tokens (including “importantAWStokens” file)
* Plaintextusernames and passwordsfor internal CISA systems
* “AWS-Workspace-Firefox-Passwords.csv” containing login credentials
* Credentials for internal system “LZ-DSO” (Landing Zone DevSecOps)
* Internal CISA/DHS system authentication credentials
* Credentials for internal Artifactory (software repository)
* SSH keys exposed in a public repository

## "The worst leak in my career"

Valadon said the archive detailed how CISA builds and deploys software internally and that, in general, it is “the worst leak that I’ve witnessed in my career.”

In a letter shared withKrebsOnSecurity, Valadon said he first thought the entire database was fake, given the sensitivity of the files found inside. “It is obviously an individual’s mistake, but I believe that it might reveal internal practices,” he said.

Multiple security researchers confirmed the authenticity of the leak and said that at least some of the credentials found inside worked. They managed to get the repository locked down after getting in touch with the US Cybersecurity and Infrastructure Security Agency (CISA), who confirmed it was looking into the matter:

“Currently, there is no indication that any sensitive data was compromised as a result of this incident,” the CISA spokesperson allegedly wrote. “While we hold our team members to the highest standards of integrity and operational awareness, we are working to ensure additional safeguards are implemented to prevent future occurrences.”

Are you a pro? Subscribe to our newsletter

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

The researchers later established that the repository was maintained by a government contractor called Nightwing, which declined to comment and directed all inquiries to CISA. It is unknown for how long the repository remained open, but it was created in mid-November 2025, and chances are it was unlocked since inception.

The best antivirus for all budgets

➡️Read our full guide to the best antivirus1. Best overall:Bitdefender Total Security2. Best for families:Norton 360 with LifeLock3. Best for mobile:McAfee Mobile Security

 

Follow TechRadar on Google Newsandadd us as a preferred sourceto get our expert news, reviews, and opinion in your feeds.

Sead Fadilpašić

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

View More

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

Logout

LATEST ARTICLES
1. 1Google I/O 2026 live — Gemini upgrades, Android XR, and more of what to expect from today's big software showcase
2. 2World of Tanks: HEAT, Wargaming's new standalone and free-to-play tactical vehicle shooter, officially launches later this month
3. 3Worried about the future of the internet? Tor launches crypto-powered fundraising initiative to secure internet freedoms — and your vote matters more than your wallet size
4. 4Streamline your checkout with 15% off Square POS hardware at Best Buy
5. 5Miniature cameras are trending, and you can't get smaller than these 9 digital models — and they all cost under $50