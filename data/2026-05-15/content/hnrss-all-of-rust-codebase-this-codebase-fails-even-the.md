---
title: 'all of rust codebase: This codebase fails even the most basic miri checks, allows for UB in safe rust · Issue #30719 · oven-sh/bun · GitHub'
url: https://github.com/oven-sh/bun/issues/30719
site_name: hnrss
content_file: hnrss-all-of-rust-codebase-this-codebase-fails-even-the
fetched_at: '2026-05-15T19:34:10.167617'
original_url: https://github.com/oven-sh/bun/issues/30719
date: '2026-05-15'
description: 'error: Undefined Behavior: constructing invalid value of type &[u8]: encountered a dangling reference (0x20933[noalloc] has no provenance) --> src/main.rs:97:18 | 97 | unsafe { core::slice::from_raw_parts(ptr as *const u8, self.len()) } ...'
tags:
- hackernews
- hnrss
---

oven-sh

 

/

bun

Public

* NotificationsYou must be signed in to change notification settings
* Fork4.5k
* Star90.6k

# all of rust codebase: This codebase fails even the most basic miri checks, allows for UB in safe rust#30719

Open
#30728
Open
all of rust codebase: This codebase fails even the most basic miri checks, allows for UB in safe rust
#30719
#30728

## Description

AwesomeQubic
opened 
on 
May 14, 2026
Issue body actions
error: Undefined Behavior: constructing invalid value of type &[u8]: encountered a dangling reference (0x20933[noalloc] has no provenance)
 --> src/main.rs:97:18
 |
97 | unsafe { core::slice::from_raw_parts(ptr as *const u8, self.len()) }
 | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Undefined Behavior occurred here
 |
 = help: this indicates a bug in the program: it performed an invalid operation, and caused Undefined Behavior
 = help: see https://doc.rust-lang.org/nightly/reference/behavior-considered-undefined.html for further information
 = note: stack backtrace:
 0: PathString::slice
 at src/main.rs:97:18: 97:75
 1: main
 at src/main.rs:130:22: 130:34

code:

fn main() {
 let test = Box::new(*b"Hello World");
 let init = PathString::init(&*test);
 drop(test);

 println!("{:?}", init.slice());
}

Please consider not vibe coding rust as AIs are not good at writing Rust and also hire a real rust dev

Reactions are currently unavailable

## Metadata

## Metadata