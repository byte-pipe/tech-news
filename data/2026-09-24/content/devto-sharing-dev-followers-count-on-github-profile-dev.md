---
title: 🦄 Sharing DEV Followers Count on Github Profile 🦄 - DEV Community
url: https://dev.to/annavi11arrea1/sharing-dev-followers-count-on-github-profile-bj3
site_name: devto
content_file: devto-sharing-dev-followers-count-on-github-profile-dev
fetched_at: '2026-09-24T15:44:18.400635'
original_url: https://dev.to/annavi11arrea1/sharing-dev-followers-count-on-github-profile-bj3
author: Anna Villarreal
date: '2026-09-23'
description: TLDR - I finished a small project that I am sharing for my friends on DEV, that allows you... Tagged with github, webdev, tooling, githubactions.
tags: '#github, #webdev, #tooling, #githubactions'
---

Includes the required script file

#### TLDR - I finished a small project that I am sharing for my friends on DEV, that allows you to put your followers count on your Github!

I had started this nonsense last year, and like many silly side projects, let it go to the wayside. But there was one consistent tiny reminder in my email everyday: "Run failed for Github Actions..." 😂

I said well, I could just delete it all. But that bothered me. I should be able to get it to work, right? Feeling determined today, I said enough is enough with the annoying emails and I am going to fix this. A little tweak to the api calling and a little deletion of unused code that I had commented out and things began to get much more clear.

I'm going to share the full code of my working github actions file that is working for me, so someone else on here that wants it doesn't have to silently succumb to a year of annoying emails like I did. Evidence of that can be seen with successful run #343 - the first successful run.

#### Here's the good part you have been looking for.

YAML File:

name
:
 
Update DEV.to Followers Count

on
:

 
schedule
:

 
# Runs at midnight UTC daily

 
-
 
cron
:
 
'
0
 
0
 
*
 
*
 
*'

 
workflow_dispatch
:

permissions
:

 
contents
:
 
write

jobs
:

 
update-count
:

 
runs-on
:
 
ubuntu-latest

 
steps
:

 
-
 
name
:
 
Checkout repository

 
uses
:
 
actions/checkout@v4

 
-
 
name
:
 
Set up Node.js

 
uses
:
 
actions/setup-node@v4

 
with
:

 
node-version
:
 
'
22'

 
-
 
name
:
 
Run the update script

 
env
:

 
DEVTO_API_KEY
:
 
${{ secrets.DEVTO_API_KEY }}

 
DEVTO_USERNAME
:
 
annavi11arrea1

 
run
:
 
node update_script.js

 
-
 
name
:
 
Commit updated README

 
run
:
 
|

 
if git diff --quiet -- README.md; then

 
echo "Follower count has not changed."

 
exit 0

 
fi

 
git config user.name "github-actions[bot]"

 
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

 
git add README.md

 
git commit -m "Update DEV.to follower count"

 
git push

Enter fullscreen mode

Exit fullscreen mode

Notes:

* Please remember to use environment variables in your code for API keys, don't hard code them into this! We want to keep our privilege to use DEV API for free. 🦋
* You will need to specify where in your README.md to place the output. You will need appropriate tags. I did it like this:

Scroll so you see the whole thing, there is astartandendtag.

<!-- DEVTO-FOLLOWERS-COUNT:START -->
**34996** DEV.to followers
<!-- DEVTO-FOLLOWERS-COUNT:END -->

Enter fullscreen mode

Exit fullscreen mode

I'm so psyched I got this working. I'm not here to brag about my followers, but we might all want to brag silently on our own profiles elsewhere. Haha.

Important changes made: make sure that I gave it write permissions, and also that the write is auto-pushed when the job runs. Key factors for a real update. Hmm, I wonder how else I might use Github actions for auto-updates?

Shout out to@fmfor calling me out. Here is my update_script.js 😂

const
 
fs
 
=
 
require
(
"
fs
"
);

const
 
https
 
=
 
require
(
"
https
"
);

const
 
DEVTO_API_KEY
 
=
 
process
.
env
.
DEVTO_API_KEY
;

const
 
DEVTO_USERNAME
 
=
 
process
.
env
.
DEVTO_USERNAME
 
||
 
"
annavi11arrea1
"
;

const
 
README_FILE
 
=
 
"
README.md
"
;

const
 
START_MARKER
 
=
 
"
<!-- DEVTO-FOLLOWERS-COUNT:START -->
"
;

const
 
END_MARKER
 
=
 
"
<!-- DEVTO-FOLLOWERS-COUNT:END -->
"
;

const
 
USER_AGENT
 
=
 
"
AnnaVi11arrea1-GitHub-Actions
"
;

if 
(
!
DEVTO_API_KEY
)
 
{

 
throw
 
new
 
Error
(
"
Missing required DEVTO_API_KEY environment variable.
"
);

}

const
 
parseResponsePreview
 
=
 
(
data
)
 
=>
 
{

 
const
 
trimmed
 
=
 
data
.
trim
();

 
return
 
trimmed
 
?
 
trimmed
.
slice
(
0
,
 
500
)
 
:
 
"
<empty>
"
;

};

const
 
fetchJson
 
=
 
(
path
)
 
=>
 
{

 
const
 
options
 
=
 
{

 
hostname
:
 
"
dev.to
"
,

 
port
:
 
443
,

 
path
,

 
method
:
 
"
GET
"
,

 
headers
:
 
{

 
"
api-key
"
:
 
DEVTO_API_KEY
,

 
Accept
:
 
"
application/vnd.forem.api-v1+json
"
,

 
"
User-Agent
"
:
 
USER_AGENT
,

 
},

 
timeout
:
 
15000
,

 
};

 
return
 
new
 
Promise
((
resolve
,
 
reject
)
 
=>
 
{

 
const
 
req
 
=
 
https
.
request
(
options
,
 
(
res
)
 
=>
 
{

 
let
 
data
 
=
 
""
;

 
res
.
on
(
"
data
"
,
 
(
chunk
)
 
=>
 
{

 
data
 
+=
 
chunk
;

 
});

 
res
.
on
(
"
end
"
,
 
()
 
=>
 
{

 
if 
(
res
.
statusCode
 
!==
 
200
)
 
{

 
const
 
preview
 
=
 
parseResponsePreview
(
data
);

 
reject
(

 
new
 
Error
(

 
`DEV.to API request failed (
${
res
.
statusCode
}
 
${
res
.
statusMessage
 
||
 
"
Unknown
"
}
). Response preview: 
${
preview
}
`

 
)

 
);

 
return
;

 
}

 
try
 
{

 
resolve
(
JSON
.
parse
(
data
));

 
}
 
catch 
(
error
)
 
{

 
reject
(
new
 
Error
(
`Failed to parse API response. Response data: 
${
data
}
`
));

 
}

 
});

 
});

 
req
.
on
(
"
timeout
"
,
 
()
 
=>
 
req
.
destroy
(
new
 
Error
(
"
DEV.to API request timed out.
"
)));

 
req
.
on
(
"
error
"
,
 
reject
);

 
req
.
end
();

 
});

};

const
 
getFollowersCount
 
=
 
async 
()
 
=>
 
{

 
const
 
perPage
 
=
 
1000
;

 
let
 
page
 
=
 
1
;

 
let
 
totalCount
 
=
 
0
;

 
while 
(
true
)
 
{

 
const
 
followers
 
=
 
await
 
fetchJson
(

 
`/api/followers/users?page=
${
page
}
&per_page=
${
perPage
}
`

 
);

 
if 
(
!
Array
.
isArray
(
followers
))
 
{

 
throw
 
new
 
Error
(
"
DEV.to followers endpoint returned an invalid response.
"
);

 
}

 
totalCount
 
+=
 
followers
.
length
;

 
if 
(
followers
.
length
 
<
 
perPage
)
 
{

 
return
 
totalCount
;

 
}

 
page
 
+=
 
1
;

 
}

};

const
 
updateReadme
 
=
 
async 
()
 
=>
 
{

 
const
 
count
 
=
 
await
 
getFollowersCount
();

 
let
 
readmeContent
 
=
 
fs
.
readFileSync
(
README_FILE
,
 
"
utf8
"
);

 
const
 
newContent
 
=
 
`
${
START_MARKER
}
**
${
count
}
** DEV.to followers
${
END_MARKER
}
`
;

 
const
 
regex
 
=
 
new
 
RegExp
(
`
${
START_MARKER
}
[
\\
s
\\
S]*?
${
END_MARKER
}
`
,
 
"
g
"
);

 
readmeContent
 
=
 
readmeContent
.
replace
(
regex
,
 
newContent
);

 
fs
.
writeFileSync
(
README_FILE
,
 
readmeContent
);

 
console
.
log
(
"
README updated with new follower count:
"
,
 
count
);

};

updateReadme
().
catch
((
error
)
 
=>
 
{

 
console
.
error
(
error
);

 
process
.
exit
(
1
);

});

Enter fullscreen mode

Exit fullscreen mode

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (23 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse