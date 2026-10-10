---
title: REA — Reverse Engineering for Your Coding Agent
url: https://rea.tools/
site_name: hackernews_api
content_file: hackernews_api-rea-reverse-engineering-for-your-coding-agent
fetched_at: '2026-10-10T16:07:53.593327'
original_url: https://rea.tools/
author: modinfo
date: '2026-10-10'
description: Reverse engineer apps, binaries and browser behavior with your coding agent. Follow clear guides and try interactive examples with REA.
tags:
- hackernews
- trending
---

Reverse engineering, with your coding agent

# Find out howsoftware works.

REA gives your agent the tools to inspect a program and explain
 what it does.

See how REA works ↓

Setup guide

Showcases →

Already know RE?Skip to analysis guides →

Want to go deeper?Read the Blog →

## Set up REA

Copy this into your coding agent:

Your coding agent

 Copy
 

›Install REA and connect it to this coding agent using npx
 rea-agents@latest setup. Show me the setup plan for approval,
 then verify the installation.

Or run this in your terminal:

npx rea-agents@latest setup

 Copy
 

Approve the setup plan, then restart your agent.

## What is reverse engineering?

Finding out how software works byexamining the program itself.

The goal: understand a feature well enough toexplain it,change itorrebuild it.

One question:why does Calculator give 220 for 200 + 10%?

Before REA · You investigate ityourself

01
 Decode branches
 

02
 Trace calls
 

03
 Recover the rule
 

Original x64 · selected instructions

0x180124945: MOV EAX, dword ptr [R13 + 0x18]
0x180124949: CMP EAX, 0x5c
0x18012494c: JZ 0x180124aba
0x180124952: CMP EAX, 0x5b
0x180124955: JZ 0x180124aba

0x18012495b: MOV EDX, 0x64
0x180124960: LEA RCX, [RSP + 0x160]
0x180124968: CALL 0x180122650
0x18012496e: LEA RDX, [R13 + 0x160]
0x180124975: LEA RCX, [RSP + 0x78]
0x18012497a: CALL 0x180109720

0x18012497f: MOV RSI, RAX
0x180124982: MOV qword ptr [RSP + 0x28], RAX

0x180124987: LEA RDX, [RSP + 0x160]
0x18012498f: MOV RCX, RAX
0x180124992: CALL 0x180123190

; … value-copy instructions omitted …

0x180124a14: MOV RDX, RDI
0x180124a17: LEA RCX, [RSP + 0xf8]
0x180124a1f: CALL 0x180109720
0x180124a24: LEA R8, [RSP + 0x30]
0x180124a29: MOV RDX, RAX
0x180124a2c: LEA RCX, [RSP + 0xb8]
0x180124a34: CALL 0x180123c10

You decode the instructions, follow the calls and reconstruct
 the calculation.

With REA · You askyour agent

### One prompt.

Ask your agentin plain English.

Example prompt · Calculator

 Copy
 

›Use REA to inspect Windows Calculator. Why does 200 + 10%
 give 220?

Example answer · based on the findings

After +, the % button takesa percentage of the first number.

10% of 200 = 20
↓
200 + 20 = 220

REA supplies

 The handler’s instructions, decompiled code and calls.
 

Your agent explains

 Which branch applies, what it calculates and how to rebuild
 it.
 

 Selected assembly from the installed Calculator DLL. The thoughts
 and reply illustrate the findings.
 
Continue with the Calculator example ↓

Let's try two examples.Change a game's speed, then return to Calculator and rebuild its %
 button.

Example 01 · Chrome’s dinosaur game

## Why does the dinosaur get faster?

Goal

 Rebuild the game with
 
adjustable speed.

Why reverse engineer it?

 To reproduce its acceleration, we need
 
the rule in the running game
: how fast it
 starts, how much it increases and when it stops.
 

Play the reconstruction

 6 → 10 → 13
 

 Play
 

Jump ↑

Restart

Speed 
6.0

 Use the
 recovered acceleration rule

Original rule: start at 6, then increase toward 13.

 Move the slider to set your own speed. Space or Jump clears a
 cactus.
 

Enable JavaScript to play the reconstruction. The code and
 explanation above remain readable.

REA returned

The script actually running in the page.The
 agent reads its update function and speed settings, then uses
 that rule in a new game.

Example prompt · Dinosaur game

 Copy
 

›Use REA to inspect this dinosaur game. Why does it get
 faster? Show the speed rule, then build a small version with
 an adjustable speed.

Inspected target:wayou’s Chromium-derived browser edition.

REA · loaded index.js · selected lines

if (this.currentSpeed < this.config.MAX_SPEED) {
 
this.currentSpeed += this.config.ACCELERATION;

}

Start at 6.Add0.001each
 update without a collision, while speed is below13.

Open the speed lab →

What each part does

1. 01 · REARead the running game’s scriptReturn its actual code and settings to the agent.
2. 02 · Your agentRebuild the rule, add a controlUse the recovered acceleration in a small game with a speed
 slider.
3. 03 · YouChange the speed and playTry the original acceleration, then choose your own
 pace.

 See the script, checks and how to try the analysis
 

REA inspected the HTTP browser edition through a local debugging
 connection and returned the loadedindex.js,
 including its source and digest.

Selected settings from the inspected script

ACCELERATION: 0.001,
MAX_SPEED: 13,
SPEED: 6

We called the original game’s update function in a controlled
 browser check, with obstacles and automatic scheduling disabled.
 After 4,000 updates, speed was 10.0; after 10,000, it was 13.0,
 rounded to one decimal.

The new mini-game keeps that speed rule. Its drawing, jumping and
 collision code are a small teaching implementation.Open the labto see the new code
 and run the same speed check.

To inspect the target yourself, follow thebrowser connection stepsusingthe dinosaur page. Give your agent that page URL and your local debugging
 endpoint, then copy the prompt above.

Inspected speed code·Chromium Authors · BSD license

Example 02 · Windows Calculator

## Rebuild Calculator’s % button.

We saw why200 + 10% gives 220.Now let’s recover
 the rules for both + and ×, and try them.

Goal

 Build a small calculator that handles
 
both + and × correctly.

Why reverse engineer it?

 The same button uses
 
different rules after + and ×.
 We inspect the
 installed app to find which number the percentage is applied to.
 

Try the calculation

 200 + 10%
 

 200 × 10%
 

200 +

20

 %
 

 =
 

 Reset
 

10% of 200 = 20. Then 200 + 20 = 220.

 Interactive illustration of the inspected percentage rule.
 

REA returned

One branch divides by 100. The other also multiplies by the
 first number.The agent uses both to recreate the % button.

For this example,previous = 200andcurrent = 10.

Example prompt · Rebuild the % button

 Copy
 

›Use REA to inspect Windows Calculator’s % button. Recover
 the rules after + and ×, then build a small calculator that
 uses both.

Readable summary of the % handler

if (operation == multiply || operation == divide) {
 percent = current / 100;
} else {
 
percent = current * previous / 100;

}

With +

Take 10% of the first number.
10% of 200 = 20 → 200 + 20 = 220

With ×

Turn 10% into 0.1.
200 × 0.1 = 20

From the installed app to a working % button

1. 01 · REA reads calc.exeIt launches the Calculator appThe code opensms-calculator:. The agent then
 selects the installed app’s library.
2. 02 · REA reads the libraryReturn the % handler’s codeThe function checks the operator and uses the constant100.
3. 03 · Your agent interprets itExplain and reproduce the rulesCrosscheck the branch with Microsoft’s source, then try + and
 × above.

See the real code and how the answer was checked

REA · selected original instructions

0x180124945: MOV EAX, dword ptr [R13 + 0x18]
0x180124949: 
CMP EAX, 0x5c

0x18012494c: JZ 0x180124aba
0x180124952: 
CMP EAX, 0x5b

0x180124955: JZ 0x180124aba
0x18012495b: 
MOV EDX, 0x64

Operator IDs · Microsoft’s source

#define IDC_MUL 92 // 0x5c
#define IDC_DIV 91 // 0x5b
#define IDC_PERCENT 118 // 0x76

0x64 = 100

Inspected with REA 4.1.0: Windows Calculator 11.2508.4.0, x64. The
 readable summary uses names from Microsoft’s public source to
 explain the recovered branch.

Percentage implementation·Microsoft’s test cases·Native setup guide

Your first investigation

## Try REA on a small app.

Download our Notes example, trace its CSV export, and check one
 changed input.

Try the guided example

## Want to go deeper?

Tell your agent what you want to understand or build. With REA,
 you can work together on anything fromcloning this websitetoreconstructing a game from its executable.

Example prompt · Website
 

 Copy
 

›Use REA to inspect https://rea.tools/. Clone this website
 for me.

Yes, this one.

Example prompt · Game reconstruction
 

 Copy
 

›Use REA to reconstruct this game from its executable.
 Recover the gameplay logic in C and test it against the
 original.

See the DX-Ball case study →

For setup and analysis steps, choose your target:

### Native binaries

Inspect functions, strings, references and call relationships in
 executables and libraries.

Native analysis guide

### JavaScript & Electron

Map modules, routes, IPC and native dependencies from an
 application folder or ASAR archive.

Application workflows

### Browser & runtime activity

Capture selected browser or process activity, then compare the
 results across runs.

Browser observation guide

## Any questions?

Read the FAQ,chat with us on Discord,
 oropen a GitHub issuefor bugs and feature requests.

## Join the community

Share investigations and get help from other REA users on Discord.
 Follow REA on X for project updates.

Join the community

Follow @reatools on X