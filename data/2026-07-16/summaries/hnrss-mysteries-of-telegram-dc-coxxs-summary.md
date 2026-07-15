---
title: Mysteries of Telegram DC - Coxxs
url: https://dev.moe/en/3025
date: 2026-07-15
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-16T03:40:58.276248
---

# Mysteries of Telegram DC - Coxxs

# Mysteries of Telegram DC – Coxxs

## Overview of Telegram Data Centers
- Telegram operates five data centers (DC1 ~ DC5) as referenced in its code and documentation.  
- Physical locations:  
  - **DC1** – Miami, USA  
  - **DC2** – Amsterdam, Netherlands  
  - **DC3** – Miami, USA  
  - **DC4** – Amsterdam, Netherlands  
  - **DC5** – Singapore  

- Each account is bound to a specific DC at registration; the assignment does **not** change with phone‑number changes or user location.  
- Clients cannot freely select a DC; connecting to the wrong DC triggers a migration error directing the client to the correct one.

## DC5 – The Frequently Down Center
- In Chinese Telegram circles, DC5 is notorious for repeated outages.  
- When DC5 is offline, its users cannot access Telegram and must wait for automatic reconnection attempts.  
- The downtime becomes a common discussion topic, with users from other DCs joining the chat to comment on DC5’s instability.

## The “Missing” DC2 and DC3
- A community bot that reports a user’s DC showed many users on DC1, DC4, and DC5, but **zero** on DC2 and DC3.  
- Initial speculation:  
  - DC2 and DC3 might have no users.  
  - Or they could be subordinate to DC1 and DC4, handling overflow traffic.  

## Telegram DC Allocation Rules (as of May 2022)
- **DC1, DC2, DC4, DC5**: Assignments are based on the country code of the phone number used at registration. These DCs accept new registrations continuously and host large user bases.  
- **DC3**: Previously had users, but around 2020 its existing accounts were migrated to DC1. It now likely has **no active users** and does not accept new registrations.  

- The bot’s failure to detect DC2 users stems from an **incorrect detection method**, not from the absence of DC2 accounts.

## How to Determine a User’s DC
Three common approaches were examined using a newly created DC2 account:

1. **Login Method (MTProto “auth.sendCode”)**  
   - Connect to DC1, request a verification code.  
   - Server returns `PHONE_MIGRATE_2`, indicating the account belongs to DC2.  
   - Works for any account but requires knowledge of the phone number.

2. **Profile Picture / File Method**  
   - Use a third‑party client (e.g., Plus Messenger) that reads the `dc_id` field from the `UserProfilePhoto` structure.  
   - The DC is revealed only after the user uploads a profile picture or file, because the DC is where those media are stored.

3. **Web CDN Method (Bot Query)**  
   - Bots that inspect the URL of a user’s profile picture (e.g., `cdn4`) infer the DC from the CDN domain.  
   - Since DC2 and DC3 share the CDN domains of DC4 and DC1 respectively, this method misclassifies DC2 users as DC4 and cannot detect DC3 users at all.

## Findings on DC2 and DC3
- **DC2**: Real users exist globally; the misidentification by CDN‑based bots explains why earlier surveys reported zero DC2 accounts.  
- **DC3**: Extremely rare. After testing >10,000 generated phone numbers with the Login Method, no new registrations were assigned to DC3. Existing accounts appear to have been migrated to DC1, and new users cannot be created on DC3.

## Practical Takeaways
- To join a specific DC (e.g., avoid DC5 downtime), register with a phone number whose country code maps to the desired DC (see allocation table in the original article).  
- For reliable DC detection, use the **Login Method** or the **Profile Picture/File Method**; avoid CDN‑based bot queries.  
- The article’s conclusions rely on observed behavior and speculation, as Telegram’s server internals are not open source. Corrections or additional evidence are welcomed from the community.