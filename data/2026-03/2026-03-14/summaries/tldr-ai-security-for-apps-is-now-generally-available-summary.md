---
title: AI Security for Apps is now generally available
url: https://blog.cloudflare.com/ai-security-for-apps-ga/
date: 2026-03-14
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-14T06:01:55.069932
---

# AI Security for Apps is now generally available

# AI Security for Apps is now generally available

## Overview
- Cloudflare announces the general availability of **AI Security for Apps**, a solution that detects and mitigates threats to AI‑powered applications.
- New capabilities include **custom topics detection** and **custom prompt extraction**.
- AI endpoint discovery is now free for all Cloudflare customers (Free, Pro, Business).
- Partnerships expanded with **IBM** (cloud customers) and **Wiz** (unified AI security posture).

## New Attack Surface
- AI applications accept natural language and produce probabilistic outputs, making deterministic security rules ineffective.
- Risks include **prompt injection**, **sensitive data leakage**, **unbounded consumption**, and **tool‑call abuse** (e.g., unauthorized refunds or data access).
- OWASP Top 10 for LLM Applications catalogs these threats.
- Real‑world example: Newfold Digital’s teams are adding generative AI safeguards but acknowledge inevitable gaps.

## What AI Security for Apps Provides
### Discovery (free for everyone)
- Automatically identifies LLM‑powered endpoints across web properties, independent of model or hosting location.
- Uses behavioral analysis rather than URL patterns; requires sufficient valid traffic.
- Discovered endpoints appear under **Security → Web Assets** labeled `cf-llm`.
- Free plan users trigger discovery manually; paid plans run it continuously in the background.

### Detection
- Continuous inspection of every prompt with modules for:
  - Prompt injection
  - PII exposure
  - Toxic or sensitive topics
- Results are attached as metadata for custom WAF rule enforcement.
- Leverages Cloudflare’s global network (≈20 % of web traffic) to surface emerging attack patterns.

#### Custom topics detection (new in GA)
- Users define business‑specific off‑limit topics (e.g., securities, patient data, competitor products).
- System returns a relevance score for each prompt, enabling logging, blocking, or custom handling.

#### Custom prompt extraction (new in GA)
- Identifies the exact location of the prompt within request payloads using known JSON structures for major providers (OpenAI, Anthropic, Google Gemini, etc.).
- When unknown, applies a secure default that scans the whole body (may cause false positives).
- Upcoming feature: user‑defined JSONPath expressions and automatic prompt‑learning to reduce false positives.

### Mitigation
- Threats can be blocked, logged, or responded to via the existing WAF rule engine.
- Combines AI‑specific signals with broader request context (IP reputation, fingerprinting, botnet activity).
- Enables nuanced decisions, e.g., distinguishing a lone injection attempt from one originating from a known malicious source.

## Ecosystem Growth
- AI Security for Apps will be accessible through Cloudflare’s ecosystem, including integration with **IBM Cloud Internet Services (CIS)**.
- Collaboration with **Wiz** provides mutual customers a consolidated view of AI security posture.
