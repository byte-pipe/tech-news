---
title: I Programmed an AI in 6502 Assembly - It Worked - DEV Community
url: https://dev.to/newellpaul/i-programmed-an-ai-in-6502-assembly-it-worked-gpi
date: 2026-05-06
site: devto
model: llama3.2:1b
summarized_at: 2026-05-07T12:36:31.612762
---

# I Programmed an AI in 6502 Assembly - It Worked - DEV Community

# Programmed an AI in 6502 Assembly - Achieving a Useful Triage Workflow

I have programmed myself a version of Claude Code in 6502 assembly language. This skills is called opcode, which maps the syntax and semantics of the original code onto issue triage workflows.

## Same Verbs, Bigger Nouns

LDA (Load D into A) - this can be compared to looking up an issue on PR databases

The verbs haven't changed, but the nouns got significantly more. The new words are often tens or even hundreds of times larger than their original counterparts.

## Same Syntax, Different Language

peek.s (Look at S) compares to looking out-of-place in Colourscope: a tool for visualizing large amounts of data

## A Simple yet Powerful Workflow

The most basic version is poke.s (Peek), which checks the current status. It uses 6502 opcodes and includes flags.

* if test succeed (C=1): commits; else (C=0) skips
If you break a single step, a full chain of tests, diff review, commit fails: retried with retry

## A Brief Analysis

My first idea didn't succeed. I wanted the original 6502 code to understand my assembly language.

It worked on LDA: Load D into A

## Useful Code for Automated Issue Fixing

LDA (Load D into A) - loads issue #42 from PR database
STAPERSISTS(tospecialslot)
LDX/INX/CPX(handle) loops to test each label
JSR calls I/O vectors:
   FETCH  : fetches an issue
   FIX  : fixes and tests the issue
   TEST: tests if it passes all checks
   LINT: if fails, tries again with retry
   REPLY  : sends diff back to maintain PR workflow

## More Useful Code - A Full Workflow

issue.s
LDA loads its description and a set of labels
LTSS  : loops to examine file at specified location
JMP test : skips if issue doesn't pass
JMP loop 2 : loop again, unless fix succeeds immediately
    JFS   : fixes the issue immediately
    JFCPT: fix fails, proceed with retry
JFLAUS: fails on first attempt; send to human reviewer


## Full Workflow - Oneshot

FILLissue. This code combines the steps of load, store, append, and loop until fix succeeds or fail.

One shot s - a shorter version in 65k assembly language, which still achieves similar results.