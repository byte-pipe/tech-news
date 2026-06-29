---
title: My commit message said "You've hit your session limit" - DEV Community
url: https://dev.to/shyamala_u/my-commit-message-said-youve-hit-your-session-limit-2abn
site_name: devto
content_file: devto-my-commit-message-said-youve-hit-your-session-limi
fetched_at: '2026-06-29T19:36:42.886824'
original_url: https://dev.to/shyamala_u/my-commit-message-said-youve-hit-your-session-limit-2abn
author: Shyamala
date: '2026-06-29'
description: How I ended up running a local LLM to generate my git commit messages. Tagged with genai, ollama, learning, llm.
tags: '#genai, #ollama, #learning, #llm'
---

## 🧐 Context 🧐

I had this one-liner that I was using.

git commit 
-m
 
"
$(
git diff 
--staged
 | claude 
-p
 
"Provide a simple, one-line git commit message based on this diff following best practices. Output absolutely nothing else."
)
"

Enter fullscreen mode

Exit fullscreen mode

Pipe the staged diff to Claude, get a commit message back. Worked well until I hit my Claude usage limit mid commit. The shell captured the error instead of a commit message.

So I had a commit in my repo that said:

You've hit your session limit

That's when it hit me! Voila, ✨My use case for a Local Model.✨

## ⚠️ Disclaimer ⚠️

* I am learning GenAI, this is my journey
* This is not a tutorial
* What is obvious to you might not be obvious to me

## Getting Ollama running

Ollamalets you run open source models locally. After installing it, you have a server running athttp://localhost:11434.

ollama pull qwen2.5-coder:1.5b

Enter fullscreen mode

Exit fullscreen mode

I pickedqwen2.5-coder:1.5bbecause it's small and code-aware.

Why 1.5b specifically? My laptop has 8GB RAM. That's not a lot when you're running a model locally.

Here's the rough math (these are estimates from my machine, yours may vary):

* Total Mac RAM: 8.0 GB
* macOS + apps already running: ~4.0 to 5.0 GB
* Model loaded in memory: ~1.2 GB (based on the model file size of ~1 GB)
* Context window: ~0.03 GB
* Remaining: ~1.77 to 2.77 GB free

Interestingly, despite being a 1.5 billion parameter model, qwen2.5-coder:1.5b only takes up about 1 GB of disk space. That's because it's a quantized model.

Quantizationmeans themodel's weightsare stored at lower precision, using 4-bit or 8-bit integers instead of the usual 16-bit or 32-bit floating point numbers. This significantly reduces the model size and memory footprint, although it may slightly impact accuracy.

I tried larger models. My laptop became unusable. Fans spinning, apps freezing, the whole thing. So 1.5b it is.

There's another quantized model I found that could work —gemma3:1b-it-qat. I plan to test it sometime and see how it compares in terms of performance and resource usage.

## First attempt

I swapped Claude with Ollama in my one-liner:

git commit 
-m
 
"
$(
git diff 
--staged
 | ollama run qwen2.5-coder:1.5b 
"Provide a simple, one-line git commit message based on this diff following best practices. Output absolutely nothing else."
)
"

Enter fullscreen mode

Exit fullscreen mode

I ran it against a change where I had removed thetoolssection from some agent config front matter from 6 files. This Worked

The commit message said it was a change to a README file.

### 🤔 What does this mean? 🤔

Despite qwen2.5-coder:1.5b's large native context window of 32,768 tokens, Ollama actually restricts the default context size when running without a Modelfile.

I checked Ollama's logs and found this line:

level=INFO source=routes.go:2073 msg="vram-based default context" total_vram="5.3 GiB" default_num_ctx=4096

Enter fullscreen mode

Exit fullscreen mode

It shows that based on my machine's VRAM of 5.3 GiB, Ollama set a defaultnum_ctxof 4096 tokens. That's why the model only saw the beginning of the diff and guessed about the README file.

## Second attempt

I thought maybe I need a better prompt. So I ran it again with more instructions.

This time it said the change was incode-reviewer.md. That was one of the 6 files, and it completely ignored the other 5.

The important thing here is that the model did not complain. It did not say "I couldn't read the rest". It just gave me a confident answer based on partial input.

At this point I understood tuning the prompt alone is insufficient and I need to tune the model too.

## Creating a Modelfile

This is something I just learned. A Modelfile is a config layer on top of a base model. You can change parameters and create a named model from it.

FROM
 qwen2.5-coder:1.5b

PARAMETER num_ctx 8192 
PARAMETER temperature 0.2

Enter fullscreen mode

Exit fullscreen mode

Two things I changed:

num_ctx 8192— While qwen2.5-coder:1.5b can handle up to 32k tokens natively, Ollama defaults to a smaller context window when run without a Modelfile (in my case, 4096 based on VRAM). I bumped it to 8k, and be memory-efficient on my 8GB machine.

temperature 0.2— lower temperature for more predictable output. For commit messages I don't want creative, I want consistent.

ollama create qwen-commit 
-f
 ./Modelfile

Enter fullscreen mode

Exit fullscreen mode

Now I have a model calledqwen-committhat I can use for this specific task.

By the way, a Modelfile is not the only way to set these. You can use the REST API directly, and pass anoptionsobject:

curl http://localhost:11434/api/generate 
-d
 
'{
 "model": "qwen2.5-coder:1.5b",
 "prompt": "${YOUR_PROMPT}",
 "options": {
 "temperature": 0.2,
 "num_ctx": 8192
 }
}'

Enter fullscreen mode

Exit fullscreen mode

For my use case the Modelfile made more sense because I just want to callollama run qwen-commitand have everything pre-configured.

## Third attempt

With the bigger context window, the model could now see all 6 files. But it still described the change as "⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏ ⠋`diff feat(.opencode/agent): update tool list for code-reviewer, frontend-enginee frontend-engineer, go-backend-engineer, project-lead, req requirements-analyst, solution-architect". Better, Mouthful but wrong.

### 🤔 What does this mean? 🤔

The model was reading the full diff now but commit message was technically correct, but nothing like what we would write in a commit message. Look at how it hadfrontend-enginee frontend-engineerorreq requirements-analyst

So I changed the prompt. Instead of making the model figure it out, I just told it.

bash
affected_files=$(git diff --staged --name-only | paste -sd, -)

Enter fullscreen mode

Exit fullscreen mode

Then added to the prompt:"Note that the changes are located in these files: [$affected_files]"

After this the commit messages got much better. The model didn't have to guess anymore.

## One more thing

The commit messages were now accurate but the model kept wrapping them in weird formatting despite the prompt saying not to. Sometimes backticks. Sometimes it prefixed with "diff". Sometimes random quotes around the message.

So I added a cleanup step to strip all of that out:

bash
msg=$(echo "$msg" | tr -d '\r' | sed -E \
 -e 's/

```(diff)?//g' \
 -e 's/^diff[[:space:]]+//I' \
 -e 's/^[[:space:]]+//;s/[[:space:]]+$//' \
 -e 's/^["'\'']//' -e 's/["'\'']$//')

Enter fullscreen mode

Exit fullscreen mode

Not elegant but it catches most of the junk the model adds. Till the time I tune the prompt and model this stays!

I also switched fromgit diff --stagedtogit diff --staged --unified=0. By default, git shows 3 lines of context around each change. For a commit message, the model doesn't need that surrounding context. It just needs to know what changed.--unified=0strips all that out, which means fewer tokens sent to the model. On a small context window, every token counts.

Tada 🎉

* b6f0abc (HEAD -> main, origin/main, origin/HEAD) fix: update tool list for all agents

Enter fullscreen mode

Exit fullscreen mode

Much bigger code related commit, you can see gradual improvements.

* b13f344 (HEAD -> main) fix(inspection-workflow): add requirement for editing confirmed vess vessel profile
* 958053c sh fix(app_test.go, sqlite.go, sqlite_test.go, tasks.md): add save and cancel behaviour tests for vessel profile editing
* 0f33259 sh fix: update vessel profile form and edit flow in App.svelte, add tests for editing workflow, and improve styles in styles.css, update model in go/mode go/models.ts

Enter fullscreen mode

Exit fullscreen mode

## The final Modelfile

After all the iterations, my Modelfile looks quite different from where I started:

FROM
 qwen2.5-coder:1.5b

PARAMETER num_ctx 8192
PARAMETER temperature 0.2
PARAMETER top_p 0.7
PARAMETER num_predict 256
PARAMETER repeat_penalty 1.2
PARAMETER stop "Changes to be committed:"
PARAMETER stop "Note:"
SYSTEM """
You are an expert developer's assistant. Your sole task is to generate a clean, concise one-line Git commit message based on the provided code diff.
Rules:
- Respond ONLY with the commit message text.
- Do NOT include markdown code blocks, backticks, explanations, intro text, or outro text.
- Use the Conventional Commits format (e.g., feat(scope): message, fix: message).
- Keep the one line under 100 characters.
- Use the imperative mood ("Add feature", not "Added feature" or "Adds feature").
"""

Enter fullscreen mode

Exit fullscreen mode

What each parameter does and why I added it:

temperature 0.2: controls randomness. Lower means more predictable. I don't want creative commit messages.

top_p 0.7: works with temperature. It limits the model to only consider the top 70% most likely next words. Another way to keep the output focused and not wander off.

num_predict 256: maximum number of tokens the model can output. A commit message is one line. I don't need the model writing an essay. This caps it.

repeat_penalty 1.2: penalizes the model for repeating itself. Without this I was getting things likefrontend-enginee frontend-engineerorreq requirements-analyst. The model would stutter and repeat parts of words.

stop "Changes to be committed:"andstop "Note:"— stop sequences. Sometimes the model would keep going after the commit message and start generating text that looked like git output. These tell the model to stop immediately if it starts outputting these strings.

TheSYSTEMblock is the prompt baked into the model. Every time I runollama run qwen-commit, this prompt is already there. I don't have to pass it every time.

## The final function

After all the iterations, here is what I ended up with. A custom shell functiongacand an aliasgacc. It defaults to the local model, but I can also use Claude when I want to.

gac
()
 
{

 
# 1. Check for staged changes

 
if 
git diff 
--cached
 
--quiet
;
 
then
 
echo
 
"❌ Error: No staged changes found. Run 'git add' first."

 
return 
1
 
fi

 
local 
mode
=
"
${
1
:-
qwen
}
"

 
local 
msg
=
""

 
local 
exit_code
=
0

 
# Gather file names for context

 
local 
affected_files
 
affected_files
=
$(
git diff 
--staged
 
--name-only
 | 
paste
 
-sd
, -
)

 
# ---------------------------------------------------------

 
# IMPROVED PROMPT: Strict rules for Conventional Commits

 
# ---------------------------------------------------------

 
local 
system_prompt
=
"You are a strict code assistant. Write a single-line Conventional Commit message for the provided diff.
Strict Rules:
1. Format must exactly match: type(scope): description
2. Allowed types ONLY: feat, fix, docs, style, refactor, perf, test, chore.
3. The 'scope' must be a single, broad feature/module name (e.g., vessel-profile, api). NEVER use file names.
4. The 'description' must summarize the high-level intent in the imperative mood (e.g., 'add form validation').
5. ABSOLUTELY DO NOT list specific file names, paths, or extensions in the commit message.
6. Output EXACTLY one line. No markdown blocks, no quotes, no explanations, and no stray prefixes like 'sh'.
Context: The files modified are [
$affected_files
]."

 
# 2. Execution Routing

 
if
 
[
 
"
$mode
"
 
=
 
"claude"
 
]
;
 
then
 
msg
=
$(
git diff 
--staged
 
--unified
=
0 | claude 
-p
 
"
$system_prompt
"
 
--output-format
 text 2>&1
)

 
exit_code
=
$?

 
else
 if
 
!
 curl 
-s
 
--max-time
 2 http://localhost:11434 
>
 /dev/null
;
 
then
 
echo
 
"❌ Error: Local Ollama server is not running on port 11434."

 
return 
1
 
fi
 
msg
=
$(
git diff 
--staged
 
--unified
=
0 | ollama run qwen-commit 
"
$system_prompt
"
 2>/dev/null
)

 
exit_code
=
$?

 
fi

 
# 3. Robust Error Validation

 
if
 
[
 
$exit_code
 
-ne
 0 
]
 
||
 
[
 
-z
 
"
$msg
"
 
]
;
 
then
 
echo
 
"❌ Error: Failed to generate a response via 
$mode
."

 
echo
 
"Details received: 
$msg
"

 
return 
1
 
fi

 
# 4. Strict Text Cleaning Pipeline

 
msg
=
$(
echo
 
"
$msg
"
 | 
tr
 
-d
 
'\r'
 | 
sed
 
-E
 
-e
 
's/```(diff)?//g'
 
-e
 
's/^[[:space:]]+//;s/[[:space:]]+$//'
 
-e
 
's/^["'
\'
']//'
 
-e
 
's/["'
\'
']$//'
)

 
# 5. Run git commit cleanly

 git commit 
-m
 
"
$msg
"

}

# Alias to explicitly force Claude

alias 
gacc
=
"gac claude"

Enter fullscreen mode

Exit fullscreen mode

## Lessons Learned

* Tell the model what you already know. Don't make it guess things you can easily extract.
* Low temperature for tasks where you want some determinism.
* Modelfiles are useful. You can create a named model configured for a specific job.
* Model size, (V)RAM, and context size are all connected. On a constrained machine, you have to be intentional about all three.

## Is this perfect?

No. It still sometimes misses the point of a change. It takes time on larger commits. There is room for improvement.

Why not just use Claude directly? That's the easiest thing to do, but it still costs me tokens. And I wanted to learn how local models work. How context windows affect output. How to tune a model for a specific job. That was the whole point for me.

It works offline, costs nothing 💰, and I understand every piece because I broke it and fixed it.

I find the best way to learn is to find a real use case, however trivial. It helps you understand concepts one thing at a time.

Next up: My learnings building a green field product with OpenSpec meant for Brown field projects

I welcome all constructive feedback and comments

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse