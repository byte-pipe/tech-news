---
title: My company packaged 12 years of my experience into an AI Skill, then laid me off. When it crashed, the CTO called at 5x my salary. - DEV Community
url: https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e
date: 2026-06-08
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-09T06:49:05.653792
---

# My company packaged 12 years of my experience into an AI Skill, then laid me off. When it crashed, the CTO called at 5x my salary. - DEV Community

# Static AI failing in dynamic systems – Summary

## Act 1 – Knowledge Extraction
- Spent three months in a windowless conference room answering an engineer’s questions about my infrastructure decisions.  
- The recordings were used to build an “AI Skill” that encoded my 12 years of experience.  
- The system could reproduce my diagnostic reasoning faster than I could.

## Act 2 – “96.8% Accuracy”
- Validation presented a Knowledge Retention Rate of 96.8 % across 312 historical failure scenarios.  
- The CTO announced that I had essentially created my own replacement.  
- I realized the manual I was writing would soon make the original author redundant.

## Act 3 – The Severance
- The CTO informed me that my role was eliminated; I received three months’ severance.  
- I quickly registered a consulting LLC, obtained liability insurance, and set an hourly rate of $215.

## Act 4 – AI Skill Goes Live
- The AI Skill took over 70 % of tier‑2 tickets, cutting onboarding time for new engineers from six months to three weeks.  
- The company marketed the skill as “12 years of Mark’s experience available as a prompt.”  
- A new Platform Lead rebuilt the monitoring stack but never re‑validated the skill after migrating to Kafka.

## Act 5 – Crash
- At 3:47 am a latency spike in the payment chain triggered a cascade failure.  
- The AI Skill diagnosed the issue as “message broker latency – apply 450 ms retry backoff,” a solution that had succeeded in 312 prior cases.  
- The 450 ms backoff was tuned for an old RabbitMQ setup; on the current Kafka consumer group it caused poll timeouts, rebalance storms, and amplified the outage.  
- The skill failed not because its logic was wrong, but because it was based on a legacy architecture that no longer existed.

## Act 6 – The Call
- The former CTO called me at 4:12 am, calm but urgent, seeking help to resolve the incident caused by the outdated AI recommendation.  
- The call underscored the risk of relying on static AI knowledge in a constantly evolving system.