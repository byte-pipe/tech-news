---
title: "Anatomy of Apple's Personal Knowledge Graph — Eighth Rank"
url: https://8rank.ai/game/apple-intelligence-personal-knowledge-graph
date: 2026-11-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:03:44.809263
---

# Anatomy of Apple's Personal Knowledge Graph — Eighth Rank

# Anatomy of Apple's Personal Knowledge Graph

## Overview
- Since macOS 13 (2022) every Mac runs two daemons, **knowledgeconstructiond** and **intelligenceplatformd**, whose sole purpose is to build a personal knowledge graph (PKG) about the user and their contacts.  
- The PKG aggregates data from Contacts, Calendar, Photos, Messages, Mail, location, Screen Time, and many low‑level device signals.  
- Apple claims the graph is stored locally and queried by on‑device large language models (LLMs).

## Data Storage
- All graph data resides in `~/Library/IntelligencePlatform`, protected by TCC Full Disk Access.  
- The most important file is `graph.db`, a SQLite triple store containing:
  - **181 entity classes** (people, places, events, apps, etc.).
  - **278 predicates** that describe relationships (employer, family member, communication partner, etc.).
  - Each edge is represented by two rows sharing a `relationshipId`, allowing confidence scores and timestamps per relationship.

## Sources of Information
- **Contacts** – names, emails, phone numbers.  
- **Photos** – facial recognition links people appearing together.  
- **Calendar** – event titles, attendees, times.  
- **Family Sharing** – family members and ages.  
- **Health** – emergency contact from Medical ID.  
- **Siri Suggestions** – people extracted from Mail and Messages.  
- **App Intents** – contacts donated by third‑party apps.  
- **Installed apps** – app identifiers and metadata.  
- **Communication logs** – who communicated, when, via which app (content omitted).  
- **Location & movement** – GPS traces, Wi‑Fi/Bluetooth proximity.  
- **Device signals** – screen lock, charging state, ambient light, etc.  
- Additional tables record co‑appearance in photos, physical proximity logs, and contextual understanding streams.

## Inference Mechanisms
- The daemons infer relationships such as employment, family ties, social circles, and roles.  
- Confidence values are stored per edge, allowing later retraction if the inference is deemed uncertain.  
- Some entity classes (e.g., `SB470` “device primary user”) are present but the exact inference path was not identified by the authors.

## Prior Research & Tools
- Apple published a 2023 research paper describing the underlying techniques but omitted implementation details.  
- Independent investigations:
  - Nic Lydon’s “I Built a Personal Knowledge Graph. Apple Had Already Built One on My Laptop.”  
  - Alexis Brignoni’s iLEAPP extension for iOS, reading `graph.db` and `ontology.db` from `/private/var/mobile/Library/IntelligencePlatform`.  
- The authors released an open‑source dashboard **iKnow** to let users explore their own PKG on macOS.

## Privacy and Security Implications
- The PKG consolidates a rich portrait of a user’s social network, habits, and movements in a single, queryable store.  
- If compromised, an attacker could combine the graph with a powerful LLM to generate highly personalized phishing, social engineering, or surveillance attacks.  
- The graph represents a “single point of failure” for privacy, especially because it is stored in plaintext SQLite files (albeit behind TCC restrictions).

## Conclusions
- macOS now continuously constructs a detailed, on‑device knowledge graph using a wide array of personal data sources.  
- The graph is exposed through `graph.db`, which can be inspected with the provided iKnow tool.  
- Understanding the PKG’s scope is essential for evaluating privacy risks and for developing mitigations against potential exploitation.