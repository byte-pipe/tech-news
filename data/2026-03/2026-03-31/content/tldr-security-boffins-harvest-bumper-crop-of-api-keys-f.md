---
title: Security boffins harvest bumper crop of API keys from web • The Register
url: https://www.theregister.com/2026/03/27/security_boffins_harvest_bumper_crop
site_name: tldr
content_file: tldr-security-boffins-harvest-bumper-crop-of-api-keys-f
fetched_at: '2026-03-31T11:22:26.596983'
original_url: https://www.theregister.com/2026/03/27/security_boffins_harvest_bumper_crop
date: '2026-03-31'
description: API keys all over the web (3 minute read)
tags:
- tldr
---

#### Research

# Security boffins scoured the web and found hundreds of valid API keys

 

## Global bank's devs have some cleaning up to do after cloud creds found in website code

Computer security boffins have conducted an analysis of 10 million websites and found almost 2,000 API credentials strewn across 10,000 webpages.

The researchers detail their findings in a preprintpapertitled "Keys on Doormats: Exposed API Credentials on the Web," and say they conducted the study because much of the attention on exposed credentials has focused on scouring code repositories and source code. They argue that dynamic analysis of production websites is essential to understand the scope of the problem.

"What we found were highly sensitive API credentials left publicly exposed on public webpages," Nurullah Demir, a PhD candidate at Stanford and corresponding author, toldThe Registerin an email. "These act as access tokens that authorize applications to interact with third-party services, granting direct access to critical infrastructure like cloud platforms and payment providers."

Demir contends that API credentials are even more dangerous than exposed login details because they provide programmatic access to resources.

The researchers scanned approximately 10 million websites using a tool calledTruffleHog, and found 1,748 valid credentials belonging to organizations including multinational corporations, critical infrastructure entities, and government agencies. The keys provide access to services like AWS, GitHub, Stripe, and OpenAI.

Demir said one of the affected organizations was a global bank. Another makes firmware for electronic devices.

"A 'Global Systemically Important Financial Institution' exposed its cloud credentials directly on its webpages," said Demir. "This gave direct access to multiple core cloud infrastructure services, including databases and key management systems."

* GitHub hits CTRL-Z, decides it will train its AI with user data after all
* Staff too scared of the AI axe to pick it up, Forrester finds
* Anthropic tweaks timed usage limits to discourage Claude demand during peak hours
* Using AI to code does not mean your code is more secure

The researchers also found repository credentials for a developer responsible for firmware used by various manufacturers of drones and remote-controlled devices. Attackers could use those credentials to modify source code and push malicious firmware updates to various devices, Demir said.

"Exposure is widespread across service categories, with cloud services (e.g., AWS, Cloudflare) and payment services (e.g., Stripe, Razorpay) accounting for the majority of verified credentials," the paper explains. "AWS credentials alone represent more than 16 percent of all verified exposures and were found on over 4,693 websites. Email and communication services such as SendGrid and Twilio also appear frequently, with a significant portion of their exposures originating from embedded third-party resources."

Most of the credentials the researchers found were present in JavaScript resources (84 percent), followed by HTML (eight percent) and JSON (seven percent) files. They also turned up unusual cases like a verified GitHub access token embedded in a CSS file.

In JavaScript files, 62 percent of credential exposures show up in bundles created by build tools like Webpack.

Demir said he and his co-authors – Yash Vekaria of UC Davis, Georgios Smaragdakis from TU Delft/Stanford, and Zakir Durumeric from Stanford – made a significant effort to contact affected organizations. The number of exposed credentials declined by half in about two weeks after the researchers started to report their findings.

"When we got feedback from the developers, we saw that a significant number of them were completely unaware of the exposures," he explained. "What is perhaps most concerning is that our historical analysis showed these credentials often remain exposed for an average of 12 months, in some cases for years."

Demir said that he and his co-authors only verified credentials for 14 different service providers, so the exposure figure represents a lower bound.

"We strongly believe that the actual number of exposed credentials across the web is much higher than what we captured in this study," he said. ®

 

Get our
 
Tech Resources

Share

#### More about

* Development
* Enterprise
* Security

More like these

×

### More about

* Development
* Enterprise
* Security
* Software

### Narrower topics

* 2FA
* Accessibility
* AdBlock Plus
* Advanced persistent threat
* App
* Application Delivery Controller
* Audacity
* Authentication
* BEC
* Black Hat
* BSides
* Bug Bounty
* Center for Internet Security
* CHERI
* CISO
* Common Vulnerability Scoring System
* Confluence
* Cybercrime
* Cybersecurity
* Cybersecurity and Infrastructure Security Agency
* Cybersecurity Information Sharing Act
* Database
* Data Breach
* Data Protection
* Data Theft
* DDoS
* DEF CON
* Devops
* Digital certificate
* Encryption
* End Point Protection
* Exploit
* Firewall
* FOSDEM
* FOSS
* Google Project Zero
* Grab
* Graphics Interchange Format
* Hacker
* Hacking
* Hacktivism
* IDE
* Identity Theft
* Image compression
* Incident response
* Infosec
* Infrastructure Security
* Jenkins
* Kenna Security
* Legacy Technology
* LibreOffice
* Map
* Microsoft 365
* Microsoft Office
* Microsoft Teams
* Mobile Device Management
* NCSAM
* NCSC
* OpenOffice
* Palo Alto Networks
* Password
* Personally Identifiable Information
* Phishing
* Programming Language
* QR code
* Quantum key distribution
* Ransomware
* Remote Access Trojan
* Retro computing
* REvil
* Rimini Street
* RSA Conference
* Search Engine
* Software Bill of Materials
* Software bug
* Software License
* Spamming
* Spyware
* Surveillance
* Text Editor
* TLS
* Trojan
* Trusted Platform Module
* User interface
* Visual Studio
* Visual Studio Code
* Vulnerability
* Wannacry
* WebAssembly
* Web Browser
* WordPress
* Zero trust

#### More about

Share

#### More about

* Development
* Enterprise
* Security

More like these

×

### More about

* Development
* Enterprise
* Security
* Software

### Narrower topics

* 2FA
* Accessibility
* AdBlock Plus
* Advanced persistent threat
* App
* Application Delivery Controller
* Audacity
* Authentication
* BEC
* Black Hat
* BSides
* Bug Bounty
* Center for Internet Security
* CHERI
* CISO
* Common Vulnerability Scoring System
* Confluence
* Cybercrime
* Cybersecurity
* Cybersecurity and Infrastructure Security Agency
* Cybersecurity Information Sharing Act
* Database
* Data Breach
* Data Protection
* Data Theft
* DDoS
* DEF CON
* Devops
* Digital certificate
* Encryption
* End Point Protection
* Exploit
* Firewall
* FOSDEM
* FOSS
* Google Project Zero
* Grab
* Graphics Interchange Format
* Hacker
* Hacking
* Hacktivism
* IDE
* Identity Theft
* Image compression
* Incident response
* Infosec
* Infrastructure Security
* Jenkins
* Kenna Security
* Legacy Technology
* LibreOffice
* Map
* Microsoft 365
* Microsoft Office
* Microsoft Teams
* Mobile Device Management
* NCSAM
* NCSC
* OpenOffice
* Palo Alto Networks
* Password
* Personally Identifiable Information
* Phishing
* Programming Language
* QR code
* Quantum key distribution
* Ransomware
* Remote Access Trojan
* Retro computing
* REvil
* Rimini Street
* RSA Conference
* Search Engine
* Software Bill of Materials
* Software bug
* Software License
* Spamming
* Spyware
* Surveillance
* Text Editor
* TLS
* Trojan
* Trusted Platform Module
* User interface
* Visual Studio
* Visual Studio Code
* Vulnerability
* Wannacry
* WebAssembly
* Web Browser
* WordPress
* Zero trust

#### TIP US OFF

Send us news