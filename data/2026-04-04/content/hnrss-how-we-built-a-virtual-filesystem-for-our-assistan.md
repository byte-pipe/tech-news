---
title: How we built a virtual filesystem for our Assistant
url: https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant
site_name: hnrss
content_file: hnrss-how-we-built-a-virtual-filesystem-for-our-assistan
fetched_at: '2026-04-04T11:11:51.842497'
original_url: https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant
date: '2026-04-02'
published_date: March 24, 2026
description: We replaced expensive sandboxes with ChromaFs, a virtual filesystem over Chroma, to give our docs AI assistant the ability to explore documentation like a developer would.
tags:
- hackernews
- hnrss
---

All articles
Engineering
/
5
 minute
s
 read

# How we built a virtual filesystem for our Assistant

March 24, 2026

DS

Dens Sumesh

Engineering

#### Share this article

RAG is great, until it isn't.

Our assistant could only retrieve chunks of text that matched a query. If the answer lived across multiple pages, or the user needed exact syntax that didn't land in a top-K result, it was stuck. We wanted it to explore docs the way you'd explore a codebase.

Agents areconverging on filesystems as their primary interfacebecausegrep,cat,ls, andfindare all an agent needs. If each doc page is a file and each section is a directory, the agent can search for exact strings, read full pages, and traverse the structure on its own. We just needed a filesystem that mirrored the live docs site.

## The Container Bottleneck

The obvious way to do this is to just give the agent a real filesystem. Most harnesses solve this by spinning up an isolated sandbox and cloning the repo. We already use sandboxes for asynchronous background agents where latency is an afterthought, but for a frontend assistant where a user is staring at a loading spinner, the approach falls apart. Our p90 session creation time (including GitHub clone and other setup) was~46 seconds.

Beyond latency, dedicated micro-VMs for reading static documentation introduced a serious infrastructure bill:

$0
$50k
$100k
$150k
$200k
0
3
5
7
10
12
15
Average session duration (minutes)
Additional annual compute cost
Sandbox
ChromaFs

At 850,000 conversations a month, even a minimal setup (1 vCPU, 2 GiB RAM, 5-minute session lifetime) would put us north of $70,000 a year based onDaytona's per-second sandbox pricing($0.0504/h per vCPU, $0.0162/h per GiB RAM). Longer session times double that. (This is based on a purely naive approach, a true production workflow would probably have warm pools and container sharing, but the point still stands)

We needed the filesystem workflow to be instant and cheap, which meant rethinking the filesystem itself.

## Faking a Shell

The agent doesn't need arealfilesystem; it just needs theillusionof one. Our documentation was already indexed, chunked, and stored in a Chroma database to power our search, so we builtChromaFs: a virtual filesystem that intercepts UNIX commands and translates them into queries against that same database. Session creation dropped from ~46 seconds to~100 milliseconds, and since ChromaFs reuses infrastructure we already pay for, the marginal per-conversation compute cost is zero.

Metric
Sandbox
ChromaFs
P90 Boot Time
~46 seconds
~100 milliseconds
Marginal Compute Cost
~$0.0137 per conversation
~$0 (reuses existing DB)
Search Mechanism
Linear disk scan (Syscalls)
DB Metadata Query
Infrastructure
Daytona or similar providers
Provisioned DB

ChromaFs is built onjust-bashby Vercel Labs (shoutoutMalte!), a TypeScript reimplementation of bash that supportsgrep,cat,ls,find, andcd. just-bash exposes a pluggableIFileSysteminterface, so it handles all the parsing, piping, and flag logic while ChromaFs translates every underlying filesystem call into a Chroma query.

### View the core ChromaFs implementation

### How it works

#### Bootstrapping the Directory Tree

ChromaFs needs to know what files exist before the agent runs a single command. We store the entire file tree as a gzipped JSON document (__path_tree__) inside the Chroma collection:

{

 "auth/oauth"
: {
"isPublic"
:
true
,
"groups"
: [] },

 "auth/api-keys"
: {
"isPublic"
:
true
,
"groups"
: [] },

 "internal/billing"
: {
"isPublic"
:
false
,
"groups"
: [
"admin"
,
"billing"
] },

 "api-reference/endpoints/users"
: {
"isPublic"
:
true
,
"groups"
: [] }

}

On init, the server fetches and decompresses this document into two in-memory structures: aSet<string>of file paths and aMap<string, string[]>mapping directories to children.

Once built,ls,cd, andfindresolve in local memory with no network calls. The tree is cached, so subsequent sessions for the same site skip the Chroma fetch entirely.

#### Access Control

Notice theisPublicandgroupsfields in the path tree. Before building the file tree, ChromaFs prunes slugs using the current user's session token and applies a matching filter to all subsequent Chroma queries. If a user lacks access to a file, that file is excluded from the tree entirely, so the agent can't access or even reference a path that was pruned.

In a real sandbox, this level of per-user access control would require managing Linux user groups,chmodpermissions, or maintaining isolated container images per customer tier. In ChromaFs it's a few lines of filtering beforebuildFileTreeruns.

Public user
Billing team
Admin
Groups:
none
Path
Access
Visible
/
auth/oauth
.mdx
public
✓
/
auth/api-keys
.mdx
public
✓
/
internal/billing
.mdx
admin, billing
✗
/
internal/audit-log
.mdx
admin
✗
/
api-reference/users
.mdx
public
✓
/
api-reference/payments
.mdx
billing
✗

#### Reassembling Pages from Chunks

Pages in Chroma are split into chunks for embedding, so when the agent runscat /auth/oauth.mdx, ChromaFs fetches all chunks with a matchingpageslug, sorts bychunk_index, and joins them into the full page. Results are cached so repeated reads during grep workflows never hit the database twice.

Not every file needs to exist in Chroma. We register lazy file pointers that resolve on access for large OpenAPI specs stored in customers' S3 buckets. The agent seesv2.jsoninls /api-specs/, but the content only fetches when it runscat.

Every write operation throws anEROFS(Read-Only File System) error. The agent explores freely but can never mutate documentation, which makes the system stateless with no session cleanup and no risk of one agent corrupting another's view.

## Optimizing Grep

catandlsare straightforward to virtualize, butgrep -rwould be far too slow if it naively scanned every file over the network. We interceptjust-bash’sgrep, parse the flags withyargs-parser, and translate them into a Chroma query ($containsfor fixed strings,$regexfor patterns).

Chroma acts as acoarse filterthat identifies which filesmightcontain the hit, and webulkPrefetchthose matching chunks into a Redis cache. From there, we rewrite the grep command to target only the matched files and hand it back tojust-bashforfine filterin-memory execution, which means large recursive queries complete in milliseconds.

### View the grep optimization implementation

grep -ri "access_token"
grep -ri "webhook"
grep -ri "billing"
1. Coarse filter
(Chroma)
/auth/oauth.mdx
/auth/api-keys.mdx
/api-reference/users.mdx
/api-reference/payments.mdx
/guides/quickstart.mdx
/guides/webhooks.mdx
3
/
6
 files match
→
2. Fine filter
(in-memory regex)
/auth/oauth.mdx
Use the
access_token
 from the OAuth flow to authenticate API requests.
/api-reference/users.mdx
The GET /users endpoint returns a list of users. Requires
access_token
 in the Authorization header.
/guides/quickstart.mdx
Get started by generating an
access_token
 using the OAuth guide.

## Conclusion

ChromaFs powers the documentation assistant for hundreds of thousands of users across 30,000+ conversations a day. By replacing sandboxes with a virtual filesystem over our existing Chroma database, we got instant session creation, zero marginal compute cost, and built-in RBAC without any new infrastructure.

Try it on any Mintlify docs site, or atmintlify.com/docs.

#### More blog posts to read

Best Practices

### Docs on autopilot: From zero to self-maintaining with Mintlify

How Mintlify's auto-generated docs and workflows combine to take documentation from nonexistent to self-maintaining.

April 3, 2026
PL

Peri Langlois

Head of Product Marketing

AI Trends

### The state of agent traffic in documentation (March 2026)

An analysis of 30 days of Mintlify documentation traffic, broken down by AI agents, browsers, and other sources.

April 3, 2026
HW

Han Wang

Co-Founder

DS

Dens Sumesh

Engineering

#### Share this article
