---
title: Avoid the Temptation of bool - DEV Community
url: https://dev.to/pauljlucas/avoid-the-temptation-of-bool-5g31
date: 2025-10-04
site: devto
model: llama3.2:1b
summarized_at: 2025-10-08T11:12:59.828531
screenshot: devto-avoid-the-temptation-of-bool-dev-community.png
---

# Avoid the Temptation of bool - DEV Community

## Avoiding bool: Alternatives and Best Practices

The Boolean type, also known as `bool` in C, C++, Go, and Rust, is fundamental to programming. However, its use can be misleading due to how it's represented as a literal `true` or `false`. Instead of relying on the true/false association, consider using alternatives like two functions or an enumeration to create a clear interface.

## Using Two Functions

### Alternative Implementation of public API
```c
void* alloc_raw(size_t size) {
  // implementation for raw allocation
}

void* alloc_zero(size_t size) {
  // implementation for zeroed allocation
}
```

### Using An Enumeration
In Go, you can define an enumeration to replace `bool`:
```go
type AllocationOpt int

const (
    AllocationRaw   AllocationOpt = iota
    AllocationZeroed
)

func Alloc(alignment AllocatedAlignmentType, size SizeBytes) (memory.Address, error) {
    switch AlignmentCase(alignment) {
    case Aligned:
        return alloc_raw(size)
    default:
        return alloc_zero(size)
    }
}
```
## Using Bit Flags for Additional Options

Adding custom flags to an enumeration allows you to add new options easily without modifying the existing function signature.

```go
type MemoryMode int

const (
    MemAllocated  MemMemoryMode = iota
    MemNonAllocated MemMemoryMode = iota
)

func Alloc(alignment AlignedMemMode, size SizeBytes) (memory.Address, error) {
    switch alignment {
    case Aligned:
        return alloc_raw(size)
    default:
        if AlignResult != NoAlignment {
            throw NewMemoryOverflowError(&size)
        }
        switch MemOption {
        case NonAllocated:
            return alloc_zero(size)
        default:
            return nil
        }
    }
}
```
## Recommendations

- **Use two functions** for public interfaces instead of relying solely on `bool`.
- **Define an enumeration** when possible to add custom flags or make code more readable.
- **Use bit flags** as additional options when you need flexibility without modifying existing function signatures.
