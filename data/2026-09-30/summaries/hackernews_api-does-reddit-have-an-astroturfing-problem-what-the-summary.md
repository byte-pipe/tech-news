---
title: Does Reddit have an astroturfing problem? What the data suggests — Peter Vijeh
url: https://www.petervijeh.com/projects/reddit-astroturf
date: 2026-09-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-30T06:00:58.492636
---

# Does Reddit have an astroturfing problem? What the data suggests — Peter Vijeh

# Summary of “Does Reddit have an astroturfing problem? What the data suggests — Peter Vijeh”

## Background and Motivation
- The author, an avid cook, often searches for knife recommendations by adding “reddit” to product queries, trusting Reddit users to give unbiased opinions.
- Recognizes that the same platform could be exploited by brands to plant paid recommendations (astroturfing).
- Goal: determine whether knife‑related subreddits contain evidence of coordinated, paid promotion.

## Data Collection and Tools
- Developed a fine‑tuned named‑entity model (GLiNER) to extract brand, model, and steel information from comments.
- Ran the model on all comments collected by the New Knife Day scraper across six subreddits: r/knives, r/knifeclub, r/chefknives, r/japaneseknives, r/FixedBladeEdc, and r/KnifeSteels.
- Identified “buying threads” using regex patterns (e.g., “should I buy”, “recommend”, “best knife”).

## Expected Signature of Astroturfing
A paid campaign would likely produce accounts that:
- Contribute a disproportionate share of brand mentions in buying threads.
- Mention the same brand repeatedly.
- Have few overall comments, low scores, and limited subreddit history (thin or young accounts).
- Post mainly in knife subreddits and include affiliate links.

## Corpus Statistics (after refresh)
- Posts examined: 6,675  
- Comments after refresh: 51,129  
- Authors with ≥10 comments: 987  
- Brand mentions in buying threads from these authors: 1,471  

## Analytical Approach
1. Defined “brand‑loyal” accounts as the top 5 % (49 accounts) of authors with ≥10 comments who most heavily mention a single brand.  
2. Performed a permutation test: randomly reassigned author names to each brand mention 1,000 times, preserving each author’s overall comment volume.  
3. Compared the actual share of brand mentions by the 49 brand‑loyal accounts to the distribution from the random permutations.

## Key Findings
- Expected share for the 49 accounts (by chance): average 7.9 %, 95 % confidence interval 6.3 %–10.1 %.  
- Observed share: 11.3 % of brand mentions in buying threads, exceeding the 95 % threshold (only 2 of 1,000 permutations reached this level).  
- Interpretation: roughly one recommendation in nine comes from these accounts, versus one in thirteen expected by chance—about 50 extra recommendations out of 1,471.

### Subreddit‑Level Results
| Subreddit | Observed Share of Brand Mentions by Brand‑Loyal Accounts |
|----------|-----------------------------------------------------------|
| All six subs | 11.3 % |
| r/knives | 6.7 % (within chance range) |
| r/chefknives | 14.9 % (above chance) |
| r/knifeclub | 12.4 % (above chance) |
| r/japaneseknives | 15.2 % (above chance) |
| r/FixedBladeEdc | 8.5 % (within chance range) |

### Brand‑Specific Results
- Brands B001, B002, B003, B004 show varying degrees of over‑representation; three brands receive significantly more recommendations from the brand‑loyal accounts than expected, one large brand receives slightly less, and three receive none.

## Interpretation
- The over‑representation is concentrated in specific subreddits (r/chefknives, r/knifeclub) and specific brands, matching the pattern expected from targeted paid campaigns rather than a platform‑wide manipulation.
- The pattern could also arise from enthusiastic fan groups or brand employees, but the data alone confirms only that a small group of accounts disproportionately influences buying advice.  

## Conclusion
- A minority of highly brand‑focused accounts (≈5 % of active commenters) produce more buying‑thread recommendations than random chance predicts, suggesting the presence of coordinated promotion—potentially astroturfing—within certain knife subreddits.  
- The effect is not uniform across all knife communities, indicating that any manipulation is likely limited to specific brands and subreddits rather than a pervasive Reddit‑wide issue.