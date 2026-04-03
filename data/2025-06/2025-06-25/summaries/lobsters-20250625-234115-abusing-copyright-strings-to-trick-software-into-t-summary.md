---
title: "Abusing copyright strings to trick software into thinking it's running on your competitor's PC - The Old New Thing"
url: https://devblogs.microsoft.com/oldnewthing/20250624-00/?p=111299
date: 2025-06-25
site: lobsters
model: llama3.2:1b
summarized_at: 2025-06-25T23:41:15.058725
---

# Abusing copyright strings to trick software into thinking it's running on your competitor's PC - The Old New Thing

**Analysis**

The article discusses the creative strategies used by a solo developer (Raymond Chen) in bootstrapping Plug and Play, a wireless networking technology, into various PC systems before its widespread adoption and standardization. The developer's main goal was to ensure compatibility with legacy hardware, despite Plug and Play being still under development.

One effective approach was searching for copyright strings in the BIOS, particularly "Not Copyright Fabrikam Computer," which was used by PCs manufacturing companies to detect if they were running on PC devices from other manufacturers (not including their own). By adding this string to the BIOS, the system could identify itself as being compatible with non-Fabrikam models. This workaround allowed the developer to retrofit Plug and Play onto legacy hardware.

**Market indicators**

* User adoption: The article suggests that compatibility issues with legacy hardware are a common pain point for businesses investing in software solutions.
* Revenue mentions: There is no mention of revenue figures, but it's essential to note that this aspect cannot be quantified without further context or data.
* Growth metrics: This text does not provide growth metrics related to the Plug and Play technology adoption.

**Technical feasibility**

* Required skills: The article does not specify the required technical expertise for developers to retrofit Plug and Play onto legacy hardware. However, it implies that it requires some programming and configuration knowledge.
* Time investment: It is likely a complex process requiring significant time and effort from the developer to create an adequate compatibility code.

**Business viability signals**

* Willingness to pay: The article does not indicate whether customers are willing to pay for this technology. However, if adopted as standard by PC manufacturers and users, compatibility with legacy hardware could lead to higher sales in the long run.
* Existing competition: The development of Plug and Play is ongoing, indicating that existing wireless networking technologies may still have a market share.

**Actionable insights**

1. Understanding copyright strings and their usage can help identify non-standardized systems or firmware versions that need compatibility improvements. Consider investigating customers' use cases to develop effective solutions.
2. Developing a compatible protocol like Plug-and-Play could lead to increased adoption of wireless networking technologies in various industries, opening new opportunities for business growth and customer satisfaction.
3. As technology advances, it is essential to keep abreast of emerging standards and compatibility issues, even for those that seem to have completed their development cycle.

Overall, this instance highlights the creative problem-solving approach used by developers working with complex technical requirements to address compatibility gaps, which ultimately can lead to increased market potential and customer satisfaction.
