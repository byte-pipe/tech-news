---
title: Jira IS Turing-Complete
url: https://seriot.ch/computation/jira.html
site_name: hnrss
content_file: hnrss-jira-is-turing-complete
fetched_at: '2026-05-25T12:12:10.482936'
original_url: https://seriot.ch/computation/jira.html
date: '2026-05-25'
description: Jira Is Turing-Complete
tags:
- hackernews
- hnrss
---

### Nicolas Seriot

#### Computation> Jira is Turing-Complete

# Jira is Turing-Complete

Building a Minsky Machine in Atlassian Automation22nd May 2026

Engineering folkloreholdsthatJira(Atlassian's project-tracking tool) isTuring-complete.
Existing claims point vaguely at automation features without exhibiting a reduction.
This article supplies a proof, with setup instructions and execution trace.

### Mapping the Computational Model

AMinsky register machineneeds only two unbounded counters and a finite set of labeled instructions:

* INC r; goto S
* DEC r; if r == 0 goto S else goto S'

Or, in plain English:

* increment register R, then goto some state S
* decrement register R, if R == 0 goto zero-state S, else goto nonzero-state S'

A Minsky program that adds register A into register B looks like:

1. DEC A; if A == 0 goto 3 else goto 2
2. INC B; goto 1
3. HALT

Minskyproved this model Turing-complete (1967).
Exhibiting it in Jira's automation language therefore establishes the reduction.
Here is how the model maps onto Jira:

Minsky Machine

Jira

Register A

Count of linked issues of type 
Bug

Register B

Count of linked issues of type 
Task

Program Counter

Status of a single 
Epic
 issue

Dispatch Table

Jira Automation rules, one per instruction state

Clock

Automation-triggered transitions, or external re-triggering past chain caps

The Epic's status encodes the current instruction.Automation rulesinspect the linked-issue counts and decide the next status.INCandDECare implemented as issue creation and deletion on the appropriate linked-issue type.
Conditional branching is implemented as aJQL-conditioned rule.

### Implementing Addition

Here is a minimal working implementation using one Epic, five linked issues, and one Automation rule per instruction state (Space Settings > Automation).

1. Create Workflow

Create a Jira Workflow with statuses initial stateBACKLOG, thenTODO,DEVandPROD.
Any state can transition to any other.

Create an Epic in statusBACKLOG.

2. Create Rule for TODO

DEC A; if A=0 halt, else goto DEV.

* Trigger: Epic status changed toTODO.
* If at least one linked Bug exists: delete one Bug, transition Epic toDEV.
* Else: transition Epic toPROD(halt).

3. Create Rule for DEV

INC B; goto TODO.

* Trigger: Epic status changed toDEV.
* Create a new Task, link it to the Epic.
* Transition Epic toTODO.

Both rules have"Allow rule to trigger other rules"enabled.

The screenshot below shows the two rules wired into the Epic's workflow.

4. Init Registers

Link 2 Bugs (A=2) and 3 Tasks (B=3) to the Epic.

5. Bootstrap the Machine.

Transition the Epic toTODOto start the cascade. Five transitions:

(2,3) TODO → 
(1,3) DEV → 
(1,4) TODO → 
(0,4) DEV → 
(0,5) TODO → 
(0,5) PROD

Recorded on a real*.atlassian.netinstance.

The Epic lands inPRODwith 0 Bugs and 5 Tasks linked. We've just added 2 + 3 = 5.

### Fibonacci in Three States

The reduction above suffices to prove Turing-completeness.
In addition to that, Jira's automation language can simplify Minsky operations.Convert Issue Typechanges an issue's type instantly: Bug → Story, Story → Task, and so on.

CONVERT is expressible as DEC + INC. It doesn't extend Jira's computational power, but it shrinks the dispatch table dramatically for any move-loop, making non-trivial programs tractable.

Fibonacci as(A, B) → (B, A+B)collapses to three states with three registers (A=Bug, B=Task, C=Story), usingTODO,QA(add it to the workflow), andDEVas the three instruction states:

TODO:
 if any linked Task exists:
 CONVERT Task → Story
 INC Bug
 transition to TODO
 else:
 transition to QA

QA:
 if any linked Bug exists:
 CONVERT Bug → Task
 transition to QA
 else:
 transition to DEV

DEV:
 if any linked Story exists:
 CONVERT Story → Bug
 transition to DEV
 else:
 transition to TODO

Initial state A=1, B=1, C=0. The sequence 1, 1, 2, 3, 5, 8, 13, … appears in B (Task count).

Unlike the addition machine, the Fibonacci machine has no halt state.
It runs until Jira Cloud's chain-depth cap of 10 triggers, at which point the operator re-triggers the Epic to continue.
A single status edit restarts the cascade.

The reduction still holds, the human just supplies the next clock tick.
Jira Data Center exposes the same asautomation.rule.execution.timeoutand related, configurable properties.

### Conclusion

Jira's automation language can encode a two-counter machine given unbounded issue creation and rule execution.
Every physical computer is finite, so Jira Cloud's finite quotas do not refute the construction.
Under that standard convention, Jira is Turing-complete.

So, if complex Jira automations feel like programs, it is because they literally are.