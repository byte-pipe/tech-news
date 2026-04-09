---
title: Serving 200 million requests per day with a cgi-bin
url: https://simonwillison.net/2025/Jul/5/cgi-bin-performance/
date: 2025-07-07
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-07T23:41:41.500736
---

# Serving 200 million requests per day with a cgi-bin

**Analysis**

The article discusses a solo developer's test of serving 200 million requests per day using a CGI (Common Gateway Interface) program running on relatively modest hardware. The developer, Jake Gold, is using a Go + SQLite CGI program to achieve this feat.

**Market Indicators**

* User adoption: No explicit mentions of user adoption, but the article implies that there are many developers testing and experimenting with 90s-era CGI.
* Revenue mentions: None
* Growth metrics: The article mentions growth in computing power (from AMD's 3700X to modern CPUs) but does not provide specific revenue or user demographics.

**Technical Feasibility for a Solo Developer**

* Complexity: A complex system like this would be challenging even for an experienced solo developer. Testing and debugging such systems can take significant time and resources.
* Required skills: The developer will need expertise in Go, SQLite, and likely other system-related technologies to maintain and optimize the CGI program.

**Business Viability Signals**

* Willingness to pay: There is no mention of how much the business itself was paying for such an endeavor. However, readers may be interested in what pricing strategy the author employs.
* Existing competition: None
* Distribution channels: Likely limited direct-to-users or testing-focused web development communities.

**Actionable Insights**

1. **Refactor from CGI to a real application**: If this solo developer aims to make significant increases in efficiency and scalability, consider refactoring their system into a more structured application with clear data structures and proper error handling.
2. **Consider using cloud services for increased resources**: Instead of relying on single-server hardware, look into cloud providers like AWS or Google Cloud that can offer greater resource availability.
3. **Evaluate cost per user**: While the exact pricing strategy is not outlined in this article, consider how the costs per users might differ compared to a traditional web application.
4. **Highlight limitations and improvements**: Acknowledge the challenges of scaling CGI-style applications on relatively modest hardware and outline potential solutions or modifications to improve efficiency.

**Specific Numbers**

* Requests per day: 200 million
* Requests per second (approximate): 2400+
* CPU threads available on servers with 16 CPUs, compared to the original AMD 3700X which could achieve ~2-4 CPU cores.

**Quotes about Pain Points**

None mentioned in this article.
