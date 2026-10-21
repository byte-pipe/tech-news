---
title: "France's Supermarket Fridges Were Vulnerable Online for Months | IPinfo.io"
url: https://ipinfo.io/blog/france-fridges-hack
date: 2026-10-20
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-21T11:12:23.196802
---

# France's Supermarket Fridges Were Vulnerable Online for Months | IPinfo.io

# France's Supermarket Fridges Were Vulnerable Online for Months

## TL;DR
- France hosted 1,331 exposed Danfoss fridge dashboards, more than the rest of the world (72 countries) combined (1,197).  
- 85 % of French dashboards ran software with known vulnerabilities; only 195 (≈15 %) had all fixes applied.  
- Most dashboards had been exposed for at least six months; the share fully patched rose from 14 % to 24 % in that period.  
- After the October 11‑12 attack, only 316 French dashboards remained online (a 76 % drop).  

## What Happened
- On the night of 11‑12 Oct 2026, attackers forced refrigeration controllers into defrost mode, causing temperatures up to 50 °C, fires, and loss of fresh/frozen goods.  
- Over 400 stores were affected; losses estimated in the millions of euros.  
- Major chains hit: Carrefour (≈80 stores), Intermarché & Netto (≈300 stores combined), Monoprix (≈5 % of stores), Leclerc, Coopérative U (≈80 stores).  
- The compromised hardware were Danfoss legacy controllers (models AK‑SM 800 and AK‑SC 355).  
- France’s cybersecurity agency (CERT‑FR) issued alerts, recommending disconnection or restricted access; the attack’s origin remains unknown.  

## France Stood Out, by Far
- Weekly IPv4 scans (Oct 6‑7) found 2,528 Danfoss StoreView dashboards globally; 1,331 (53 %) were in France.  
- Poland (179), United States (101), Portugal (92) and Belgium (85) followed.  
- French dashboards used the same software mix as elsewhere and connected mainly through a single national telecom provider (≈98 % on ISP networks, not data‑centers).  

## Most Fridge Software Was Out of Date
- Two dashboard generations:  
  - Legacy Flash‑based (AK‑SM 800, end‑of‑life 2023).  
  - Current (AK‑SM 800A) showing build dates.  
- Known issues:  
  - Firmware < 3.3 missed three 2023 critical fixes.  
  - Firmware < 4.2 missed a 2025 login‑bypass fix.  
  - Firmware < 4.3.1 missed two additional 2025 fixes.  
- Overall, 1,136 French dashboards (85 %) ran vulnerable software: 527 legacy units, 280 missing 2023 fixes, 329 missing 2025 fixes. Only 195 were fully patched.  

## The Exposure Has Existed for Months
- From March 30 to October 6, 2026, the total number of open dashboards remained stable (≈2,500 worldwide, half in France).  
- 1,019 French dashboards were present at the same IP address on both March 30 and October 6, indicating six‑month exposure.  
- The proportion of fully patched French controllers increased slowly from 14 % to 24 % over the same period.  

## Did Stores Disconnect After the Attack?
- Post‑attack scan (Oct 14) showed only 316 French dashboards still reachable (76 % reduction).  
- Legacy controllers dropped from 527 to 64; fully patched ones from 195 to 54, suggesting stores chose to disconnect rather than patch.  
- Outside France, 25 % of dashboards disappeared (higher than the usual 9‑12 %).  
- Independent scans (Censys) reported a similar 71 % drop in France between Oct 11‑14.  

## Where Else These Controllers Are Open
- After France, the next highest counts of exposed Danfoss dashboards were in Poland, the United States, Portugal, and Belgium.  
- The pattern mirrors France’s reliance on ISP‑based connections rather than cloud or data‑center hosting.