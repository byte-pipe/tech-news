---
title: "It’s not wrong that \"🤦🏼‍♂️\".length == 7"
url: https://hsivonen.fi/string-length/
date: 2025-08-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-24T23:23:42.485022
---

# It’s not wrong that "🤦🏼‍♂️".length == 7

Here's an analysis of the article from a solo developer business perspective:

**Problem:**
The problem being discussed is whether using JavaScript's `length` property to get the length of a string containing an emoji results in a number greater than 1, which can be misleading.

**Market indicators:**

* Python 3 is cited as having an unambiguously bad approach to string length comparisons.
* Rust is also mentioned as learning from predecessors and having a better approach, with an example provided that shows it correctly outputs 17 for "🤦🏼‍♂️".

**Technical feasibility:**
The technical feasibility of using these alternatives is:
* JavaScript (with `length` property): Requires understanding of Unicode scalar values and how strings are represented in different systems.
* Python 3: Does not have a built-in function to get the length of an emoji, but it can be implemented by parsing the string to extract the individual characters or using regular expressions.

**Business viability signals:**
The following business viability signals are present:

* No competition: The only alternative mentioned is Rust, which implies there is little to no existing competition in this space.
* Existing market size: While Python 3 has a larger user base for its sake (as noted by the author), it's possible that there is still demand for the current approach.

**Actionable insights:**

1. **Rust is a viable alternative:** As demonstrated, Rust can correctly output a number close to what would be expected from comparing an emoji string using `length` property.
2. **Understand Unicode scalar values:** Familiarize yourself with how strings are represented in different systems, as this knowledge can help you understand true lengths of strings containing emojis.
3. **Consider alternative development frameworks:** Think ahead to potential solutions that can take advantage of similar technological advancements made by JavaScript (e.g., React, Angular) for string length comparisons.

**Specific numbers and quotes:**
"The total number [of Unicode scalar values] is 20 or more". However, the quote "That’s better!" at the end of the article suggests that using string length properties can be a viable approach in certain situations.
