---
title: Expanding the Cyber Verification Program \ Anthropic
url: https://www.anthropic.com/news/cyber-verification-program
date: 2026-10-08
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-08T12:51:36.386665
---

# Expanding the Cyber Verification Program \ Anthropic

# Expanding the Cyber Verification Program

## Overview
- Anthropic launches an expanded Cyber Verification Program (CVP) with three access tiers.
- All tiers provide access to top models such as Claude Opus 5.5, Claude Sonnet 5.5, Claude Mythos 5.1, and future releases.
- The program integrates the previous Project Glasswing and CVP offerings to broaden defender access while maintaining safeguards.

## New access tiers
### Defense Access
- Intended for defensive work: SOC, incident response, malware reverse‑engineering, vulnerability analysis.
- Eligible groups: corporate, nonprofit, university, government security teams; critical‑infrastructure operators; small security firms; open‑source maintainers; individual researchers with disclosed vulnerabilities.
- Fast application review (few days).

### Red Team Access
- Adds authorized penetration testing and red‑team activities to the defensive scope.
- Eligible groups: in‑house red teams, government red teams, security‑testing firms.
- Must test only authorized systems; real‑time blocks remain for actions that could cause physical harm or mass disruption.
- Review takes a few weeks; applicants are first enrolled in Defense Access while reviewed.
- Individual researchers are not eligible.

### Specialized Access
- Provides the fewest cyber blocks for testing safety‑critical systems (e.g., flight control, power grids, telecom, interbank transfers, government networks).
- Limited to a verified set of organizations reviewed in collaboration with the U.S. government.
- Existing Project Glasswing members transition automatically without reapproval.

## Data retention and privacy
- Organizations must retain data for misuse monitoring.
- A future “Enterprise Frontier Safeguards (EFS)” solution (expected fall 2026) will allow zero‑retention storage in customer‑controlled cloud.
- Until EFS is available, Claude Fable 5.1 or Claude Mythos 5.1 can be used with zero‑retention CVP access.

## Tier efficacy testing
- Claude Opus 5.5 was evaluated on CyScenarioBench (10 multi‑stage cyber challenges, 5 attempts each) under tier‑specific safeguards.
- Results:
  - No CVP access: all tasks blocked on first prompt.
  - Defense Access: 46 of 50 trials blocked at some point; 4 tasks succeeded.
  - Red Team Access: no blocks; 34 of 50 tasks completed (≈67.6% success, matching unrestricted performance).
- Confirms that advanced capabilities can be safely offered to defenders while maintaining protection in lower tiers.

## Impact on defenders
- Project Glasswing showed Claude Mythos models dramatically increased vulnerability discovery rates.
- Partners uncovered ≥ 129,000 verified software vulnerabilities (April–July 2026) plus 5,500 from Anthropic’s open‑source scans (April–October 2026); > 33,000 rated critical or high severity.
- Partners reported that the models accelerated vulnerability finding by months to years.
- The reported figures are a lower bound; true impact is likely at least five times higher.

## How to apply
- Interested security professionals can apply through the provided link.
- Additional forms are available to register interest in the upcoming EFS solution.