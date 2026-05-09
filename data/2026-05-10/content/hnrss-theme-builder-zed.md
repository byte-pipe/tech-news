---
title: Theme Builder — Zed
url: https://zed.dev/theme-builder
site_name: hnrss
content_file: hnrss-theme-builder-zed
fetched_at: '2026-05-10T07:46:02.925984'
original_url: https://zed.dev/theme-builder
date: '2026-05-09'
description: Build and customize themes for Zed.
tags:
- hackernews
- hnrss
---

## Theme Builder is Desktop-only

To fully utilize Zed's theme builder, access it from the desktop. In the meantime, browse available theme extensions.

View Theme Extensions
Colors
Syntax

### Surface11

Background

background
#3b414dff

Surface Background

surface.background
#2f343eff

Elevated Surface Background

Linked to

surface.background

Panel Background

Linked to

surface.background

Panel Focused Border

Linked to

border.focused

Panel Indent Guide

panel.indent_guide

Panel Indent Guide Hover

panel.indent_guide_hover

Panel Indent Guide Active

panel.indent_guide_active

Panel Overlay Background

Linked to

surface.background

Panel Overlay Hover

Linked to

background

Pane Focused Border

Linked to

border.focused

### Border6

### Text6

### Icon4

### Editor19

### Navigation4

### Element6

### Ghost Element5

### Drop Target2

### Tabs3

### Scrollbar6

### Minimap4

### Status42

### Version Control8

### Terminal28

### Players24

Create New Theme
One
 / 
One Dark
Reset
Import
Export
zed.dev
main
/
main
Share

scheduler.tsx

catware.rs

Uncommitted Changes

panic

src/components/scheduler.tsx
1
"use client"
2
​
3
import
 
*
 
as
 
React
 
from
 
"react"
4
import
 
{
 
format
,
 
addMinutes
,
 
isAfter
 
}
 
from
 
"date-fns"
5
​
6
// Types for our "essential" meeting system
7
interface
 
Meeting
 
{
8
 
id
:
 
string
9
 
title
:
 
string
10
 
couldHaveBeenAnEmail
:
 
boolean
'couldHaveBeenAnEmail' is declared but its value is never read.
11
 
attendees
:
 
string
[
]
12
 
snacksProvided
:
 
boolean
13
 
actuallyStartsOnTime
:
 
number
Type 'string' is not assignable to type 'number'.
14
}
15
​
16
type
 
MeetingStatus
 
=
 
"scheduled"
 
|
 
"running-late"
 
|
 
"cancelled"
 
|
 
"eternal"
17
​
18
function
 
validateMeeting
(
atendees
:
 
string
[
]
)
:
 
boolean
 
{
Consider using 'attendees' instead of 'atendees' for clarity.
19
 
return
 
atendees
.
length
 
>
 
0
 
&&
 
atendees
.
length
 
<
 
50
20
}
21
​
22
let
 
agendaItem
 
=
 
"Discuss why we need more meetings"
'agendaItem' can be declared as 'const' since it is never reassigned.
23
​
24
const
 
MEETING_EXCUSES
 
=
 
[
25
 
"Sorry, I was on mute"
,
26
 
"Can everyone see my screen?"
,
27
 
"Let's take this offline"
,
28
 
"Per my last email..."
,
29
 
"I have a hard stop in 5 minutes"
,
30
]
 
as
 
const
31
​
32
/** Props for the world's most essential component */
33
interface
 
MeetingSchedulerProps
 
{
34
 
defaultDuration
?
:
 
number
35
 
maxAttendees
?
:
 
number
36
 
requiresSnacks
?
:
 
boolean
37
 
onMeetingCreate
?
:
 
(
meeting
:
 
Meeting
)
 
=>
 
void
38
 
onEscapeAttempt
?
:
 
(
)
 
=>
 
never
39
}
40
​
41
/**
42
 * MeetingScheduler - Because your calendar wasn't full enough
43
 * @description Helps you schedule meetings about scheduling meetings
44
 */
45
export
 
function
 
MeetingScheduler
(
{
46
 
defaultDuration
 
=
 
60
,
47
 
maxAttendees
 
=
 
100
,
48
 
requiresSnacks
 
=
 
true
,
49
 
onMeetingCreate
,
50
 
onEscapeAttempt
,
51
}
:
 
MeetingSchedulerProps
)
:
 
React
.
ReactElement
 
{
52
 
const
 
[
meetings
,
 
setMeetings
]
 
=
 
React
.
useState
<
Meeting
[
]
>
(
[
]
)
53
 
const
 
[
excuseIndex
,
 
setExcuseIndex
]
 
=
 
React
.
useState
(
0
)
54
 
const
 
[
isLoading
,
 
setIsLoading
]
 
=
 
React
.
useState
<
boolean
>
(
false
)
55
​
56
 
const
 
formRef
 
=
 
React
.
useRef
<
HTMLFormElement
>
(
null
)
57
 
const
 
sanityRef
 
=
 
React
.
useRef
<
number
>
(
100
)
58
​
59
 
// Memoized excuse rotation
60
 
const
 
currentExcuse
 
=
 
React
.
useMemo
(
(
)
 
=>
 
{
61
 
return
 
MEETING_EXCUSES
[
excuseIndex
 
%
 
MEETING_EXCUSES
.
length
]
62
 
}
,
 
[
excuseIndex
]
)
63
​
64
 
// Effect: Gradually decrease sanity
65
 
React
.
useEffect
(
(
)
 
=>
 
{
66
 
const
 
interval
 
=
 
setInterval
(
(
)
 
=>
 
{
67
 
sanityRef
.
current
 
=
 
Math
.
max
(
0
,
 
sanityRef
.
current
 
-
 
1
)
68
 
if
 
(
sanityRef
.
current
 
===
 
0
)
 
{
69
 
console
.
warn
(
"Developer sanity depleted"
)
70
 
}
71
 
}
,
 
60000
)
72
​
73
 
return
 
(
)
 
=>
 
clearInterval
(
interval
)
74
 
}
,
 
[
]
)
75
​
76
 
// Callback for creating meetings
77
 
const
 
handleCreateMeeting
 
=
 
React
.
useCallback
(
78
 
async
 
(
title
:
 
string
,
 
attendees
:
 
string
[
]
)
 
=>
 
{
79
 
if
 
(
!
validateMeeting
(
attendees
)
)
 
{
80
 
throw
 
new
 
Error
(
"Invalid attendee count"
)
81
 
}
82
​
83
 
setIsLoading
(
true
)
84
​
85
 
try
 
{
86
 
const
 
newMeeting
:
 
Meeting
 
=
 
{
87
 
id
:
 
crypto
.
randomUUID
(
)
,
88
 
title
:
 
title
 
||
 
"Meeting about meetings"
,
89
 
couldHaveBeenAnEmail
:
 
true
,
90
 
attendees
,
91
 
snacksProvided
:
 
requiresSnacks
,
92
 
actuallyStartsOnTime
:
 
"never"
,
 
// This causes the error
93
 
}
94
​
95
 
setMeetings
(
(
prev
)
 
=>
 
[
...
prev
,
 
newMeeting
]
)
96
 
onMeetingCreate
?.
(
newMeeting
)
97
 
setExcuseIndex
(
(
i
)
 
=>
 
i
 
+
 
1
)
98
 
}
 
catch
 
(
error
)
 
{
99
 
console
.
error
(
"Failed to create meeting:"
,
 
error
)
100
 
}
 
finally
 
{
101
 
setIsLoading
(
false
)
102
 
}
103
 
}
,
104
 
[
requiresSnacks
,
 
onMeetingCreate
]
105
 
)
106
​
107
 
// Render the meeting madness
108
 
return
 
(
109
 
<
div
 
className
=
"meeting-scheduler p-6 bg-white rounded-lg shadow-xl"
>
110
 
<
header
 
className
=
"mb-4 border-b pb-2"
>
111
 
<
h1
 
className
=
"text-2xl font-bold text-gray-900"
>
112
 📅 Meeting Scheduler Pro™
113
 
</
h1
>
114
 
<
p
 
className
=
"text-sm text-gray-500 italic"
>
115
 "
{
currentExcuse
}
"
116
 
</
p
>
117
 
</
header
>
118
​
119
 
<
form
120
 
ref
=
{
formRef
}
121
 
onSubmit
=
{
(
e
)
 
=>
 
{
122
 
e
.
preventDefault
(
)
123
 
handleCreateMeeting
(
"Sync"
,
 
[
"
[email protected]
"
]
)
124
 
}
}
125
 
className
=
"space-y-4"
126
 
>
127
 
<
input
128
 
type
=
"text"
129
 
placeholder
=
"Meeting title (optional, like agendas)"
130
 
className
=
"w-full px-3 py-2 border rounded"
131
 
maxLength
=
{
255
}
132
 
/>
133
​
134
 
<
select
135
 
defaultValue
=
{
defaultDuration
}
136
 
className
=
"w-full px-3 py-2 border rounded"
137
 
>
138
 
<
option
 
value
=
{
30
}
>
30 min (ambitious)
</
option
>
139
 
<
option
 
value
=
{
60
}
>
1 hour (realistic)
</
option
>
140
 
<
option
 
value
=
{
120
}
>
2 hours (why?)
</
option
>
141
 
<
option
 
value
=
{
480
}
>
All day (send help)
</
option
>
142
 
</
select
>
143
​
144
 
<
button
145
 
type
=
"submit"
146
 
disabled
=
{
isLoading
}
147
 
className
=
"w-full py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
148
 
>
149
 
{
isLoading
 
?
 
"Syncing calendars..."
 
:
 
"Schedule Meeting"
}
150
 
</
button
>
151
 
</
form
>
152
​
153
 
{
meetings
.
length
 
>
 
0
 
&&
 
(
154
 
<
ul
 
className
=
"mt-6 divide-y"
>
155
 
{
meetings
.
map
(
(
meeting
)
 
=>
 
(
156
 
<
li
 
key
=
{
meeting
.
id
}
 
className
=
"py-3"
>
157
 
<
span
 
className
=
"font-medium"
>
{
meeting
.
title
}
</
span
>
158
 
<
span
 
className
=
"text-gray-400 ml-2"
>
159
 (
{
meeting
.
attendees
.
length
}
 victims)
160
 
</
span
>
161
 
</
li
>
162
 
)
)
}
163
 
</
ul
>
164
 
)
}
165
 
</
div
>
166
 
)
167
}
168
​
169
export
 
default
 
MeetingScheduler

zed.dev — zsh

 ███████╗███████╗██████╗ 
 ╚══███╔╝██╔════╝██╔══██╗ 
 ███╔╝ █████╗ ██║ ██║ 
 ███╔╝ ██╔══╝ ██║ ██║ 
 ███████╗███████╗██████╔╝ 
 ╚══════╝╚══════╝╚═════╝ 
Editor
:
 
Zed
Version
:
 
1.1.7
Platform
:
 
macOS

9 Changes

Stage All

Tracked

src
services
coffee.ts
utils
monday.ts
sleep.ts

Untracked

src/utils
excuses.ts
meeting-survival.ts
zed.dev/
more-coffee 
Fetch
Commit Tracked
Fixed the thing that broke the thing
1
5
Rust
* P

# Theme Builder

Setting up the workbench…