---
title: How I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline | D. J. Speckhals
url: https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/
date: 2026-05-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-28T06:04:48.309427
---

# How I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline | D. J. Speckhals

# How I Bypassed Adobe and Microsoft to Build a Git‑Tracked Book Production Pipeline

## Overview  
- The core of a novel is the story and its writing quality; formatting is a technical step that many authors find daunting.  
- I combined my experience as an independent novelist and software developer to create a workflow that avoids reliance on Adobe InDesign and Microsoft Word for final production.  

## Original Toolchain: Word → InDesign → Calibre → Kindle Create  
- All four of my Christian historical novels began as DOCX files edited with Word’s tracked‑changes feature.  
- I used paragraph styles in Word to keep formatting consistent; the DOCX served as the single source of truth.  
- InDesign was chosen for print because it offers professional‑grade typography (hyphenation, micro‑typography, baseline grids, etc.).  
- For e‑books I used Calibre to generate EPUBs from the DOCX, then tried Kindle Create to produce KFX files for Amazon KDP.  
- Maintaining four separate outputs (PDF, EPUB, KPF, and KFX) required repetitive manual updates and forced me to switch between Windows, macOS, and a Linux laptop.

## Pain Points  
- Every small edit required:  
  1. Updating the master DOCX.  
  2. Re‑exporting the InDesign PDF for print distributors.  
  3. Re‑building the EPUB in Calibre for generic e‑book stores.  
  4. Re‑building the KPF in Kindle Create for Amazon.  
- Kindle Create does not run on Linux, and InDesign is unavailable on my daily driver, creating workflow friction.  
- The process felt cumbersome and error‑prone, especially when trying to keep all formats in sync.

## Inspiration from Standard Ebooks (SE)  
- Discovered SE on Hacker News; their public‑domain EPUBs are of exceptionally high quality.  
- SE’s “Manual of Style” and command‑line tooling act like a linter for e‑book formatting, enforcing strict, reproducible standards.  
- Examples of lint checks: illegal units for font‑size, mismatched word counts, improper header semantics, and incorrect placement of possessive apostrophes.  

## Pivot to an SE‑Based Workflow  
- For the third book, *Prince of Savoy*, I converted the DOCX to a clean EPUB with Calibre, then applied SE’s style guide using the `standardebooks` CLI.  
- The linter forced me to add semantic markup (e.g., character styles for foreign languages, poems, letters) that improves accessibility and downstream formatting.  
- After passing all lint rules, the EPUB built cleanly and converted well to Kindle’s format, allowing me to drop Kindle Create from the pipeline.  

## Open‑Source Tooling and Version Control  
- When revisiting the first novel, *Heretics of Piedmont*, I switched to LibreOffice Writer (ODT) to avoid Windows/Office 365.  
- Defined rich paragraph and character styles for songs, epigraphs, maps, foreign‑language passages, and other semantic elements.  
- Stored the resulting XHTML source files in a Git repository, enabling:  
  - Precise change tracking.  
  - Automated builds of EPUBs via the SE command line.  
  - Easy collaboration and rollback if needed.  

## Resulting Pipeline  
1. Write and edit in a word processor that supports styles (Word DOCX or LibreOffice ODT).  
2. Convert to EPUB with Calibre (or directly to ODT → EPUB).  
3. Run the `standardebooks` linter to enforce SE style and generate clean XHTML.  
4. Build the final EPUB (and, if desired, a Kindle‑compatible file) from the version‑controlled source.  
5. Publish the PDF for print using InDesign only when a print edition is required, otherwise rely on the high‑quality EPUB for all digital channels.  

## Takeaways  
- A strict, code‑like style guide (SE) turns e‑book formatting into a reproducible, testable process.  
- Keeping the source files in Git eliminates the “master DOCX” bottleneck and makes every change auditable.  
- By removing Kindle Create and limiting InDesign to print‑only tasks, the workflow becomes platform‑agnostic and fits comfortably on a Linux workstation.  

This pipeline lets me treat book production like software development: write, version, lint, build, and deploy—all without being locked into proprietary Adobe or Microsoft tools.