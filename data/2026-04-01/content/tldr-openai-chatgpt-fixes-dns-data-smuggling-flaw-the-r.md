---
title: OpenAI ChatGPT fixes DNS data smuggling flaw • The Register
url: https://www.theregister.com/2026/03/30/openai_chatgpt_dns_data_snuggling_flaw/
site_name: tldr
content_file: tldr-openai-chatgpt-fixes-dns-data-smuggling-flaw-the-r
fetched_at: '2026-04-01T11:24:25.581353'
original_url: https://www.theregister.com/2026/03/30/openai_chatgpt_dns_data_snuggling_flaw/
date: '2026-04-01'
description: AI Data Can Slip Through DNS (3 minute read)
tags:
- tldr
---

#### Security

# OpenAI patches ChatGPT flaw that smuggled data over DNS

 

## Check Point says outbound controls blocked web traffic but overlooked DNS

OpenAI talks up data security for its AI services, yet Check Point says that ChatGPT allowed data to leak through a DNS side channel before the flaw was fixed.

In February, the free-spending AI biz fixed a data exfiltration vulnerability in ChatGPT that allowed a single prompt to bypass the notional safeguards OpenAI had put in place.

"We found that a single malicious prompt could activate a hidden exfiltration channel inside a regular ChatGPT conversation," researchers from Check Point said in ablog poston Monday.

It's not supposed to be that easy. OpenAI has implemented various safeguards around ChatGPT to limit data exfiltration by the various tools it can use. For example, the companysays, "The ChatGPT code execution environment is unable to generate outbound network requests directly."

But Check Point researchers found that wasn't entirely correct.

"The vulnerability we discovered allowed information to be transmitted to an external server through a side channel originating from the container used by ChatGPT for code execution and data analysis," the researchers said. "Crucially, because the model operated under the assumption that this environment could not send data outward directly, it did not recognize that behavior as an external data transfer requiring resistance or user mediation."

That side channel? The Domain Name System (DNS), which resolves domain names into IP addresses.

* Microsoft yanks Windows 11 preview update after install failures
* FCC says it's making it easier for US telcos to ditch legacy lines
* European Commission admits attackers broke into public web systems, but says little else
* US PC shipments to fall 13% as memory and storage crunch hits budget systems

The Check Point security bods explain that, while OpenAI prevents ChatGPT from communicating with the internet without authorization, it didn't have any controls on data smuggled via DNS.

The security biz created three proof-of-concept attacks that show how this side channel might be abused. One involved a "GPT," a third-party app implementing ChatGPT APIs, that served as a personal health analyst.

In the demonstration, a user uploaded a PDF containing laboratory results and personal information for the GPT to interpret. The app did so, and when asked whether it had uploaded the data, "ChatGPT answered confidently that it had not, explaining that the file was only stored in a secure internal location."

Nonetheless, the GPT app transmitted the data to a remote server controlled by the attacker.

Flaws like this suggest serious implications for regulated industries that deploy AI services. Were a corporate AI service to leak this sort of data, it could be a GDPR violation, a HIPAA breach, or could run afoul of various financial compliance rules.

OpenAI is said to have fixed this particular issue on February 20, 2026. The AI biz did not immediately respond to a request for comment. ®

 

Get our
 
Tech Resources

Share

#### More about

* AI
* DNS
* Security

More like these

×

### More about

* AI
* DNS
* Security
* Software

### Narrower topics

* 2FA
* AdBlock Plus
* Advanced persistent threat
* AIOps
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
* DeepSeek
* DEF CON
* Digital certificate
* Encryption
* End Point Protection
* Exploit
* Firewall
* FOSDEM
* FOSS
* Gemini
* Google AI
* Google Project Zero
* GPT-3
* GPT-4
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
* Large Language Model
* Legacy Technology
* LibreOffice
* Machine Learning
* Map
* MCubed
* Microsoft 365
* Microsoft Office
* Microsoft Teams
* Mobile Device Management
* NCSAM
* NCSC
* Neural Networks
* NLP
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
* Retrieval Augmented Generation
* Retro computing
* REvil
* RSA Conference
* Search Engine
* Software Bill of Materials
* Software bug
* Software License
* Spamming
* Spyware
* Star Wars
* Surveillance
* Tensor Processing Unit
* Text Editor
* TLS
* TOPS
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

### Broader topics

* Internet
* Self-driving Car

#### More about

Share

#### More about

* AI
* DNS
* Security

More like these

×

### More about

* AI
* DNS
* Security
* Software

### Narrower topics

* 2FA
* AdBlock Plus
* Advanced persistent threat
* AIOps
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
* DeepSeek
* DEF CON
* Digital certificate
* Encryption
* End Point Protection
* Exploit
* Firewall
* FOSDEM
* FOSS
* Gemini
* Google AI
* Google Project Zero
* GPT-3
* GPT-4
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
* Large Language Model
* Legacy Technology
* LibreOffice
* Machine Learning
* Map
* MCubed
* Microsoft 365
* Microsoft Office
* Microsoft Teams
* Mobile Device Management
* NCSAM
* NCSC
* Neural Networks
* NLP
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
* Retrieval Augmented Generation
* Retro computing
* REvil
* RSA Conference
* Search Engine
* Software Bill of Materials
* Software bug
* Software License
* Spamming
* Spyware
* Star Wars
* Surveillance
* Tensor Processing Unit
* Text Editor
* TLS
* TOPS
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

### Broader topics

* Internet
* Self-driving Car

#### TIP US OFF

Send us news