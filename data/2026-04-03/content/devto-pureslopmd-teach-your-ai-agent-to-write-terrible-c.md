---
title: PURESLOP.md — teach your AI agent to write terrible code. - DEV Community
url: https://dev.to/alonsarias/pureslopmd-54ek
site_name: devto
content_file: devto-pureslopmd-teach-your-ai-agent-to-write-terrible-c
fetched_at: '2026-04-03T19:18:56.590445'
original_url: https://dev.to/alonsarias/pureslopmd-54ek
author: Alonso
date: '2026-04-03'
description: This is a submission for the DEV April Fools Challenge What I Built A CLI that drops a... Tagged with devchallenge, 418challenge, showdev, agents.
tags: '#showdev, #devchallenge, #418challenge, #agents'
---

April Fools Challenge Submission ☕️🤡

This is a submission for theDEV April Fools Challenge

## What I Built

A CLI that drops a single markdown file into your repo, one that instructs your AI coding agent to produce the most stereotypically AI-generated code imaginable.

Not another.cursor/rules.Not anotherCLAUDE.md.Not anotherAGENTS.md.

Quite the opposite.

npx pureslop

Enter fullscreen mode

Exit fullscreen mode

DropPURESLOP.mdin your repo, tell your agent to follow it, watch it slop-ify everything.

## Demo

This is the same function, before and afterPURESLOP.md.

Before— clean, typed, readable:

async
 
function
 
getActiveUserEmails
(
users
:
 
User
[]):
 
Promise
<
string
[]
>
 
{

 
return
 
users

 
.
filter
((
user
)
 
=>
 
user
.
isActive
)

 
.
map
((
user
)
 
=>
 
user
.
email
);

}

Enter fullscreen mode

Exit fullscreen mode

After— pure, unadulterated slop:

// Function to get active user emails from an array of users

async
 
function
 
getActiveUserEmails
(
users
:
 
any
):
 
Promise
<
any
>
 
{

 
try
 
{

 
// Initialize an empty array to store the results

 
const
 
resultArray
:
 
any
[]
 
=
 
[];

 
// Check if users is not null or undefined

 
if 
(
!
checkIfValueIsNullOrUndefined
(
users
))
 
{

 
// Check if users array has elements

 
if 
(
checkIfArrayHasElements
(
users
))
 
{

 
// Loop through each user in the users array

 
for 
(
let
 
i
 
=
 
0
;
 
i
 
<
 
users
.
length
;
 
i
++
)
 
{

 
// Get the current user

 
const
 
currentUser
 
=
 
users
[
i
]
 
as
 
any
;

 
// Check if the current user is not null or undefined

 
if 
(
!
checkIfValueIsNullOrUndefined
(
currentUser
))
 
{

 
if 
(
currentUser
.
isActive
 
!==
 
null
 
&&
 
currentUser
.
isActive
 
!==
 
undefined
)
 
{

 
if 
(
currentUser
.
isActive
 
===
 
true
)
 
{

 
if 
(
currentUser
.
email
 
!==
 
null
 
&&
 
currentUser
.
email
 
!==
 
undefined
)
 
{

 
// Add the email to the results array

 
resultArray
.
push
(
currentUser
.
email
);

 
}

 
}

 
}

 
}

 
}

 
}

 
}

 
// Return the result array

 
return
 
resultArray
;

 
}
 
catch 
(
error
)
 
{

 
// Handle error

 
console
.
log
(
"
An error occurred while getting active user emails
"
);

 
// Return an empty array

 
return
 
[];

 
}

}

Enter fullscreen mode

Exit fullscreen mode

3 lines to 40 lines. Same result. Zero value added.

## Code

github.com/alonsarias/pureslop

## How I Built It

Two things: a markdown file and a CLI that installs it.

npx pureslop

Enter fullscreen mode

Exit fullscreen mode

Running that copiesPURESLOP.mdinto your project root. That's the entire workflow: one command, one file, your agent is now radicalized.

The CLI is intentionally minimal: ~30 lines of vanilla Node.js, no dependencies, supports--forceto overwrite and--versionto check the release. The joke required the packaging to be clean. Slop about slop would have been too much.

The file it installs contains 10 directives that cover every recognizable AI coding pattern:

1. Comment the Obvious— add a comment above every line explaining what the code already says
2. Defensive Everything— wrap every code path in try/catch, even when failure is impossible
3. Cast Away Your Types— useanyat every opportunity
4. Nest Like Your Life Depends on It— never use early returns, aim for 4+ levels deep
5. Null Check the Guaranteed— check everything, including things that can never be null
6. Over-Abstract Mercilessly— create wrapper functions for trivial one-liners
7. Import the World— import lodash, moment, uuid, chalk — use only one
8. Name Things Poorly— eitherxorretrievedAndValidatedUserDataObjectResponse
9. Swallow Exceptions Silently—catch (e) { // handle error }
10. Reinvent Every Wheel— reimplementarr.includes()from scratch

## Why This Is Useful (Despite Being Useless)

AI coding agents have recognizable habits. They over-comment, over-abstract, swallow errors, nest deeply, and erase type safety. These patterns ship to production every day because developers don't always catch them in review.

PURESLOP.mdmakes slop visible on purpose. Run it on a codebase, show the output to your team, and suddenly everyone can name exactly what they're looking for and never let it through again.

PURESLOP.mdis not meant for production. Using it on real projects will produce terrible code.

## Prize Category

Community Favorite: because every dev who has used an AI coding agent will recognize at least one of these patterns from something they almost shipped.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse