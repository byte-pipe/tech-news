---
title: ZigCool
url: https://nilostolte.github.io/tech/articles/ZigCool.html
date: 2025-11-07
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-09T11:16:35.859138
screenshot: hackernews_api-zigcool.png
---

# ZigCool

## Why Zig Is So Cool

by Nilo Stolte

# Introduction

In my 45-year-long career as a software developer, I have had the opportunity to work with many programming languages. However, I can confidently say that Zig is one of the most surprising languages I've come across.

### Installing and Compiling Zig

To get started with Zig, you need to download the language and install it on your system. Here's how:

*   **Installation**: Downloading the `.zip` file from the [Zig Language Distribution](https://ziglang.org/downloads/) website provides four installation options:
    *   `x86_64-windows-1.0.0.zip`
    *   `x86_64-macos-1.0.0.zip`
    *   `x86_64-linux-1.0.0.zip` (for Linux)
    *   `i386-win-x86_64-1.0.0.zip` (for Windows)
*   **Installation Path**: After downloading the zip file, find the `zig` directory in your system and add its path to your system's `PATH` environment variable.

### Building a "Hello World!" Program

Building a simple "Hello World!" program in Zig is easy. You can follow these steps:

1.  **Open Terminal**: Open your terminal or command prompt and activate an empty project folder (with no files).
2.  **Copy and Paste the Code**: Copy and paste the given code into this empty space, replacing `src/main.zig` with a temporary file name.
3.  **Run the Program**: Use the compiler to run the program:

    ```
    $ ./main.zig
```

### Main Concepts and Commands

Here's an overview of some key concepts and commands in Zig:

*   **Variables**: In Zig, variables are declared using `let` or `var`. `const` is used to declare immutable variables.
*   **Data Structures**: Zig supports basic data structures like arrays, vectors, linked lists, lists, maps, sets, tuples, and structs.
*   **Functions**: Functions in Zig can be defined inline or as separate functions.
*   **Error Handling**: Zig has a robust error handling system that allows you to declare exceptions using `e` and then handle their occurrence.

This is just a basic overview of the language. To go further, I recommend exploring more advanced topics like concurrency, parallelism, and multithreading in the [Zig Language Reference](https://ziglang.org/docs/#reference).
