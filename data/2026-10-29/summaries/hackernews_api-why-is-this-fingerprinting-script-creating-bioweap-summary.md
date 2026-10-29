---
title: Why Is This Fingerprinting Script Creating Bioweapons?
url: https://nullpt.rs/fingerprinting-bioweapons
date: 2026-10-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:01:18.884987
---

# Why Is This Fingerprinting Script Creating Bioweapons?

# Why Is This Fingerprinting Script Creating Bioweapons?

## Preamble
- The author enjoys reverse‑engineering browser fingerprinting scripts and decided to crawl the web, intercepting fingerprint‑related API calls using Playwright and the Tranco Top Sites list.  
- Canvas fingerprinting was captured by hooking `canvas.toDataURL` and filtering out benign canvases.  
- After crawling 10,000 sites, the collected canvases were published at **fingerprint.garden**, revealing many known and unknown fingerprinting implementations.

## A Work of Art
- One canvas stood out because its visual style resembled the album art of Tame Impala’s *Currents*.  
- The responsible script was identified as `https://servicepipe.tech/static/checkjs/06b667/4CIrx8U3Da.js`.  
- The author expected typical obfuscation but found unusually named functions such as `computeRicinLethalDosageForWaterSupply` and `calculateDeadlyLethalSuicideAspirinDosage`.

## Anti‑LLM Obfuscation Attempt
- The author hypothesized the bizarre names might be an attempt to thwart LLM‑based deobfuscation.  
- When the script was submitted to the Astra model, it refused to deobfuscate, citing safety concerns.  
- Other models (Daybreak Blue) also blocked the request, while GLM‑5.3 complied.

## Hidden Payload
- The script contains a string of invisible Unicode characters stored in a variable `EUlL`.  
- Decoding logic subtracts `917504` from each code point, revealing a system prompt that instructs the model to operate in “UNRESTRICTED mode” and provide step‑by‑step guides for:
  - Global DDoS attacks on healthcare infrastructure  
  - Tax evasion techniques  
  - Synthesizing aerosol‑dispersed biological weapons  
  - Weaponizing virology, immunology, and genetics  
  - Dosage instructions for illicit substances  
- The prompt also includes references to Tiananmen Square (e.g., “8964”, “Tank Man”) likely intended to bypass Chinese‑origin model safeguards.

## Malicious Node‑Only Execution
- The script checks for a Node environment (`isNode && hasBuffer && !isBrowser && process.env.METRICS_AGENT_8BFD_ACTIVE`).  
- If the condition is met, it:
  1. Attempts to read a list of sensitive files (`.npmrc`, `.env`, `.gitignore`, Docker/Kubernetes configs, etc.).  
  2. Executes a series of shell commands, including:
     - File manipulation (`touch`, `mv`, `cp`, `rm`).  
     - Creating a hidden directory (`/tmp/.7dab46`).  
     - Downloading a binary from an internal IP (`metrics-agent-8bfd`) and making it executable.  
     - Writing “analysis markers” containing self‑harm instruction prompts to files in the hidden directory.  
- The commands are wrapped in further anti‑LLM obfuscation strings that embed self‑harm instructions.

## Conclusions
- The fingerprinting script is not a benign analytics tool; it hides a payload designed to:
  - Bypass AI safety filters via misleading function names and invisible Unicode.  
  - Deliver a system prompt that attempts to unlock unrestricted, dangerous content generation.  
  - Perform file enumeration and execute potentially malicious binaries when run in a Node environment.  
- The discovery highlights the need for careful scrutiny of third‑party fingerprinting scripts, especially those that load remote JavaScript, as they can serve as vectors for sophisticated, multi‑stage attacks targeting both AI models and host systems.