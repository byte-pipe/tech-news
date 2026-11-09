---
title: unlocking any car from X brand in most of the world
url: https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/
date: 2026-11-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-10T04:42:42.385021
---

# unlocking any car from X brand in most of the world

# unlocking any car from X brand in most of the world

## Background
- Author owns several X‑brand vehicles and uses their connected‑car platform since 2023.  
- Prior skepticism about the security of such platforms led to a joint investigation with Sam Curry in July 2024.  
- Focus is on the internet‑facing services that enable remote actions (e.g., unlocking) rather than hardware exploits.

## Initial Reconnaissance
- Decompiled the mobile app APK to trace API calls.  
- Primary endpoint identified: `api.redacted-telematics.com.au` (all consumer app traffic routes here).  
- Noted additional subdomains under `*.redacted-telematics.com.au` for admin and identity services.

## Admin Tool Findings
- Discovered `admintool.redacted-telematics.com.au` exposing a plain login page with a full JavaScript bundle.  
- JavaScript contained hard‑coded API keys granting unauthenticated access to many internal APIs.  
- Capabilities observed:
  - Lookup of user accounts by email.  
  - Retrieval of VIN from a licence plate via a public registration lookup, then conversion VIN → subscriber GUID → user email (PII).  
  - Provisioning of vehicle features, adding secondary users, generating remote‑access codes.  
- However, the admin tool did **not** provide direct remote‑control commands (unlock, lock, horn, engine start).

## Identity Platform Investigation
- Authentication flow uses `login.redacted-identity.com.au` → MFA → issuance of a consumer auth token.  
- Token grants full access to `api.redacted-telematics.com.au` (REST & GraphQL) for vehicle control.  
- Platform built on ForgeRock (OpenAM/OpenIDM).  
- OpenIDM instance located at `openidm.redacted-identity.com.au`.  
- JavaScript bundle from the telematics domain leaked admin credentials for OpenIDM (intended for staging but likely functional in production).

## WAF and Exploitation Attempts
- Strong WAF rules block direct access to `/openidm/*` endpoints, returning Nginx WAF blocks.  
- Researchers attempted path‑traversal bypasses (e.g., `/XUI/..%2fopenidm/endpoint`) which partially succeeded in obtaining an admin JWT but failed to reach actual endpoints due to routing quirks.  
- Each malformed request resulted in generic errors, indicating no registered servlets for the traversed paths.

## Current Status (as of article cut‑off)
- Admin credentials are valid in production, but WAF and routing protections prevent straightforward API abuse.  
- The chain to remotely unlock any vehicle remains incomplete: plate → VIN → subscriber GUID → user email is achievable, but minting a valid auth token for arbitrary users is still blocked by the hardened OpenIDM front‑end.  

*The article continues beyond this point, detailing further attempts and any eventual breakthroughs.*