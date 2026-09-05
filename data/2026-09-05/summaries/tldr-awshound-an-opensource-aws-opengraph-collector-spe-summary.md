---
title: AWSHound: An OpenSource AWS OpenGraph Collector - SpecterOps
url: https://specterops.io/blog/2026/08/19/awshound-opensource-aws-opengraph-collector/
date: 2026-09-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-05T10:36:14.678371
---

# AWSHound: An OpenSource AWS OpenGraph Collector - SpecterOps

# AWSHound: An OpenSource AWS OpenGraph Collector

## Overview
- AWSHound is a read‑only collector that converts an AWS account or an entire AWS Organization into a BloodHound Community Edition (BHCE) OpenGraph dataset.  
- It performs offline IAM policy evaluation so that edges are created only when a principal’s effective permissions truly allow an action, taking SCPs, RCPs, and permission boundaries into account.  
- The resulting graph can be analyzed with BloodHound’s built‑in path‑finding to reveal realistic attack pathways between AWS principals.  
- The tool is free, self‑hosted, and works with both the Community and Enterprise editions of BloodHound.  
- Enterprise customers can apply for SpecterOps’ official enterprise AWS beta program.

## The Problem
- Determining “where can I end up starting from my current access?” is difficult in AWS because permissions depend on four variables: principal, action, resource, and request context.  
- Permissions are assembled from multiple policy sources (inline, managed, group‑inherited, permission boundaries, Service Control Policies, and resource‑specific policies such as S3 bucket policies or Lambda trust policies).  
- No single console or CLI view presents all four variables together, making manual analysis error‑prone.  
- Existing tools either evaluate a single action for a single principal per API call (e.g., `iam:SimulatePrincipalPolicy`) or require extensive custom graph viewers.

## Policy Evaluation Challenges
- Combining identity‑side and resource‑side policies varies by service (e.g., STS requires both identity and trust policy, S3 uses identity **OR** bucket policy, Lambda uses identity **OR** function policy).  
- KMS follows a unique three‑layer evaluation (key policy, account root delegation, KMS grant) and currently supports only same‑account edges.  
- Conditional statements (IP address, MFA, tags, region, etc.) introduce an “unknown” state; AWSHound assumes unknown allows are kept (favoring the attacker) and unknown denies are dropped.  
- Scaling offline evaluation across thousands of principals and dozens of accounts avoids the impracticality of making millions of API calls.

## Why BloodHound and Why Free
- Existing collectors (ApeMan, PMapper, Aurelian, Cartography) ship their own graph interfaces, requiring additional development effort and user training.  
- BloodHound already solves three critical challenges:
  - **Volume:** Handles large graphs efficiently.  
  - **Pathfinding:** Provides built‑in shortest‑path queries via Cypher.  
  - **Familiarity:** Analysts are already comfortable with its UI.  
- Using BloodHound’s OpenGraph format lets AWSHound focus on accurate data collection without re‑implementing a graph viewer.

## Key Takeaways
- AWSHound makes complex, multi‑hop AWS attack paths visible by generating a precise permission graph offline.  
- It leverages BloodHound’s mature graph storage and analysis capabilities, reducing development overhead and user learning curve.  
- The project is open source, free, and integrates with existing security workflows, while offering an enterprise beta for larger organizations.