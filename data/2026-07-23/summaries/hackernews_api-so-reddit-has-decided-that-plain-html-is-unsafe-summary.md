---
title: So Reddit has decided that plain HTML is unsafe
url: https://www.cole-k.com/2026/07/21/reddit/
date: 2026-07-22
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-23T19:01:59.092800
---

# So Reddit has decided that plain HTML is unsafe

# Summary of “So Reddit has decided that plain HTML is unsafe”

## Background
- Reddit hosts many popular forums and monetizes user‑generated content, especially valuable in the LLM era.  
- The author no longer engages with Reddit but still uses site‑restricted searches (`site:reddit.com`) to find human‑written material.  

## Reddit’s Announcement
- Reddit announced that the logged‑out experience on **old.reddit.com** is a major source of abusive scraping and automated traffic.  
- The stated goal is to “keep Reddit safe,” though the author questions who is being protected and what safety means.  

## Old Reddit vs. New Reddit
### Old Reddit
- Serves pages as plain HTML; most content (including comments) is delivered without JavaScript.  
- Page size is about 1 MB (≈0.5 MB transferred) and loads slowly (≈2 s), suggesting possible rate‑limiting.  
- Because the HTML is fully exposed, it is easier for scrapers to harvest data.  

### New Reddit
- Relies heavily on JavaScript; without it only the post itself loads.  
- Loads roughly five times more resources than Old Reddit, making the page bulkier.  
- The author could still retrieve comments by allowing a few specific JS endpoints, indicating that executing the site’s JS is the main barrier for scrapers.  
- Additional “heartbeat” requests are sent when the user scrolls or moves the cursor, which the author interprets as a security‑oriented feature.  

## Security & Scraping Implications
- Reddit claims the lack of a “modern security stack” on Old Reddit justifies restricting access.  
- The author argues that the security claim is a PR move; the real motive appears to be protecting Reddit’s data (its “gold”) from large‑scale scraping.  
- Scrapers may simply switch to the newer, more resource‑intensive frontend, which still allows data extraction if JavaScript is executed.  

## Author’s Critique
- Dislikes being forced off a functional, lightweight frontend that works on old devices and with tools like NoScript.  
- Finds Reddit’s approach of disabling Old Reddit while keeping New Reddit accessible contradictory.  
- Suggests a cleaner solution would be to return proper HTTP error codes (e.g., 403/404) for Old Reddit or to retire it outright.  
- Expresses frustration that the “safety” justification is vague and that users must enable JavaScript to continue using the service.  

## Conclusion
- Reddit’s move to block logged‑out access to the plain‑HTML Old Reddit is framed as a safety measure but primarily serves to hinder easy scraping of human‑generated content.  
- While the new, JavaScript‑heavy frontend raises the technical bar for scrapers, it does not make scraping impossible and imposes additional load on users and devices.  
- The author remains skeptical of Reddit’s security narrative and disappointed by the loss of a simple, low‑resource browsing option.