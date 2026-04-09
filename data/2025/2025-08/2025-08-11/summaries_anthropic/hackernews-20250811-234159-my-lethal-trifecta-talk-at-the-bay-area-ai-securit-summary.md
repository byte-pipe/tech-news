---
title: My Lethal Trifecta talk at the Bay Area AI Security Meetup
url: https://simonwillison.net/2025/Aug/9/bay-area-ai/
date: 2025-08-11
site: hackernews
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-08-11T23:41:59.872749
---

# My Lethal Trifecta talk at the Bay Area AI Security Meetup

This article discusses the problem of "prompt injection" - a security vulnerability that arises when AI systems are built by concatenating trusted instructions and untrusted user input. The key insights for a solo developer building a profitable business are:

1. Problem/Opportunity: Prompt injection is a growing security challenge as more powerful AI systems are built on top of large language models (LLMs). There is a strong demand for "digital assistants" that can safely handle sensitive tasks like email, but the risk of prompt injection attacks has prevented their widespread adoption so far.

2. Market Indicators: The author has documented numerous instances of prompt injection vulnerabilities being discovered in high-profile AI chatbots and assistants over the past 3 years. This indicates a significant market need for secure AI systems that can handle sensitive user data and tasks.

3. Technical Feasibility: Addressing prompt injection is technically complex, requiring careful input sanitization, domain whitelisting, and other advanced security measures. This may be challenging for a solo developer, but the author provides useful insights like the limitations of "prompt begging" and AI-based detection approaches.

4. Business Viability: The willingness of major tech companies to invest in AI assistants, and the lack of a widely adopted secure solution, suggests there is a viable business opportunity for a solo developer who can effectively address the prompt injection problem. Potential revenue streams could include selling a secure AI platform, offering consulting/integration services, or licensing the technology.

Key quotes:
- "We need to be very confident that this [prompt injection] won't work! Three years on we still don't know how to build this kind of system with total safety guarantees."
- "If we protected our databases against SQL injection with defenses that only worked 99% of the time, our bank accounts would all have been drained."
- "The whole point of an adversarial attacker is that they will keep on trying every trick in the book (and all of the tricks that haven't been written down in a book yet) until they find something that works."

Overall, this article highlights a significant security challenge in the AI industry that represents a promising business opportunity for a solo developer who can develop effective solutions.
