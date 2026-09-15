---
title: AI-Generated Tests Can Make Coding Agents Worse. Here's How to Check Yours - DEV Community
url: https://dev.to/p0rt/ai-generated-tests-can-make-coding-agents-worse-heres-how-to-check-yours-3jc9
site_name: devto
content_file: devto-ai-generated-tests-can-make-coding-agents-worse-he
fetched_at: '2026-09-15T15:27:49.001634'
original_url: https://dev.to/p0rt/ai-generated-tests-can-make-coding-agents-worse-heres-how-to-check-yours-3jc9
author: Sergei Parfenov
date: '2026-09-11'
description: ExecCritic found that weak generated tests reduced repair success. A runnable Python example shows how to catch a test that approves the wrong fix. Tagged with ai, testing, python, agents.
tags: '#ai, #testing, #python, #agents'
---

Demonstrates a flawed Python filter fix

A bug fix can make every new test pass and still introduce a regression. Here is a deliberately constructed Python example, checked locally without an LLM.

An order filter has three requirements:

* Omit the filter, or passNone: return all orders.
* Pass an empty list: return no orders.
* Pass a list of statuses: return only matching orders.

The reported bug is that omitting the filter returns nothing. This proposed fix looks reasonable:

ORDERS
 
=
 
[

 
{
"
id
"
:
 
1
,
 
"
status
"
:
 
"
paid
"
},

 
{
"
id
"
:
 
2
,
 
"
status
"
:
 
"
pending
"
},

]

def
 
filter_orders
(
orders
,
 
statuses
=
None
):

 
if
 
not
 
statuses
:

 
return
 
list
(
orders
)

 
return
 
[
order
 
for
 
order
 
in
 
orders
 
if
 
order
[
"
status
"
]
 
in
 
statuses
]

assert
 
filter_orders
(
ORDERS
)
 
==
 
ORDERS

assert
 
filter_orders
(
ORDERS
,
 
[
"
paid
"
])
 
==
 
[
ORDERS
[
0
]]

print
(
"
2 checks passed
"
)

Enter fullscreen mode

Exit fullscreen mode

Both checks pass. Both branches of theifhave been exercised. The reported symptom is fixed.

Now add the check for the second requirement:

assert
 
filter_orders
(
ORDERS
,
 
[])
 
==
 
[]

Enter fullscreen mode

Exit fullscreen mode

It fails. The function returns every order.

Python treats bothNoneand[]as falsey. Our requirements give them different meanings, and the patch erases that distinction.

The connection to coding agents becomes more consequential when those checks determine what the agent does next.

On September 8, Leitian Tao and colleagues published theExecCritic preprint. Holding the Qwen-3.5-35B-A3B Repair agent fixed, they reported these SWE-bench Verified results:

Feedback source

Tasks resolved

Initial repair, before generated-test feedback

61.2%

Tests from the base Qwen Test agent

57.3%

Tests from GPT-5.6-sol

65.3%

The weaker tests reduced the resolved rate by3.9 percentage points. Better tests improved it.

Rates average three repair runs, reusing generated tests. Failed test qualification retains the initial patch in the all-task score. The baseline does not forbid repository tests. A separate official evaluator determines resolution. Feedback adds test-generation and revision work; compute budgets are not matched. These are the authors' results, not a benchmark replication for this article.Method and results.

A bad test can do more than miss a defect. It can give the next edit the wrong target.

Imagine adding this assertion to the filter example:

# This expectation contradicts the stated empty-list requirement.

assert
 
filter_orders
(
ORDERS
,
 
[])
 
==
 
ORDERS

Enter fullscreen mode

Exit fullscreen mode

Our broken patch passes it. A correct implementation would fail it. Feed that failure into an automatic repair loop, and the loop now has a reason to damage correct behavior.

Adding assertions has strengthened the wrong interpretation.

Even the familiar “fails before the fix, passes afterward” check needs a closer look. Here is the original implementation from the fixture:

def
 
filter_orders
(
orders
,
 
statuses
=
None
):

 
statuses
 
=
 
statuses
 
or
 
[]

 
return
 
[
order
 
for
 
order
 
in
 
orders
 
if
 
order
[
"
status
"
]
 
in
 
statuses
]

Enter fullscreen mode

Exit fullscreen mode

The default-filter assertion fails against this version and passes against our proposed patch. It correctly detects the original bug. It simply cannot detect the new one.

The complete fix handlesNoneexplicitly:

def
 
filter_orders
(
orders
,
 
statuses
=
None
):

 
if
 
statuses
 
is
 
None
:

 
return
 
list
(
orders
)

 
return
 
[
order
 
for
 
order
 
in
 
orders
 
if
 
order
[
"
status
"
]
 
in
 
statuses
]

Enter fullscreen mode

Exit fullscreen mode

Running the same checks against all three implementations produces:

Implementation

Default + paid-filter checks

Those checks + empty-list check

Original

1 passes, 1 fails

2 pass, 1 fails

Plausible patch

2 pass

2 pass, 1 fails

Corrected patch

2 pass

3 pass

Therunnable companionincludes all three implementations, the checks, and the verified output. It uses Python’s standard library and makes no LLM or network calls.

The extra check earns its place because it distinguishes two implementations the earlier checks considered equally acceptable.

That is the question I would bring to an AI-generated test review:which plausible wrong implementation would this test reject?

For the filter, the candidate mistakes are easy to name: ignore the filter entirely, treat every missing filter as empty, or treat every empty filter as missing. They correspond to different misunderstandings of the contract. Tests that separate those cases tell us more than several additional examples of paid orders.

This is also wheremutation testingcan help: make small changes to the implementation and check whether the suite detects them. Inspect surviving mutations to understand what they change; some are equivalent for the supported inputs. For this fixture, changingstatuses is Nonetonot statusesis a useful manual mutation because it has a known, observable effect on required behavior.

For an agent workflow, I would make four changes.

1. Write down the expected behavior before reviewing the patch.Include the ordinary case, the reported failure, and the neighboring case most likely to be confused with it. Here,Noneand[]belong on separate rows. If the issue leaves that distinction unspecified, get a product decision before turning either interpretation into a test.
2. Review expected values as carefully as production code.An assertion is a claim about the product. Trace that claim to a requirement, an established compatibility promise, or an independently checked example. Copying the current output into an expected value can preserve the exact behavior you meant to question.
3. Keep an accepted regression check stable during repair.Let the agent change the implementation while a separate runner evaluates it with the reviewed tests. Protect the test command and configuration too: an unchanged test file helps little if the patch can skip its execution. If the test itself is wrong, revise and review it explicitly, then evaluate the candidate again.
4. Inspect the failure before asking the agent to fix it.An assertion showing the wrong returned orders is actionable behavioral evidence. A missing dependency, an import failure, or a command that selected zero tests needs a different response. Record what ran and why it failed.

ExecCritic separates test creation from repair, qualifies tests on the original repository, and keeps them unchanged during revision. That limits the repairer's ability to change its target. Separate contexts and permissions still cannot guarantee that both agents understood the issue correctly.Paper;released implementation.

The four steps above are a review procedure you can try in an existing project. They do not require training a model. Their value should be judged by the bugs and mistaken expectations they expose.

For your next AI-assisted fix, keep the original code, the proposed patch, and the new tests. Identify one plausible alternative implementation that violates the requirement. Run the tests against it.

If both implementations get the same green result, you have found a specific question the suite still cannot answer. Add the check that separates them, and review its expected result before trusting the next repair.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (37 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse