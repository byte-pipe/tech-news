---
title: "8 Million Users' AI Conversations Sold for Profit by \"Privacy\" Extensions | Koi Blog"
url: https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection
date: 2025-12-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-16T11:19:45.625403
screenshot: hackernews_api-8-million-users-ai-conversations-sold-for-profit-b.png
---

# 8 Million Users' AI Conversations Sold for Profit by "Privacy" Extensions | Koi Blog

### Discovering a Secret User Base for AI Conversations Sold for Profit by "Privacy" Extensions

**Introduction**

A researcher discovered a hidden user base of 8 million people's AI conversation records, sold to companies behind "privacy" extensions. The research reveals how these extensions harvest conversations from multiple platforms and can continue running independently even when the VPN is disabled.

### The Discovery

The researcher used an agentic-AI risk engine called Wings to scan for browser extensions with the capability to read and exfiltrate conversations from AI chat platforms. They expected a small number of obscure extensions but found something entirely different:

1.  **Urban VPN Proxy**, with over 6 million users, stands out as one of the top targets.
2.  This extension works on multiple AI platforms: ChatGPT, Claude, Gemini, Microsoft Copilot, Perplexity, DeepSeek, Grok (xAI), and Meta AI.
3.  The harvesting is enabled automatically using hardcoded flags in the configuration.

### How It Works

The data collection operates independently of the VPN functionality:

1.  **Script Injection**: The extension monitors the user's browser tabs and injects an "executor" script into the platforms it targets, including chatgpt.js, claude.js, gemini.js, and others.
2.  **Overriding Native Functions**: Once injected, the script overrides the original fetch() and XMLHttpRequest functions to capture conversations from any of these platforms.

The technical breakdown is as follows:

*   Script injection into AI platforms using hardcoded flags in configuration
*   Execution of the injectors on an ongoing basis

### Implications

This discovery has significant implications for individuals who choose "privacy" extensions, which may enable companies behind these services to harvest sensitive information from their devices. It raises concerns about data security and user privacy.

**Recommendations**

To address this issue:

1.  **Verify Authenticity**: Verify the authenticity of any browser extension you install.
2.  **Disable Unnecessary Features**: Disable features that grant access to sensitive information, such as VPNs.
3.  **Monitor Online Activities**: Regularly review online activity for signs of unusual or suspicious behavior.

By acknowledging these facts and taking necessary precautions, individuals can minimize the risks associated with "privacy" extensions sold compromised user data.
