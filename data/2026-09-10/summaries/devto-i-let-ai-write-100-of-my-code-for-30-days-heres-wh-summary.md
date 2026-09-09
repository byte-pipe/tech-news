---
title: "I let AI write 100% of my code for 30 days. Here's what broke. - DEV Community"
url: https://dev.to/infoinlet1/i-let-ai-write-100-of-my-code-for-30-days-heres-what-broke-1aa0
date: 2026-09-09
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-09-10T07:21:17.632227
---

# I let AI write 100% of my code for 30 days. Here's what broke. - DEV Community

# Summary of “I let AI write 100% of my code for 30 days. Here’s what broke.”

## The Rules I Followed
- I never typed application logic myself; I only wrote prompts and let the AI generate code.  
- I could read every line, reject it, and ask for a new version, but I was not allowed to edit the code directly.  
- Configuration, secrets, and UI actions (clicking buttons) remained my responsibility.  
- If I was stuck for more than an hour, I logged a “break” and wrote the code manually.  
- Over the month I recorded nine breaks; those are the focus of the report.

## What Worked Shockingly Well
- **Greenfield scaffolding**: A full Next.js + Postgres + Drizzle + auth setup was generated correctly in a single prompt.  
- **Boilerplate generation**: CRUD endpoints, form validation, Zod schemas, and table components with sorting/pagination were produced flawlessly every time.  
- **Debug‑as‑rubber‑duck**: The AI identified performance issues (missing index, N+1 query) better than I could on my own.  
- The first week felt like a glimpse of “developers are obsolete.”

## The Nine Breaks – Where the AI Fell Short
### Breaks 1–3: Lack of System‑wide Context
- The AI duplicated helpers, re‑implemented auth checks, and introduced a new `User` type without noticing existing implementations.  
- Resulted in subtle architecture drift that only became costly after weeks.

### Breaks 4–5: Plausible but Wrong Code
- A billing webhook acknowledged Stripe events before persisting them, leading to lost records in production.  
- The code looked correct and passed tests, but hidden bugs would have been missed by a junior.

### Break 6: Debugging Loop
- When the AI couldn’t fix a bug, its revisions introduced new issues, creating a time‑consuming back‑and‑forth without manual debugging.

### Breaks 7–8: Over‑engineering and Poor Judgment
- Generated settings pages with unnecessary options and wrapped everything in `try/catch`, swallowing errors.  
- The AI lacks the product‑design sense to know what to omit.

### Break 9: The Last 10 % Is 90 % of the Work
- Getting a demo running took a week; polishing edge cases, race conditions, and unusual user behavior took three more weeks.  
- The AI only handled what was explicitly asked; anticipating hidden cases remains a human skill.

## Uncomfortable Synthesis
- AI replaced tasks typically given to junior developers (scaffolding, boilerplate, first drafts).  
- Senior‑level skills—detecting subtle bugs, deciding what not to build, maintaining system coherence—were still essential.  
- The hierarchy isn’t flattened; the top becomes more valuable while the traditional ladder to seniority is eroded.

## What I Changed in My Workflow
- Separate the “author” (AI) from the “reviewer” (another AI or human) to catch plausible‑but‑wrong code.  
- No code is merged without a human who can assess the blast radius.  
- Compilation and passing tests are only the start of review; tests must be examined for alignment with the correct mental model.

## Would I Do It Again?
- **Prototype**: Absolutely—never scaffold by hand again.  
- **Production**: Use AI for 100 % of the typing but 0 % of the thinking. The typing is the easy part; the thinking remains human.  
- Open question to teams: If AI handles junior work, how will you cultivate the next generation of senior engineers?

*(If you found this useful, consider a ❤️ and a 🔖, and share your own “AI wrote something that looked fine” story.)*