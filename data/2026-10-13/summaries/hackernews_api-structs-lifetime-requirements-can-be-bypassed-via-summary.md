---
title: "struct's lifetime requirements can be bypassed via covariant field assignment · Issue #164250 · rust-lang/rust · GitHub"
url: https://github.com/rust-lang/rust/issues/164250
date: 2026-10-13
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-13T18:09:48.536403
---

# struct's lifetime requirements can be bypassed via covariant field assignment · Issue #164250 · rust-lang/rust · GitHub

## Bypassing lifetime requirements with covariant field assignment

### Summary

The article discusses a bug in Rust's type system that allows covariant field assignment, bypassing some lifetime requirements. This bug is P-high and has been reported by a collaborator but is 11 years old, making it only P-high.

### Key Points

* Covariant field assignment bypasses some lifetime requirements in Rust.
* The bug is related to the project zero and the type system unsoundnesses.
* The bug was reported by a collaborator but not actively tested.
* The bug was identified using a new test case.

### Description

The bug was identified in the `Q` struct, which has a lifetime that is specified as strict or optional. When using covariant reference, the reference has a higher lifetime than the original reference. Using covariant field assignment causes the original reference to become a strict reference, violating some lifetime requirements.

This bug is a soundness hole, as it would not be detected by the current borrow checker. It is also a high priority issue, as it has not been fixed for 11 years.

### Test Cases

The code includes several test cases to verify the bug. The first test case creates a `Q` struct with an immutable reference to a `Box` and pushes it onto a vector. The next test case creates a `Q` struct with a mutable reference to a `Vec`, locks the vector, and unwraps it without the original lock. This shows that the original reference is downcasted to a `String` instead of being pushed onto a `String` vector.

### Related Issues

The code includes another issue that is a similar soundness hole. It is not the focus of this summary, but discussing this code snippet helps to maintain the original context.

### Context

This bug is related to the project zero and the type system unsoundnesses in Rust. The article mentions the next-generation trait solver, the region constraint rework, and Project Zero, which are areas that need to be fixed to prevent memory unsafety.

### Output

The summary is presented as a Markdown document with header levels, bullet points, and consistent formatting.