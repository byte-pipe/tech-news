---
title: What To Do If Your Project Was Affected By The Vercel Breach - DEV Community
url: https://dev.to/dumebii/vercel-got-breached-heres-exactly-what-to-do-if-you-use-it-2026-guide-2k76
date: 2026-04-21
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:03:57.723725
---

# What To Do If Your Project Was Affected By The Vercel Breach - DEV Community

# Summary of “What To Do If Your Project Was Affected By The Vercel Breach”

## What Happened in the Vercel Breach (Plain English)

- Date of disclosure: 19 April 2026.  
- Attack chain:
  1. A Vercel employee linked their Google Workspace account to the third‑party AI tool **Context.ai** and granted broad permissions.  
  2. Context.ai was compromised in February 2026 after an employee’s machine was infected with Lumma Stealer malware, stealing OAuth tokens.  
  3. Attackers used the stolen OAuth token to access the employee’s Google account, bypassing MFA.  
  4. From the Google account they moved laterally into Vercel’s internal tools and read customer environment variables that were **not** marked “sensitive”.  
- Stolen data: plaintext values of non‑sensitive environment variables (API keys, DB URLs, tokens, etc.).  
- Sensitive variables (encrypted at rest) remain protected.  
- Threat actor (claimed ShinyHunters) attempted to sell the data for $2 million.  
- Vercel engaged Mandiant, CrowdStrike, and law enforcement.

## Am I Affected?

- Vercel says only a “limited subset of customers” were directly contacted.  
- If you have **not** received an email from Vercel, you are likely not in the confirmed‑affected group, but assume worst case.  
- Reasons to treat all credentials as potentially exposed:
  - Ongoing investigation; more data may be discovered.  
  - OAuth tokens issued as early as June 2024 could have been active for months before detection.  
- Practical rule: rotate any environment variable that was not marked “sensitive” and contains real credentials.

## How To Secure Your Vercel Account Right Now (In Order)

1. **Identify non‑sensitive environment variables**  
   - Open the Vercel dashboard → each project → Environment Variables tab.  
   - Use the new overview page to audit variables across all projects.  

2. **Rotate exposed credentials**  
   - Log in to the service that issued the credential (AWS, OpenAI, Stripe, etc.).  
   - Generate a new key/secret.  
   - Update the Vercel variable with the new value and mark it “Sensitive”.  
   - Redeploy the project.  
   - Revoke the old key in the issuing service.  

3. **Prioritise rotation by blast radius**  
   - **Tier 1 (critical):** Cloud provider keys, database connection strings, payment processor keys, source‑control tokens.  
   - **Tier 2 (high):** SaaS API keys (OpenAI, SendGrid, etc.), email signing keys, webhook secrets.  
   - **Tier 3 (medium):** Internal service tokens, feature flags, non‑credential config values.  

4. **Check activity logs for suspicious activity**  
   - Review the past 30 days in each service (AWS CloudTrail, GCP Audit Logs, GitHub audit log, Vercel activity log).  
   - Look for unknown IPs, foreign countries, unexpected resource changes, or unknown OAuth apps.  

5. **Revoke unnecessary third‑party app access**  
   - Google Account → Security → Third‑party apps with account access → revoke unused or overly‑permissive apps.  
   - Repeat for Microsoft 365 and GitHub OAuth applications.  

6. **Upgrade authentication**  
   - Enable passkeys or an authenticator‑app‑based MFA for Vercel and other critical accounts.  
   - Replace SMS‑based 2FA with hardware or app‑based methods.  

Following these steps addresses the majority of the risk and helps ensure that any potentially exposed credentials are no longer usable by attackers.