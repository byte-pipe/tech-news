---
title: Agent Memory Patterns - Tim Kellogg
url: https://timkellogg.me/blog/2026/04/27/memory-patterns
site_name: tldr
content_file: tldr-agent-memory-patterns-tim-kellogg
fetched_at: '2026-04-28T12:26:20.334495'
original_url: https://timkellogg.me/blog/2026/04/27/memory-patterns
date: '2026-04-28'
description: A short HOW TO guide for agent memory systems. Especially the difference between blocks, files and skills.
tags:
- tldr
---

# Agent Memory Patterns

Mon April 27, 2026

Say you get asked to “add memory” to an agent. What does that mean? How do you do it?

There’s three common kinds of mutable memory:

1. Files
2. Memory blocks
3. Skills

If you don’t need the agentto learn, then you’re looking in the wrong place. You don’t need memory.
But this post might also be useful if you’re just using agents, like a coding agent.

## Files are for data & knowledge

Everything in this post needs to satisfy the following functions:

1. Exploreto find items —ls,find,grep, or equivalent tools
2. Readan item —cat, or some ReadFile tool
3. Writean item — pipe,sed, or some WriteFile tool

For files, all that seems fairly obvious. Files can be complicated, but those are the parts that are
important for files to work as agent memory.
Files don’t have to be literal files. If they are, you can provide aBashtool (orPowershell) that
gives you cool Linux utilities for navigating the filesystem, reading parts of files, etc.

But also, you can absolutely use database records or S3 blobs. As long as:

1. Each file has ahierarchical path, to enable exploring, but also so that files are a key-value store
2. Long textcontent. We don’t care too much about file structure or validation, but please do give the
 agent space to work.

## Memory blocks are a learnable system prompt

Memory blocks are just a flat key-value store. Except the key isn’t used for looking things up, it’s just
used for writing. All memory blocks areincluded inlinein the system prompt, or user prompt.

Where to put it?

* System prompt— this one’s easier in a lot of systems. But can causecache invalidation(higher token cost)
when the agent calls WriteBlock.
* User prompt(prepend) — This also works, it’s still highly visible to the LLM, and it causes less prompt cache 
invalidation issues.

Either is fine. User prompt is slightly better, I guess.

Required tools:

* WriteBlock(key, value [, sort_order])— I like including a sort_order, because we know order does matter,
so let the agent control it too. Not a huge deal though.

Optional tools:

* ListBlocks()
* ReadBlock(key)

Theoretically you don’t need these because they’re in the prompt already, but I’ve noticed that coding agents
will always try to insert them and agent agents will always call them, every time. So, whatever that means..

### What goes into blocks?

Blocks are a learnable system prompt. Put stuff in there that tends to go into the system prompt — behavior,
preferences, identity, character, etc.

Since it’s in the prompt, the agent can’t look away or ignore. So you may want to promote from file to block
if you want toguarantee visibility, like you don’t want to risk the agent forgetting to read a file.

## Skills are indexed files

Skills are a combination of files & memory blocks. They’re files, literally, but they also are represented in 
the system prompt.

It’s just a directory with aSKILL.mdfile:

the-skill/
 SKILL.md
 important-concept-1.md
 helper-script.py
 worksheet.csv

TheSKILL.mdis generally just a plain markdown file, but it has a special top few lines at the start of the file:

---
name: the-skill
description: what it does and when to use it
---

Thedescriptionis the critial part. Bothnameanddescriptiongo into the system prompt, but thedescriptionis the trigger. It encourages the agent to use the skill in the right circumstance.

### Do you need a Skill tool?

Not really.Claude Codehas aSkill(name)tool, but functionally it’s the same as the agent
readingthe-skill/SKILL.mdwith a regular Read tool. The benefits are harness-side: lazy-loading
the SKILL.md content (so it only enters the context window when invoked), telemetry, and permission
scoping.

If you skip the dedicated tool, just tell the agent in the system prompt:“When a skill matches,
read its SKILL.md before doing the thing.”Works fine.

### What goes into skills?

Data or instructions that are only needed in certain circumstances. Honestly “skill” is actually a really 
good name for them.

The key phrase isprogressive disclosure— skills unfold as needed. The agent reads files as it deems
necessary. Typically you’ll include file references in theSKILL.mdfile, like“Read important-concept-1.md
when you need to…“. There’s nothing special, no notation, it’s just hints for the agent.

Scripts and data are nice too. Obviously scripts are only useful if you enable a Bash tool, but scripts especially
can act like aagent optimizer. Like, sure, the agent can probably figure out how to string together all the
headers to authenticate to your weird API, or you can just make a script for it and skip the LLM.

### Editable skills

Most people think of skills as being immutable programs of English. Sure, they’re useful when used like that,
but they’re even more useful when you allow your agent to change them.

A great way to use skills is as anexperience cache. At the end of a long investigation or research, have the
agent record the experience in a skill. Next time, it just reads the skill!
Could you use files for this? Yes, but thedescriptionfield in the system prompt makes it more likely to be 
used at the right time.

## Observability

How do you know when the agent is using memory well?

For files & skills, you can start at the entry point and construct a graph of which files reference which other
files:

1. For each file
2. Search for the file name
3. Pair “file referenced from” -> file

Then compare against reality. Find all the times those files were accessed in that order versus not. If they’re
referenced randomly, that means the agent needs to use Search or ListFiles tools to navigate. That might mean
your files or skills are becoming too unwieldy.

Also, you should monitor memory block size & count. Definitely keep them under 5000, probably under 500 characters.
When the blocks get too big, they tend to confuse the agent.

Unfortunately, given the nature of agents, there’s not that much you can do for observability. But these two 
things do tend to be useful to monitor.

## Search index

Is a search index a good idea? Yes absolutely. It’s just annoying.

Seriously, it adds a data asset that needs to be maintained. Most of the time that’s not a huge deal, but when
it is, it is. Your call.

## Git is an agent database

I highly recommend versioning files & ideally also skills & memory blocks. In open-strix I store memory blocks
in yaml so they version and diff cleanly.

Versioning gives you checkpoints and lets you see evolution. It also lets you rollback or let the agent discover
when a bad change was made. I’ve tried to use branching and merging, but not successfully.

## Bad ideas

Knowledge graphsand other writabledata models, e.g. backend by SQL, tend to not work very well because the
LLM’s weights doesn’t know about their schemas. Most people talk themselves into knowledge graphs because they
have structure and historically structure has been good. But the only structure LLMs need is tokens. They reason
just fine in token space.

## Good (but weirder) ideas

I’ve discovered that some types of generic data structures can be very useful for agents, for special purposes.

Issue trackersare oddly useful. I’ve been usingchainlink, which is an issue tracker specifically
for agents, but I’ve heardAsanaalso works fine. Probably any issue tracker would work. An issue tracker
gives you a searchable work queue.

I’ve added aninterest backlogto all of my agents now. Any time they come across something weird, interesting,
or annoying they can create an issue and tag itinterest. Then, during the night while I sleep they work 
through the backlog. This has led to multiple agents making connections between ideas & things I hadn’t discovered
yet, and generally coming up with fresh ideas that feel honestly novel.

Also, anappend-only logis super useful. I have anevents.jsonlfile that goes into all of my agents. The
agent harness writes every single event that happens, like tool calls and messages, and appends a JSON object 
minified to theevents.jsonlfile. It’s not writable memory in the normal sense, but the agent can read it
to give grounded answers about what it actually did.

# Conclusion

Editable memory is extremely powerful. I highly recommend trying it out. Hopefully this helped.

tags:aiLLMsengineeringagents

Subscribe

Tweet