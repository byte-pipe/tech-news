---
title: Share, Embed, and Curate Agent Sessions on DEV [Beta] - DEV Community
url: https://dev.to/devteam/share-embed-and-curate-agent-sessions-on-dev-beta-5bj6
site_name: devto
content_file: devto-share-embed-and-curate-agent-sessions-on-dev-beta
fetched_at: '2026-03-05T11:16:06.622644'
original_url: https://dev.to/devteam/share-embed-and-curate-agent-sessions-on-dev-beta-5bj6
author: Jon Gottfried
date: '2026-03-04'
description: Authors can now upload Agent Session transcripts to their DEV account. Those transcripts can be... Tagged with ai, forem, devto, gemini.
tags: '#ai, #forem, #devto, #gemini'
---

Authors can now upload Agent Session transcripts to their DEV account. Those transcripts can be curated, sliced up, shared publicly, and embedded into posts.This is a beta feature, and we are actively looking for feedback!

_Note:Please be very cognizant of what potentially sensitive data/keys might be in your transcripts. We have a redaction layer built in to the parser, but it is not going to catch every edge case. Do not upload sessions or data that you do not own, or that may open you up to security vulnerabilities. _

Now back to our fun announcement.

Every day, more people are creating software for the first time. Some have long histories as developers, and some have never seen a line of code in their life. In most cases, they're using the same tooling - coding agents. And yet, as these tools become ubiquitous there are surprisingly few ways to share your workflows and results in a standardized way beyond screenshots. Each tool has its own share link generator, each tool outputs logs in a different format. There are a few nascent projects out there to help, but they generally exist as standalone utilities or don't solve the sharing problem explicitly in a way that works on DEV.

We decided to solve that problem by making it possible to upload your transcripts to DEV, automatically parse them into a standardized format, and embed whole or partial sessions into your posts in a way that fits naturally into technical writing.

## Supported Platforms

To start with, our parser supports Gemini CLI, Codex, Claude Code, Pi, and GitHub Copilot CLI. If you use a different tool, you're encouraged to open a PR or Issue onForemto add a new parser yourself or ask us to do so. As an example, you can check out how our Gemini CLI parser works in our GitHub commit:https://github.com/forem/forem/commit/8f92c64a775ed3a0993e5edc0637112a95d1dae2#diff-d98a98bdd6e0d9154df5559b53644185d4ab13160e85c0fdaae3013ff985e27b

## Example Session

Here's a session from an example app I built using Gemini CLI for my pet guinea pig Pearl (obligatory pic in comments).

Wheeky Menu - Piggie Food Picker

 You


build me a simple web app to let my guinea pig tell me what food it wants

 Agent


Clarifying Application Needs/Defining Food Selection UI/Mapping Out The App's Flow

I'll build a vibrant, touch-friendly web app called"Pui Pui Picker"designed for guinea pigs (and their humans).

### The Plan:

1. Scaffold:Create a React + TypeScript project using Vite.
2. Design:A "big button" interface with high-contrast colors and bouncy animations to make it engaging.
3. Features:* Food Grid:Large cards for Hay, Carrots, Romaine, and Bell Peppers.
* Pui Pui Feedback:Visual and text-based "wheeking" feedback when an item is selected.
* History:A small "Last Requested" log to track what the piggie "chose."
4. Styling:Custom Vanilla CSS for a polished, modern look without external dependencies.

Does this sound like a good start for your guinea pig? Or should I add specific snacks they love?

I will start by scaffolding the project.

Show more

 Agent


▸

Shell

{"command":"npm create vite@latest . -- --template react-ts \u0026\u0026 npm ...

Input

{


"command"
:

"npm create vite@latest . -- --template react-ts && npm install"
,


"description"
:

"Scaffolding the React TypeScript project using Vite and installing dependencies."

}

 You


let's go simpler than vite and react

 Agent


Seeking Simplification for App/Constructing the index.html

I'll create a single-file, vibrant, and touch-friendly HTML application called"The Wheeky Menu". It will use large, colorful buttons and bouncy animations—perfect for a guinea pig's "input" (or a human's finger).

### The Plan:

1. Single File:Everything (HTML, CSS, JS) inindex.htmlfor instant loading.
2. Piggie-Centric UI:* Large Interaction Zones:Easy-to-hit cards for Hay, Carrots, Peppers, and Lettuce.
* Visual Feedback:Cards will "pop" and flash when tapped.
3. Features:* "Wheek!" Notification:A large visual alert showing what was picked.
* Order History:A simple log at the bottom to see what the piggie "requested" most.

I will now create theindex.htmlfile.

Show more

 Agent


▸

WriteFile

{"content":"\u003c!DOCTYPE html\u003e\n\u003chtml lang=\"en\"\u003e\n\u003che...

Input

{"content":"\u003c!DOCTYPE html\u003e\n\u003chtml lang=\"en\"\u003e\n\u003chead\u003e\n \u003cmeta charset=\"UTF-8\"\u003e\n \u003cmeta name=\"viewport\" content=\"width=device-width, initial...

Output

Successfully created and wrote to new file: /Users/jonmarkgo/Documents/GitHub/gemini-guinea-pig/index.html. Here is the updated code:
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
 <title>Wheeky Menu - Piggie Food Picker</title>
 <style>
 :root {
 --bg-color: #fdf6e3;
 --card-bg: #ffffff;
 --text-color: #5d4037;
 --accent-color: #ff8a65;
 --shadow: 0 8px 16px rgba(0,0,0,0.1);

 --color-hay: #fff176;
 --color-carrot: #ffb74d;
 --color-pepper: #ef5350;
 --color-lettuce: #81c784;
 }

 * {
 box-sizing: border-box;
 -webkit-tap-highlight-color: transparent;
 }

 body {
 font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
 background-color: var(--bg-color);
 color: var(--text-color);
 margin: 0;
 display: flex;
 flex-direction: column;
 align-items: center;
 min-height: 100vh;
 padding: 20px;
 overflow-x: hidden;
 }

 header {
 text-align: center;
 margin-bottom: 30px;
 }

 h1 {
 font-size: 2.5rem;
 margin: 0;
 color: var(--accent-color);
 text-shadow: 2px 2px 0px #fff;
 }

 p.subtitle {
 font-style: italic;
 margin-top: 5px;
 opacity: 0.8;
 }

 .grid {
 display: grid;
 grid-template-columns: repeat(2, 1fr);
 gap: 20px;
 width: 100%;
 max-width: 600px;
 }

 .food-card {
 background: var(--card-bg);
 border-radius: 24px;
 padding: 30px 10px;
 text-align: center;
 box-shadow: var(-
... (truncated)

 Agent


Constructing The Interface/Refining The UX Design

The"Wheeky Menu"is ready! It's a single-file web app with large, high-contrast buttons designed for easy "selection" (by snout or finger).

### How to use:

1. Open the file:You can openindex.htmldirectly in any web browser.
2. Piggie Input:Place your tablet or phone on the floor or near the cage. When your guinea pig taps or "boops" a card:* A large"WHEEK!"announcement pops up.
* The request is added to theRequest Historyat the bottom (so you can see what they picked if you step away).
* On mobile devices, it will provide a small vibration (haptic feedback) when touched.

I've used high-contrast colors and bouncy animations to make it visually stimulating. Enjoy the wheeking!

Show more

 You


Find the current Gemini CLI session log file. Look in ~/.gemini/sessions/ for the most recently modified .json or .jsonl file.

Then run the devto command to upload it:

Error: No file specified. Use --auto or provide a file path.\nRun 'devto --help' for usage.[Shell command 'devto --yes --tool gemini_cli --title "" "$(ls -t ~/.gemini/sessions//*.json ~/.gemini/sessions//*.jsonl 2>/dev/null | head -1)"' exited with code 1]

If devto is not installed, use curl directly:

jq: Bad JSON in --rawfile body : Could not open : No such file or directory[Shell command 'TMPJSON=$(mktemp) && jq -n --arg title "" --rawfile body "$(ls -t ~/.gemini/sessions//*.json ~/.gemini/sessions//*.jsonl 2>/dev/null | head -1)" '{title: $title, tool_name: "gemini_cli", body: $body}' > "$TMPJSON" && curl -s -X POST "${DEVTO_HOST:-https://dev.to}/api/agent_sessions" -H "Content-Type: application/json" -H "Accept: application/vnd.forem.api-v1+json" -H "api-key: $DEVTO_API_KEY" -d @"$TMPJSON" && rm -f "$TMPJSON"' exited with code 2]

After uploading, display the URL of the created session to the user.

Show more

 Agent


Examining Upload Strategies/Implementing Dev Upload Skill

I will activate thedev-uploadskill to securely and efficiently upload your session log to DEV.to.

 Agent


▸

Activate Skill

{"name":"dev-upload"}

Input

{


"name"
:

"dev-upload"

}

Output

<activated_skill name="dev-upload">
 <instructions>
 # Upload Session to DEV

Upload the current session transcript to [DEV](https://dev.to) as an Agent Session.

## Steps

### 1. Find the transcript

Find the current session's transcript file — the most recently modified `.jsonl` file:
- Claude Code: `~/.claude/projects/` (recursive)
- Codex: `~/.codex/sessions/`
- Gemini CLI: `~/.gemini/sessions/`
- GitHub Copilot: `~/.copilot/`
- Pi: `~/.pi/sessions/`

Use the agent's own session context if available to identify the exact path.

### 2. Load config and check for API key

Load all config in a single bash call:

```bash
if [ -f ~/.config/devto/config ]; then source ~/.config/devto/config; fi
API_KEY="${DEVTO_API_KEY:-${API_KEY:-}}"
HOST="${DEVTO_HOST:-https://dev.to}"
echo "API_KEY=${API_KEY:+SET}"
echo "HOST=$HOST"
```

If no key is found:
1. Tell the user they need a DEV API key and link them to https://dev.to/settings/extensions to generate one.
2. Ask the user to paste their key here in the chat.
3. Once they provide it, save it (along with the host) so they never have to do this again:

```bash
mkdir -p ~/.config/devto
cat > ~/.config/devto/config <<'CONF'
DEVTO_API_KEY="THE_KEY_THEY_GAVE_YOU"
DEVTO_HOST="https://dev.to"
CONF
```

4. Then continue with the upload. Do NOT stop or ask the user to run commands themselves.

### 3. Upload

Do the entire upload in a single bash call. Replace TRANSCRIPT, TITLE, HOST, and API_KEY with actual values:

```bash
set -e
TRANSCRIPT="/path/to/session.jsonl"
TITLE="the session title"
HOST="https://dev.to"
API_KEY="the-key"

TMPJSON=$(mktemp)
trap "rm -f '$TMPJSON'" EXIT

jq -n \
 --arg title "$TITLE" \
 --arg tool_name "auto" \
 --rawfile body "$TRANSCRIPT" \
 '{title: $title, tool_name: $tool_name, body: $body}' > "$TMPJSON"

RESPONSE=$(curl -s -w "\n%{http_code}" \
 -X POST "$HOST/api/agent_sessions" \
 -H "Content-Type: application/json" \
 -H "Accept: application/vnd.forem.api-v1+json" \
 -H "api-key: $API_KEY"
... (truncated)

 Agent


Defining the Upload Process/Analyzing the Configuration Steps

I'll locate your most recent session log and check for a DEV.to API key to begin the upload.

 Agent


▸

Shell

{"description":"Locating the most recent session log and checking for a DEV.t...

Input

{"description":"Locating the most recent session log and checking for a DEV.to API key.","command":"# Find the most recent session log\nTRANSCRIPT=$(ls -t ~/.gemini/sessions/*.jsonl 2\u003e/dev/nul...

Output

Output: TRANSCRIPT=
API_KEY=SET
HOST=https://dev.to
Process Group PGID: 73065

 Agent


Searching the File System/Refining the Search Strategy

I'll look for the session log again, including both.jsonand.jsonlfiles across all session subdirectories.

 Agent


▸

Shell

{"command":"# Find the most recent session log\nTRANSCRIPT=$(ls -t ~/.gemini/...

Input

{"command":"# Find the most recent session log\nTRANSCRIPT=$(ls -t ~/.gemini/sessions/**/*.json ~/.gemini/sessions/**/*.jsonl 2\u003e/dev/null | head -1)\necho \"TRANSCRIPT=$TRANSCRIPT\"","descript...

Output

Output: TRANSCRIPT=
Process Group PGID: 73508

 Agent


Exploring the Directory

I'll list the contents of~/.gemini/sessions/to find the exact session log files.

 Agent


▸

Shell

{"command":"ls -R ~/.gemini/sessions/ | head -n 20","description":"Listing th...

Input

{


"command"
:

"ls -R ~/.gemini/sessions/ | head -n 20"
,


"description"
:

"Listing the contents of the Gemini CLI sessions directory."

}

Output

Output: ls: /Users/jonmarkgo/.gemini/sessions/: No such file or directory
Process Group PGID: 73515

 Agent


Examining Session Locations/Inspecting Gemini Directory Contents

I'll list the contents of the~/.gemini/directory to locate the session logs.

 Agent


▸

Shell

{"command":"ls -F ~/.gemini/","description":"Listing the contents of the ~/.g...

Input

{


"command"
:

"ls -F ~/.gemini/"
,


"description"
:

"Listing the contents of the ~/.gemini directory."

}

Output

Output: antigravity/ google_accounts.json mcp-oauth-tokens-v2.json settings.json tmp/
commands/ history/ oauth_creds.json settings.json.orig trustedFolders.json
GEMINI.md installation_id projects.json state.json user_id
Process Group PGID: 73530

 Agent


Checking the History

I'll list the contents of~/.gemini/history/to find the session log.

 Agent


▸

Shell

{"command":"ls -F ~/.gemini/history/ | head -n 20","description":"Listing the...

Input

{


"command"
:

"ls -F ~/.gemini/history/ | head -n 20"
,


"description"
:

"Listing the contents of the ~/.gemini/history directory."

}

Output

Output: cookieparser/
gemini-dog-app/
gemini-guinea-pig/
mlh-core/
Process Group PGID: 73565

 Agent


Examining Project Location

I'll list the contents of~/.gemini/history/gemini-guinea-pig/to find the current session's log.

 Agent


▸

Shell

{"command":"ls -t ~/.gemini/history/gemini-guinea-pig/*.jsonl 2\u003e/dev/nul...

Input

{


"command"
:

"ls -t ~/.gemini/history/gemini-guinea-pig/*.jsonl 2>/dev/null | head -1"
,


"description"
:

"Searching for the most recent session log in the history directory."

}

Output

Output: (empty)
Process Group PGID: 74637

 Agent


Beginning File Enumeration

I'll list all files in~/.gemini/history/gemini-guinea-pig/to find the session log.

 Agent


▸

Shell

{"command":"ls -R ~/.gemini/history/gemini-guinea-pig/ | head -n 100","descri...

Input

{


"command"
:

"ls -R ~/.gemini/history/gemini-guinea-pig/ | head -n 100"
,


"description"
:

"Listing all files in the history folder to locate the log file."

}

Output

Output: (empty)
Process Group PGID: 75100

 Agent


Pinpointing the Missing Path/Re-evaluating the Scope

I'll list the contents of~/.gemini/tmp/gemini-guinea-pig/to find the session log.

 Agent


▸

Shell

{"command":"ls -F ~/.gemini/tmp/gemini-guinea-pig/ | head -n 20","description...

Input

{


"command"
:

"ls -F ~/.gemini/tmp/gemini-guinea-pig/ | head -n 20"
,


"description"
:

"Listing the contents of the ~/.gemini/tmp/gemini-guinea-pig directory."

}

Output

Output: chats/
logs.json
Process Group PGID: 75368

 Agent


Investigating Log Location

I'll read the first 10 lines oflogs.jsonto see if it's the session log.

 Agent


▸

Shell

{"command":"head -n 10 ~/.gemini/tmp/gemini-guinea-pig/logs.json","descriptio...

Input

{


"command"
:

"head -n 10 ~/.gemini/tmp/gemini-guinea-pig/logs.json"
,


"description"
:

"Reading the beginning of logs.json to confirm its format."

}

Output

Output: [
 {
 "sessionId": "295d2fe2-6276-49c4-9229-db8a61d33f2a",
 "messageId": 0,
 "type": "user",
 "message": "build me a simple web app to let my guinea pig tell me what food it wants",
 "timestamp": "2026-03-04T01:15:24.210Z"
 },
 {
 "sessionId": "295d2fe2-6276-49c4-9229-db8a61d33f2a",
Process Group PGID: 75447

 Agent


Investigating the Discrepancy/Unraveling File Paths

I'll look for any other directories starting with 's' in~/.gemini/to find the sessions folder.

 Agent


▸

Shell

{"command":"ls -d ~/.gemini/s*","description":"Listing directories in ~/.gemi...

Input

{


"command"
:

"ls -d ~/.gemini/s*"
,


"description"
:

"Listing directories in ~/.gemini that start with 's'."

}

Output

Output: /Users/jonmarkgo/.gemini/settings.json /Users/jonmarkgo/.gemini/settings.json.orig /Users/jonmarkgo/.gemini/state.json
Process Group PGID: 75492

 Agent


Examining Possible Locations

I'll list all directories starting with.geminiin my home directory to find the session logs.

 Agent


▸

Shell

{"command":"ls -d ~/.gemini*","description":"Listing all directories and file...

Input

{


"command"
:

"ls -d ~/.gemini*"
,


"description"
:

"Listing all directories and files that start with .gemini in the home folder."

}

Output

Output: /Users/jonmarkgo/.gemini
Process Group PGID: 75500

 Agent


Searching for Session Logs/Identifying Alternative Locations

I'll search for all.jsonand.jsonlfiles in~/.gemini/to find the correct session log.

 Agent


▸

Shell

{"description":"Searching recursively for .json and .jsonl files in the ~/.ge...

Input

{


"description"
:

"Searching recursively for .json and .jsonl files in the ~/.gemini directory."
,


"command"
:

"find ~/.gemini/ -name
\"
*.json
\"
 -o -name
\"
*.jsonl
\"
 | head -n 20"

}

Output

Output: /Users/jonmarkgo/.gemini/google_accounts.json
/Users/jonmarkgo/.gemini/state.json
/Users/jonmarkgo/.gemini/oauth_creds.json
/Users/jonmarkgo/.gemini/settings.json
/Users/jonmarkgo/.gemini/projects.json
/Users/jonmarkgo/.gemini/trustedFolders.json
/Users/jonmarkgo/.gemini/antigravity/mcp_config.json
/Users/jonmarkgo/.gemini/mcp-oauth-tokens-v2.json
/Users/jonmarkgo/.gemini/tmp/08d27515e40a8c790d53798895cf6650d5843987a3978f7ef5be01987a09b3e1/logs.json
/Users/jonmarkgo/.gemini/tmp/a9c39dae5288a24cdef1cf1d8c6bc99a5cf8b751707de794545fc5f5986be7b2/logs.json
/Users/jonmarkgo/.gemini/tmp/dd9dc36095d552fc5d0c79d94e889e2c50c1b76a76ea3f41ac6b22dd6076ce19/logs.json
/Users/jonmarkgo/.gemini/tmp/dd9dc36095d552fc5d0c79d94e889e2c50c1b76a76ea3f41ac6b22dd6076ce19/chats/session-2025-12-04T21-23-e153598e.json
/Users/jonmarkgo/.gemini/tmp/gemini-guinea-pig/logs.json
/Users/jonmarkgo/.gemini/tmp/gemini-guinea-pig/chats/session-2026-03-04T01-15-295d2fe2.json
/Users/jonmarkgo/.gemini/tmp/gemini-guinea-pig/chats/session-2026-03-04T12-42-295d2fe2.json
/Users/jonmarkgo/.gemini/tmp/79261791c475d806f2ff6cdf73b50843055032e35b2854d7e91e3a92762f2e96/logs.json
/Users/jonmarkgo/.gemini/tmp/79261791c475d806f2ff6cdf73b50843055032e35b2854d7e91e3a92762f2e96/chats/session-2025-12-06T18-02-b9fe7181.json
/Users/jonmarkgo/.gemini/tmp/79261791c475d806f2ff6cdf73b50843055032e35b2854d7e91e3a92762f2e96/chats/session-2025-11-18T16-06-1f38a3eb.json
/Users/jonmarkgo/.gemini/tmp/79261791c475d806f2ff6cdf73b50843055032e35b2854d7e91e3a92762f2e96/chats/session-2025-11-18T18-32-22205976.json
/Users/jonmarkgo/.gemini/tmp/79261791c475d806f2ff6cdf73b50843055032e35b2854d7e91e3a92762f2e96/chats/session-2025-11-18T16-52-0863224c.json
Process Group PGID: 76229

 Agent


Analyzing File Locations/Pinpointing Key Files

I'll select the latest session log from~/.gemini/tmp/gemini-guinea-pig/chats/and upload it to DEV.to using the discovered session file and your API key.

 35 of 35 messages


Let's check out how the upload, curation, and embedding workflow works.

## Upload a Session

First, you need touploada session. You can drag and drop your session transcripts via your browser on theAgent Sessions page. We will soon be launching a CLI and Agent skill to give you a slash command for uploads as well.

## Curate a Session

Once you upload the session, you cancurateit. You can select which pieces of a session transcript are included in your whole-session embed. You can mass enable/disable different pieces of your transcript, as shown here.

## Slice Up a Session

If you don't want to embed your whole session (even in curated form) you can instead use theSlicetool to create a sub-transcript that can include any and all parts of a session. You can have multiple Slices per session, if you want to break up your prompt and embed it in different places in your post.

## Share a Session

Lastly, to make this utility more generally useful beyond DEV, you can also share curated Agent Sessions publicly by using theMake Publicbutton. See my sessionhere.

We look forward to seeing what you build and share with this new feature. Happy hacking!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)


Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse
