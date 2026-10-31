---
title: We Need to Talk About How Gross Modern Web Design Has Become (And How We Built an AI to Catch It) - DEV Community
url: https://dev.to/dj29/we-need-to-talk-about-how-gross-modern-web-design-has-become-and-how-we-built-an-ai-to-catch-it-5gin
date: 2026-10-30
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-31T19:03:58.231318
---

# We Need to Talk About How Gross Modern Web Design Has Become (And How We Built an AI to Catch It) - DEV Community

# We Need to Talk About How Gross Modern Web Design Has Become (And How We Built an AI to Catch It)

## Problem Overview
- Modern websites use “dark patterns” – UI/UX tricks that pressure or deceive users (e.g., fake countdowns, hidden fees, malicious download buttons).  
- Traditional ad‑blockers rely on static blocklists or CSS selectors and cannot handle these dynamic, visual manipulations.  
- Developers feel responsible to stop the web from actively manipulating its users.

## OmniGuard AI – The Proposed Solution
- A real‑time, multimodal Chrome extension that acts as a visual shield against dark patterns.  
- Captures a compressed screenshot of the viewport, sends it to an AI backend, and overlays red bounding boxes on deceptive elements before the user can interact.

## Technical Stack
1. **Extension Front‑end (“Eyes”)** – React 18 + Vite, built as a Manifest V3 Chrome extension.  
2. **Backend (“Brain”)** – FastAPI server that receives the screenshot and calls Gemini 3.7 Flash for multimodal visual analysis.  
3. **Overlay (“Shield”)** – Shadow DOM injection with HTML5 Canvas to draw bounding boxes, isolating the extension’s CSS from the host page.

## Six Dark‑Pattern Categories Detected
| Category | What It Looks Like |
|----------|-------------------|
| Disguised Clicks | Buttons that appear as downloads or actions but lead to ads or malware |
| Confirmshaming | Guilt‑laden opt‑out language (“No thanks, I hate saving money”) |
| Urgency Traps | Fake countdown timers or artificial scarcity messages |
| Hidden Costs | Fees or taxes that appear only at the final checkout step |
| Sneak into Basket | Unwanted add‑ons or insurance pre‑checked in a cart |
| Forced Continuity | “Free trial” offers that hide auto‑renewal terms in fine print |

## Zero‑DB Privacy Architecture
- The backend is completely stateless; screenshots exist only in memory for the few milliseconds needed for Gemini processing.  
- No logs, no storage, and no persistent data are ever kept, ensuring user privacy.

## Open Source & Community Involvement
- The full project, including Manifest V3 tab capture and Gemini prompting logic, is available on GitHub: `Tarkash-Labs/OmniGuard`.  
- Contributors Yug Vasava (Lead Dev) and Avadh Vaishnani (Lead QA) are acknowledged.  
- Users are invited to test the extension, review the code, and suggest additional dark patterns for training.

## Call to Action
- The author asks readers to share the most unethical or infuriating dark pattern they have encountered, to help improve OmniGuard’s detection capabilities.