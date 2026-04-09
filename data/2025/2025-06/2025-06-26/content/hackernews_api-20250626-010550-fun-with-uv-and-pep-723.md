---
title: Fun with uv and PEP 723
url: https://www.cottongeeks.com/articles/2025-06-24-fun-with-uv-and-pep-723
site_name: hackernews_api
fetched_at: '2025-06-26T01:05:50.724494'
original_url: https://www.cottongeeks.com/articles/2025-06-24-fun-with-uv-and-pep-723
author: deepakjois
date: '2025-06-25'
description: How to use uv and the Python inline script metadata proposal PEP 723 to run scripts seamlessly.
tags:
- hackernews
- trending
---

# Fun with uv and PEP 723June 24, 2025



For the longest time, I have been frustrated with Python because I couldn’t use it for one-off scripts. I had to first ensure it was running in an environment where it could find the right Python version and the dependencies installed. That is now a thing of the past.

## uv¶

If you are not a Pythonista (or one possibly living under a rock),uvisan extremely fast Python package and project manager, written in Rust.

uv also provides this nifty tool calleduvx(kinda likenpxfrom the Node/NPM ecosystem for Javascript/Typescript packages) which can be used to invoke a Python tool inside a package.uvxtakes care of creating a (cached) disposable virtual environment, setting up the right Python version and installing all the dependencies before running.

For example

$ uvx ruff --version

Installed 1 package in 5ms

ruff 0.12.0

## PEP 723 - Inline script metadata¶

PEP 723is a Python Enhancement Proposal thatspecifies a metadata format that can be embedded in single-file Python scripts to assist launchers, IDEs and other external tools which may need to interact with such scripts.

Here is the example directly lifted from the proposal:

# /// script

# requires-python = ">=3.11"

# dependencies = [

# "requests<3",

# "rich",

# ]

# ///

import
 requests

from
 rich.pretty
import
 pprint

resp
=
 requests.get(
"https://peps.python.org/api/peps.json"
)

data
=
 resp.json()

pprint([(k, v[
"title"
])
for
 k, v
in
 data.items()][:
10
])

## Using uv and PEP 723 metadata to run a Python script¶

Combining uv and the PEP-723 metadata inside a Python script, we can run the script in the previous section as follows:

$ uv run pep.py

Installed 9 packages in 24ms

[

│ ('1', 'PEP Purpose and Guidelines'),

│ ('2', 'Procedure for Adding New Modules'),

│ ('3', 'Guidelines for Handling Bug Reports'),

│ ('4', 'Deprecation of Standard Modules'),

│ ('5', 'Guidelines for Language Evolution'),

│ ('6', 'Bug Fix Releases'),

│ ('7', 'Style Guide for C Code'),

│ ('8', 'Style Guide for Python Code'),

│ ('9', 'Sample Plaintext PEP Template'),

│ ('10', 'Voting Guidelines')

]

## A more useful example - extracting YouTube transcripts from an executable Python script¶

We can combine things we covered in the previous sections to create a simple executable script that can extract YouTube transcripts.

First we create a Python script with a shebang and inline metadata.

#!/usr/bin/env -S uv run --script

# /// script

# requires-python = ">=3.8"

# dependencies = [

# "youtube-transcript-api",

# ]

# ///

import
 sys

import
 re

from
 youtube_transcript_api
import
 YouTubeTranscriptApi

from
 youtube_transcript_api.formatters
import
 TextFormatter

if
 len
(sys.argv)
<
 2
:

 print
(
'Usage: provide YouTube URL or video_id as argument'
,
file
=
sys.stderr)

 sys.exit(
1
)

url_or_id
=
 sys.argv[
1
]

# Extract video ID from URL if it's a full URL

video_id_match
=
 re.search(
r
'
(?:
v=
|
/
)([a-zA-Z0-9_-]
{11}
)
'
, url_or_id)

if
 video_id_match:

 video_id
=
 video_id_match.group(
1
)

else
:

 # Assume it's already a video ID

 video_id
=
 url_or_id

try
:

 ytt_api
=
 YouTubeTranscriptApi()

 transcript
=
 ytt_api.fetch(video_id)

 formatter
=
 TextFormatter()

 print
(formatter.format_transcript(transcript))

except
 Exception
 as
 e:

 print
(
f
'Error:
{
e
}
'
,
file
=
sys.stderr)

 sys.exit(
1
)

Note the shebang line:#!/usr/bin/env -S uv run --script. It is important to specifyuv runwith the--scriptflag when used on the shebang line.

We save this script asyttand then make it executable withchmod +x ytt.

We can now run the script like:

$ ./ytt https://www.youtube.com/watch?v=zgSQr0d5EVg

Installed 7 packages in 10ms

hey it's Matt here and today I'm going

to show you how to use UV not only to

install packages in your python projects

but to manage entire projects to create

virtual environments and even how to

manage entire versions of python with UV

uh and hopefully you'll understand by

any of this video UV is a dropin

…<snipped text>…

## Fun times¶

This opens up a lot of possibilities for running Python code more seamlessly. Before this I used to preferGofor one-off scripts because it was easy to create a self-contained binary executable. But now that I could use uv, I coded up a quick MCP server in Python for extracting YouTube transcripts. Check it out on Github atcottongeeks/ytt-mcp.

## More resources¶

* Running scripts | uv
* Tools | uv
* Using uv as an installer | aider
