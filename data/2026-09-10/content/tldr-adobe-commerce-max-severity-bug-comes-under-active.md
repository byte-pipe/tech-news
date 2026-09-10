---
title: Adobe Commerce max-severity bug comes under active attack | CSO Online
url: https://www.csoonline.com/article/4219626/adobe-commerce-max-severity-bug-comes-under-active-attack.html
site_name: tldr
content_file: tldr-adobe-commerce-max-severity-bug-comes-under-active
fetched_at: '2026-09-10T21:24:32.955103'
original_url: https://www.csoonline.com/article/4219626/adobe-commerce-max-severity-bug-comes-under-active-attack.html
date: '2026-09-10'
description: Attackers are exploiting the critical StyleSmuggler flaw to execute code without authentication and plant stealthy backdoors on vulnerable online stores.
tags:
- tldr
---

by									
Shweta Sharma

Senior Writer

# Adobe Commerce max-severity bug comes under active attack

News

Sep 8, 2026
4 mins

Online stores running Adobe Commerce and Magento Open Source have been hit by a max-severity, zero-day bug that lets unauthenticated attackers execute code on vulnerable servers.

Security firm Sansec is calling the flaw StyleSmuggler because of the way attackers abused Magento’s Style properties to inject malicious code past existing safeguards.

“When the attack succeeds, a backdoor background process is launched. This is a small Rust program that connects to the 99.84.67.186 C2 server and waits for commands,” Sansec researchers said in a blogpost, adding that the backdoor had not been weaponized at the time of writing.

The flaw, tracked asCVE-2026-75650, carries a CVSS score of 10.0 and affects Magento and Adobe Commerce versions 2.4.4 through 2.4.9. Magento is the open-source edition of an e-commerce platform used to build and operate online stores. Adobe Commerce is the commercial/enterprise version of Magento. Adobe acquired Magento in 2018.

According to Sansec, exploitation began on September 4, with the first confirmed attack recorded at 22:20 UTC. The company reproduced the complete unauthenticated attack chain against clean Magento Open Source installations running versions 2.4.7, 2.4.8, and 2.4.9.

One victim was running 2.4.6-p15 with both July and August security updates installed, the researchers noted.

Adobe has released an emergency hotfix,VULN-393411, for the vulnerability. But because attackers had three days to exploit the flaw before a fix arrived, Sansec warns that patching alone isn’t enough for stores that may already have been compromised.

## Attack triggered through failed payment email

StyleSmuggler’s first trick is to get malicious PHP code into data that Magento itself will write out, such as a payment failure report. “StyleSmuggler deliberately triggers Magento’s standard ‘Payment Transaction Failed Reminder’email,” the researchers explained. “Unexpected bursts of these messages are a reason to investigate, although legitimate declined payments can generate the same notification.”

The attackers abuse Magento’s template processing by passing specially crafted “styles properties,” allowing the poisoned data, the injected PHP code, to execute on the server.

The customer doesn’t have to open the email, the researchers pointed out. The code executes while Magento renders the message, meaning the attack can succeed even if delivery of the email subsequently fails.

Once execution is achieved, the attacker moves on to a small Rust-based backdoor being launched as a background process. The implant was seen adopting names such as “[kworker/u:8:0]” and “fc-cache,” non-suspicious to a human eye.

## The backdoor is not weaponized, yet

The Rust implant establishes command-and-control communication and uses persistence mechanisms, includingcron jobs. The fc-cache variant copied itself into the fontconfig cache directory and scheduled itself to restart twice an hour. Its C2 traffic was disguised as NTP traffic over UDP port 123, an attempt to make malicious communications blend into routine system activity, the researchers noted.

Sansec says it has not yet seen evidence that this backdoor was actually weaponized after installation. But the investigation revealed that another attacker was already exploiting the same StyleSmuggler access.

On September 7, Samsec found a separate 485-byte PHP dropper that used the vulnerability to deploy a web shell inside Magento’s product-image cache. The shell could execute PHP commands when supplied with the correct header, giving the second operator a foothold independent of the Rust implant.

The researchers recommended checking for unexpected PHP files under “pub/media,” while also looking for the known malicious processes, cron entries, and other indicators of compromise. Adobe’s emergency hotfix closes the vulnerability, but stores feared to be exposed should scan for implants and secondary backdoors and rotate potentially compromised credentials and secrets.

Vulnerabilities
Security
Zero-Day Vulnerabilities
 

 

														by 															

																Shweta Sharma															

Senior Writer

1. Follow Shweta Sharma on X
2. Follow Shweta Sharma on LinkedIn

Shweta has been writing about enterprise technology since 2017, most recently reporting on cybersecurity for CSO online. She breaks down complex topics from ransomware to zero trust architecture for both experts and everyday readers. She has a postgraduate diploma in journalism from the Asian College of Journalism, and enjoys reading fiction, watching movies, and experimenting with new recipes when she’s not busy decoding cyber threats.

## More from this author

* news### Stealth rootkit targeting F5 BIG-IP could expose enterprise identity gatewaysSep 10, 20264 mins
* news### ShinyHunters claims Florida DMV breach, puts data on the clockSep 9, 20264 mins
* news### Back-to-back N-able bugs send admins on a patching spreeSep 7, 20264 mins
* news### Decade-old PostgreSQL flaw turns backup account into a backdoorSep 3, 20264 mins
* news### Exploited JFrog Artifactory bug puts software supply chain on alertSep 2, 20263 mins
* news### Fake Cloudflare CAPTCHA tricks victims into opening a tunnel for attackersSep 1, 20263 mins
* news### AI can be made to read an email much differently than you doAug 27, 20264 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

news
 
 

### AI workflows may be creating a dangerous new authorization blind spot

 
By Gyana Swain
Sep 10, 2026
5 mins

Access Control
Authentication
Identity and Access Management

opinion
 
 

### The longitude problem: In the AI era, detection is won on facts, not guesses

 
By Alan LeFort
Sep 10, 2026
6 mins

Artificial Intelligence
Data and Information Security
Security

opinion
 
 

### Getting ahead of ‘harvest-now-decrypt-later’: Post-quantum cryptography planning

 
By Ashish Mishra
Sep 10, 2026
6 mins

Data and Information Security
Encryption
Security

podcast
 
 

### Why Security Debt May Be a Bigger Risk Than Security Spend

 
By Joan Goodchild
Sep 10, 2026
16 mins

Cybercrime

podcast
 
 

### Cybersecurity on the Front Lines of Critical Infrastructure

 
By Joan Goodchild
Aug 12, 2026
10 mins

Cyberattacks

podcast
 
 

### Cloud Security at a Breaking Point: AI, Complexity, and the Future of Trust

 
By Joan Goodchild
Aug 6, 2026
17 mins

Cybercrime

video
 
 

### Why Security Debt May Be a Bigger Risk Than Security Spend

 
By Joan Goodchild
Sep 10, 2026
16 mins

Cyberattacks

video
 
 

### Cybersecurity on the Front Lines of Critical Infrastructure

 
By Joan Goodchild
Aug 12, 2026
10 mins

Cyberattacks

video
 
 

### Cloud Security at a Breaking Point: AI, Complexity, and the Future of Trust

 
By Joan Goodchild
Aug 6, 2026
17 mins

Cybercrime