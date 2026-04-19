---
title: A simplified model of Fil-C
url: https://www.corsix.org/content/simplified-model-of-fil-c
date: 2026-04-18
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-04-19T06:11:54.055163
---

# A simplified model of Fil-C

**A Simplified Model of Fil-C**

### Overview

Fil-C (Flexible Implementation of C) is a memory-safe implementation of C/C++ that rewrites LLVM IR to transform unsafe code into safe code. This article provides an overview of the simplified model, which automates rewriting source code for pointer variables.

### Key Points

* The simplified model is a compiler pass that rewrites LLVM IR.
* It includes three distinct allocations: one for pointer storage, and two for object allocation and deallocation.
* Pointer dereferences are bound checks performed using AllocationRecord pointers.
* Local variables of pointer type have their accompanying AllocationRecord pointed at by the compiler.

### Major Rewrite

The modified source code looks like this:
```c
#include <stdio.h>
#include <stdlib.h>

struct AllocationRecord {
    char *visible_bytes;
    char *invisible_bytes;
    size_t length;
};

int main() {
    AllocationRecord ar1, ar2;

    // Allocate space for storage of a short integer
    void *p1 = malloc(sizeof(int));
    ar1.visible_bytes = p1;

    // Make an array allocation (1 point)
    char **p2 = /* allocate memory for pointer to pointees */;
    AllocationRecord npa;
    int *np_int = (*p2)[0];
    np_int = npar.visible_bytes + sizeof(*np_int);

    // Allocate space for a long integer
    void *p3 = malloc(sizeof(long));
    ar3.visible_bytes = p3;

    // Make a struct allocation (1 point)
    char **p4 = /* allocate memory for pointer to structs */;
    AllocationRecord npa_struct;
    struct {
        int x; /* not visible bytes */
    } npa_struct;
    papa_visible_bytes[0] = &npa_struct.x;  // make sure it's visible

    // Free the allocated space
    void* free_func(size_t length) {
        AllocationRecord *ap = malloc(sizeof(AllocationRecord));
        ap->visible_bytes = malloc(length);
        ap->length = length;
        return ap; /* actually perform three distinct allocations */
    }
}
```
### Code Explanation

When a variable is dereferenced, the compiler checks if it's visible by looking at the AllocationRecord pointing to it:

* In the first example, `x` is not visible, so the check fails.
* In the second example, `p1ar[0]` points to an allocation containing only 3 bytes of data. The check succeeds.

When a local variable is added with a pointer type, the compiler automatically updates the AllocationRecord with it:

* When accessing a dereferenced pointer variable `x`, `[0] - p1ar.visible_bytes` retrieves 4 bytes (the size of `T2`) from an allocation containing only 3 bytes, which passes the check.

The modified functions use three distinct allocations instead of one for object storage and two for object deallocation. This reduces the memory footprint of the program by up to 3 times.