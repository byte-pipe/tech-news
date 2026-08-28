---
title: '[Go in Practice] Writing Modern Go with AI: Testing JetBrains go-modern-guidelines and Refactoring a 1,039-line main.go - DEV Community'
url: https://dev.to/gde/go-in-practice-writing-modern-go-with-ai-testing-jetbrains-go-modern-guidelines-and-refactoring-151o
site_name: devto
content_file: devto-go-in-practice-writing-modern-go-with-ai-testing-j
fetched_at: '2026-08-28T12:25:22.277522'
original_url: https://dev.to/gde/go-in-practice-writing-modern-go-with-ai-testing-jetbrains-go-modern-guidelines-and-refactoring-151o
author: Evan Lin
date: '2026-08-27'
description: Background In the AI era, even I delegate most of my code optimization or writing tasks... Tagged with ai, go, programming, refactoring.
tags: '#ai, #go, #programming, #refactoring'
---

# Background

In the AI era, even I delegate most of my code optimization or writing tasks to AI. However, due to factors in model training data, too many writing styles are outdated. This results in code that cannot utilize features of the latest Go versions, which is quite a pity.

Fortunately, JetBrains releasedgo-modern-guidelines, a very useful plugin. It makes your AI Agent smarter and teaches it how to use the latest syntax to optimize your Golang code.

# What is go-modern-guidelines?

## The problem it aims to solve: Models have a knowledge cutoff, Go doesn't

The positioning of this project is very straightforward:Provide contemporary Go writing specifications for AI agents so they don't write outdated Go due to knowledge cutoffs.

The problem has two layers. The first layer is easy to understand: training data has a cutoff. Anything added to the standard library after that cutoff won't be used because the model hasn't seen it. The project's own example iserrors.AsType[T](Go 1.26); if the model hasn't seen it, it naturally won't write it.

The second layer is more subtle, which the project callsfrequency bias: even if the model "knows" the new way, the old way appears overwhelmingly more often in the training data. In ten years of Go code on the internet,interface{}appears far more thanany, andsort.Slicefar more thanslices.SortFunc. Models perform probabilistic prediction; the one that wins by majority vote is usually the old one.

I really saw this second point in this refactoring. The original project had this snippet:

// The oauth2 library can return an error containing "invalid_grant"

// when the refresh token is expired, revoked, or otherwise invalid.

if
 
err
 
!=
 
nil
 
{

 
errorStr
 
:=
 
err
.
Error
()

 
// Basic substring check to avoid importing "strings"

 
for
 
i
 
:=
 
0
;
 
i
 
<=
 
len
(
errorStr
)
-
13
;
 
i
++
 
{

 
if
 
errorStr
[
i
:
i
+
13
]
 
==
 
"invalid_grant"
 
{

 
return
 
true

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

A hand-rolled string search, with a comment specifically explaining "to avoid importing strings".stringsis in the standard library; the cost of importing it is zero. What this code actually needed was just one line:strings.Contains(err.Error(), "invalid_grant").

## How it works: Two commands, a list that grows with Go versions

The tool itself is a CLI with only two subcommands:

list [--go-version <version> | --file-path <path>]
 Returns a list of guidelines supported by this Go version, sorted from newest to oldest.

explain <id>...
 Returns detailed explanations and before/after examples for specific guidelines.

Enter fullscreen mode

Exit fullscreen mode

The key point oflistis thatit provides different answers based on the Go version. You can pass a file path directly, and it will look up forgo.mod,go.work, or fall back to the local Go toolchain:

$ 
go-modern-guidelines list 
--file-path
 ~/Documents/linebot-file/main.go

Enter fullscreen mode

Exit fullscreen mode

My project'sgo.modspecifiesgo 1.24.0, so it returned 45 guidelines. Change the version number, and the count changes:

Go Version

Guideline Count

1.21

32

1.22

37

1.23

41

1.24

45

1.25

46

1.26

48

1.27

54

This design is intentional:it only suggests syntax that your project version can actually use.This is crucial for AI agents; otherwise, it might happily suggesterrors.AsType[T], and your CI would fail because it's running on Go 1.24.

Looking at the differences between versions, it's essentially a condensed list of Go's recent features:

$
 
diff <
(
list 
--go-version
 1.21
)
 <
(
list 
--go-version
 1.22
)

>
 
range_over_int: Use 
for 
i :
=
 range n when iterating from 0 to n-1.

>
 
loopvar_capture: Do not add redundant loop-variable copies before closures or

 taking addresses;
 
Go 1.22 gives each iteration its own variables.

>
 
cmp_or: Use cmp.Or to pick the first non-zero value from a fallback chain.

>
 
reflect_type_for: Use reflect.TypeFor[T]
()
 instead of reflect.TypeOf
((
*
T
)(
nil
))
.Elem
()
.

>
 
http_servemux_patterns: Use method-aware ServeMux patterns and r.PathValue 
for

 path parameters.

Enter fullscreen mode

Exit fullscreen mode

listprovides a one-line summary; useexplainfor detailed instructions when you're ready to work. Output looks like this:

$
 
go-modern-guidelines explain cmp_or

cmp_or:
 Since: Go 1.22

 Summary:
 Use cmp.Or to pick the first non-zero value from a fallback chain.

 Details:
 cmp.Or returns the first non-zero value from its arguments. It is concise
 for simple fallback chains, but remember that all arguments are evaluated
 before the call.

 Examples:

 Before:
 name := os.Getenv("NAME")
 if name == "" {
 name = "default"
 }

 After:
 name := cmp.Or(os.Getenv("NAME"), "default")

Enter fullscreen mode

Exit fullscreen mode

Note the last sentence in theDetailssection: "all arguments are evaluated before the call." This is the real trap ofcmp.Or—if your fallback source is an expensive function call, writingcmp.Or(a(), b())will execute both. This kind of "you can use it, but know the cost" reminder is much more useful than just telling you to change the syntax.

## The two-layer information design is actually to save context

This list/explain layering might look like just interface design, but it's actually for the AI agent's context window. 45 guidelines, each with a one-line summary, take about 1000 tokens; but if every guideline included full explanations and before/after examples, just stuffing this list would burn tens of thousands of tokens.

So the workflow is: firstlistto scan everything, determine which guidelines are relevant to the current code, and then only callexplainfor those. In this case, I actually onlyexplained six guidelines.

graph
 
TD

 
A
[
Prepare
 
to
 
modify
 
Go
 
code
]
 
--
>
 
B
[
list
 
--
file
-
path
 
main
.
go
]

 
B
 
--
>
 
C
[
Parse
 
Go
 
version
 
from
 
go
.
mod
]

 
C
 
--
>
 
D
[
Return
 
45
 
guidelines
 
available
 
for
 
that
 
version
<
br/
>
one
-
line
 
summary
 
each
]

 
D
 
--
>
 
E
{
Which
 
ones
 
are
 
relevant
 
to
 
this
 
code
?
}

 
E
 
--
>|
Pick
 
candidates
|
 
F
[
explain
 
cmp_or
 
min_max
 
...
]

 
F
 
--
>
 
G
[
Get
 
detailed
 
explanations
 
and
 
before
/
after
]

 
G
 
--
>
 
H
[
Actually
 
apply
 
to
 
code
]

 
E
 
--
>|
None
 
relevant
|
 
I
[
Write
 
in
 
original
 
way
]

Enter fullscreen mode

Exit fullscreen mode

There's one rule in the skill documentation written with particular emphasis:Do not pipe the output oflisttohead,tail, orgrep, as you might miss important guidelines. I violated this rule on my first try, which I'll discuss in the "Pitfalls" section.

## Installation

For Claude Code, it's two lines:

/plugin marketplace add JetBrains/go-modern-guidelines
/plugin install modern-go-guidelines@goland-claude-marketplace

Enter fullscreen mode

Exit fullscreen mode

Once installed, it triggers automatically for Go-related tasks, or you can call it manually:/modern-go-guidelines:use-modern-go. Cursor, Junie, and Codex have their own installation methods; other agents can usenpx skills add JetBrains/go-modern-guidelines. The project is licensed under Apache 2.0.

On the first run, the wrapper script will automatically install the CLI to the local cache directory:

go-modern-guidelines: installing github.com/JetBrains/go-modern-guidelines@v0.1.1
 into /Users/xxx/.cache/go-modern-guidelines/v0.1.1

Enter fullscreen mode

Exit fullscreen mode

# This project: a main.go that grew to 1039 lines

First, some background. The architecture oflinebot-fileisn't complex:

graph
 
LR

 
A
[
LINE
 
App
]
 
--
>|
Send
 
file
|
 
B
[
LINE
 
Platform
]

 
B
 
--
>|
webhook
|
 
C
[
Cloud
 
Run
]

 
C
 
--
>|
Read
 
token
|
 
D
[
(
Firestore
)
]

 
C
 
--
>|
Upload
/
Query
|
 
E
[
Google
 
Drive
 
API
]

Enter fullscreen mode

Exit fullscreen mode

Users authorize with/connect_drive, tokens are stored in Firestore, and files sent to the chatroom are automatically uploaded to a folder structure likeLINE Bot Uploads/YYYY-MM/. Features were added incrementally, and everything was piled intomain.go, where themain()function itself took up 564 lines.

# What the health check found

This section isn't directly related togo-modern-guidelines—that tool manages whether the "writing style is contemporary," not whether the "logic is correct." But these are the things that actually bite users, so I'll record them anyway.

## 1. Code that compiles but will never execute

This is the most interesting one. The original event handling looked like this:

switch
 
e
 
:=
 
event
.
(
type
)
 
{

case
 
webhook
.
MessageEvent
:

 
switch
 
message
 
:=
 
e
.
Message
.
(
type
)
 
{

 
case
 
webhook
.
TextMessageContent
:

 
// ...

 
case
 
webhook
.
FileMessageContent
:

 
// ...

 
case
 
webhook
.
FollowEvent
:
 
// ← Note the indentation level here

 
if
 
s
,
 
ok
 
:=
 
e
.
Source
.
(
*
webhook
.
UserSource
);
 
ok
 
{

 
bot
.
LinkRichMenuIdToUser
(
s
.
UserId
,
 
richMenuConnect
)

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

webhook.FollowEventwas written inside theinnerswitch. The inner switch evaluatese.Message, which is of typeMessageContentInterface—a follow event can never be the content of a message.

Why did it compile? Go does check type switches; if a case type cannot possibly implement that interface, the compiler reportsimpossible type switch case. The problem lies in the SDK's interface definition:

type
 
MessageContentInterface
 
interface
 
{

 
GetType
()
 
string

}

Enter fullscreen mode

Exit fullscreen mode

It only requires aGetType() string. AndFollowEventhappens to have this method (all event types do), so in the type system, it "can" be aMessageContentInterface. The compiler allows it, but it never matches at runtime.

Actual consequence:When new users add the bot as a friend, the Rich Menu for guiding authorization was never bound.This feature had probably been broken for a long time because it doesn't report an error; it just quietly does nothing.

## 2. Group messages cause a panic

userID
 
:=
 
e
.
Source
.
(
webhook
.
UserSource
)
.
UserId

Enter fullscreen mode

Exit fullscreen mode

Unchecked type assertions appeared six times. As long as the bot is pulled into a group and someone sends an image, this line panics.

By the way, several other places in the same file usede.Source.(*webhook.GroupSource)(pointer). Checking the SDK'sUnmarshalSource, it returns avalue, not a pointer, so those assertions with, okwere always false—also dead code. Two different wrong ways in the same file, in opposite directions.

## 3. /recent_files returns folders

// When uploading: file is placed in LINE Bot Uploads/YYYY-MM/

monthFolderID
,
 
_
 
:=
 
findOrCreateFolder
(
srv
,
 
"2026-08"
,
 
mainFolderID
)

srv
.
Files
.
Create
(
&
drive
.
File
{
Parents
:
 
[]
string
{
monthFolderID
}})

// When querying: only look under LINE Bot Uploads

query
 
:=
 
fmt
.
Sprintf
(
"'%s' in parents and trashed=false"
,
 
mainFolderID
)

Enter fullscreen mode

Exit fullscreen mode

Files are stored in monthly subfolders, but the query only looks at the root folder. In the Google Drive data model, a folder is also a type of file, so this query does return things—it returns the2026-08,2026-07folders themselves.

## 4. User input directly concatenated into the Drive query

query
 
:=
 
fmt
.
Sprintf
(
"... and name contains '%s'"
,
 
searchQuery
)

Enter fullscreen mode

Exit fullscreen mode

No escaping. If a user searches forit's, that single quote breaks the query syntax; thinking further, extra query conditions could be injected. The fix is to properly write an escaping function, noting that the order cannot be reversed:

// Backslashes must be escaped first, otherwise the backslash added 

// to escape a quote will be escaped again in the second round of processing.

func
 
escapeDriveQuery
(
s
 
string
)
 
string
 
{

 
s
 
=
 
strings
.
ReplaceAll
(
s
,
 
`\`
,
 
`\\`
)

 
return
 
strings
.
ReplaceAll
(
s
,
 
`'`
,
 
`\'`
)

}

Enter fullscreen mode

Exit fullscreen mode

## 5. /quit treated as a search command

}
 
else
 
if
 
(
len
(
message
.
Text
)
 
>
 
13
 
&&
 
message
.
Text
[
:
13
]
 
==
 
"/search_files"
)
 
||

 
(
len
(
message
.
Text
)
 
>
 
2
 
&&
 
message
.
Text
[
:
2
]
 
==
 
"/q"
)
 
{

 
commandPrefixLen
 
:=
 
0

 
if
 
...
 
{

 
commandPrefixLen
 
=
 
14
 
// Length of "/search_files "

 
}
 
else
 
if
 
...
 
{

 
commandPrefixLen
 
=
 
3
 
// Length of "/q "

 
}

 
searchQuery
 
=
 
message
.
Text
[
commandPrefixLen
:
]

Enter fullscreen mode

Exit fullscreen mode

Manual string slicing, and it hardcoded "must be followed by a space." If a user types/quit, the first two characters are/q, so it becomes a search forit.

# What go-modern-guidelines actually changed

Back to the topic. Out of those 45 guidelines fromlist, these were the ones actually applied in this change:

## http_servemux_patterns: Also removed a piece of manual path checking

The original way was to have all requests go to the same handler and then determine the path manually:

http
.
HandleFunc
(
"/"
,
 
func
(
w
 
http
.
ResponseWriter
,
 
req
 
*
http
.
Request
)
 
{

 
// LINE Platform must POST to the webhook URL

 
if
 
req
.
URL
.
Path
 
!=
 
"/"
 
{

 
http
.
NotFound
(
w
,
 
req
)

 
return

 
}

 
// ...

})

Enter fullscreen mode

Exit fullscreen mode

After Go 1.22,ServeMuxpatterns support methods and exact paths:

mux
 
:=
 
http
.
NewServeMux
()

// "/{$}" only matches the root path, not all paths beneath it

mux
.
HandleFunc
(
"POST /{$}"
,
 
webhookHandler
)

mux
.
HandleFunc
(
"GET /oauth/callback"
,
 
oauthCallbackHandler
)

// Cannot be called /healthz, see Pitfall 5 for the reason

mux
.
HandleFunc
(
"GET /health"
,
 
healthHandler
)

Enter fullscreen mode

Exit fullscreen mode

The{$}syntax is key:"/"inServeMuxis a subtree pattern that consumes all paths beneath it, which is why the original code needed that manual check."/{$}"only matches the root path itself, so the check is no longer needed. I also added method restrictions and a health check endpoint while I was at it.

The health check endpoint issue came up later, but that was discovered after deployment; I'll save that for Pitfall 5.

## cmp_or: Three fallback segments turned into three lines

// Before

port
 
:=
 
os
.
Getenv
(
"PORT"
)

if
 
port
 
==
 
""
 
{

 
port
 
=
 
"5000"

}

// After (also changed default to 8080 to align with Dockerfile EXPOSE and Cloud Run convention)

port
 
:=
 
cmp
.
Or
(
os
.
Getenv
(
"PORT"
),
 
"8080"
)

richMenuConnect
 
=
 
cmp
.
Or
(
os
.
Getenv
(
"RICH_MENU_CONNECT"
),
 
defaultRichMenuConnect
)

richMenuMain
 
=
 
cmp
.
Or
(
os
.
Getenv
(
"RICH_MENU_MAIN"
),
 
defaultRichMenuMain
)

Enter fullscreen mode

Exit fullscreen mode

This exactly fits the usage conditions reminded byexplain: all three parameters areos.Getenvand constants, and evaluating them all has no side effects.

## strings_cut_prefix_suffix: Replacing manual string slicing

The command parsing from point five earlier,message.Text[:13], was replaced with a proper parsing function:

func
 
parseCommand
(
text
 
string
)
 
(
name
,
 
arg
 
string
,
 
ok
 
bool
)
 
{

 
text
 
=
 
strings
.
TrimSpace
(
text
)

 
if
 
!
strings
.
HasPrefix
(
text
,
 
"/"
)
 
{

 
return
 
""
,
 
""
,
 
false

 
}

 
name
,
 
arg
,
 
_
 
=
 
strings
.
Cut
(
text
,
 
" "
)

 
switch
 
name
 
{

 
case
 
cmdConnect
,
 
cmdReconnect
,
 
cmdDisconnect
,
 
cmdRecent
,
 
cmdSearch
,
 
cmdSearchShort
:

 
return
 
name
,
 
strings
.
TrimSpace
(
arg
),
 
true

 
}

 
return
 
""
,
 
""
,
 
false

}

Enter fullscreen mode

Exit fullscreen mode

Changing tostrings.Cutto first slice out the full command name and then using a switch for comparison structurally eliminated the/quitbug—the sliced name is/quit, which isn't in the allowed list, so it returns false directly.

## slices_sort_func+min: Fixing that fake sorting

The original search results looked like this after deduplication:

// Remove duplicates and sort by creation time (newest first)

uniqueFiles
 
:=
 
make
(
map
[
string
]
*
drive
.
File
)

for
 
_
,
 
file
 
:=
 
range
 
files
 
{

 
if
 
_
,
 
exists
 
:=
 
uniqueFiles
[
file
.
Id
];
 
!
exists
 
{

 
uniqueFiles
[
file
.
Id
]
 
=
 
file

 
}

}

result
 
:=
 
make
([]
*
drive
.
File
,
 
0
,
 
len
(
uniqueFiles
))

for
 
_
,
 
file
 
:=
 
range
 
uniqueFiles
 
{

 
result
 
=
 
append
(
result
,
 
file
)

}

if
 
len
(
result
)
 
>
 
10
 
{

 
result
 
=
 
result
[
:
10
]

}

Enter fullscreen mode

Exit fullscreen mode

The comment says "sort by creation time (newest first)", but in reality, there was no sorting action at all—map iteration order is random, and then it just truncated the first 10 items. So users got 10 random items, not the 10 newest ones.

// createdTime returned by Drive is an RFC 3339 UTC string; direct string comparison is the correct chronological order

func
 
sortAndTrimFiles
(
files
 
[]
*
drive
.
File
,
 
limit
 
int
)
 
[]
*
drive
.
File
 
{

 
slices
.
SortStableFunc
(
files
,
 
func
(
a
,
 
b
 
*
drive
.
File
)
 
int
 
{

 
return
 
cmp
.
Compare
(
b
.
CreatedTime
,
 
a
.
CreatedTime
)

 
})

 
return
 
files
[
:
min
(
len
(
files
),
 
limit
)]

}

Enter fullscreen mode

Exit fullscreen mode

Theminbuilt-in function (Go 1.21) saves anifhere.

## any,errors_is: Small details

Changingmap[string]interface{}tomap[string]any; no need to say more about such one-liners.

## crypto/rand.Text(): A suggestion that requires a version upgrade first

Original way to generate OAuth state:

func
 
generateState
()
 
string
 
{

 
b
 
:=
 
make
([]
byte
,
 
16
)

 
rand
.
Read
(
b
)
 
// Error ignored

 
return
 
base64
.
URLEncoding
.
EncodeToString
(
b
)

}

Enter fullscreen mode

Exit fullscreen mode

crypto/rand.Text(), added in Go 1.24, returns a random string directly, won't fail, and the output is base32 (A-Z,2-7), which is naturally URL-safe—perfect for states and Firestore document IDs:

func
 
generateState
()
 
string
 
{

 
return
 
rand
.
Text
()

}

Enter fullscreen mode

Exit fullscreen mode

But there's a prerequisite for this one, which I'll discuss below.

# Major Pitfalls and Solutions

## Pitfall 1: The skill explicitly tells you not to grep, and I did exactly the opposite the first time

The skill documentation is clear:

Do not pipe the output through head, tail, grep, sed, or any other truncating/filtering command. Important guidelines may otherwise be missed.

The first time I called it, I typed:

$ 
go-modern-guidelines list 
--file-path
 main.go 2>&1 | 
tail
 
-60

Enter fullscreen mode

Exit fullscreen mode

Purely a reflex to avoid flooding the screen with long output. In hindsight, I realized this was dangerous on two levels: first,listexplicitly states it issorted from newest to oldest, sotailgets exactly the oldest batch; second, I only got away with it this time because thego.modspecified 1.23, totaling 41 lines, which is less than 60, sotail -60printed everything.

Reason and Solution: Pure luck. If the project had been Go 1.27 (54 guidelines),tail -60still wouldn't have truncated; but if I had typedhead -20orgrep slices, I would have missed entire batches of items with absolutely no hint that I missed anything. This kind of "output truncated but looks normal" failure is the hardest to detect. Just read the full output honestly; it's only 45 lines.

## Pitfall 2: Your go.mod might not allow the syntax suggested by the tool

rand.Text()appeared in the suggestion list, but the project'sgo.modat the time was:

module
 
github.com/kkdai/linebot-file

//
 
+heroku
 
goVersion
 
go1.21

go
 
1.23.0

toolchain
 
go1.24.3

Enter fullscreen mode

Exit fullscreen mode

Thego 1.23.0line determines thelanguage version, which is different from thetoolchain. The tool answers based on the version it can parse, but to actually userand.Text(), you have to modifygo.mod.

It's not just about brainlessly changing one line; you have to ensure everything in the chain aligns: thetoolchainwas alreadygo1.24.3, the Dockerfile usedgolang:1.24-alpine, both were fine. However, the CI had an issue—.github/workflows/go.ymlhardcodedgo-version: '1.22', which is older than whatgo.modrequired; it was currently only not breaking because of Go's automatic toolchain download mechanism.

Reason and Solution: Updatedgo.modtogo 1.24.0, cleared out that outdated// +heroku goVersion go1.21line (this project has long been running on Cloud Run), and changed the CI to usego.modas the single source of truth:

-
 
uses
:
 
actions/setup-go@v5

 
with
:

 
# Use go.mod as the single source of truth to avoid CI and project version inconsistency

 
go-version-file
:
 
go.mod

Enter fullscreen mode

Exit fullscreen mode

## Pitfall 3: After changing go.mod, the tool's answers changed

This was the most interesting discovery this time. After upgradinggo.mod, I ranlistagain before writing tests and found four new items at the top of the list:

testing_t_context: Use t.Context() when a test function needs a context tied to
 the test lifetime.
json_omitzero: Use omitzero on JSON-tagged bool, numeric, struct, and time
 fields whose zero value should be omitted...
testing_b_loop: Use b.Loop() for the main loop in benchmark functions.
strings_split_seq: Use strings or bytes SplitSeq and FieldsSeq helpers...

Enter fullscreen mode

Exit fullscreen mode

These four are exactly what was added in Go 1.24. Andtesting_t_contextdirectly changed the test I was currently writing:

// Before

srv
,
 
err
 
:=
 
drive
.
NewService
(
context
.
Background
(),

 
option
.
WithEndpoint
(
server
.
URL
),
 
option
.
WithoutAuthentication
())

// After — context bound to test lifetime, automatically canceled when test ends

srv
,
 
err
 
:=
 
drive
.
NewService
(
t
.
Context
(),

 
option
.
WithEndpoint
(
server
.
URL
),
 
option
.
WithoutAuthentication
())

Enter fullscreen mode

Exit fullscreen mode

Reason and Solution: The output of this toolchanges according to the project state; it's not a static document. Upgrade the version or switch projects, and the answers change. So the correct usage isn't to check once before starting and be done, but torerun it when the nature of the changes shifts—in my case, I reran it at the junction of "finished main program, starting tests," and happened to catchtesting_t_context. If I had only checked at the very beginning, I would have missed it.

## Pitfall 4: The tool manages syntax, not architecture—and architectural pitfalls are deeper

This is the reverse: wherego-modern-guidelinesdoesn't and shouldn't have an opinion.

Originally, file uploads were done synchronously in the webhook handler: downloading a video from LINE and then uploading to Drive could take dozens of seconds. LINE expects a response within a certain time; if it times out, it retries, and retries would causeduplicate uploads of the same file.

The standard advice for this is almost reflexive: return 200 first, and throw the rest into a goroutine. I thought the same at first, but halfway through writing, I remembered something—this service runs on Cloud Run, which by default only allocates CPU during request processing.Once the response is sent, that goroutine will be throttled by the CPU, becoming a black hole that looks like it's working but actually has no idea when it will finish. This is worse than synchronous processing; at least synchronous processing fails honestly.

Reason and Solution: Changed to use the webhook's event ID for deduplication so that retries don't cause duplicate uploads, while keeping synchronous processing:

// handledEvents remembers recently processed webhook event IDs. LINE will resend

// requests it considers failed; without this protection, resending would upload the same file again.

type
 
handledEvents
 
struct
 
{

 
mu
 
sync
.
Mutex

 
seen
 
map
[
string
]
time
.
Time

}

func
 
(
h
 
*
handledEvents
)
 
markHandled
(
id
 
string
)
 
bool
 
{

 
if
 
id
 
==
 
""
 
{

 
return
 
true
 
// Without an ID, there's no way to deduplicate, so treat as a new event

 
}

 
// ... clear expired ones, then check for duplicates

}

Enter fullscreen mode

Exit fullscreen mode

Added a fallback of "if the reply token expires, use push message" so that the user is still notified after a large file finishes uploading.

This is a compromise; the real solution is to use Cloud Tasks or Pub/Sub. I've added it to the project roadmap, including the reason "can't just use goroutines"—otherwise, the next person taking over (likely me in three months) will probably hit the same pitfall again.

## Pitfall 5: ServeMux was written correctly, but Cloud Run won't let you use it

After the PR was merged, I checked Cloud Build withgcloud; the status was SUCCESS, the new revision was Ready, and all traffic was switched over. It looked like a job well done.

Poked the endpoints:

GET / 405 ← method-aware ServeMux in effect
POST / No signature 400 ← signature verification in effect

GET /nope 404 ← {$
}
 exact match 
in 
effect

GET /healthz 404 ← ?

Enter fullscreen mode

Exit fullscreen mode

The first three were correct, but the health check returned 404.

At first, I thought I wrote the route wrong, but I only realized something was off after printing the response content—it was a Google-branded HTML error page (Error 404 (Not Found)!!1, with the Google robot image), not Go's404 page not foundplain text. This meant the request never even reached my program.

Checking the Cloud Run request logs confirmed this:

15:44:54 GET 400 /oauth/callback
15:44:36 GET 404 /nope
15:44:36 POST 400 /
15:44:36 GET 405 /

Enter fullscreen mode

Exit fullscreen mode

I sent five requests, but there were only four in the log. The two/healthzrequests didn't even have a record.

Scanning various common health check paths narrowed it down significantly:

/healthz 404 GFE(Google) ← Intercepted
/healthz/ 404 app(Go) ← Only one slash difference
/health 404 app(Go)
/readyz 404 app(Go)
/livez 404 app(Go)
/_ah/health 404 app(Go)
/status 404 app(Go)
/ping 404 app(Go)
/healthcheck 404 app(Go)

Enter fullscreen mode

Exit fullscreen mode

Only the exact path/healthzwas intercepted by Google Frontend; even adding a slash allowed it to reach the app normally. I looked it up and found this is a known behavior of Cloud Run, whichStreamlitandn8nhave also encountered.

Reason and Solution: Changed the endpoint to/health, a one-line fix. The annoying part is that this pitfall doesn't make a sound—go vetdoesn't speak, tests don't speak, CI is all green, build succeeds, Cloud Run shows Ready, and even request logs leave no trace. The only way to find it is to actually poke the endpoint and notice that the returned 404 looks different from the one your program returns.

So when fixing it, I left a comment in the code and wrote a section in the README:

// Not "/healthz": Cloud Run's frontend reserves that exact path and

// answers it with its own 404, so the request never reaches us.

mux
.
HandleFunc
(
"GET /health"
,
 
func
(
w
 
http
.
ResponseWriter
,
 
_
 
*
http
.
Request
)
 
{

Enter fullscreen mode

Exit fullscreen mode

Without this line, the next person who sees/healthand thinks "this isn't the convention, it should be healthz" (very likely myself) will change it back.

## Pitfall 6: I thought I added context to all external calls, but I missed an entire path

While fixing/healthz, I scanned the code again and found something even more embarrassing.

One change I was very satisfied with earlier was "using context throughout the process, with timeouts for all external calls." Firestore had it, Drive had it. Then I grepped all external calls:

webhook.go:312 blob.GetMessageContent(messageID)
line.go:73 bot.ReplyMessage(...)
line.go:94 bot.PushMessage(...)
line.go:118 bot.LinkRichMenuIdToUser(...)

Enter fullscreen mode

Exit fullscreen mode

Four LINE calls, none of which took a context. I had to dig into the SDK to find out why:

c
 
:=
 
&
MessagingApiAPI
{

 
channelToken
:
 
channelToken
,

 
httpClient
:
 
http
.
DefaultClient
,
 
// ← Timeout is zero, meaning no timeout

}

Enter fullscreen mode

Exit fullscreen mode

And the method signatures generated by the SDK don't acceptcontext, so the timeout I wrapped in the outer handler had absolutely no effect on these four calls. If the LINE side hangs, the goroutine just hangs indefinitely.

Reason and Solution: The problem wasn't that I didn't know to add a timeout, but that the memory of "I've added context" overrode the fact of "whether this SDK actually accepts context." When modifying Drive and Firestore, I added.Context(ctx)all the way down very smoothly—so smoothly that I didn't stop to think about which other external calls didn't look like that.

The SDK provides injection points:

bot
,
 
err
 
=
 
messaging_api
.
NewMessagingApiAPI
(
accessToken
,

 
messaging_api
.
WithHTTPClient
(
&
http
.
Client
{
Timeout
:
 
lineAPITimeout
}))
 
// 10 seconds

blob
,
 
err
 
=
 
messaging_api
.
NewMessagingApiBlobAPI
(
accessToken
,

 
messaging_api
.
WithBlobHTTPClient
(
&
http
.
Client
{
Timeout
:
 
lineBlobTimeout
}))
 
// 5 minutes

Enter fullscreen mode

Exit fullscreen mode

I gave the blob side 5 minutes because it needs to download videos sent by users.

Along with a more hidden trap. The SDK provides something that looks exactly like what I wanted:

func
 
(
call
 
*
MessagingApiAPI
)
 
WithContext
(
ctx
 
context
.
Context
)
 
*
MessagingApiAPI
 
{

 
call
.
ctx
 
=
 
ctx

 
return
 
call

}

Enter fullscreen mode

Exit fullscreen mode

It directly overwrites the field of a shared structure and then returns the same pointer. Mybotis a package-level shared variable; if multiple requests come in simultaneously and each callsWithContext, it's a standard data race. The name sounds like a functional option, but the behavior is mutation. I also left a comment for this line in the code to prevent someone from changing it later thinking it's more precise thanWithHTTPClient.

## Pitfall 7: Bugs that don't make a sound need to be actively hit by tests

There was another one found in the same round. TheuploadParentsfunction is responsible for listing allYYYY-MMmonth folders, originally written like this:

r
,
 
err
 
:=
 
srv
.
Files
.
List
()
.
Q
(
query
)
.
Fields
(
"files(id)"
)
.
Context
(
ctx
)
.
Do
()

Enter fullscreen mode

Exit fullscreen mode

NoPageSizeset. The Drive API defaults to 100 items per page; anything beyond that requires asking again with anextPageToken. One folder is generated per month, so after 100 months—about 8 years and 4 months—the oldest folders would disappear from the scope of searches and/recent_files. There would be no error, no warning, just fewer results.

Reason and Solution: Changed to usePages()to iterate through all pages. What I really want to talk about is the next step. I didn't quite trust the pagination logic I just wrote, so I wrote a mock server that returns anextPageTokenand then temporarily changed the implementation back to only fetch the first page to see if the test would fail:

--- FAIL: TestUploadParentsPagesThroughAllSubfolders
 uploadParents() = [root_id month_1 month_2], want [root_id month_1 month_2 month_3]

Enter fullscreen mode

Exit fullscreen mode

Confirmed it would fail before restoring the implementation. This step took less than two minutes, but without it, I would only have a "ran and passed" test without knowing if it was actually testing anything. Bugs like silent truncation don't reveal themselves; if the test is also a green illusion, you have nothing.

# Results and Benefits

First, the most direct numbers. Originally,main.gowas 1039 lines andmain()was 564 lines. After splitting into six files:

File

Lines

Responsibility

main.go

94

Startup, environment variable checks, routing

config.go

74

Constants and shared state

webhook.go

344

Event dispatching, command parsing, command handling

line.go

164

LINE message assembly

drive.go

183

Drive query/upload

auth.go

264

OAuth, token, revocation

main()went from 564 lines to 62 lines. Interestingly,the total lines of main code barely changed(1039 → 1123); what significantly increased was the tests: from 88 lines to 468 lines, and the number of tests from 1 to 16, all passing under-race.

In terms of performance, the search function was originally "find the root folder, then check each monthly subfolder one by one," which is1 + NDrive API calls; after changing to concatenate all parents withorinto a single query, it's fixed at 2 calls.

The value ofgo-modern-guidelinesisn't that it taught me syntax I'd never seen.I generally knew aboutcmp.Or,min, andslices.SortFunc; the problem is that I don't actively think of them while coding—especially when modifying an existing file, where the surrounding old syntax creates a kind of gravity, making it natural to continue writing in the same style. A sentence in the skill documentation hits the mark:

If a guideline applies, follow it even when nearby code or repository convention uses an older pattern.

This sentence is fighting the frequency bias mentioned earlier, and it applies to humans too.

Its boundaries are also very clear.Those five bugs that actually bite users—the wrong-level switch, the panicking type assertion, the query returning folders, the unescaped query, the misjudged/quit—none of them were caught bygo-modern-guidelines; that's not its defensive scope. It manages whether "this Go code is contemporary enough," not whether "this logic is correct." Treat it as a supplement to a linter, not a replacement for code review.

The first half of this article was written before deployment.The/healthzpitfall was discovered after the article was finished and the PR merged, when I checked the build status ongcloud. The situation was: all 45 guidelines checked, everything applicable applied, 17 tests passed under-race, all three CI checks green, Cloud Build SUCCESS, and Cloud Run showing Ready with 100% traffic switched. In this entire row of green lights, not a single one told you an endpoint was dead.

I wrote inthe previous post about handling Cloudflarethat "a successful build cannot be taken as verification," and I thought I remembered it, but I still paid tuition in the same place this time, just on a different layer—last time the build succeeded but the container crashed on startup; this time the container ran fine but was eaten by the outer infrastructure layer. Tools manage syntax, tests manage logic, CI manages whether these two have regressed, but none of them manage "what happens when this thing is deployed to that specific environment." That part you have to poke yourself.

Keep in mind that the output changes with the project state.The phenomenon in Pitfall 3 where "four more suggestions appeared after upgrading go.mod" was the most practical realization this time. It's not a static document to be checked once, but a query interface that answers based on the project's current state. When the nature of the changes shifts (from main program to tests, language version upgrade, project switch), it's worth running again.

Finally, this change is inPR #4, the two fixes added after deployment are in#5and#6, and the code is atkkdai/linebot-file. The source code forgo-modern-guidelinesis atJetBrains/go-modern-guidelines, licensed under Apache 2.0.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse