---
title: Claude Desktop changes software permissions without consent • The Register
url: https://www.theregister.com/2026/04/20/anthropic_claude_desktop_spyware_allegation/
site_name: tldr
content_file: tldr-claude-desktop-changes-software-permissions-withou
fetched_at: '2026-04-25T19:42:37.510949'
original_url: https://www.theregister.com/2026/04/20/anthropic_claude_desktop_spyware_allegation/
date: '2026-04-25'
description: Claude Desktop Changes App Access Settings For Browsers You Don't Even Have Installed Yet (3 minute read)
tags:
- tldr
---

#### Security

# Claude Desktop changes app access settings for browsers you don't even have installed yet

 

## Installation and pre-approval without consent looks dubious under EU law

One app should not modify another app without asking for and receiving your explicit consent. Yet Anthropic's Claude Desktop for macOS installs files that affect other vendors' applications without disclosure, even before those applications have been installed, and authorizes browser extensions without consent.

Alexander Hanff, a privacy consultant and occasional contributor toThe Register,contends this makes Claude Desktop "spyware" and amounts to a violation of European privacy law.

"I want to be blunt," Hanff wrote in ablog postover the weekend. "This is a dark pattern. It is also, in my professional opinion, a direct breach of Article 5(3) ofDirective 2002/58/EC(the ePrivacy Directive) as well as a multitude of computer access and misuse laws (usually criminal law), on a scale large enough to matter, in a vendor which has spent considerable effort on being perceived as the safety conscious AI lab."

Article 5(3) requires service providers seeking access to a person's data to provide clear details about the data access request and to obtain consent unless access is strictly necessary to provide the service.

Hanff explains that he found the undisclosed file installation while trying to debug another application that usedNative Messaging, an API for communicating between Chrome and other applications. Claude Desktop relies on the cross-platform Electron framework, which in turn relies on a bundled version of Chromium.

The file that Claude Desktop installed was:

com.anthropic.claude_browser_extension.json

It's a Native Messaging manifest file that gets called when Chromium-based browsers want to run a local executable. The file pre-authorizes three different Chrome extension identifiers (e.g.Claude in Chrome extension) so that associated browsers will run the binary identified in the manifest file.

Basically, Claude Desktop is setting up its AI model's ability to access various browsers for automated operation. And it does this for browsers not yet present on the user's device, so that those browsers will grant Claude access if they are installed at some point in the future.

But Hanff claims he never installed any Anthropic browser extensions due to privacy and security concerns. Claude Desktop did so for him, without disclosure or permission.

Browser extensions magnify security and privacy challenges because they often request overly broad permissions. Hanff observes that Claude in Chrome has authenticated session access and can read web pages, fill out forms, and capture the screen. What's more, he says, the binary bridge application runs outside of the browser's sandbox at user privilege level, without surfacing any permission prompts.

Anthropic's approach has numerous problems, according to Hanff. It amounts to forced bundling across trust boundaries by writing configuration files for other vendors' browsers. It's invisible by default, with no opt-in. It's difficult to remove. It pre-authorizes browser extensions that haven't been installed. Its file is named in a way that fails to clarify the scope of what is being allowed. And it pre-authorizes non-present browsers to use the Native Messaging binary, among other concerns.

Hanff says, "Anthropic's own safety data statesClaude for Chromeis vulnerable to prompt injection at a 23.6 percent success rate without mitigations, and 11.2 percent with their current mitigations. … With the bridge pre-installed on the user's laptop, a successful prompt injection against Claude for Chrome has a path, through the extension, through the bridge, to a helper binary running outside the browser sandbox at user privilege."

Anthropic did not respond to a request for comment.

We note that the Claude Desktop native messaging host hasan unfixed bugthat was auto-closed on February 28th by a GitHub Actions bot. The problem is that the Claude Code and Claude Desktop native messaging host registrations conflict with one another, so the associated Chrome extension fails with Claude Code.

* AI quota inflation is no token effort. It's baked in
* Schmoozebots: study finds flattery will get AI everywhere
* One of Europe's sovereign cloud picks may not be so-sovereign after all
* AI is reshaping Britain's datacenter map away from London

Noah M. Kenney, founder and principal consultant for advisory firmDigital 520, takes issue with Hanff's use of the term "spyware" but says his findings appear to support his legal reasoning.

"The technical claims here are largely testable and, as described, reproducible," said Kenney in an email toThe Register. "Independent reviewers can verify that identical Native Messaging manifests are written across multiple Chromium-based browser paths, that the activity is attributed at the OS level to the desktop application, and that installation events are recorded in the app's own logs. If those artifacts hold, the core behavior is difficult to dispute: the desktop app is registering a Native Messaging host across multiple browser environments, including ones the user has not actively chosen to integrate, and maintaining that registration persistently."

With the disclaimer that he's not an attorney, Kenney said the legal framing is more complicated.

"Article 5(3) of the ePrivacy Directive clearly applies to storing information on a user's device, so the act of writing these manifests is in scope. The key question is whether that action is 'strictly necessary' for a service the user actually requested.

"Vendors will argue this is part of a unified product experience, but regulators, particularly in Europe, tend to interpret 'strictly necessary' narrowly. Silently installing cross-application integrations, especially into browsers the user has not opted into, is likely to fall outside that exemption, which carries credible regulatory risk."

Kenney said he would push back on the term "spyware" because it traditionally implies active and covert data exfiltration.

"What is described here is different," he said. "It is a pre-positioned integration layer that remains dormant until triggered by a browser extension, which is an important distinction. Regardless, the risk is still real as this creates a persistent, pre-authorized bridge from browser extensions into a local executable running outside the browser sandbox, installed without clear user awareness and resistant to removal. From a security perspective, that meaningfully expands the attack surface."

Kenney agrees that the way Anthropic has designed its software in this instance breaks a widely understood trust boundary.

"Users do not expect a desktop application to silently modify other applications, especially across vendors," he said. "European regulators, in particular, expect explicit opt-in, installation scoped only to user-selected integrations, and clear persistent controls with real revocation. This implementation falls short of that baseline. European enforcement is moving toward demonstrable, user-visible control rather than implied or deferred consent. Silent system modification across application boundaries is exactly the kind of pattern regulators are increasingly focused on."

Hanff toldThe Registerthat Anthropic has yet to respond to his post. He said he hasn't filed a formal complaint but intends to if the company fails to fix the Claude for Desktop installation process.

Kenney said, "Putting the legal ramifications aside, there is substantial reputational damage and loss of user trust that comes from a company that users perceive as being committed to safety and privacy releasing tools that seemingly undercut that posture." ®

 

Get our
 
Tech Resources

Share

#### More about

* AI
* Anthropic
* Privacy

More like these

×

### More about

* AI
* Anthropic
* Privacy
* Software
* Web Browser

### Narrower topics

* AdBlock Plus
* AIOps
* App
* Application Delivery Controller
* Audacity
* Brave
* Chrome
* Claude
* Confluence
* cookies
* Database
* DeepSeek
* Firefox
* FOSDEM
* FOSS
* Gemini
* Google AI
* GPT-3
* GPT-4
* Grab
* Graphics Interchange Format
* HTTP
* IDE
* Image compression
* Internet Explorer
* Jenkins
* Legacy Technology
* LibreOffice
* Machine Learning
* Map
* MCubed
* Microsoft 365
* Microsoft Edge
* Microsoft Office
* Microsoft Teams
* Mobile Device Management
* Neural Networks
* NLP
* OpenOffice
* Opera
* Personally Identifiable Information
* Privacy Sandbox
* Programming Language
* QR code
* Retrieval Augmented Generation
* Retro computing
* Safari
* Search Engine
* Software Bill of Materials
* Software bug
* Software License
* Star Wars
* Tensor Processing Unit
* Text Editor
* TOPS
* User interface
* Visual Studio
* Visual Studio Code
* Vivaldi
* WebAssembly
* WordPress

### Broader topics

* Large Language Model
* Self-driving Car

#### More about

Share

#### More about

* AI
* Anthropic
* Privacy

More like these

×

### More about

* AI
* Anthropic
* Privacy
* Software
* Web Browser

### Narrower topics

* AdBlock Plus
* AIOps
* App
* Application Delivery Controller
* Audacity
* Brave
* Chrome
* Claude
* Confluence
* cookies
* Database
* DeepSeek
* Firefox
* FOSDEM
* FOSS
* Gemini
* Google AI
* GPT-3
* GPT-4
* Grab
* Graphics Interchange Format
* HTTP
* IDE
* Image compression
* Internet Explorer
* Jenkins
* Legacy Technology
* LibreOffice
* Machine Learning
* Map
* MCubed
* Microsoft 365
* Microsoft Edge
* Microsoft Office
* Microsoft Teams
* Mobile Device Management
* Neural Networks
* NLP
* OpenOffice
* Opera
* Personally Identifiable Information
* Privacy Sandbox
* Programming Language
* QR code
* Retrieval Augmented Generation
* Retro computing
* Safari
* Search Engine
* Software Bill of Materials
* Software bug
* Software License
* Star Wars
* Tensor Processing Unit
* Text Editor
* TOPS
* User interface
* Visual Studio
* Visual Studio Code
* Vivaldi
* WebAssembly
* WordPress

### Broader topics

* Large Language Model
* Self-driving Car

#### TIP US OFF

Send us news