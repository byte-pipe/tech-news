---
title: 'proposal: crypto/uuid: add API to generate and parse UUID · Issue #62026 · golang/go · GitHub'
url: https://github.com/golang/go/issues/62026
site_name: hnrss
content_file: hnrss-proposal-cryptouuid-add-api-to-generate-and-parse
fetched_at: '2026-03-07T11:07:38.863897'
original_url: https://github.com/golang/go/issues/62026
date: '2026-03-07'
description: I would like to suggest the addition to the standard library of a package to generate and parse UUID identifiers, specifically versions 3, 4 and 5. The main reason I see to include it is that the most popular 3rd-party package (github.co...
tags:
- hackernews
- hnrss
---

golang

 

/

go

Public

* NotificationsYou must be signed in to change notification settings
* Fork18.8k
* Star133k

# proposal: crypto/uuid: add API to generate and parse UUID#62026

Open
Open
proposal: crypto/uuid: add API to generate and parse UUID
#62026
Labels
Proposal
Proposal-Crypto
Proposal related to crypto packages or other security issues
Proposal related to crypto packages or other security issues
Proposal-FinalCommentPeriod
Milestone
Proposal

## Description

mzattahri
opened 
on 
Aug 14, 2023
Issue body actions

I would like to suggest the addition to the standard library of a package to generate and parse UUID identifiers, specifically versions 3, 4 and 5.

The main reason I see to include it is that the most popular 3rd-party package (github.com/google/uuid) is a staple import in every server/db based Go program, as confirmed by a quickGithub code search.

Additionally:

* UUID isa standard;
* The interface exposed bygithub.com/google/uuidhas been stable for years.

Addendum

Would like to point out how Go is rather the exception than the norm with regards to including UUID support in its standard library.

* C#
* Java
* JavaScript
* Python
* Ruby
Reactions are currently unavailable
Pinned by
 
neild
Pinned comment options
neild
on 
Feb 25, 2026

Updated proposal with more permissive Parse, Nil and Max as vars, and a reference to RFC 9562 in the Compare documentation:// Package uuid provides support for generating and manipulating UUIDs.//// See [RFC 9562] for details.//// Random components of new UUIDs are generated with a// cryptographically secure random number generator.//// UUIDs may be generated using various algorithms.// The [New] function returns a new UUID generated using// an algorithm suitable for most purposes.//// [RFC 9562]: https://www.rfc-editor.org/rfc/rfc9562.htmlpackageuuid// A UUID is a Universally Unique Identifier as specified in RFC 9562.//// UUIDs are comparable, such as with the == opera…

View full comment 

## Metadata

## Metadata