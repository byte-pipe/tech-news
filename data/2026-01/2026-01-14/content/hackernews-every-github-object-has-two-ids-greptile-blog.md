---
title: Every GitHub Object Has Two IDs | Greptile Blog
url: https://www.greptile.com/blog/github-ids
site_name: hackernews
fetched_at: '2026-01-14T11:08:04.415103'
original_url: https://www.greptile.com/blog/github-ids
author: dakshgupta
date: '2026-01-14'
published_date: '2025-01-13'
description: How I reverse-engineered GitHub node IDs to avoid a database migration and discovered their dual ID system along the way.
---

# Every GitHub Object Has Two IDs

Soohoon Choi • Jan 13, 2025

Table of Contents

### Table of Contents

### Table of Contents

I was recently building a feature for Greptile (an AI-powered code review tool), when I hit a weird snag with GitHub's API.

The feature should have been simple: I wanted to add clickable links to GitHub PR comments, so users could jump directly from our reviews to relevant GitHub discussions. We already stored the comment IDs, so I just needed to construct the URLs.

The problem was, when I tested it, the links didn't work.

Searching throughGitHub's documentationfor answers revealed that their team maintains two separate ID systems. We'd been using GitHub's GraphQL API, which returnsnode IDslikePRRC_kwDOL4aMSs6Tkzl8. GitHub designed these node IDs to uniquely identify any object across its entire system. But web URLs required database IDs, integer values visible in URLs and often associated with REST responses, like2475899260.

I was looking at either backfilling millions of records or migrating our entire database, and neither sounded fun. So I did what any annoyed engineer would do: I stared at these IDs for way too long, looking for a way out of the migration.

And I found it.

## Spotting a pattern between node and database IDs

I looked for a relationship between these two ID formats. I pulled up a few of our stored node IDs and opened the corresponding PR comments from the same pull request in my editor:

Node ID
Database ID
PRRC_kwDOL4aMSs
6Tkzl8
2475
899260
PRRC_kwDOL4aMSs
6Tkzya
2475
900058
PRRC_kwDOL4aMSs
6Tkz3e
2475
900382

The database IDs incremented sequentially, and the node IDs were almost identical too, differing only in their last few characters. GitHub's documentation mentioned that node IDs are base64 encoded. I tried decoding just the part afterPRRC_:

def base64_2_int(s):
 base64_part = s.split("_")[1]
 return int.from_bytes(base64.b64decode(base64_part))

The decoded values were very long (96 bit) integers:

Node ID
Decoded Integer
Database ID
PRRC_kwDOL4aMSs6Tkz
l8
454952701279253740627272
15484
24758992
60
PRRC_kwDOL4aMSs6Tkz
ya
454952701279253740627272
16282
24759000
58
PRRC_kwDOL4aMSs6Tkz
3e
454952701279253740627272
16606
24759003
82

The decoded integers were incremented by 798, exactly matching the database ID increment. The database ID had to be embedded in there somewhere.

## Extracting the database ID

Since both values were changing by the same amount, and the decoded value was 96 bits, I figured the database ID was likely embedded in the lower 32 bits of the node ID. I wrote a quick test:

def node_id_to_database_id(s):
 decoded = int.from_bytes(base64.b64decode(s.split("_")[1]))
 # Mask to keep only the lower 32 bits
 return decoded & ((1 << 32) - 1)

node_id_to_database_id("PRRC_kwDOL4aMSs6Tkzl8")
# Returns: 2475899260

It worked! The database ID was just the last 32 bits of the decoded node ID. I could skip the entire migration, and extract what I needed with a simple bitmask operation.

After the relief sunk in, I couldn't help but ask, "If the database ID only used the last 32 bits out of the 96 total bits, what were the first 64 bits being used for?"

Since the node ID is a global identifier across all of GitHub, I assumed that the extra 64 bits had to encode either the object type or an id to another resource that "owned" the current node. I wanted to see if I could decode them the same way I'd decoded the database ID.

## The archaeology of GitHub's node IDs

To understand what was in those 64 bits, I startedquerying different GitHub objects. My test repository returned the familiarPRRC_format for everything. I tried the first famous repository that came to mind,torvalds/linux, to see if the pattern held.

The response was a completely different base64 encoded string:

MDEwOlJlcG9zaXRvcnkyMzI1Mjk4
MDQ6VHJlZTIzMjUyOTg6NzIwMWJmYjkyOGIyOWU4MGIwMDVkYTE1OTc4MzQ1ZjIzYmEwZmY5Yg==
MDQ6QmxvYjIzMjUyOTg6ZjM3MWExM2I0ZDE5MmQyZTM3ZDcwMTdiNjNlMzNkZmE3YzY3Mzc4Zg==

When I decoded these they showed the following:

base64.b64decode("MDEwOlJlcG9zaXRvcnkyMzI1Mjk4")
# Returns: b'010:Repository2325298'

The Linux repository was using a completely different format. I realized the repository was created in 2011. By picking an old repository, I'd accidentally stumbled onto GitHub's legacy ID format which was quite simple:

[Object Type Number]:[Object Type Name][Database ID]

That repository ID (010:Repository2325298) had a clear structure:010is some type enum, followed by a colon, the wordRepository, and then the database ID2325298. Since repositories are just containers, I wanted to see if git objects like trees would reveal more complexity:

base64.b64decode("MDQ6VHJlZTIzMjUyOTg6NzIwMWJmYjkyOGI...")
# Returns: b'04:Tree2325298:7201bfb928b29e80b005da15978345f23ba0ff9b'

That's the enum again, the wordTree, the repository ID, and the tree SHA.

It was apparent that GitHub had two systems for ID'ing their internal objects. Somewhere in GitHub's codebase, there's an if-statement checking when a repository was created to decide which ID format to return.

I started mapping out which objects used which format. The pattern wasn't as simple as "old repos use old IDs, new repos use new IDs":

Format
Example
Usage
Legacy
MDEwOlJlcG9zaXRvcnkyMzI1Mjk4
Old repositories like torvalds/linux
New
PRRC_kwDOL4aMSs6Tkzl8
Newer repositories and most objects

Old repositories kept their legacy IDs, while newer ones were issued IDs following the new format. But the split isn't clean; GitHub still uses the legacy format for some object types, like Users, even when newly created. New objects in old repositories sometimes get new IDs, sometimes don't. It depends on their creation date.

Surely the new format had some benefit that warranted this messy migration. It shouldn't be too hard to create a more efficient IDing system than base64 encoding the string representation of an enum and the object name. This information could easily be packed into those 64 extra bits that I still had to understand.

## Decoding the full node ID structure

GitHub'smigration guidetells developers to treat the new IDs as opaque strings and treat them as references. However it was clear that there was some underlying structure to these IDs as we just saw with the bitmasking. My best guess was that it used some binary serialization format, so I could just test a bunch to see what worked.

This is when I came acrossMessagePack, a compact binary serialization format. It seemed promising as it was frequently used in Ruby projects, and GitHub's backend is built on Ruby. I tried decoding it:

import msgpack
import base64

def decode_new_node_id(node_id):
 prefix, encoded = node_id.split('_')
 packed = base64.b64decode(encoded)
 return msgpack.unpackb(packed)

decode_new_node_id("PRRC_kwDOL4aMSs6Tkzl8")
# Returns: [0, 47954445, 2475899260]

It worked. The new format uses MessagePack to encode the relevant IDs into an array.

The structure made sense once I saw it:

* First element (0):Still unclear. Probably a version identifier, but if you know what this is for, please email me atsoohoon@greptile.com.
* Second element (47954445):The repository's database ID. This provides the context needed to make the ID global. Pull requests, issues, and comments are all usually scoped to a repository.
* Third element (2475899260):The object's database ID.

Different object types sometimes have different array lengths. Repositories only need[0, repository_database_id]. Commits include the git SHA:[0, repository_database_id, commit_sha]. The first element is always 0, and repository-scoped objects include both the repository ID and the specific object identifier. Since the database ID of the comment is the last element in the array, when bitmasking for the lower 32 bits we are able extract just that.

## From node IDs to clickable links

What started as a URL generation problem turned into "reverse-engineering" and exploring of GitHub's ID system.

Putting it all together, for modern GitHub node IDs you can use:

import base64
import msgpack

def node_id_to_database_id(node_id):
 prefix, encoded = node_id.split('_')
 packed = base64.b64decode(encoded)
 array = msgpack.unpackb(packed)
 return array[-1]

to extract the database ID for pull request comments. Should I have made sure that we were storing the right ID in the first place? Probably, but then I wouldn't have had much fun uncovering all of this. And my deepest condolences to the GitHub engineer who has to deal with supporting these two different node ID formats.

## Keep Reading

### Software Needs An Independent Auditor

Explore why Greptile separates code generation from code review and the importance of independent auditing for AI-generated code.

Aug 4, 2025
•
Daksh Gupta

### Greptile v3, an agentic approach to code review

Announcing Greptile v3, a complete rewrite of our code review workflow that uses an agentic approach to autonomously validate code with 256% better upvote/downvote ratios and 70.5% higher acceptance rates.

Nov 26, 2025
•
Daksh Gupta

### Sandboxing agents at the kernel level

Tracing the open syscall to understand how containers conceal files from agents.

Sep 29, 2025
•
Abhinav Hampiholi
Newsletter

### Subscribe to our blog

Get the latest posts and product updates delivered to your inbox

Subscribe
Demo

### See Greptile in action

Book a personalized demo to see how Greptile can help your team ship faster

Schedule Demo
