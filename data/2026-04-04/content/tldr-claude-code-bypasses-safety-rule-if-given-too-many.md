---
title: Claude Code bypasses safety rule if given too many commands • The Register
url: https://www.theregister.com/2026/04/01/claude_code_rule_cap_raises/
site_name: tldr
content_file: tldr-claude-code-bypasses-safety-rule-if-given-too-many
fetched_at: '2026-04-04T11:11:43.578535'
original_url: https://www.theregister.com/2026/04/01/claude_code_rule_cap_raises/
date: '2026-04-04'
description: Claude Code bypasses safety rule if given too many commands (3 minute read)
tags:
- tldr
---

#### AI + ML

# Claude Code bypasses safety rule if given too many commands

 

## A hard-coded limit on deny rules drops automatic enforcement for concatenated commands

UpdatedClaude Code will ignore its deny rules, used to block risky actions, if burdened with a sufficiently long chain of subcommands. This vuln leaves the bot open to prompt injection attacks.

Adversa, a security firm based in Tel Aviv, Israel, spotted the issue following the leak of Claude Code's source.

Claude Code implements various mechanisms for allowing and denying access to specific tools. Some of these, like curl, which enables network requests from the command line, might pose a security risk if invoked by an over-permissive AI model.

One way the coding agent tries to defend against unwanted behavior is through deny rules that disallow specific commands. For example, to prevent Claude from using curl via~/.claude/settings.json, you'd add something like{ "deny": ["Bash(curl:*)"] }.

But deny rules have limits. The source code file bashPermissions.ts contains a comment that references an internal Anthropic issue designated CC-643. The associated note explains that there's a hard cap of 50 on security subcommands, set by the variableMAX_SUBCOMMANDS_FOR_SECURITY_CHECK = 50. After 50, the agent falls back on asking permission from the user. The comment explains that 50 is a generous allowance for legitimate usage.

"The assumption was correct for human-authored commands," the Adversa AI Red Team said in awriteupprovided ahead of publication toThe Register. "But it didn't account for AI-generated commands from prompt injection – where a malicious CLAUDE.md file instructs the AI to generate a 50+ subcommand pipeline that looks like a legitimate build process."

The Adversa team's proof-of-concept attack was simple. They created a bash command that combined 50 no-op "true" subcommands and a curl subcommand. Claude asked for authorization to proceed instead of denying curl access outright.

* Claude Code source leak reveals how much info Anthropic can hoover up about you and your system
* Don't open that WhatsApp message, Microsoft warns
* Ruby Central report reopens wounds over RubyGems repo takeover
* One in seven Americans are ready for an AI boss, but they might not trust it

In scenarios where an individual developer is watching and approving coding agent actions, this rule bypass might be caught. But often developers grant automatic approval to agents (--dangerously-skip-permissions mode) or just click through reflexively during long sessions. The risk is similar in CI/CD pipelines that run Claude Code in non-interactive mode.

Ironically, Anthropic has developed a fix – a parser referred to as "tree-sitter" that's also evident in its source code and is available internally but not in public builds.

Adversa argues that this is a bug in the security policy enforcement code, one that has regulatory and compliance implications if not addressed.

A fix would be easy. Anthropic already has "tree-sitter" working internally and a simple one line change, switching the "behavior" key from "ask" to "deny" in the bashPermissions.ts file at line 2174, would address this particular vulnerability.

Anthropic did not immediately respond to a request for comment. ®

### Updated on April 2 to add:

After this story was filed, Adversa said that the vulnerability appears to have been fixed without notice in the newly releasedClaude Code v2.1.90.

 

Get our
 
Tech Resources

Share

#### More about

* AI
* Claude
* Development

More like these

×

### More about

* AI
* Claude
* Development
* Security
* Software

### Narrower topics

* 2FA
* Accessibility
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
* Devops
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

* Anthropic
* Self-driving Car

#### More about

Share

#### More about

* AI
* Claude
* Development

More like these

×

### More about

* AI
* Claude
* Development
* Security
* Software

### Narrower topics

* 2FA
* Accessibility
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
* Devops
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

* Anthropic
* Self-driving Car

#### TIP US OFF

Send us news