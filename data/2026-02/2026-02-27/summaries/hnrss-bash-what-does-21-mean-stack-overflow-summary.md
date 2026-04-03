---
title: "bash - What does \" 2>&1 \" mean? - Stack Overflow"
url: https://stackoverflow.com/questions/818255/what-does-21-mean
date: 2026-02-26
site: hnrss
model: llama3.2:1b
summarized_at: 2026-02-27T11:35:59.791618
---

# bash - What does " 2>&1 " mean? - Stack Overflow

Here is a concise and informative summary of the given text passage:

The command `2>&1` redirects error messages from one process to another, while still capturing its standard output ( STDOUT ).

In summary:

* `&` indicates redirection; this applies to each `>`.
* `2<1` is interpreted as redirecting error message `stdout 2` to `stderr (file descriptor 1)`.
