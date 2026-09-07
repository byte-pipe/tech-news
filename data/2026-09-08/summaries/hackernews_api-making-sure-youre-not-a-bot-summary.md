---
title: "Making sure you're not a bot!"
url: https://anubis.techaro.lol/blog/2026/anubis-wasm/
date: 2026-09-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-08T00:32:29.342007
---

# Making sure you're not a bot!

# Making sure you're not a bot!

- Anubis is a JavaScript‑based protection system that shows a proof‑of‑work (PoW) challenge when the page fails to load its scripts, indicating server overload or anti‑scraping measures.  
- The PoW scheme, inspired by Hashcash, is intended to be negligible for individual users but costly for large‑scale scrapers, thereby discouraging automated data extraction.  
- The current implementation is a temporary placeholder while developers work on more sophisticated fingerprinting techniques (e.g., detecting headless browsers via font rendering) to avoid showing challenges to legitimate users.  
- Modern JavaScript features are required; extensions like JShelter that block such features must be disabled for the site to function.  
- Enabling JavaScript is necessary to pass the challenge, as a non‑JavaScript solution is still under development due to evolving AI‑driven scraping practices.