---
title: "GitHub - CAPCOM-TD-OSS/REDox: High-performance, token-based structured data engine for .NET. A core component of REX, the technology behind CAPCOM's n..."
url: https://github.com/CAPCOM-TD-OSS/REDox
date: 2026-10-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-03T03:07:32.471469
---

# GitHub - CAPCOM-TD-OSS/REDox: High-performance, token-based structured data engine for .NET. A core component of REX, the technology behind CAPCOM's n...

# REDox (RE:Dox) Overview

## What is REDox?
- High‑performance, token‑based structured data engine for .NET.  
- Core component of CAPCOM’s REX technology for the next‑generation game engine.  
- Parses JSON, JSON5, CBOR, MessagePack, TOML, XML, HTML, CSV, INI, DOX into a compact fixed‑size token DOM/IR.  
- Provides unified reader, writer, serializer, and deserializer for all supported formats.

## Why use REDox?
- Combines the parse speed of a tape DOM, the editability of a node DOM, and the flexibility of Newtonsoft.Json.  
- Benchmarks show up to ~1.8× faster sequential deserialization, ~2.8× faster automatic parallel deserialization, and ~1.6× faster serialization compared with System.Text.Json.  
- Significantly lower memory allocations (e.g., 2.56 MB vs 8.53 MB for `canada.json`).  
- Single converter model across formats via `DataConverter<T>` targeting format‑agnostic `DataReader`/`DataWriter`.  
- Mutable token DOM allows in‑place edits without rebuilding a heavyweight object tree.  
- Trivia‑preserving JSON5 editing retains comments and whitespace after modifications.  
- Compatibility layers for System.Text.Json, Newtonsoft.Json, and DataContractJsonSerializer.  
- Licensed under Apache‑2.0.

## Quick 30‑second example
```csharp
dotnet add package CAPCOM.REDox

using REDox.Json;

var player = new Player {
    Name = "Leon",
    Level = 42,
    Items = ["Handgun", "Green Herb"]
};

var json = JsonSerializer.Serialize(player);
var restored = JsonSerializer.Deserialize<Player>(json);

using var doc = JsonDocument.Parse(json);
var root = doc.RootElement.AsObject();

root["Name"] = "Claire";
root.Add("Hp", 100);
root.Remove("Level");

var items = root["Items"].AsArray();
items.Add("First Aid Spray");
items.Insert(0, "Knife");
items.RemoveAt(1);

var edited = doc.RootElement.ToJsonString();
```

```csharp
public sealed class Player {
    public string? Name { get; set; }
    public int Level { get; set; }
    public string[] Items { get; set; } = [];
}
```

## Performance Highlights
- **Environment:** BenchmarkDotNet, .NET 10 (x64 RyuJIT), AMD Ryzen Threadripper PRO 5975WX, Windows 11.  
- **Speedup vs System.Text.Json (JsonSerializer):**

| Dataset            | Deserialize | Parallel Deserialize | Serialize |
|--------------------|-------------|----------------------|-----------|
| canada.json        | 1.68×       | 2.84×                | 1.06×     |
| citm_catalog.json  | 1.77×       | 2.25×                | 1.62×     |
| twitter.json       | 1.36×       | 2.34×                | 1.42×     |

- **Memory usage:** `canada.json` allocation reduced from ~8.73 MB (System.Text.Json) to ~2.56 MB (REDox).  
- Benchmarks can be reproduced with:  
  `dotnet run -c Release --project benchmarks/REDox.Json.Benchmarks`

## Architecture Overview
- **64‑bit dual‑mode token:** Fixed‑size token with an extension bit.
  - Bit 0 = payload interpreted by the format‑specific layer (source‑backed view).  
  - Bit 1 = payload interpreted by REDox for format‑agnostic editing (insert/remove/replace).  
- Token can represent null, boolean, integers, floating‑point, strings, binary, timestamps, big numbers, arrays, objects, trivia, or format‑specific extensions.  
- **Asymmetric read/write design:**
  - **Write path:** `DataWriter` streams directly to the output buffer in a single pass (no intermediate DOM).  
  - **Read path:** `DataReader` first builds a compact token DOM, enabling random access, pre‑sizing of collections, and out‑of‑order processing.  
- Unchanged values can reuse original source slices, avoiding eager materialization.

## Repository Structure (selected)
- `src/` – core library implementation.  
- `benchmarks/` – performance benchmark suite.  
- `docs/` – documentation and images.  
- `tests/` – unit and integration tests.  
- `experimental/`, `external/` – auxiliary and experimental components.  
- Supporting files: `.editorconfig`, `.gitattributes`, `.gitignore`, `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`.

## Getting Started
1. Add the package: `dotnet add package CAPCOM.REDox`.  
2. Use `JsonSerializer`, `JsonDocument`, or `DataConverter<T>` for format‑agnostic operations.  
3. Run the benchmark suite to evaluate performance on your own data.