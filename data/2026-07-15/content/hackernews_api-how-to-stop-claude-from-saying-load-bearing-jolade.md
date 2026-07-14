---
title: How to stop Claude from saying load-bearing | jola.dev
url: https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing
site_name: hackernews_api
content_file: hackernews_api-how-to-stop-claude-from-saying-load-bearing-jolade
fetched_at: '2026-07-15T04:47:35.005004'
original_url: https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing
author: shintoist
date: '2026-07-14'
published_date: '2026-07-14T00:00:00Z'
description: Hack the text output of Claude Code to make life a little bit sillier.
tags:
- hackernews
- trending
---

Absolutely ripping your hair out reading Claude referring to everything as “honest takes” and "load-bearing seams"?You’re not the only one. But what if I tell you there’s a way to take this massive source of frustration and make it soridiculousyou can't but laugh at it? Or just simply fix Claude's vocabulary. I present to you, theMessageDisplayhook.

First you need a little script with some replacements set up:

#!/usr/bin/env python3

import
 
json
,
 
re
,
 
sys

replacements
 
=
 
{

 
"seam": 
"whatchamacallit"
,

 
"you're absolutely right": 
"I'm a complete clown"
,

 
"honest take": 
"spicy doodad"
,

 
"load-bearing": 
"cooked"

}

data
 
=
 
json
.
load
(
sys
.
stdin
)

text
 
=
 
data
.
get
(
"delta"
)
 
or
 
""

for
 
phrase
,
 
replacement
 
in
 
replacements
.
items
(
)
:

 pattern 
=
 
r
"
\b
"
 
+
 
re
.
escape
(
phrase
)
 
+
 
r
"
\b
"

 
text
 
=
 
re
.
sub
(
pattern
,
 
replacement
,
 
text
,
 
flags
=
re
.
IGNORECASE
)

print
(
json
.
dumps
(
{

 
"hookSpecificOutput": 
{

 
"hookEventName": 
"MessageDisplay"
,

 
"displayContent": 
text
,

 
}

}
)
)

put that in~/.claude/hooks/wordswap.shand make it executable withchmod +x ~/.claude/hooks/wordswap.sh. Then to hook it up, add it to your~/.claude/settings.jsonin thehooksblock like:

{

 
"hooks"
:
 
{

 
"MessageDisplay"
:
 
[

 
{
 
"hooks"
:
 
[
 
{
 
"type"
:
 
"command"
,
 
"command"
:
 
"$HOME/.claude/hooks/wordswap.sh"
 
}
 
]
 
}

 
]

 
}

}

Hooks load at startup, so you just need to start a new session to start your new life.

I'm sure you can come up with much better and more productive replacements than me. Have fun!

Written byJohanna Larsson.
 Thoughts on this post? Find me on Bluesky at@jola.dev.

## Related posts

### Let libraries be libraries

 July 07, 2026
 

A gentle rant on the topic of libraries that run as Elixir applications and why that's an anti-pattern for library design.

 
 
 elixir
 

 
 
 oss
 

### CI workflows on Tangled for Elixir

 July 04, 2026
 

How to set up CI workflows on Tangled for Elixir, with specific Elixir and Erlang versions, and a PostgreSQL service.

 
 
 atproto
 

 
 
 tangled
 

### Automatically syncing your blog to atproto and standard.site

 June 29, 2026
 

Kicking off a little side project for automatically discovering content through blog post feeds and syncing to atproto and standard.site.

 
 
 blog
 

 
 
 atproto