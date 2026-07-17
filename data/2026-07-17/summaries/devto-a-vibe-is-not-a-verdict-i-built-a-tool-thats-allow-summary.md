---
title: "A Vibe Is Not a Verdict: I Built a Tool That's Allowed to Say 'I Don't Know' - DEV Community"
url: https://dev.to/copyleftdev/a-vibe-is-not-a-verdict-i-built-a-tool-thats-allowed-to-say-i-dont-know-4foe
date: 2026-07-13
site: devto
model: llama3.2:1b
summarized_at: 2026-07-17T11:39:00.398081
---

# A Vibe Is Not a Verdict: I Built a Tool That's Allowed to Say 'I Don't Know' - DEV Community

Here is a concise and informative summary of the article in Markdown format:

### **Introduction**

* A new tool called kiloCheck has been built for vetting suspicious links.
* The creator, who remains anonymous due to an "exciting opportunity" job description, wanted to ensure their knowledge ended there.

### **The Challenge**

* The creator received a recruiter pitch for a Quality Engineer role at an aerospace firm with a mysterious link as the source of the message.
* The message included multiple unrelated trades in one job title and claimed skills that don't match the person's resume.

### **The Toolkilo**

* kiloCheck is an offline IP-reputation engine written in Rust that uses a four-stage pipeline for threat analysis:
  * ingest signed threats
  * normalize observations
  * compile to local index
  * check IPs against it

### **Features and Design**

* kiloCheck has a binary design with limited networking.
* The tool verifies going in cryptographically without calling APIs.
* Install is done using a checksum and self-copy procedure.
* Tool status provides a verified freshness report on a signed data release.

### **Goals and Limitations**

* kilo is designed to be quick, knowing its limits.
* The creator aims to ensure they know where their knowledge ends by testing the tool "to see one link that isn't".

### **Morning Experiment**

* The morning began with a familiar frustration - receiving suspicious links without taking action.
* After re-testing the tool, the creator knew it was more than just an annoyance.
* kiloCheck had proven its utility for vetting suspicious links without revealing sensitive information.