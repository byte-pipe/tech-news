---
title: Ruby 4.0.0 Released | Ruby
url: https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/
date: 2025-12-25
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-26T11:11:15.530869
screenshot: hackernews_api-ruby-4-0-0-released-ruby.png
---

# Ruby 4.0.0 Released | Ruby

# Ruby 4.0.0 Released

Ruby 4.0.0 is the latest release of the popular programming language Ruby, announced by the developers and released on 25 December 2025.

## New Features

- **Ruby Box** (Experimental): A new feature that provides separation of definitions in Ruby boxes, isolating concepts such as monkey patches, global/class variables, module definitions, and loaded libraries from other boxes. This makes it easier to manage complex applications and reduces code bloat.
  * Use `RUBY_BOX=1` environment variable to enable the feature.

- **ZJIT (Just-In-Time Compiler)**: A new JIT compiler developed as the next generation of YJIT, which is now compatible with Ruby 4.0. This update improves performance by allowing for faster compilation and more efficient use of resources.

## Ractor Improvements

- **Ractor Port**: An improved class `R actor::Port` that resolves issues related to message sending and receiving.
- **Sharing Procs between Ractors**: Making it easier to share objects between Ractors, reducing data transmission and improvement in parallel execution efficiency.

## Language Changes

- ** nilno longer returns empty arrays** (Feature #21047): The feature allows nil instances of Array instances to be returned correctly without calling `to_a`, similar to how Nil instances do not call `to_hash`.
- **Improved Logical Binary Operators** (Feature #20925): Binary operators like `||` (`&&` and `&`) now continue the previous line seamlessly, maintaining line continuation in fluent style.

## Other Updates

* The code examples provided have changed to follow a more modern syntax as per Feature #21047 about improved nil handling.
* Some minor changes are made in Ruby 4.0 updates which include:
    - **Array#rfind`:** Returns the index of the first occurrence of the specified value within the array, or `nil` if not found.

The release of Ruby 4.0.0 brings numerous improvements and features that enhance the overall user experience of writing code in Ruby.
