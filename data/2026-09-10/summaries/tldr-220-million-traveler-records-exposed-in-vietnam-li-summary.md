---
title: 220 million traveler records exposed in Vietnam-linked APIS leak
url: https://www.bleepingcomputer.com/news/security/220-million-traveler-records-exposed-in-vietnam-linked-apis-leak/
date: 2026-09-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-10T07:21:36.649939
---

# 220 million traveler records exposed in Vietnam-linked APIS leak

# 220 million traveler records exposed in Vietnam-linked APIS leak

## Overview
- An Advance Passenger Information System (APIS) database containing over 220 million passenger and crew records was found exposed online.
- The database appears to be linked to a Vietnamese organization and covers travel from January 2017 to April 2026.
- Researchers from Kinryū Labs discovered the exposure on 3 June 2026 while investigating ransomware‑related databases.

## Data contained in the leak
- **Total entries:** 220,783,700 (210,318,069 passenger records + 10,465,631 crew records).
- **Personal details:** names, dates of birth, sex, nationality, passport/travel‑document numbers, expiration dates, issuing countries.
- **Travel details:** flight numbers, dates, airlines, departure/destination/transit airports, seat assignments, baggage references, scheduled/estimated/actual flight times.
- Records include travelers from many nationalities (e.g., Korean, Chinese, Canadian, New Zealand) and airlines across Asia‑Pacific, Europe, and the Middle East.
- The figures represent travel events; individuals who flew multiple times appear multiple times.

## How the database was accessed
- Access required chaining two misconfigurations:
  1. An internet‑facing endpoint returned HTTP 401 “Unauthorized,” blocking direct access.
  2. A cloud‑based path allowed reachability to the Elasticsearch cluster, which accepted default credentials.
- FOFA first logged the host and port in October 2022 and identified it as a database in July 2023, but the exact start of data exposure is unknown.
- The exposure duration cannot be determined from the available information.

## Response and remediation
- Kinryū Labs reported the issue to Vietnamese authorities, airline representatives, and national computer emergency response teams on 3 June.
- The database was secured on 8 June after coordinated effort with Singapore Airlines’ security team.
- No ransom note or evidence of the data being sold or downloaded was found, though researchers could not confirm whether any copies were taken.

## Open questions
- Whether the data was ever downloaded, sold, or otherwise exploited remains unclear.
- No confirmation from Vietnamese authorities or the operating organization has been received.
- Further technical details are expected to be published by Kinryū Labs later in the week.

## Related articles
- IDScan sued over alleged data breach affecting 153 million drivers  
- FulcrumSec claims Manchester Airports hack, theft of 86 GB of data  
- ExfilSquad hackers leak info of over 100,000 UK police officers, staff  
- Coca‑Cola confirms data theft in Fairlife ransomware attack  
- DentaQuest data breach exposed info of 2.6 million accounts