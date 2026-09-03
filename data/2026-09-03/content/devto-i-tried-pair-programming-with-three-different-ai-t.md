---
title: I Tried Pair Programming With Three Different AI Tools For a Month - DEV Community
url: https://dev.to/elsie-rainee/i-tried-pair-programming-with-three-different-ai-tools-for-a-month-2nnc
site_name: devto
content_file: devto-i-tried-pair-programming-with-three-different-ai-t
fetched_at: '2026-09-03T14:53:14.565095'
original_url: https://dev.to/elsie-rainee/i-tried-pair-programming-with-three-different-ai-tools-for-a-month-2nnc
author: Elsie Rainee
date: '2026-09-02'
description: AI coding tools can write a function in seconds. The harder question is whether that function... Tagged with productivity, ai, tools, discuss.
tags: '#discuss, #productivity, #ai, #tools'
---

Context matters more than raw speed

AI coding tools can write a function in seconds. The harder question is whether that function actually belongs in your codebase. Does it follow the existing architecture? Does it handle edge cases? Will the tests still pass? And when something breaks three files later, can the AI help find the real cause instead of generating another patch?

To answer those questions, I spent a month using Cursor, GitHub Copilot, and Claude Code as pair-programming tools while working through practical development tasks: writing code, debugging errors, refactoring functions, creating tests, and making changes across multiple files.

I wasn't testing which tool could produce the most code. I was testing which one could make real programming work faster without creating more work afterward.

## The Short Answer

After using all three tools on real development tasks, I wouldn't call one tool the absolute winner.

Each was better at a different part of programming:

* Cursor was strongest for interactive coding and multi-file changes inside an AI-focused editor.
* GitHub Copilot was the most convenient for everyday coding, autocomplete, boilerplate, and smaller functions.
* Claude Code was strongest when a task required understanding a larger codebase, debugging across files, or completing several steps from the terminal.

The biggest difference wasn't how quickly they generated code. It was how much useful context they could use before generating it.

That became the most important lesson of the entire test.

## What I Actually Tested

I wanted to avoid the usual AI coding comparison where every tool gets the same simple prompt:

"Build a todo app."

That doesn't tell you much about real development.

Instead, I used tasks that resemble normal work inside an existing project.

### Task 1: Add a New Function

I started with existing code and asked each tool to implement a missing function.

For example:

async
 
function
 
getUserById
(
id
)
 
{

 
// implementation needed

}

Enter fullscreen mode

Exit fullscreen mode

The requirement was straightforward: fetch the user, handle an unsuccessful response, validate the returned data, and return a predictable result.

This tested something basic but important:

Could the AI follow the existing project's coding style instead of inventing its own?

All three could generate a working starting point.

The difference came during cleanup.

Copilot was very good at quickly producing the first implementation. Cursor made it easier to reference related files and adapt the function to the surrounding project. Claude Code was particularly useful when I wanted it to inspect how similar functions were already implemented elsewhere before making any changes.

That distinction matters in an existing application.

Writing code from scratch is easy.

Writing code that belongs in an existing codebase is harder.

## Debugging Was a Better Test

Code generation wasn't where I saw the biggest differences.

Debugging was.

I gave the tools actual errors rather than asking them to invent a solution.

A typical task looked something like this:

TypeError: Cannot read properties of undefinedat UserList.jsx:42

Instead of asking:

"Fix this error."

I provided the relevant component, API function, and data structure and asked the tool to identify the root cause.

This produced much more useful results.

### GitHub Copilot

Copilot was good when the problem was close to the code I was currently editing.

If the error was caused by a missing null check or an obvious incorrect variable, it could quickly suggest the fix.

The limitation arose when the cause was elsewhere.

I sometimes had to manually provide additional files and context.

### Cursor

Cursor handled these situations better when the related code was already inside the project.

I could ask it to inspect the component, API call, and related types and explain where the data shape stopped matching expectations.

That made debugging feel less like autocomplete and more like having a second pair of eyes.

### Claude Code

Claude Code was particularly useful when the debugging task crossed several files.

Instead of focusing only on the line that threw the error, I could ask it to trace the data flow.

That was valuable because many real bugs aren't located where the application crashes.

The crash is often just the final symptom.

## Refactoring: Where AI Can Save Time and Create It

Refactoring was another useful test.

I took working code that had become difficult to maintain and asked each tool to improve it without changing its behavior.

For example:

function
 
calculateTotal
(
items
)
 
{

 
let
 
total
 
=
 
0
;

 
for 
(
let
 
i
 
=
 
0
;
 
i
 
<
 
items
.
length
;
 
i
++
)
 
{

 
if 
(
items
[
i
].
active
)
 
{

 
total
 
+=
 
items
[
i
].
price
 
*
 
items
[
i
].
quantity
;

 
}

 
}

 
return
 
total
;

}

Enter fullscreen mode

Exit fullscreen mode

A simple refactor is easy.

But real refactoring usually comes with constraints:

* Don't change the API.
* Preserve existing behavior.
* Keep the current data structure.
* Don't introduce another dependency.
* Maintain test coverage.
* Follow the project's existing conventions.

That's where the tools started behaving differently.

Copilot was excellent for smaller refactoring suggestions.

Cursor was better when I wanted to make a broader change while reviewing the affected files.

Claude Code was useful when the refactoring involved understanding how the function was used throughout the repository.

### The important part: review the diff

This became a rule for me.

Never accept a large AI-generated refactor without reading the diff.

A cleaner-looking implementation isn't automatically a safer implementation.

AI can remove duplication while accidentally changing behavior.

It can also "improve" something that was intentionally written that way because of another part of the application.

## Writing Tests With AI

Testing was one area where all three tools saved me time.

I could provide an existing function and ask for unit tests covering:

* Normal input
* Empty input
* Invalid input
* Missing values
* API failures
* Boundary conditions

The first set of generated tests was usually reasonable.

But there was an obvious problem.

AI tends to write tests based on the implementation it sees.

That can result in tests that confirm what the code currently does rather than tests that prove what the application should do.

For example, if the implementation has an incorrect default value, an AI-generated test may encode that behavior.

So I stopped asking:

"Write tests for this function."

I got better results with:

"Write tests based on the expected behavior described below. Include edge cases and failure scenarios. Do not assume the current implementation is correct."

That small change produced much more useful tests.

## Multi-File Changes Changed My Opinion

The biggest difference between these tools became obvious when I stopped asking them to write individual functions.

I gave them a feature.

For example:

Add pagination to the existing user list. Keep the current API response format, add loading and error states, update the API request, preserve the existing filters, and add tests for the new behavior.

Now the AI needs to understand:

1. Where the API request happens.
2. Where the user list is rendered.
3. How state is currently managed.
4. How filters work.
5. Where tests live.
6. Which files need modification.
7. Whether the existing API supports the requested behavior.

That's much closer to real software development.

### Cursor

Cursor performed well when I wanted to stay inside the editor and interactively guide the changes.

I could inspect the proposed modifications and adjust the implementation as I went.

### GitHub Copilot

Copilot remained useful, but I found myself having to provide more direction for larger changes.

It was excellent when I already knew what needed to happen and wanted assistance implementing it.

### Claude Code

Claude Code was particularly useful when the task required repository-level investigation before implementation.

That made it valuable for larger changes where the first step wasn't writing code; it was figuring out where to change the code.

## Which Tool Required the Least Correction?

This was harder to measure than lines of generated code.

I started paying attention to a more practical metric:

How much work did I have to do after the AI finished?

That included:

* Fixing incorrect assumptions
* Removing unnecessary code
* Correcting APIs
* Changing variable names
* Adding missing error handling
* Rewriting tests
* Fixing regressions
* Reverting unnecessary changes

This changed my view of productivity.

A tool that generates 200 lines in a minute isn't necessarily faster than one that generates 80 useful lines if I have to spend another 30 minutes fixing the first result.

For me, useful code was more important than generated code.

## My Practical Comparison

Programming Task

Best Fit

Why

Inline autocomplete

GitHub Copilot

Fast suggestions while typing

Small functions

GitHub Copilot

Low friction and quick generation

Interactive refactoring

Cursor

Strong editor-based workflow

Multi-file editing

Cursor

Easier to guide and review changes

Debugging a simple error

GitHub Copilot

Quick contextual suggestions

Debugging across files

Claude Code

Better suited to repository-level investigation

Understanding an unfamiliar repository

Claude Code

Useful for tracing project structure

Writing unit tests

All three

Good starting point with human review

Large implementation tasks

Cursor / Claude Code

Better suited to multi-step work

Final code review

Human developer

AI shouldn't be the final authority

## What AI Pair Programming Actually Changed

The biggest productivity improvement wasn't that I stopped programming.

I programmed differently.

Before using AI heavily, a lot of time went into:

* Searching documentation
* Looking up syntax
* Writing repetitive code
* Creating test boilerplate
* Tracing unfamiliar functions
* Building the first version of a solution

AI reduced much of that friction.

But another category of work became more important:

* Reviewing generated code
* Checking assumptions
* Testing edge cases
* Reading diffs
* Writing better prompts
* Breaking large tasks into smaller requirements

So AI didn't remove engineering work.

It shifted where I spent my time.

## The Mistakes I Had to Watch For

After a month, I became much more careful about a few recurring problems.

### 1. AI assumes things

If the requirement isn't clear, the tool fills in the gaps.

That can mean choosing an API pattern, library, naming convention, or architecture that isn't appropriate for the project.

### 2. Working code can still be bad code

Something can compile, pass basic tests, and still be unnecessarily complicated.

### 3. Tests can give false confidence

A generated test suite isn't automatically good coverage.

### 4. Large changes need smaller checkpoints

I got better results when I broke large tasks into stages rather than asking for an entire feature in a single prompt.

### 5. Git became even more important

With AI making more changes, reviewing commits and diffs became essential.

I wanted to know exactly what changed and why.

## The Pair-Programming Workflow That Worked Best for Me

The most reliable workflow was surprisingly simple.

### Step 1: Explain the existing code

Give the AI the relevant files and ask it to explain the current behavior before making any changes.

### Step 2: Define the requirement

State exactly what should change and what must remain unchanged.

### Step 3: Ask for a plan

For larger tasks, have the AI identify which files need to be modified before writing code.

### Step 4: Implement in smaller pieces

Don't unquestioningly accept a giant change.

### Step 5: Review the diff

Check every meaningful modification.

### Step 6: Run tests

Never treat generated code as finished simply because it looks correct.

### Step 7: Ask the AI to challenge its own solution

One useful prompt was:

"Review this implementation for edge cases, regressions, unnecessary complexity, and assumptions that may be incorrect."

That often uncovered issues I hadn't noticed.

## So, Which AI Pair Programmer Would I Choose?

If I were starting a project today, I wouldn't choose based only on benchmark scores or feature lists.

I'd choose based on my workflow.

* For everyday coding and autocomplete:GitHub Copilot.
* For an editor-centered workflow with interactive AI assistance:Cursor.
* For repository-level debugging, investigation, and larger terminal-based tasks:Claude Code.

But there's an important qualification.

I wouldn't let any of them become the final decision-maker.

The AI can suggest the implementation.

I still decide whether the implementation is correct.

That's the difference between using AI as a pair programmer and using AI as a code generator.

## Conclusion

After a month of using three different AI tools for pair programming, I came away with a much less exciting but more useful answer: AI doesn't make programming disappear; it makes certain parts of programming dramatically faster.

GitHub Copilot was excellent when I needed fast assistance while writing code. Cursor became more useful when the work involved interactive editing and multiple files. Claude Code stood out when I needed to investigate a repository, trace a problem, or work through a larger task from the terminal.

The real productivity gain came from combining AI generation with normal engineering discipline.

I still read the code.

I still review diffs.

I still run tests.

I still debug failures.

And I still make the architectural decisions.

That's the most realistic way to think about AI pair programming today. The goal isn't to have an AI write your entire application while you sit back. The goal is to remove repetitive work, shorten the distance between an idea and a working implementation, and give you another tool for thinking through difficult programming problems.

The best AI pair programmer isn't the one that writes the most code. It's the one that helps you spend more time solving engineering problems and less time fighting repetitive implementation work.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (15 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse