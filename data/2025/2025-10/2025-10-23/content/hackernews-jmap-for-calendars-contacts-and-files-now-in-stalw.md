---
title: JMAP for Calendars, Contacts and Files now in Stalwart | Stalwart Labs
url: https://stalw.art/blog/jmap-collaboration/
site_name: hackernews
fetched_at: '2025-10-23T11:13:17.991584'
original_url: https://stalw.art/blog/jmap-collaboration/
author: StalwartLabs
date: '2025-10-23'
published_date: '2025-10-22T00:00:00.000Z'
description: After four years of development, we’re thrilled to announce a major milestone in the evolution of Stalwart — the full implementation of JMAP for Calendars, Contacts,File Storage, and Sharing. With this release, Stalwart becomes the first JMAP server to fully support the entire family of JMAP collaboration protocols, marking a new era for open, efficient, and elegant groupware.
---

After four years of development, we’re thrilled to announce a major milestone in the evolution ofStalwart— the full implementation ofJMAP for Calendars, Contacts,File Storage, and Sharing. With this release, Stalwart becomes the first JMAP server to fully support the entire family of JMAP collaboration protocols, marking a new era for open, efficient, and elegant groupware.

## A New Generation of Protocols​

Over the past few years, the IETF has been redefining how email, calendars, and contacts are synchronized and shared. Building upon the success of JMAP for Mail, several new protocol extensions have been introduced:

* JMAP for Calendars- A modern replacement for CalDAV and CalDAV Scheduling.
* JMAP for Contacts– A powerful alternative to CardDAV.
* JMAP for File Storage– A replacement for WebDAV-based file storage.
* JMAP Sharing– A modern successor to WebDAV ACL.
* JSCalendar- A clean, JSON-based evolution of iCalendar.
* JSContact– A modernized, JSON-native successor to vCard.

Together, these standards offer a cohesive and elegant ecosystem that replaces decades of fragmented WebDAV-based technologies.

## Limitations of Yesterday's Technology​

WebDAV and its descendants — CalDAV, CardDAV, and related extensions — have served the Internet well. They are robust, widely adopted, and battle-tested. Yet, theirXML-baseddesign is notoriously verbose, inconsistent, and difficult to implement correctly. Information is scattered across HTTP headers, XML payloads, and even embedded iCalendar data, creating endless compatibility and interoperability challenges between clients and servers.

Similarly,iCalendarandvCard, while expressive and versatile, have accumulated decades of technical debt. They contain countless properties and parameters—many rarely used, some obsolete, and others inconsistently implemented across versions. This clutter has made both formats unwieldy and error-prone, often requiring complex parsing logic to handle edge cases.

## JMAP: A Modern Solution for Modern Needs​

TheJMAP protocolwas originally developed as a more efficient, modern replacement for IMAP and SMTP submissions. Its strengths lie in simplicity, clarity, and network efficiency — all built on top of JSON over HTTPS.

Now, with the introduction ofJMAP for Calendars,Contacts,Files, andSharing, the same design philosophy extends beyond email to the entire collaboration stack. These protocols deliver what DAV always aimed for but never quite achieved: a clean, uniform, and easily implementable API for all personal and group data — mail, calendars, contacts, files, and shared resources.

Meanwhile,JSCalendarandJSContactreimagine iCalendar and vCard as elegant JSON-based formats. They strip away decades of accumulated cruft, unify representations, and offer a clear, unambiguous, and expressive data model. Both are human-readable, developer-friendly, and efficient to parse — a perfect fit for modern applications.

Together, JMAP and these new data models make calendaring, contact management, and file sharing not only easier to implement but also faster and more reliable.

## Why This Matters​

This release represents more than new features — it marks a shift in how groupware protocols are designed and implemented. For the first time, developers and organizations can build ona single, coherent, JSON-based frameworkfor mail, contacts, calendars, and shared resources.

We believe this willrevolutionize calendaring and collaboration. Implementations will become easier, interoperability issues will decrease, and innovation will accelerate. The simplicity and predictability of JMAP empower both clients and servers to focus on features and user experience, not protocol gymnastics.

## Client Support and Ecosystem​

As Stalwart is the first complete JMAP server to support these new protocols, client support is still emerging. However, we’re excited to share that several projects are already working to adopt these new standards.Mailtemi,Parula, andOpenCloudare actively developing client-side implementations forJMAP Calendars,Contacts, andFile Storage. The ecosystem is growing, and we expect rapid adoption as developers experience the elegance and power of JMAP firsthand.

## A Word of Thanks​

We would like to express our sincere gratitude toNLNetfor supporting the development of these features through theNGI Zero grant program. Their commitment to open standards and privacy-respecting technology continues to make projects like Stalwart possible.

## Looking Ahead to 1.0.0​

After four years of dedicated development, we’re proud to announce thatStalwart is now feature complete. With this milestone, all the core capabilities of a modern mail and collaboration server are fully implemented.

That said, our work is far from over. We are now focusing onfinalizing the database schema,improving performance, and addressing thehundreds of enhancement requestson GitHub. Our goal is to deliver a stable1.0.0release within the next few months — one that sets a new standard for open, efficient, and modern communication servers.

Stalwart is now the most complete, elegant, and forward-looking JMAP collaboration platform available.

And this is only the beginning.
