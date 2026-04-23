---
title: "Surveillance vendors caught abusing access to telcos to track people's phone locations, researchers say | TechCrunch"
url: https://techcrunch.com/2026/04/23/surveillance-vendors-caught-abusing-access-to-telcos-to-track-peoples-phone-locations-researchers-say/
date: 2026-04-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:04:37.194519
---

# Surveillance vendors caught abusing access to telcos to track people's phone locations, researchers say | TechCrunch

# Surveillance vendors exploiting telecom networks to track phones

## Background
- Citizen Lab released a report exposing two separate spying campaigns that misuse weaknesses in global telecom infrastructure.
- The campaigns are believed to represent a broader pattern of surveillance vendors seeking access to phone networks.
- Vendors operated as “ghost” companies, posing as legitimate cellular providers to obtain network access.

## Telecom providers used as entry points
- **019Mobile** (Israeli operator) – identified as a conduit for several surveillance attempts.
- **Tango Networks U.K.** (British provider) – used for surveillance activity over multiple years.
- **Airtel Jersey** (Channel Island operator, owned by Sure) – linked to prior surveillance campaigns.
- Sure’s CEO Alistair Beak denied knowingly leasing signaling access for tracking and described mitigation measures.

## Technical methods exploited
- **SS7 (Signaling System 7)**
  - Legacy protocol for 2G/3G networks lacking authentication and encryption.
  - Allows rogue operators to query location data of phones.
- **Diameter**
  - Intended replacement for SS7 in 4G/5G networks with added security.
  - Exploitable when carriers fail to implement its protections; attackers can fallback to SS7.
- **SIMjacker attacks**
  - Special SMS messages sent to a target’s SIM card, invisible to the user.
  - Commands turn the phone into a location‑tracking device.
  - First identified by Enea in 2019; considered common and hard to detect.

## Campaign details
- **First campaign**
  - Spanned several years, targeted various global subjects.
  - Utilized SS7 flaws, switching to Diameter when needed.
  - Researchers infer multiple government customers behind the operation.
- **Second campaign**
  - Focused on a single “high‑profile” target.
  - Relied on SIMjacker‑style SMS commands to covertly track the device.

## Researchers’ observations
- The operations show deliberate, well‑funded integration into mobile signaling ecosystems.
- Clues suggest involvement of an Israeli‑based commercial geo‑intelligence provider, though unnamed.
- Researchers view the two examined campaigns as only the “tip of the iceberg” among millions of global attacks.

## Responses from involved parties
- Sure (owner of Airtel Jersey) issued a statement denying intentional leasing of signaling for tracking and outlined monitoring and blocking measures.
- Tango Networks and 019Mobile did not comment when contacted by TechCrunch.
- Gil Nagar, head of IT and security at 019Mobile, sent a letter stating the company cannot confirm that the identified infrastructure belongs to them.

## Implications
- Ongoing exploitation of both legacy (SS7) and newer (Diameter) signaling protocols highlights gaps in carrier security implementations.
- The use of ghost companies underscores the difficulty of vetting network access partners.
- The prevalence of SIMjacker attacks suggests a need for broader detection and mitigation strategies across carriers worldwide.