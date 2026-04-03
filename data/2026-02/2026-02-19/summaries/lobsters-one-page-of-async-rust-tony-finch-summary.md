---
title: One page of async Rust – Tony Finch
url: https://dotat.at/@/2026-02-16-async.html
date: 2026-02-19
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-19T06:01:31.494119
---

# One page of async Rust – Tony Finch

# One page of async Rust – Tony Fiinch

This blog post details the author's exploration of low-level asynchronous programming in Rust, driven by the need to simulate tasks with delays and ordered execution. Instead of using existing crates, the author aims to understand the underlying mechanisms of async Rust.

## async fn-damentals
The author starts with a basic async function `deep_thought()` that returns 42. Calling this function immediately creates a `Future`, which represents the initial state of the task. To execute the task, the `Future::poll()` method is needed.

## pin a task
`Future`s in Rust can hold references to themselves, requiring the use of `Pin` to prevent memory issues. The author defines a `Task` struct to wrap a pinned `Future`, providing methods for spawning and managing the task.

## noop context
The `poll()` method takes a `Context`, which is a wrapper around a `Waker`. The simplest `Context` is created using `Waker::noop()`, allowing the `deep_thought()` task to run without any actual delay.

## primops, generally
In async Rust, calling an async function results in a `Future` that needs to be awaited. This `await` operation is internally implemented by calling `poll()` on the `Future`. A chain of `await` calls ultimately leads to a primitive operation that interacts with the outside world. This primitive operation involves polling the `Future` twice: once to initiate the operation and again to retrieve the result.

## primops, minimally
The author creates a minimal `Sleep` struct that represents a primitive `Future` simulating a delay. It suspends the task for a specified duration and then resets the delay for the next iteration. The `deep_thought()` function can utilize this by awaiting a `Sleep` object.

## contexts and wakers
The `Context` and its `Waker` are crucial for primitive `Future`s to communicate with the async executor. The `Waker` is a wrapper around a smart pointer to the current task. When a primitive `Future` suspends a task, it stores the `Waker`. Upon completion, the `Waker` is used to signal the task to resume. The author notes the complexity of manually creating a `Waker` using raw pointers and unsafe code, but ultimately decided against using the safer `Wake` trait due to added complexity.
