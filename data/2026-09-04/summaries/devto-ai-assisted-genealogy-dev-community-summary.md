---
title: AI-assisted genealogy - DEV Community
url: https://dev.to/nfrankel/ai-assisted-genealogy-9cn
date: 2026-09-03
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-09-04T07:25:53.655678
---

# AI-assisted genealogy - DEV Community

# AI‑assisted genealogy – summary

## Setup
- Treated the research as a software project: version control with git, hosted on Codeberg and GitHub, visualized via Cloudflare Pages.  
- Chose GEDCOM (version 5.5.1) as the data format for storing genealogical records.  

## GEDCOM 101
- GEDCOM is a hierarchical, line‑based format where each line starts with a level number.  
- Core elements: `INDI` for an individual, name delimited by slashes, sex, birth event, date, place, and source references.  
- Proper indentation uses level numbers, not spaces; example provided for a single person record.  

## The loop
1. Select an individual with unknown parents.  
2. Prompt the AI assistant to search appropriate genealogy sites and archives for the relevant civil record.  
3. AI transcribes the record, adds the parents as new `INDI` entries, links them to the child, and records the source in the GEDCOM file.  
4. Commit the changes to the repository.  
5. Repeat until no further records are found, thereby extending the tree generation by generation.  

## What worked with the assistant
- **Model selection:** Use lightweight models for simple tasks (e.g., sending emails) and stronger models for multi‑step research to avoid errors.  
- **Skills:** Create reusable instruction sets (skills) for common actions such as site navigation, record transcription, and autonomous sessions; this keeps the main prompt concise.  
- **Transcription:** Convert PDFs and images to plain text once, then reuse the text to save tokens. Claude Code performed well on this task.  
- **Grammar checks:** Validate GEDCOM structure after each commit using pre‑commit hooks or CI jobs to prevent file corruption.  
- **Long‑running autonomous tasks:** When token limits become a bottleneck, switch to a higher‑quota model (Claude Max) and run sessions overnight, using a sub‑agent architecture to isolate context and manage commits.  

## What I learned about genealogy
- **Geographic variability:** Different countries, and even regions within a country, yield uneven amounts of available data; expect an unbalanced tree.  
- **Existing data:** Many free genealogy websites already contain extensive ancestor information; leveraging shared ancestors can accelerate research.  
- **Data reliability:** Third‑party contributions can contain errors; always verify facts with official civil records before accepting them as true.  
- **Case example:** A presumed Swiss death turned out to be a French hunting accident, discovered only after checking primary sources.