---
title: 220 million traveler records exposed in Vietnam-linked APIS leak
url: https://www.bleepingcomputer.com/news/security/220-million-traveler-records-exposed-in-vietnam-linked-apis-leak/
site_name: tldr
content_file: tldr-220-million-traveler-records-exposed-in-vietnam-li
fetched_at: '2026-09-10T07:20:54.880522'
original_url: https://www.bleepingcomputer.com/news/security/220-million-traveler-records-exposed-in-vietnam-linked-apis-leak/
date: '2026-09-10'
description: 'Exclusive: An exposed Advance Passenger Information System (APIS) database held 220 million passenger and crew records containing names, passport numbers, dates of birth, nationalities, and flight details spanning 2017 to 2026. Researchers accessed the Vietnam-linked system through a cloud-based path using default credentials.'
tags:
- tldr
---

# 220 million traveler records exposed in Vietnam-linked APIS leak

 By 

###### Ax Sharma

* September 8, 2026
* 03:35 AM
* 0

An Advance Passenger Information System (APIS) database holding more than 220 million passenger and crew records, including passport numbers and flight details, was accessible online through a chain of security misconfigurations. The system appears linked to a Vietnamese organization, according to the researchers who discovered it.

Advance Passenger Information Systems are used worldwide to collect identity, passport, and flight information from airlines before passengers and crew arrive at or depart from a country.

The exposed records span January 2017 to April 2026 and could involve travelers of many nationalities who flew to, from, or through Vietnam during that period.

## Nine years of passenger and crew data

Kinryū Labs discovered the Elasticsearch cluster on June 3 while surveying exposed databases as part of research into ransomware activity.

The cluster, named 'pax-info', contained 29 indices and roughly 107 GB of data. Its two principal indices held 210,318,069 passenger records and 10,465,631 crew records, for a combined 220,783,700 entries.

According to Kinryū Labs, the cluster was hosted in Viettel-assigned IP space in Hanoi. BleepingComputer could not confirm which Vietnamese organization operated the system.

The exposed information included passengers' and crew members' names, dates of birth, sex, nationalities, passport or travel-document numbers, document expiration dates, and issuing countries.

Associated travel data included flight numbers and dates, airlines, departure, destination and transit airports, seat assignments, baggage references, and scheduled, estimated, and actual flight times, information typically carried by APIS and related airline systems.

Sample records reviewed by BleepingComputer included travelers of Korean, Chinese, Canadian, and New Zealand nationality, among others.

Sample database records showing passenger names, nationalities, passport information, and flight details

(Kinryū Labs)

While the researchers could not provide a complete breakdown by nationality, the data covered numerous international airlines across Asia-Pacific, Europe, and the Middle East. As a result, the exposed records could relate to people from virtually anywhere who visited or transited through Vietnam over the nine-year period.

Kinryū Labsverified that the information was legitimate by matching records in the database against its researchers' own travel to Vietnam.

The figures represent travel records rather than unique individuals. Passengers and crew members who flew multiple times may therefore appear repeatedly in the database.

## Database accessible through chained misconfigurations

Kinryū Labs told BleepingComputer that it reached the database by chaining two misconfigurations.

From the open internet, the endpoint returned an HTTP 401 "Unauthorized" response, preventing direct access to the database. However, a cloud-based path enabled researchers to reach the cluster, which then accepted default credentials.

Internet intelligence platform FOFA first recorded the host and port in October 2022 and identified the service as a database in July 2023. However, Kinryū Labs could not determine when the passenger data first became retrievable through the second access path.

As a result, while the records themselves span more than nine years, the actual length of the exposure is unknown.

Kinryū Labs said it reported the issue to Vietnamese authorities, airlines represented in the database, and national computer emergency response teams beginning June 3. The researchers said access to the database was remediated on June 8.

An authenticated email reviewed by BleepingComputer shows that Singapore Airlines' security team helped coordinate the response, informing Kinryū Labs on June 8 that it had "engaged the relevant parties" and "taken steps to contain the issue." Singapore Airlines did not provide an additional comment to BleepingComputer.

The findings shared with BleepingComputer identify several major airlines whose passenger records appeared in the database. However, there is no indication that the airlines operated the exposed system or that their own networks were compromised.

Changi Airport Group, which manages and operates Singapore's Changi Airport, told BleepingComputer that it had investigated the matter but declined to comment.

BleepingComputer also contacted Vietnamese authorities well in advance of publication but received no response.

It remains unclear whether the database was downloaded, sold, ransomed, or otherwise exploited by malicious actors before it was secured. Kinryū Labs said it found no ransom notes or unfamiliar indices on the cluster and could not identify the dataset being offered for sale online.

However, without access to server logs, the researchers could not conclusively determine whether anyone had copied the data.

Kinryū Labs expects to publish additional technical findings on itsbloglater this week.

## Once attackers have valid credentials, only 37% of their actions are blocked

Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply.

The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments.

Get the report

### Related Articles:

IDScan sued over alleged data breach affecting 153 million drivers

FulcrumSec claims Manchester Airports hack, theft of 86 GB of data

ExfilSquad hackers leak info of over 100,000 UK police officers, staff

Coca-Cola confirms data theft in Fairlife ransomware attack

DentaQuest data breach exposed info of 2.6 million accounts