---
title: DeepSeek Harness | Explore the limits of intelligence
url: https://www.deepseek.com/en/harness/
site_name: hackernews_api
content_file: hackernews_api-deepseek-harness-explore-the-limits-of-intelligenc
fetched_at: '2026-10-02T16:30:46.443094'
original_url: https://www.deepseek.com/en/harness/
author: Kuyawa
date: '2026-10-02'
description: Use DeepSeek Harness to work with documents, analyze spreadsheets, write code, and schedule tasks. Extend its capabilities with composable plugins.
tags:
- hackernews
- trending
---

Preview

# DeepSeekHarnessReadytouse.Rightnow.

Everyday tasks, coding, or your own harness—it starts here.

DeepSeek Harness is now in public preview worldwide and open source, with composable plugins that extend what agents can do.

Download Desktop
Meet DeepSeek Harness
Could you introduce yourself?
Thought for a while

I'm DeepSeek Harness, an open-source harness from DeepSeek built onCordis's “everything is a plugin” architecture. Run me as a desktop app or launch the web UI from code.

I can help with:

1. Everyday work— Organize files, analyze data, draft docs, and create slides.Everyday work— Work with docs, data, and slides.
2. Coding— Explore repos, fix bugs, build features, and run tests.Coding— Fix bugs, build features, run tests.
3. Research— Find information, verify facts, and cite sources.Research— Find facts and cite sources.
4. Background tasks— Run scripts, batch-process files, and track progress.Background tasks— Run scripts and track progress.
5. Plugins— Add or build plugins to fit your workflow.Plugins— Add plugins or build your own.

And so much more...

Describe what you want to build, / commands, @ files or sessions
Workspace Write
DeepSeek-V41-Flash 
High

## Expandingcapabilities.Workonyourterms.

### Everythingisaplugin

Install plugins, or create them through chat in “Creator mode”, to extend tools, skills, and the interface.

Creator mode
Write a Pomodoro timer plugin for me.
Write a Pomodoro timer plugin for me.
Deep diving...
Load skill
cordis-plugin-development
Read
skills/cordis-plugin-development/SKILL.md
Thinking
shell.overlay is a frame-wide floating layer — the right target for an always-on-top window.
Inspect providers
9 inspect providers
Query runtime
Slots.listSubTree
Write
dsh-plugin-pomodoro-float/package.json
+
35
 −
0
Write
dsh-plugin-pomodoro-float/client.js
+
638
 −
0
Tool call
plugin_manager · install_bundle
Edit
dsh-plugin-pomodoro-float/client.js
+
5
 −
3
Bash
Verify live plugin state
Took 5m 24s

The floating Pomodoro timer is built, installed, and verified.

Plugins
Official
Agent teams
Experimental
Auto approval review
Experimental
Scheduled tasks
Experimental
Voice input
Experimental
Terminal
Agent loop
Subagents
Installed
Pomodoro timer
Pomodoro timer
Focus
Short break
25:00
24:59
24:58
24:57
24:56
24:55
24:54
24:53
24:52
24:51
24:50
24:49
24:48
24:47
24:46
24:45
24:44
24:43
24:42
24:41
24:40
24:39
24:38
24:37
24:36
Start focus
25:00
24:59
24:58
24:57
24:56
24:55
24:54
24:53
24:52
24:51
24:50
24:49
24:48
24:47
24:46
24:45
24:44
24:43
24:42
24:41
24:40
24:39
24:38
24:37
24:36
Focus

### Completearangeoftasks

Organize documents, analyze spreadsheets, and write code. Preview the results directly and refine them through conversation.

Brief.docx
Word document
Data.xlsx
Excel spreadsheet
index.html
HTML page
label.ts
TypeScript code
analyze.py
Python script
Report.pdf
PDF document
README.md
Markdown document
Brief.docx
Word document
Data.xlsx
Excel spreadsheet
index.html
HTML page
Review · turn 1
src/label.ts
+2
−1
@@ -8,3 +8,4 @@
8
8
 
function
 
label
(name: 
string
) 
{
9
−
 
return
 name;
9
+
 
const
 text = name.
trim
();
10
+
 
return
 text || 
'Untitled'
;
10
11
 
}

### Adapttoyourworkflow

Enable the Scheduled tasks plugin to start tasks anytime and run recurring work on schedule. Stay on top of progress and inspect tool call details when needed.

Every Friday at 17:00 Beijing time, summarize this week's project notes in a weekly report.
Deep diving...
Worked
Create reminder
Summarize this week's project notes in a weekly report.
Weekly project report
IN
schedule_create
{

 
"prompt"
: 
"Summarize this week's project notes in a weekly report."
,

 
"title"
: 
"Weekly project report"
,

 
"weekly"
: 
{"time":"17:00:00","time_zone":"Asia/Shanghai","weekdays":[5]}

}
Weekly project report
Scheduled for
Repeat
Weekly on Fri at 17:00 (Asia/Shanghai)
Status
Scheduled

Created “Weekly project report”, scheduled for Fridays at 17:00 Beijing time.

Weekly project report
Weekly on Fri at 17:00 (UTC+08:00 · China Standard Time)
Open

### Developertools

Inspect execution traces and detailed runtime information to troubleshoot issues with tool calls and task execution.

Duration
Turns
⊟
Calls
⊟
Search
Input
Model
Tools
SYSTEM
Initial System Prompt
Turn 1
USER
First run bash to print exactly NAVIGATION_OK, then read nav-a.md and nav-b.md with two read calls, then reply with the single word FIRST_DONE.
CONTEXT
Current runtime context: workspace policy, available skills, and this turn's environment snapshot.
ASSISTANT
Run bash to confirm the output, then read both navigation files.
TOOL
bash
{"command": "echo NAVIGATION_OK", "description": "Print NAVIGATION_OK"}
→
NAVIGATION_OK
TOOL
read
{"file_path": "nav-a.md"}
→
nav-a.md
TOOL
read
{"file_path": "nav-b.md"}
→
nav-b.md
ASSISTANT
FIRST_DONE
Turn 2
USER
Reply in markdown with a level-2 heading “Navigation Summary” and summarize both files.
ASSISTANT
Navigation summary: alpha nav, beta nav, and the NAVIGATION_OK output.
TOOL
bash
{"command": "ls -la", "description": "List workspace files"}
→
nav-a.md nav-b.md README.md
TOOL
grep
{"pattern": "NAVIGATION", "path": "."}
→
2 matches
TOOL
read
{"file_path": "README.md"}
→
README.md
ASSISTANT
Verified the workspace listing and grep results; the task is complete.
TOOL
Turn 1
 · 
Step 1
×
Summary
Payload
Result
Schema
Timing
NAVIGATION_OK
Started
2026-08-12 17:30:52.637
Duration
34 ms
Timing source
Session timestamps
Hierarchy
Assistant Message

## Developerexperience

### Startwithonecommand

Install Node.js, then launch the Web UI with npx.

$ 
npx @deepseek-ai/dsh web
Copy

### Installfromsource

Clone the full source and follow the setup instructions in the repository.

$ 
git clone https://github.com/deepseek-ai/deepseek-harness
Copy

## JointheDSHpluginecosystem

DeepSeek Harness is in preview, with evolving core plugins and APIs. We invite users and developers worldwide to explore the limits of intelligence together through open-source, reusable, and composable infrastructure.

View on GitHub
Developer docs
Community plugins
Cordis paper