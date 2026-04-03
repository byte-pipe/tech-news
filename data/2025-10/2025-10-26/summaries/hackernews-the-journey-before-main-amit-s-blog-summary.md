---
title: "The Journey Before main() | Amit's Blog"
url: https://amit.prasad.me/blog/before-main
date: 2025-10-26
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-26T11:17:12.810481
screenshot: hackernews-the-journey-before-main-amit-s-blog.png
---

# The Journey Before main() | Amit's Blog

# The Journey Before main()

### Understanding the Boot Process and ELF Files

On Linux, when an executable program is run, the operating system first calls the `execve` function to start executing its code. This process requires a full path to the executable file, which is resolved by the kernel's `PATH` environment variable.

#### Command Execution

To execute a command, you can use Rust's higher-level library `process` and create an instance of it:

```rust
use std::process;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    println!("Arguments: {:?}", args);
}
```

In this example, the program simply prints out its command-line arguments without executing any commands.

#### Interpreters and Shebangs

If your executable file starts with a shebang (!), the kernel will use it to determine which interpreter to run. For example:

```bash
#!/usr/bin/env rustc main.rs
```

In this case, Rust's `rustc` compiler is used as the interpreter.

#### Executable File Format (ELF)

An executable file on Linux typically uses the ELF format, also known as Object File Format or Object Relocation Format. The typical ELF header includes:

* **Magic:** A 7-byte sequence indicating that it's an ELF file (0xe7)
* **Class:** Specifies that it's a 32-bit binary, ELF type: execute-only section
* **Data:** Provides information about the elf section
* **Version:** Current version of ELF format
* **OS/ABI:** Specifies the operating system and ABI (Platform Not Integrated)
* **ABI Version:** Specifies the current version of the executable's ABI
* **Type:** Specifies that it's an executable file
* **Machine:** Indicates the target machine, e.g., RISC-V
* **Version:** Current version of machine instruction
* **Entry point address:** The starting address of the program
* **Section headers:** Information about the ELF sections

#### Main Function Execution

The `.main` entry point of an ELF executable is a symbol (section) in the file. In this context, it's used to call other functions that form the execution flow:

```c
Elf64_Ehdr {
    .e_ident[EI_MAG0] = (1u16, 0x49, 0x46, 0x01), /* Mach-O version */
    .e_ident[EI_MAGIC2] = (0x00, 0x00, 0x00, 0x00),
};

struct MyProgram {
    func: *mut usize,
}

fn main() -> std::io::Status {
    let section_headers_count = SectionHeadersSize - SectionHeaderSize;
    for i in (0..section_headers_count).map(|x| x as usize) {
        let &entry_point_address =
            &MyProgram::func.offset_add(i * MyMyProgramSize);
        println!("Section {}: {}", i+1, entry_point_address >> SectionHeadersOffset);
    }
    Ok(())
}
```

**Main Function Execution**

In this example, we execute an executable symbol by traversing the ELF section headers and finding the `main` function entry point. The size of the program will depend on how many sections it contains.

**Example Output**
```plaintext
Section 1: 0x10000    [0xe7]           main
Section 3: 0x10040     [0x01]         18
```
The `main` function's entry point is located at offset 10000 in the ELF file.

**Note**: This code snippet only provides a basic overview of how an executable might be structured. A real-world program will also include dynamic linker symbols, relocation tables, and other details that aren't shown here.
