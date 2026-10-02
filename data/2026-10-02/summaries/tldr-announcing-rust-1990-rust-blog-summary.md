---
title: Announcing Rust 1.99.0 | Rust Blog
url: https://blog.rust-lang.org/2026/10/01/Rust-1.99.0
date: 2026-10-02
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-02T16:39:18.875595
---

# Announcing Rust 1.99.0 | Rust Blog

**Rust 1.99.0 Release Announce**

The Rust team is pleased to announce the release of Rust 1.99.0, a stable version of the programming language. This release marks a significant milestone in the development of Rust, with several key improvements and additions.

**Main Features and Improvements**

* **Defining C-ABI Variadic Functions**: Rust 1.99.0 stabilizes the ability to define C-ABI variadic functions with both "C" and "C-unwind" ABIs, enabling the use of variadic functions in Rust.
* **Non-"C" Variadic Functions**: The release also includes support for defining naked variadic functions with non-"C" ABIs, making it easier to write variadic functions in Rust.
* **Improved Layout Information**: The language ensures that the size and alignment of raw pointers are safe, eliminating the need to worry about "round-trip un-leaking" after memory allocation.
* **New APIs**: Several new APIs have been added, including `IntoIterator` for `Box` and `&Box` collections, `retain_back`, and several API additions to the standard library.

**Key Safety Features**

* **Guarded Types**: New types, such as `VaList`, are ABI-compatible with the C `va_list` type, ensuring safe usage.
* **Sized Safety**: Three functions, `Layout::for_value_raw`, `mem::size_of_val_raw`, and `mem::align_of_val_raw`, are now sized trivially safely, eliminating the need for size calculations.

**Recommendations**

* **Update Locally**: Testers can update to the beta channel or nightly channel to test future releases and report any bugs.
* **Use Recommendations Wisely**: Update to `Box::into_non_null` and `Box::from_non_null` instead of `leak` functions, as they are more safe and efficient.

**More Information**

* **Release Notes**: Read the detailed release notes for 1.99.0 for more information on the changes.
* **Documentation**: The documentation has been updated to recommend against patterns that later deallocate memory, which can lead to problems with compiler optimizations.