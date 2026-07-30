---
title: Preface - The Rust on ESP Book
url: https://docs.espressif.com/projects/rust/book/
site_name: hnrss
content_file: hnrss-preface-the-rust-on-esp-book
fetched_at: '2026-07-30T11:39:50.104248'
original_url: https://docs.espressif.com/projects/rust/book/
date: '2026-07-25'
description: A comprehensive guide on using the Rust programming language with Espressif SoCs and modules
tags:
- hackernews
- hnrss
---

# Preface

Welcome to our guide to embedded Rust development on Espressif products. This book is designed to help you get started and become comfortable using our tools and ecosystem. Along the way, we’ll introduce the structure of our software stack, and walk through basic workflows using project generation and tooling. By the end, you’ll be ready to explore more advanced material through our reference documentation and external training resources.

## Who This Book Is For

This book is intended for Rust developers who are interested in embedded development, even if they don’t have prior experience with embedded systems. While some familiarity with low-level programming concepts can be helpful, we aim to introduce key ideas as they come up. If you would like to expand your baseline knowledge, consider studying the additionalResources.

## Stability and Availability

While we strive for stability, users should expect periodic modifications as we improve the API, enhance performance, and introduce new features.Modulesthat are already stabilized will not be subject to breaking changes, in accordance with semantic versioning -SemVer. However,unstablefeatures—such as parts of theesp-haland certain drivers are actively being developed and are not covered bySemVerguarantees. This means that using theseunstablecomponents may break your project with a simplecargo update, much like working with Rust’snightlycompiler. This kind of instability is common across the broader Rust embedded ecosystem, which is still rapidly evolving. Expect frequent changes and track dependencies closely. For all major crates, we provide migration guides between releases to help you stay up to date.

## Additional Resources

If you’re unfamiliar with certain concepts covered in this book or would like to deepen your understanding, the following resources may be helpful:

Resource
Description

The Rust Programming Language
Learn Rust fundamentals before diving into embedded development.

The Embedded Rust Book
A collection of resources from Rust’s Embedded Working Group.

Embedded Rust (
no_std
) on Espressif
Guide for working in 
no_std
 environments with Espressif SoCs.

Awesome ESP Rust
A list of resources for development in the Rust programming language for Espressif products

Awesome Embedded Rust
A list of resources related to embedded and low-level programming in the Rust programming language, including a selection of useful crates.

## Contributing to This Book

The work on this book is coordinated inthis repository.

If you encounter difficulties following the instructions or find unclear sections, please report them inthe issue tracker. Contributions in the form of pull requests for typo fixes or clarity improvements are always welcome!

## Support and Community

If you need help, have questions, or would like to discuss topics related toesp-rs, you can reach out through the following channels:

* Matrix:Join our community chat.
* GitHub Discussions:Engage with the community.

We hope this book provides you with the knowledge and confidence to build robust, efficient, and safe embedded applications using Rust on Espressif products. Let’s get started!