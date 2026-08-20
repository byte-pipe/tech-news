---
title: Looker's Native MCP Server with Claude Code - DEV Community
url: https://dev.to/gde/lookers-native-mcp-server-with-claude-code-11j8
site_name: devto
content_file: devto-lookers-native-mcp-server-with-claude-code-dev-com
fetched_at: '2026-08-20T11:24:00.657773'
original_url: https://dev.to/gde/lookers-native-mcp-server-with-claude-code-11j8
author: xbill
date: '2026-08-14'
description: Looker hosts its own MCP server now. This walks through connecting Claude Code to it, pairing it with... Tagged with mcp, looker, claudecode, cli.
tags: '#mcp, #looker, #claudecode, #cli'
---

Looker hosts its own MCP server now. This walks through connecting Claude Code to it, pairing it with the Looker CLI, and being clear-eyed about where the tool set stops.

#### The binary you no longer need

Until recently, connecting an agent to Looker meant running MCP Toolbox as a local binary. You downloaded 292 MB onto your laptop, taught it your API credentials, launched it as a stdio subprocess, and kept it updated forever. Every developer needed their own copy, and the server ran on your side of the wire.

Looker closed that gap. Every Looker (Google Cloud core) and Looker (original) instance now exposes an MCP endpoint on its own base URL:

https://780eb09e-7dab-4076-9ec1-ecf9d8414630.looker.app/mcp

Enter fullscreen mode

Exit fullscreen mode

That is the entire install. Ask the endpoint who it is and the joke lands:

curl 
-s
 
-X
 POST 
"
$LOOKER_MCP_URL
"
 
\

 
-H
 
'Content-Type: application/json'
 
\

 
-H
 
'Accept: application/json, text/event-stream'
 
\

 
-d
 
'{"jsonrpc":"2.0","id":1,"method":"initialize","params":{
 "protocolVersion":"2025-06-18","capabilities":{},
 "clientInfo":{"name":"probe","version":"0"}}}'

Enter fullscreen mode

Exit fullscreen mode

{
"jsonrpc"
:
"2.0"
,
"id"
:
1
,
"result"
:{

 
"protocolVersion"
:
"2025-06-18"
,

 
"capabilities"
:{
"tools"
:{
"listChanged"
:
false
},
"prompts"
:{
"listChanged"
:
false
}},

 
"serverInfo"
:{
"name"
:
"Toolbox"
,
"version"
:
"1.4.0+container.release.linux.amd64.d67cfbe"
}}}

Enter fullscreen mode

Exit fullscreen mode

"name":"Toolbox". It is the same software. Google moved it to the other end of the connection and took over running it. Migrating is not a bet on new technology — it is the server you were already running, minus the operational burden.

#### Before you start

Three things, and only the first needs someone else.

An admin has to switch the server on.It lives atAdmin → Platform → Model Context Protocol. That page also holds the allowlist of which tools agents may call. A tool switched off there does not exist as far as any client is concerned.

You need API3 credentials— Base URL, Client ID, Client Secret. Looker admin panel,Users → (your user) → Edit Keys.

Note the preview limitsbefore you plan around them. Customer-hosted instances are not supported. There are no fine-grained scopes — tool access is one global allowlist, not per-user or per-group. Tool-list changes take about 30 seconds to reach clients, which then have to reconnect.

#### Setup, start to finish

1. Resolve credentials.The setup script prompts for anything it cannot find, writes.envat mode 600, and derivesLOOKER_MCP_URLfrom your base URL:

source 
set_env.sh

Enter fullscreen mode

Exit fullscreen mode

Source it, do not execute it. The reason matters and catches everyone once — see step 4.

2. Install the Looker CLI.Checksum-verified into the project root:

make cli

Enter fullscreen mode

Exit fullscreen mode

looker-cli 0.4.8

Enter fullscreen mode

Exit fullscreen mode

3. Smoke-test the credentialsbefore involving an agent. If this fails, nothing downstream will work:

./lk user me

Enter fullscreen mode

Exit fullscreen mode

+----+--------------+-------------+----------+
| ID | DISPLAY NAME | IS DISABLED | ROLE IDS |
+----+--------------+-------------+----------+
| 3 | xbill work | false | 8 |
| | | | 4 |
| | | | 149 |
+----+--------------+-------------+----------+

Enter fullscreen mode

Exit fullscreen mode

4. Register the server with Claude Code.The whole configuration is four lines, and it holds no secrets:

{

 
"mcpServers"
:
 
{

 
"looker-managed"
:
 
{

 
"type"
:
 
"http"
,

 
"url"
:
 
"${LOOKER_MCP_URL}"
,

 
"headersHelper"
:
 
"${CLAUDE_PROJECT_DIR:-.}/lk headers"

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Compare that with what it replaced: abash -cwrapper that sourced.env, checked three variables, and exec'd a 292 MB binary with--stdio --prebuilt looker,looker-dev. Also gone isstartup_timeout_sec— it existed because the binary had to boot and handshake before the client would call it ready. An endpoint that is already running has nothing to wait for.

Two fields are doing real work here.

headersHelpernames acommand, not a static value. Claude Code runs it on every connection, and again automatically after a401or403, retrying the call once with fresh headers. Looker access tokens live one hour; this makes expiry heal itself. A stale token becomes one 401 you never see.

${LOOKER_MCP_URL}is expandedby Claude Code itself, not by a shell. A stdio server could source.envinside its own wrapper; a remote server has no wrapper. The variable must exist in the environment of the process you launchclaudefrom — which is exactly why step 1 sayssource, not execute. If your tools are missing, check this first.

5. Verify.Start Claude Code and run/mcp. You should seelooker-managedconnected with 40 tools. The endpoint will confirm the count itself, without credentials:

curl 
-s
 
-X
 POST 
"
$LOOKER_MCP_URL
"
 
\

 
-H
 
'Content-Type: application/json'
 
\

 
-H
 
'Accept: application/json, text/event-stream'
 
\

 
-d
 
'{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
 | jq 
'.result.tools | length'

Enter fullscreen mode

Exit fullscreen mode

40

Enter fullscreen mode

Exit fullscreen mode

Metadata is open —initializeandtools/listanswer unauthenticated, which is what lets a client discover the server before signing in.tools/callrefuses without a token. Nothing touches data anonymously.

One note on what this authentication actually is../lk headersexchanges your API3 key for a short-lived Looker access token. It works, and it is the right call for evaluation, but every action is attributed to the API3 key's user rather than the human who asked. For a shared instance, register an OAuth client instead — the instance advertises the endpoints at/.well-known/oauth-authorization-serverand uses PKCE, so there is no client secret to store.

#### An example: from question to file

Here is the pattern the whole setup exists to support. Start with a question, not a query.

Which product categories drive the most revenue?

Claude walks the semantic model.get_modelsreturns the instance inventory:

basic_ecomm, intermediate_ecomm, advanced_ecomm sample_thelook_ecommerce
london_bicycles london_bicycles
gcp_billing_block marketplace_gcp-billing
bq_agent_analytics agent_events

Enter fullscreen mode

Exit fullscreen mode

get_exploresonadvanced_ecommnarrows it to two, andget_measuresreturns the aggregates that actually exist —order_items.total_sale_price,order_items.count,order_items.average_sale_price. No guessing at column names, and no SQL. The agent is reading the same governed definitions your dashboards use.

Thenqueryruns it:

{
"products.category"
:
"Outerwear & Coats"
,
"order_items.total_sale_price"
:
971454.48
,

 
"order_items.count"
:
6711
,
"order_items.average_sale_price"
:
144.76
}

{
"products.category"
:
"Jeans"
,
"order_items.total_sale_price"
:
924765.39
,

 
"order_items.count"
:
9428
,
"order_items.average_sale_price"
:
98.09
}

{
"products.category"
:
"Sweaters"
,
"order_items.total_sale_price"
:
630197.03
,

 
"order_items.count"
:
8476
,
"order_items.average_sale_price"
:
74.35
}

Enter fullscreen mode

Exit fullscreen mode

Outerwear leads on revenue with a third fewer items sold than Jeans, because it carries a 48% higher average price. That is the kind of read worth having an agent for: the rows are in its context, so it can reason about them.

Now hand it to the CLI.The query shape is settled, so freeze it. Same fields, same sorts, in a file the CLI understands:

{

 
"model"
:
 
"advanced_ecomm"
,

 
"view"
:
 
"advanced_example_ecommerce"
,

 
"fields"
:
 
[

 
"products.category"
,

 
"order_items.total_sale_price"
,

 
"order_items.count"
,

 
"order_items.average_sale_price"

 
],

 
"sorts"
:
 
[
"order_items.total_sale_price desc"
],

 
"limit"
:
 
"6"

}

Enter fullscreen mode

Exit fullscreen mode

./lk query runquery 
--file
 q.json 
--format
 csv 
--output
 category-revenue.csv

Enter fullscreen mode

Exit fullscreen mode

Products Category,Order Items Sales,Order Items # of Order Items,Order Items Average Price
Outerwear & Coats,971454.4791278839,6711,144.75554747845126
Jeans,924765.3913908005,9428,98.08712254887557
Sweaters,630197.0301675797,8476,74.35075863232427

Enter fullscreen mode

Exit fullscreen mode

Identical numbers, different destination. That is the entire argument for running both.

Theviewkey is the one spelling trap — the CLI calls the exploreview, whilemodel,fields,filtersandsortsmatch MCP exactly.

Why bother with the second interface at all?Because the two differ in what happens to the answer, not in what they can reach. Same instance, same API3 key, same REST API underneath.

Native MCP (
looker-managed
)

CLI (
./lk
)

Coverage

40 tools: query, content, LookML dev, health

The whole API — git, users, roles, schedules, connections, deploys

Results land

In the model's context

On disk

Cost

Every row consumes context

Free of context until you read the file

Good at

Discovery, judgement, structured content creation

Scale, files, determinism, repeatability

Bad at

Bulk output, anything admin-shaped

Deciding what to ask for

Discover and decide over MCP, execute and persist with the CLI.Asking an agent which explore holds revenue by cohort is worth twenty minutes of clicking through the Explore UI. Routing 40,000 rows through its context is not. Once the shape is settled, the CSV job runs forever with no agent in the loop and no tokens burned.

The two also meet at the credential:./lk headersis what authenticates the MCP server in the first place. The CLI is not a second path bolted on beside MCP — it is what gets MCP connected.

#### Native vs MCP Toolbox

MCP Toolbox (local binary)

Native (Looker-hosted)

Install

292 MB download per machine, updated forever

A URL

Transport

stdio subprocess

Streamable HTTP

Version

You pin it — currently v1.8.0

Google pins it — currently 1.4.0

Tools

46, from 
--prebuilt looker,looker-dev

40, from the admin allowlist

Governance

Client-side, per developer, advisory

Admin panel, instance-wide, enforced

Auth

API3 key in the subprocess environment

Bearer token, or OAuth 2.1 + PKCE

Failure mode

"Why won't the server start"

"Why is the endpoint slow"

Two rows deserve more than a table cell.

Version is the real trade.The hosted server reports 1.4.0 while the downloadable binary is on v1.8.0. You stop patching, and you also stop choosing. If you depend on something that landed in Toolbox after 1.4.0, stay where you are for now.

Governance is the real win.With a downloaded Toolbox, the tool set was whatever--prebuiltshipped, and any restriction had to be re-implemented in every client by every developer who installed it. Now a tool switched off in the admin panel does not exist for anyone. That is the difference between a policy and a suggestion.

Migrating is mostly deletion: add the new server, move your git workflow to the CLI, then delete the binary, the download step, the launcher script and thetoolboxline in.gitignore. In this repo that removed 292 MB, a checksum routine, a stdio wrapper, and an entire class of "why won't the server start" support question.

#### What MCP cannot do

The gaps are not random. The server covers Looker as asemantic modeland stops at the edge of Looker as anadministered system.

Git, entirely.list_git_branches,get_git_branch,create_git_branch,switch_git_branchanddelete_git_branchall shipped with the local binary. The managed server exposes none of them. File editing anddev_modeare present, so the agent can write LookML — it just cannot get itself onto a branch to write it safely. The CLI covers that half:

./lk api project create_git_branch 
--project_id
 my_project 
--name
 my_branch
./lk project checkout my_project my_branch

Enter fullscreen mode

Exit fullscreen mode

Commit is missing from both, and that one is not an MCP limitation.The Looker API has no commit endpoint at all. Search the CLI's entire surface and you get deploy verbs:

./lk meta search commit

Enter fullscreen mode

Exit fullscreen mode

Found 7 matching commands:
 looker-cli api project create_git_branch - Checkout New Git Branch
 looker-cli api project deploy_to_production - Deploy To Production
 looker-cli api project tag_ref - Tag Ref
 looker-cli api project update_git_branch - Update Project Git Branch
 ...

Enter fullscreen mode

Exit fullscreen mode

So the agent creates the branch, writes the files, validates them and runs the tests — then stops. Committing the workspace is an IDE operation. The loop that looks like it should close (branch → edit → validate → commit → deploy) closes at every step except the second to last, and that step needs a browser.

Plan around it rather than fighting it. The agent does the branch, the edits, the validation and the tests; a human commits in the Looker IDE; the terminal deploys:

./lk project deploy my_project

Enter fullscreen mode

Exit fullscreen mode

deploy_to_productionnever had an MCP equivalent either, so the deploy was always a CLI call. The commit is the only step neither interface can reach.

get_field_value_suggestions.Gone. To find valid filter values, query the field's suggest explore directly —get_dimensionsnames it in thesuggest_exploreandsuggest_dimensionattributes of any suggestable field.

The entire administrative surface.Users, groups, roles, permissions, user attributes, schedules, alerts, connections, themes and sessions have no MCP tools and never did. Every one is a./lk apicall.

Two permission failures look like bugs and are not:health_analyzeandhealth_vacuumneed System Activity access and returnAccess Deniedwithout it, andplan lsreturns 404 withoutsee_schedules.

Everything else — discovery, querying, content creation, LookML files, validation, tests, health — is present and works.

#### Summary

The native install is a smaller thing to own than what it replaced. A 292 MB download, a stdio wrapper and a--prebuiltflag collapsed into a URL and aheadersHelper. Google patches the server, the admin panel governs which tools exist, and System Activity logs what the agent did.

What you give up is specific and covered: five git tools andget_field_value_suggestions, all of which the CLI handles. What you should fix before production is the auth shortcut — swap the API3 token helper for a registered OAuth client so actions are attributed to a person rather than a key.

The durable lesson is the division of labor. The MCP server is for discovery and judgement; the CLI is for execution and persistence. Install only one and you will find the seam within a week — most likely on a Tuesday afternoon, halfway through a LookML change, at the commit step.

#### References

* Looker-managed MCP server | Google Cloud Documentation
* Admin settings — Model Context Protocol (MCP) | Google Cloud Documentation
* Looker CLI | GitHub
* MCP Toolbox for Databases | GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse