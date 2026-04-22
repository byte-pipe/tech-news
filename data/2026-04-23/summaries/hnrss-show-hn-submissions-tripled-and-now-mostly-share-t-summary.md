---
title: Show HN submissions tripled and now mostly share the same vibe-coded look
url: https://www.adriankrebs.ch/blog/design-slop/
date: 2026-04-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:44:51.909780
---

# Show HN submissions tripled and now mostly share the same vibe-coded look

# Show HN submissions tripled and now mostly share the same vibe‑coded look

## Background
- Noticed a generic, sterile feel on many recent Show HN project pages that suggests AI‑generated design.  
- Claude Code has caused a sharp rise in Show HN posts, leading moderators to restrict new‑account submissions.  
- The surge provides enough pages (≈500) to evaluate for AI design patterns.

## AI design patterns identified
### Fonts
- Predominant use of Inter, especially for centered hero headlines.  
- Common combos: Space Grotesk, Instrument Serif, Geist.  
- Serif italic for a single accent word in an otherwise Inter hero.

### Colors
- “VibeCode Purple”.  
- Permanent dark mode with medium‑grey body text and all‑caps section labels.  
- Barely sufficient contrast in dark themes.  
- Gradients everywhere.  
- Large colored glows and box‑shadows.

### Layout quirks
- Centered hero with generic sans‑serif.  
- Badge positioned just above the hero H1.  
- Colored borders on cards (top or left edge).  
- Identical feature cards, each topped with an icon.  
- Numbered step sequences (1, 2, 3).  
- Stat banner rows.  
- Sidebar or navigation using emoji icons.  
- All‑caps headings and section labels.

### CSS patterns
- Use of shadcn/ui components.  
- Glassmorphism effects.

## Detection method
- Load each Show HN landing page with a headless Playwright browser.  
- Run an in‑page script that inspects the DOM and computed styles.  
- Each pattern is checked via deterministic CSS/DOM rules (no screenshots, no LLM visual judgment).  
- Manual QA estimates a false‑positive rate of about 5‑10 %.

## Results (500 sites scored)
- **Heavy slop** (5 + patterns): 105 sites (21 %).  
- **Mild** (2–4 patterns): 230 sites (46 %).  
- **Clean** (0–1 pattern): 165 sites (33 %).

## Interpretation
- A single pattern does not prove AI generation; the tiers reflect overall similarity to the identified “AI vibe”.  
- The prevalence of these patterns is seen as uninspired rather than harmful—business validation rarely depends on fancy design, and pre‑AI sites often resembled Bootstrap templates.  
- Anticipated future shift: designers may return to more original aesthetics to stand out, though the relevance of design could diminish if AI agents become primary web users.

*The post is human‑written; the scoring and analysis were AI‑assisted.*