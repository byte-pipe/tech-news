---
title: UK Biobank health data keeps ending up on GitHub
url: https://biobank.rocher.lc
date: 2026-04-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-25T08:22:54.734600
---

# UK Biobank health data keeps ending up on GitHub

# Summary of “UK Biobank health data keeps ending up on GitHub”

## What UK Biobank is trying to take down
- Uses copyright takedown notices (DMCA‑style) to request removal of health‑related data from GitHub.  
- Notices usually target specific files rather than whole repositories, likely to satisfy the copyright‑infringement requirement.  
- File types most often targeted:  
  - Jupyter or R notebooks (≈ 50 %) – may contain a few rows of data.  
  - Genetic/genomic data files (PLINK, BOLT‑LMM, BGEN) (≈ 25 %) – encode participant genotypes or association results.  
  - Tabular datasets (CSV, TSV, Excel, R objects) – can hold phenotypes or health records.  
  - Remaining files include analysis scripts, documentation, and compressed archives.  

## Timeline of takedown notices
- First notice filed: July 2025.  
- Total notices filed up to 2026‑04‑17: 110.  
- Steady flow until a pause in January, February, and most of March 2026.  
- Notices resumed at the end of March 2026, shortly after The Guardian’s investigation highlighted ongoing data exposure and the limited impact of takedowns.  

## Geographic distribution of targeted developers
- Notices affect developers in at least 14 countries; the true number is likely higher.  
- 170 unique developers identified; only 76 provide a resolvable location.  
- Approximate country counts (based on available locations):  
  - United States: 24  
  - China: 22  
  - United Kingdom: 7  
  - Germany: 5  
  - Hong Kong: 4  
  - Australia: 4  
  - Spain: 3  
  - South Korea: 1  
  - Greece: 1  
  - Qatar: 1  
  - United Arab Emirates: 1  
  - Switzerland: 1  
  - India: 1  
  - Netherlands: 1  

## Methodology
- Data source: GitHub’s public `github/dmca` repository, which stores the full text of every DMCA takedown notice received.  
- Identification of UK Biobank notices:  
  - Match filenames containing the slug “uk‑biobank”.  
  - Additionally search notice bodies for “UK Biobank” or “UKBiobank” (case‑insensitive) to capture alternative slugs.  
- Extracted information: filing date (from filename) and all GitHub repository URLs mentioned in the notice.  
- User location extraction:  
  - Query GitHub REST API for each unique username to obtain the free‑text “location” field.  
  - When missing, infer country from profile details or email domain.  
  - Manual resolution of ambiguous or incomplete strings.  
- Limitations:  
  - Only 76 of 170 developers have a location that could be resolved.  
  - The analysis does not verify the actual content of the targeted repositories; it reports only what appears in the public notices.  
- Data is refreshed regularly by re‑running the collection script against the latest `github/dmca` repository.  

## Further reading (selected articles)
- **Mar 2026** – UK Biobank CEO Sir Rory Collins reassures participants that removed data lacked names or NHS numbers and advises caution on social media.  
- **Mar 2026** – The Guardian investigation shows researchers unintentionally uploaded participant data to public GitHub repos; a volunteer’s record was matched using limited identifiers.  
- **Apr 2025** – Guardian opinion by Sir Rory Collins defending UK Biobank’s data‑sharing model and its scientific contributions.  
- **Apr 2025** – Guardian report on MI5 concerns about Chinese researchers accessing half a million UK GP records.  
- **Oct 2024** – Guardian follow‑up on Heliospect Genomics using UK Biobank data to predict embryo traits for IVF.  
- **Oct 2024** – Undercover investigation of a far‑right network claiming access to UK health data.  
- **Oct 2024** – UK Biobank’s official response denying race‑science claims and stating no unauthorized individuals were granted access.  
- **Nov 2023** – Guardian reveal of UK Biobank data shared with insurance companies (2020‑2023), contradicting public assurances.  
- **Nov 2023** – Science coverage of the release of whole‑genome sequences for ~500,000 participants, noting exclusive early access for four pharmaceutical companies.