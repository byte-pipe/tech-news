---
title: [BUG] bionic: wcscspn()/wcspbrk() treat every wchar_t >= 0x100 as a match (Android 17, CP3A.260905.009) · Issue #2260 · android/ndk · GitHub
url: https://github.com/android/ndk/issues/2260
date: 2026-10-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-14T15:51:34.343945
---

# [BUG] bionic: wcscspn()/wcspbrk() treat every wchar_t >= 0x100 as a match (Android 17, CP3A.260905.009) · Issue #2260 · android/ndk · GitHub

## [BUG] bionic: wcscspn()/wcspbrk() treat every wchar_t >= 0x100 as a match (Android 17, CP3A.260905.009)

The issue with `wcscspn()` and `wcspbrk()` in Android 17 is that they incorrectly treat every `wchar_t` from U+0100 to U+10FFFF as a match when the reject set has two or more characters that are all less than U+0100. This occurs even if the code scans wide strings for ASCII delimiters, such as newline or wildcard characters.

## Summary

- The problem is caused by the treatment of `wchar_t` values from U+0100 to U+10FFFF as matches instead of non-matches in `wcscspn()` and `wcspbrk()`.
- The issue affects the following devices: Pixel 7, Pixel 8a, Nothing/PongEEA/Pong.
- The code changes from the June 2026 public release are different and introduced the current regression.
- The affected file is `llvm-libc`.

## Affected Code

```cpp
void
main
(
void
)
{
    // Original code with NDK (aarch64-linux-android30-clang)
    wchar_t
s
[] =
{
    'a',
    0x1F680,
    0x100,
    'b',
    'x',
    '\n',
    0,
};
    
    printf("wcscspn(s, L\"x\\n\") = %zu (expected 4)\n", 
           wcscspn(
               s
           , 
               L"x\\n"
           ));
    
    printf("wcspbrk(s, L\"x\\n\") = index %ld (expected 4)\n", 
           (
               long
               )
           (
           wcspbrk(
               s
           , 
               L"x\\n"
           ) 
               - 
               s
           ));
    
    printf("wcsspn(s, L\"a\\U0001F680\") = %zu (expected 2)\n", 
           wcsspn(
               s
           , 
               L"a\\U0001F680"
           ));
    
    return
 
0
};
```

## Reproducer

To reproduce the issue, create a C program with the given code and build it with the Android NDK (aarch64-linux-android30-clang). Run the program without any options using the `adb shell:` command.