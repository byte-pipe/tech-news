---
title: Do the Math: How We Took Over ChatGPT Accounts - Parameter
url: https://www.parameter.ai/labs/we-found-a-gap-at-openai
date: 2026-10-31
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-01T18:53:52.859096
---

# Do the Math: How We Took Over ChatGPT Accounts - Parameter

# Do the Math: How We Took Over ChatGPT Accounts

## Overview
- In October 2026 the research team discovered a way to execute attacker‑controlled JavaScript inside a signed‑in ChatGPT session by abusing the public “share” link feature.  
- The attack required only that the victim click the shared link; no app installation, project join, or code paste was needed.  
- OpenAI patched the issue on October 26 2026 and classified the report as a P1 severity vulnerability.

## Attack Chain
- **Attacker publishes a conversation** using ChatGPT’s normal sharing feature.  
- **Victim opens the public share** link.  
- **HTML Preview** from the shared conversation crosses into the main `chatgpt.com` page.  
- **JavaScript runs** in the victim’s authenticated session, allowing the attacker to read private chats, modify settings, and call authenticated APIs as the victim.

## Technical Details
- **Two seemingly harmless features combined:**
  1. **Graph rendering** that loads the MathLive library.  
  2. **HTML Preview** that renders user‑provided HTML in a sandboxed iframe.
- **MathLive listener:**  
  - Listens for `postMessage` events from any origin (origin policy set to `none`).  
  - Accepts a message that updates the virtual keyboard layout, where the layout can contain arbitrary HTML.
- **Message flow:**  
  - Preview sends a `mathlive#virtual-keyboard-message` to replace the keyboard layout with attacker‑controlled HTML.  
  - A second message tells MathLive to display the keyboard, causing the malicious HTML to be inserted via `innerHTML`.
- **Escalation to script execution:**  
  - The injected HTML includes an `<iframe srcdoc="...">` without a sandbox attribute, creating a new document that inherits the `https://chatgpt.com` origin.  
  - This frame can access the parent page and run JavaScript.
- **CSP bypass:**  
  - ChatGPT’s Content Security Policy blocks inline scripts but allows scripts from YouTube.  
  - The attacker uses YouTube’s oEmbed JSONP endpoint with a crafted `callback` parameter (`globalThis.__marker=31337;void`) that executes arbitrary code while still satisfying CSP.
- **Result:** Arbitrary JavaScript runs with full ChatGPT session privileges, enabling enumeration of conversations, data exfiltration, and account takeover.

## Exploitation Steps
1. Create a conversation containing a MathLive‑based graph (loads the vulnerable listener).  
2. Add an assistant‑authored HTML Preview that sends the two `postMessage` commands to replace the keyboard layout and display it.  
3. Export the conversation as a public share link; the link preserves both the graph and the preview.  
4. Distribute the link (email, chat, social media).  
5. When a signed‑in user opens the link, the chain executes automatically, granting the attacker full control over the user’s ChatGPT account.

## Impact
- **Account takeover:** Attacker can read any private conversation, retrieve files, and perform actions on behalf of the victim.  
- **No user interaction beyond clicking a link:** No installation, permission grant, or developer‑tool usage required.  
- **Broad attack surface:** Any user who receives a shared ChatGPT link could be compromised.

## Mitigation / Fix
- OpenAI removed the unsafe message handling in MathLive and added origin checks.  
- The HTML Preview sandbox was tightened, and the virtual‑keyboard layout injection path was closed.  
- CSP rules were reviewed to prevent reliance on external JSONP endpoints for script loading.  
- The vulnerability was patched on October 26 2026 and assigned a P1 severity rating.