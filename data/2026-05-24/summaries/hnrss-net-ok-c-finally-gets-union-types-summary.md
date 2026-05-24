---
title: .NET (OK, C#) finally gets union types🎉
url: https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/
date: 2026-05-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-24T18:00:57.276125
---

# .NET (OK, C#) finally gets union types🎉

# .NET (OK, C#) finally gets union types🎉

## What are union types?
- Union types let a single value represent one of several distinct types (e.g., `Option<T>` or `Result<TSuccess,TError>`).
- Common in functional languages such as F#, TypeScript, Rust.
- They enable the “result pattern”: a method returns either a success value or an error value, forcing the caller to handle both cases.

## Union types in C# 15 with the `union` keyword
- C# 15 introduces the `union` keyword to declare a union directly.
- Example declaration:

```csharp
public union SupportedOS (Windows, Linux, MacOS);
```

- Instances can be created via constructor or implicit conversion:

```csharp
SupportedOS os = new SupportedOS(new MacOS("Tahoe", 25));
SupportedOS os = new MacOS("Tahoe", 25);   // implicit
```

- The generated type implements `IUnion` with a nullable `object? Value` property to retrieve the underlying case.
- The idiomatic way to work with a union is a switch expression that pattern‑matches each case:

```csharp
string GetDescription(SupportedOS os) => os switch
{
    Windows w => $"Windows {w.Version}",
    Linux   l => $"{l.Distro} {l.Version}",
    MacOS   m => $"MacOS {m.Name} ({m.Version})"
};
```

- The compiler enforces exhaustiveness; missing cases produce a warning (`CS8509`).
- Nullable case types require handling of `null` in the switch.

### Classic patterns expressed as unions
- `Result<T>` can be declared as `public union Result<T>(T, Exception);`
- `Option<T>` can be declared with a sentinel `None` record:

```csharp
public record class None;
public union Option<T>(None, T);
```

## Using union types in .NET 11
1. Install .NET 11 preview 2+ SDK (preview 4+ recommended).
2. Enable preview language features in the project file:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <LangVersion>preview</LangVersion>
    <TargetFrameworks>net11.0;net8.0;net48</TargetFrameworks>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
```

- The union feature works on earlier runtimes because it is a compile‑time construct.
- When targeting older runtimes or using preview 2/3, add the helper `UnionAttribute` and `IUnion` definitions manually (they are built‑in from preview 4 onward).

## IDE support
- Visual Studio Preview and VS Code with C# DevKit Insiders provide initial support.
- JetBrains Rider support is pending.

## How union types are implemented
- The compiler generates a struct marked with `[Union]` that implements `IUnion`.
- Each case type gets a dedicated constructor that stores the value in the `Value` property as `object?`.
- Example generated code for `SupportedOS`:

```csharp
using System.Runtime.CompilerServices;

[Union]
public struct SupportedOS : IUnion
{
    public object? Value { get; }

    public SupportedOS(Windows value) => Value = (object?)value;
    public SupportedOS(Linux   value) => Value = (object?)value;
    public SupportedOS(MacOS   value) => Value = (object?)value;
}
```

The generated implementation is straightforward, relying on the attribute and interface to expose the stored case.