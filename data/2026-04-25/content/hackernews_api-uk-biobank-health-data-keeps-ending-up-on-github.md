---
title: UK Biobank health data keeps ending up on GitHub
url: https://biobank.rocher.lc
site_name: hackernews_api
content_file: hackernews_api-uk-biobank-health-data-keeps-ending-up-on-github
fetched_at: '2026-04-25T08:21:37.511291'
original_url: https://biobank.rocher.lc
author: Cynddl
date: '2026-04-23'
description: Tracking DMCA takedown notices filed by UK Biobank against GitHub repositories where researchers accidentally published participant health data.
tags:
- hackernews
- trending
---

## What is UK Biobank trying to take down

 

UK Biobank uses copyright takedown notices, a mechanism often associated with removing pirated software and stolen code, to remove health data from GitHub. The UK has no equivalent of DMCA for privacy breaches that would compel a platform to act so quickly.

 

Looking at the takedown notices, we often see specific files being targeted rather than entire repositories—possibly to justify the copyright infringement as required for a takedown notice. Nearly half are Jupyter or R notebooks, which can
 contain a few rows of data. A quarter are genetic and genomic data files (PLINK,
 BOLT-LMM, BGEN) that directly encode participant genotypes or association results.
 Tabular datasets (CSV, TSV, Excel, and serialised R objects) account for another
 large share and could contain phenotype or health records. The remainder
 includes analysis scripts, documentation, and compressed archives.

 
 
 

Interactive chart requires JavaScript.

 
 
 
 
 
 
 
 

## Timeline of takedown notices

 

The first takedown notice was filed in July 2025. Since then, the pace has been steady, with a total of 110 requests to GitHub. Interestingly, the requests stopped in January, February, and most of March 2026. It's hard to believe that no researcher has mistakenly uploaded UK Biobank data during these months. The notices restarted end of March, just after the Guardian's investigations revealed the ongoing data exposure and the ineffectiveness of takedowns.

 
 
 

Interactive timeline requires JavaScript. 110 notices were filed between July 2025 and 2026-04-17.

 
 
 
 
 
 
 
 

## Where in the world

 

Developers targeted by UK Biobank's takedown notices are based in at least 14 countries. The true number is likely higher: of the 170 developers identified in the notices, only 76 list a location on their GitHub profile.
 Most appear to be from United States and China.

 
 
 

Interactive map requires JavaScript. Developers are based in 14 countries.

 
 
 
* 24United States
* 22China
* 7United Kingdom
* 5Germany
* 4Hong Kong
* 4Australia
* 3Spain
* 1South Korea
* 1Greece
* 1Qatar
* 1United Arab Emirates
* 1Switzerland
* 1India
* 1Netherlands
 
 
 
 
 
 
 

Methodology

 
 

To build this webpage, I used data from thegithub/dmcarepository, where GitHub publishes the full text of every DMCA takedown notice it
 receives. When a rights holder asks GitHub to remove content that infringes their
 copyright, the notice is posted publicly as a Markdown file in this repository.
 According toThe Guardian, UK Biobank has used this process to request the removal of files or repositories that contain
 (or that it believes contain) participant data covered by its data access agreements.

 

To identify UK Biobank-related notices, I match filenames containing the
 slug "uk-biobank" (the convention GitHub uses when naming notice files). Just in case, I also
 search the full text of every other notice file for the phrases "UK Biobank" or
 "UKBiobank" (case-insensitive) to catch notices filed under different slugs, such as
 those submitted on behalf of UK Biobank. From each matching notice, I
 extract the filing date (parsed from the filename, which follows GitHub'sYYYY-MM-DD-slug.mdconvention) and all GitHub repository
 URLs mentioned in the notice body. URLs pointing to GitHub's own infrastructure
 (e.g. github.com/contact or github.com/site) are excluded.

 

For each unique GitHub username found in the notices, I query the GitHub REST API
 (GET /users/{username}) to retrieve the user's
 public profile, specifically the self-reported location field. This is a free-text
 string that users enter voluntarily. It may be a city, a country, a university name,
 or left blank entirely. Deleted accounts return a 404 and are not included further.

 

I derive countries from the raw location strings by hand. When a user's
 GitHub profile does not include a location, I also determine their
 country by inspecting their GitHub profile and associated email address domains. This process is inherently
 imperfect: some locations are ambiguous (e.g. "Cambridge" could refer to the UK
 or the US), and many users do not provide any location at all. Of
 the 170 unique developers in the dataset,
 only 76 have a location that
 could be resolved to a country.

 

The data is regularly refreshed by re-running the collection script against the latest
 state of the github/dmca repository. This page does not make any claims about the
 content of the targeted repositories, including whether they contained actual participant data,
 derived datasets, analysis code, or just documentation. It reports only what is visible in
 the public DMCA notices filed by UK Biobank.

 
 
 
 
 
 
 
 

## Further reading

 

The exposure of Biobank data on GitHub is the latest in a series of governance challenges for UK Biobank.

 
 
 
Mar 2026
 

A message to our participants: protecting your personal information— UK BiobankCEO Sir Rory Collins reassures participants that the data they took down from GitHub did not contain name or NHS number, and recommends participants do not reveal any specific details about themselves on social media or websites moving forward.

 
 
 
Mar 2026
 

Confidential health records exposed online— The GuardianInvestigation revealing that UK Biobank participant data had been uploaded to public GitHub repositories by researchers sharing their code. With a volunteer's consent, journalists successfully matched their record in an exposed dataset using only their month and year of birth and the date of a single major surgery.

 
 
 
Apr 2025
 

UK Biobank is safely sharing health data to drive medical research— The GuardianOpinion piece by Sir Rory Collins defending UK Biobank's data-sharing model, its balance between access and privacy, and its contribution to scientific discovery.

 
 
 
Apr 2025
 

Chinese researchers given access to half a million UK GP records— The GuardianReport on MI5 concerns about overseas access to sensitive UK Biobank participant data.

 
 
 
Oct 2024
 

Concerns raised over access to UK Biobank data— The GuardianFollow-up revealing Heliospect Genomics used UK Biobank data to predict embryo traits for IVF clients.

 
 
 
Oct 2024
 

Race science group says they accessed sensitive UK health data— The GuardianUndercover investigation into a far-right network claiming to have obtained UK Biobank data for pseudo-scientific research.

 
 
 
Oct 2024
 

A message to our participants: unfounded claims in The Guardian— UK BiobankOfficial response refuting the race-science claims, stating none of the named individuals were ever approved for data access.

 
 
 
Nov 2023
 

Private UK health data shared with insurance companies— The GuardianRevealed that UK Biobank had approved data access for insurance companies between 2020 and 2023, contradicting public assurances.

 
 
 
Nov 2023
 

UK Biobank releases half a million whole genome sequences— ScienceCoverage of the whole genome sequences release for ~500,000 participants, noting four pharmaceutical companies (Amgen, AstraZeneca, GSK, and Johnson & Johnson) received nine months of exclusive early access.