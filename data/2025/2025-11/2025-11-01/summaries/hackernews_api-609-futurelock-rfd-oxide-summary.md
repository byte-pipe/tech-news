---
title: 609 - Futurelock / RFD / Oxide
url: https://rfd.shared.oxide.computer/rfd/0609
date: 2025-10-31
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-01T11:24:51.923429
screenshot: hackernews_api-609-futurelock-rfd-oxide.png
---

# 609 - Futurelock / RFD / Oxide

### Published RFD: Futurelock / RFD / Oxide

#### Description:

RFD 609 describes "Futurelock", a type of deadlock in asynchronous programming involving resource ownership and another task's requirements.

#### Key Points:

*   This concern arises whenever tasks access resources from different futures simultaneously.
*   The problem becomes especially evident when the responsible future is no longer polling the original owner's resources.
*   A potential flaw in writing concurrent Rust code lies in how it handles lock acquisition, which can lead to subtle deadlocks.

#### Main Ideas:

*   Overview of futurelock: a deadlock scenario where tasks requiring multiple resources acquire them simultaneously without release
*   Example usage in RFD 9259: an incident report illustrating this issue
*   Discussion on the problem's implications and analysis of possible solutions

#### Assumed Knowledge:

-   Understanding asynchronous programming concepts, including task allocation and resource acquisition
-   Familiarity with Rust basics, such as concurrency primitives like Mutex and tokio libraries
-   Experience with parallel programming models

## Code Summaries

### oxide/oxidecomputer/omicron#9259

Although this specific code snippet only provides an example of the problem, we can infer that it demonstrates how multiple tasks can contort in ways that result in deadlocks. However, its provided structure and implementation hint towards exploring solutions which also need to be aware of such cases.

## Example Use Case (oxide/oxidecomputer/others#12345)

This snippet showcases a minimalistic example where one BackgroundTask "start" attempts to take an ARXMutex lock with another Function ("do_stuff') attempting to acquire the same lock. This creates potential deadlock conditions due to asynchronous nature of code execution.

### Task Structure

`main()`
---------------

*   `let lock = Arc::new(Mutex::new(()));`
    -   This line establishes a shared mutex for exclusive access.

```rust
async fn main() {
    let lock = Arc::new(Mutex::new(()));
    // ... rest of the code
}
```

`start_background_task()`
-----------------------------

*   `let _guard = lock.lock().await;`
    -   This line waits until the mutex is acquired before proceeding.

```rust
async fn start_background_task(lock: Arc<Mutex<())) {
    loop {
        // simulate some work
        println!("background task: starting");
        let _count= 1/0;
}
```

`do_stuff()`
----------------

*   `let mut future1 = do_async_thing("op1", lock.clone()).await;`
    -   This attempt to acquire the mutex will take longer than expected.

```rust
async fn do_async_thing(label: &str, lock: Arc<Mutex<()>>) -> Result<(), ()> {
    println!("do_stuff: entering select");
    tokio::select! {
        _ = &mut future1 => {println!("do_stuff: arm1 future finished")}
        _
            = sleep(Duration::from_millis(500)) =>
        { do_async_thing("op2", lock.clone())?.await; }
}
```

This snippet serves as a foundation to understand how deadlocks can arise through concurrent task interaction in Rust.
