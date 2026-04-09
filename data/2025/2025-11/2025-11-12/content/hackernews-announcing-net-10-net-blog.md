---
title: Announcing .NET 10 - .NET Blog
url: https://devblogs.microsoft.com/dotnet/announcing-dotnet-10/
site_name: hackernews
fetched_at: '2025-11-12T19:07:27.025657'
original_url: https://devblogs.microsoft.com/dotnet/announcing-dotnet-10/
author: .NET Team
date: '2025-11-12'
published_date: '2025-11-11T15:38:00+00:00'
---

Visual Studio 2026 Insiders is here!

The world’s most popular IDE just got an upgrade.

Download Now

Learn More



.NET Team

Today, we are excited to announce the launch of .NET 10, the most productive, modern, secure, intelligent, and performant release of .NET yet. It’s the result of another year of effort from thousands of developers around the world. This release includes thousands of performance, security, and functional improvements across the entire .NET stack-from languages and developer tools to workloads-enabling you to build with a unified platform and easily infuse your apps with AI.

Important.NET 10 is aLong Term Support (LTS) releaseand will be supported forthree yearsuntil November 10, 2028. We strongly recommend that production applications upgrade to .NET 10 to take advantage of the extended support window, significant performance improvements, and new capabilities.

Downloads of .NET 10 and updates toVisual Studio 2026and theC# Dev Kit for Visual Studio Codeare available now.

Download .NET 10Get Visual Studio 2026

The .NET team, our partners, and the .NET community are showcasing what’s new in .NET 10 at.NET Conf 2025. Watch thesessionsto see all of the excitement including thekeynote.

## A Thriving .NET Community

.NET 10 wouldn’t be possible without our amazing community. Thank you to everyone who contributed issues, pull requests, code reviews, and feedback to make this release happen. The .NET ecosystem continues to flourish with over 478,000 packages onNuGetthat have been downloaded over 800 billion times. Thousands of companies worldwide includingH&R Block, Geocaching, Chipotle, Fidelity, and many more, along with products and services here at Microsoft like Xbox, Bing, Microsoft Graph, Azure Cosmos DB, Microsoft Exchange, Microsoft Teams, and Microsoft Copilot, trust .NET to build their most critical applications.

## Unparalleled Performance – Faster Apps, Lower Memory

.NET 10 is the fastest .NET yet with improvements across the runtime, workloads, and languages. Stephen Toub’sperformance improvements deep divehighlights the latest optimizations.

Key improvements:

* JIT compiler enhancements: Better inlining, method devirtualization, and improved code generation for struct arguments
* Hardware acceleration:AVX10.2 supportfor cutting-edge Intel silicon, Arm64 SVE for advanced vectorization withArm64 write-barrier improvementsreducing GC pause times by 8-20%
* NativeAOT improvements: Smaller, faster ahead-of-time compiled apps
* Runtime optimizations:Enhanced loop inversion and stack allocationstrategies deliver measurable performance gains

## C# 14 & F# 10

C# 14andF# 10deliver powerful language improvements that make your code more concise and expressive. C# continues to be one of the world’s most popular programming languages,ranking in the top 5 in the 2025 GitHub Octoverse report.

### C# 14 highlights

Field-backed propertiessimplify property declarations by eliminating the need for explicit backing fields. The compiler generates the backing field automatically, making your code cleaner and more maintainable:

// Automatic backing field with custom logic
public string Name
{
 get => field;
 set => field = value?.Trim() ?? string.Empty;
}

Extension properties and methodsenable adding members to types you don’t own-including interfaces and static members-making extension types far more powerful. You can now create extension properties that work seamlessly with types throughout your codebase:

// Extension properties for any type
static class ListExtensions
{
 extension(List<int> @this)
 {
 public int Sum => @this.Aggregate(0, (a, b) => a + b);
 }
}

Additional C# 14 features:

* First-classSpan<T>conversions: Implicit conversion support for high-performance span operations
* Null-conditional assignment:?.=operator for cleaner null-safe assignment code
* Parameter modifiers in lambdas: Useref,in, oroutparameters without explicit types
* Collection expression extensions:.._expression_toparamsand[.._expression_]spread syntax
* Enhanced overload resolution:[OverloadResolutionPriority]attribute for better method selection
* Partial properties and constructors: Complete the partial members story with properties, constructors, and events
* ref structinterface implementations: Better performance with zero-allocation patterns

### F# 10 highlights

F# 10is a refinement release focused on clarity, consistency, and performance with meaningful improvements for everyday code.

Language improvements:

* Scoped warning suppression: Use#warnonpaired with#nowarnto enable or disable warnings within specific code sections, giving you precise control over compiler diagnostics
* Access modifiers on auto property accessors: Create publicly readable but privately mutable properties without verbose backing fields (member val Balance = 0m with public get, private set)
* ValueOptionoptional parameters: Apply[<Struct>]attribute to optional parameters to use struct-basedValueOption<'T>instead of heap-allocatedoption, eliminating allocations in performance-critical code
* Tail-call support in computation expressions: Builders can now opt into tail-call optimizations withReturnFromFinalandYieldFromFinalmethods
* Typed bindings without parentheses: Write natural type annotations likelet! x: int = fetchA()in computation expressions without parentheses

Core library & performance:

* and!in task expressions: Concurrently await multiple tasks with idiomatic syntax:let! a = fetchA() and! b = fetchB()
* Type subsumption cache: Faster compilation and IDE responsiveness through memoized type relationship checks
* Parallel compilation preview: Graph-based type checking, parallel IL code generation, and parallel optimization enabled by default withLangVersion=Preview
* Better trimming by default: Auto-generated substitutions remove F# metadata resources for smaller published apps

Read more about these features, as well as improvements to computation expression bindings, attribute target enforcement, deprecation warnings for omittedseq, and more in theWhat’s New in F# 10 documentation.

## .NET Libraries – Secure, Modern APIs

.NET 10 libraries deliver important updates across cryptography, networking, serialization, and more-making apps more secure and efficient.

### Post-Quantum Cryptography

NoteQuantum computing advances make post-quantum cryptography increasingly important. .NET 10’s expanded PQC support helps future-proof your applications against quantum threats while maintaining compatibility with existing systems.

.NET 10 expandspost-quantum cryptography (PQC) support:

* Windows CNG support: Use ML-DSA and ML-KEM algorithms with Windows cryptography APIs
* Enhanced ML-DSA: HashML-DSA variant for improved security characteristics
* Composite ML-DSA: Hybrid approaches combining traditional and quantum-resistant algorithms for defense-in-depth

### Enhanced Networking

Networking improvements make apps faster and more capable:

* WebSocketStream: Simplified WebSocket API that’s easier to use and more efficient
* TLS 1.3 on macOS: Modern TLS support across all major platforms
* Windows process group support: Better process management on Windows
* Performance optimizations: Reduced allocations and improved throughput across HTTP, sockets, and WebSockets

### Additional library improvements

* JSON enhancements: Disallow duplicate properties for safer deserialization, enhanced serialization settings,PipeReadersupport for high-performance scenarios
* Cryptography updates: AES KeyWrap with Padding for secure key wrapping in compliance scenarios
* System updates: Improved diagnostics, better interop with native code, enhanced collections

Learn more inWhat’s new in .NET Libraries.

## Aspire – Orchestrate front ends, APIs, containers, and databases effortlessly

Aspiremakes building observable, production-ready distributed apps straightforward with built-in telemetry, service discovery, and cloud integrations.Aspire 13ships with .NET 10 with major improvements for polyglot development, modern workflows, and enterprise deployment.

Key highlights:

* Modern development experience: CLI enhancements, single-file AppHost support for streamlined project organization, and quicker onboarding with simplified templates
* Seamless build & deployment: Built-in static file site support for frontend apps, robust deployment parallelization for faster releases, and production-ready container workflows
* Enterprise-ready infrastructure: Flexible connection strings and certificate trust management that works consistently across your applications

Additional features:

* Simplified AppHost SDK: SetAspire.AppHost.Sdkas the sole project SDK
* AddCSharpApp support: NewCSharpAppResourceandAddCSharpAppalternatives toAddProject
* Enhanced security: Encoded parameters for sensitive configuration data, customizable resource certificate trust
* Dashboard improvements: OpenID Connect claims configuration for flexible authentication

Working with other platforms:

When your .NET applications need to integrate with services written in Python, JavaScript, or other languages, Aspire 13 makes this seamless. You can orchestrate your entire distributed application from your .NET AppHost with comprehensive debugging support, auto-generated Dockerfiles, and unified environment variable patterns across all platforms.Read the full polyglot announcement.

Ecosystem growth: Check out theAspire Community Toolkitand earn theAspire credential.

Learn more in theAspire documentation.

## Artificial Intelligence – From Simple Integrations to Multi-Agent Systems

.NET makes building AI-powered apps straightforward, from simple integrations to complex multi-agent systems. Companies like H&R Block, Blip, and KPMG use .NET for their AI solutions, and the new Microsoft Copilot is built with .NET.

### Microsoft Agent Framework – Build Intelligent Multi-Agent Systems

TheMicrosoft Agent Frameworksimplifies building intelligent, agentic AI systems by combining the best of Semantic Kernel and AutoGen into a unified experience. Whether you’re building a single AI agent or orchestrating multiple agents working together, the framework provides the patterns and infrastructure you need.

Create sophisticated AI workflows with minimal code:

// Create agents with minimal code
AIAgent writer = new ChatClientAgent(
 chatClient,
 new ChatClientAgentOptions
 {
 Name = "Writer",
 Instructions = "Write engaging, creative stories."
 });

// Orchestrate in workflows
AIAgent editor = new ChatClientAgent(chatClient, /* ... */);
Workflow workflow = AgentWorkflowBuilder.BuildSequential(writer, editor);
AIAgent workflowAgent = await workflow.AsAgentAsync();

The framework supports multiple workflow patterns to match your application’s needs:

* Sequential workflows: Agents execute in a defined order, with each agent’s output feeding into the next
* Concurrent workflows: Multiple agents work in parallel for faster processing
* Handoff workflows: Agents dynamically pass control based on context and requirements
* Group chat: Agents collaborate through conversation to solve complex problems
* Magentic: A dedicated manager coordinates a team of specialized agents

Integrate tools seamlessly, whether they’re simple C# functions or full Model Context Protocol (MCP) servers. The framework is production-ready with built-in support for dependency injection, middleware pipelines, and OpenTelemetry for observability.

You can quickly get started with building server hosted agents with Microsoft Agent Framework and ASP.NET Core using the new AI Agent Web API template (aiagent-webapi) available in theMicrosoft.Agents.AI.ProjectTemplatestemplate package.

dotnet new install Microsoft.Agents.AI.ProjectTemplates
dotnet new aiagent-webapi -o MyAIAgentWebApi
cd MyAIAgentWebApi
dotnet run

This creates an ASP.NET Core Web API project that hosts your agents and exposes them as standard HTTP endpoints. It includes the Microsoft Agent Framework Dev UI, providing a web-based test harness to validate and visualize agents and workflows through an interactive interface.

https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/11/microsoft-agent-framework-dev-ui.webm

Microsoft Agent Framework now supports the AG-UI protocol for building rich agent user interfaces.AG-UIis a light-weight event-based protocol for human-agent interactions that makes it easy to build streaming UIs, frontend tool calling, shared state management, and other agentic UI experiences. Check out various AG-UI enabled scenarios with Microsoft Agent Framework using theAG-UI Dojosample app.

Use the newMicrosoft.Agents.AI.Hosting.AGUI.AspNetCorepackage to easily map AG-UI endpoints for your agents.

// Map an AG-UI endpoint for the publisher agent at /publisher/ag-ui
app.MapAGUI("publisher/ag-ui", publisherAgent)

You can then use existing AG-UI client frameworks, likeCopilotKit, to quickly build rich user experiences for your agents. Or, use the new .NET AG-UI chat client in theMicrosoft.Agents.AI.AGUIpackage to build your own UI experiences using your favorite .NET UI framework, like .NET MAUI or Blazor.

IChatClient aguiChatClient = new AGUIChatClient(httpClient, "publisher/ag-ui);

SeeAG-UI Agentsto learn more about getting started with Microsoft Agent Framework and AG-UI.

### Microsoft.Extensions.AI – Unified Building Blocks for AI Applications

Microsoft.Extensions.AIandMicrosoft.Extensions.VectorDataprovide unified abstractions for integrating AI services into your applications. TheIChatClientinterface works with any provider-OpenAI, Azure OpenAI, GitHub Models, Ollama-through a consistent API, making it easy to switch providers or support multiple backends without rewriting your code.

// Use any AI provider with the same interface
IChatClient chatClient = new AzureOpenAIClient(endpoint, credential)
 .AsChatClient("gpt-4o");

var response = await chatClient.CompleteAsync("Explain quantum computing");
Console.WriteLine(response.Message);

The unified abstractions support:

* Provider flexibility: Switch between AI providers without code changes
* Middleware pipeline: Add caching, logging, or custom behavior to any AI call
* Dependency injection: Register AI services using familiar .NET patterns
* Telemetry: Built-in OpenTelemetry support for monitoring AI usage
* Vector data: Unified abstractions for vector databases and semantic search

These building blocks work seamlessly with the Microsoft Agent Framework, Semantic Kernel, and your own AI implementations.

### Model Context Protocol (MCP) – Extend AI Agents with Tools and Services

.NET provides first-classMCP supportto extend AI agents with external tools and services. The Model Context Protocol enables AI agents to access data sources, APIs, and tools in a standardized way, making your agents more capable and versatile.

Install the .NET AI templatesand use the MCP server template to quickly build and publish MCP servers:

dotnet new install Microsoft.Extensions.AI.Templates
dotnet new mcpserver -n MyMcpServer

Once built, publish your MCP server to NuGet for easy consumption across your organization or the broader .NET community. TheC# MCP SDKhas regular releases to implement thelatest protocol updates, ensuring compatibility with the growing MCP ecosystem.

MCP enables AI agents to:

* Access databases and APIs securely
* Execute commands and workflows
* Read and modify files
* Integrate with business systems
* Use specialized tools and services

By standardizing how AI agents interact with external resources, MCP makes it easier to build, share, and compose AI capabilities across the .NET ecosystem.

Get started with ourAI documentationandAI samples.

## ASP.NET Core – Secure, High-Performance Web Apps and APIs

ASP.NET Corein .NET 10 includes everything you need to build secure, high-performance web applications and APIs. This release focuses on security, observability & diagnostics, performance, and developer productivity, providing more powerful tools for building modern web experiences.

Key improvements in this release include:

* Automatic Memory Pool Eviction: In long-running applications, memory pools can sometimes retain memory that is no longer needed. .NET 10 introduces automatic eviction for memory pools, which helps reduce the memory footprint of your applications by releasing idle memory back to the system.
* Web Authentication (Passkey) Support: ASP.NET Core Identity now includes support for passkeys, which are based on the WebAuthn and FIDO2 standards. This allows you to build more secure, passwordless authentication experiences. The Blazor Web App project template includes out-of-the-box support for passkey management and login.
* Native AOT Enhancements: Thewebapiaottemplate now includes OpenAPI support by default, and with new AOT-friendly validation, it’s easier to build documented, ahead-of-time compiled APIs. You can opt out with the--no-openapiflag.

### Blazor – Productive Component-Based Web Development

Blazorcontinues to evolve as a productive framework for building component-based web UIs with C#. .NET 10 brings significant improvements to performance, state management, and the overall developer experience.

Component State Persistence:

.NET 10 introduces significant enhancements to Blazor’s state management, making it more robust and easier to use, especially in server-side scenarios.

* Declarative State Persistence: Persisting state during prerendering is now much simpler. Use the[PersistentState]attribute to declaratively mark state that should be preserved.
* Circuit state persistence: Blazor circuits are now more resilient to network interruptions. Component state is automatically persisted before a circuit is evicted after a prolonged disconnection, so users don’t lose their work.
* Pause and Resume Circuits: New APIs to “pause” and “resume” circuits enable improved server scalability by freeing up resources for inactive clients

Performance and Reliability:

* Optimized Framework Scripts: The Blazor framework scripts are now delivered as precompressed and fingerprinted static web assets, which improves load performance and ensures proper caching.
* WebAssembly Preloading: To improve initial load times, Blazor Web Apps now automatically preload framework assets usingLinkheaders. Standalone WebAssembly apps also benefit from high-priority asset downloading.
* Response Streaming by Default:HttpClientresponses are now streamed by default in Blazor WebAssembly apps, which can improve performance and reduce memory usage when handling large responses.

Forms and Validation:

* Improved Form Validation: Blazor’s form validation capabilities have been significantly improved. You can now automatically validate nested objects and collection items using a new source-generator based system that is performant and AOT-compatible.
* NewInputHiddenComponent: A new component for rendering hidden form fields is now available.

Developer Experience:

* Automated Browser Testing:WebApplicationFactorynow supports end-to-end testing with browser automation tools like Playwright, making it easier to write automated UI tests for your web apps.
* JavaScript Interop Improvements: Interop with JavaScript is now more powerful. You can create instances of JavaScript objects, call their constructors, and directly read or modify their properties using both synchronous and asynchronous APIs.
* Improved “Not Found” Handling: Blazor provides a better experience for handling 404s. You can now specify a dedicated “Not Found” page in theRoutercomponent, and the newNavigationManager.NotFound()method makes it easier to trigger “Not Found” responses from code during server-side rendering or interactive rendering.
* QuickGrid enhancements: TheQuickGridcomponent now includes aRowClassparameter, allowing you to apply custom CSS classes to rows based on their data. You can also explicitly handle hiding the column options UI.

### Build Fast, Modern APIs

ASP.NET Core is an excellent choice for building fast, modern APIs. .NET 10 introduces better standards compliance, more powerful validation, and an improved developer experience.

OpenAPI Improvements:

* OpenAPI 3.1 Support by Default: ASP.NET Core now generates OpenAPI 3.1 documents, which includes support for the latest JSON Schema draft. This improves the representation of types, such as using an array for nullable types instead of a custom property.
* XML Comments Integration: The OpenAPI source generator now automatically uses your C# XML comments to populate descriptions, summaries, and other documentation fields in the generated OpenAPI document.
* YAML OpenAPI Documents: You can now serve OpenAPI documents in YAML format, providing a more human-readable alternative to JSON.
* Enhanced Response Descriptions: TheProducesResponseTypeattribute now includes an optionalDescriptionparameter, allowing you to provide more context for your API’s responses.

Minimal APIs Enhancements:

* Built-in Validation: You can now enable automatic validation for query, header, and request body parameters by callingAddValidation(). If validation fails, the framework will automatically return a 400 Bad Request response with the validation details. This works with DataAnnotations and supports nested objects and collections.
* Server-Sent Events (SSE): A newTypedResults.ServerSentEvents()method makes it easy to stream real-time updates to clients over a single HTTP connection.
* Customizable Error Responses: You can now integrate your validation logic withIProblemDetailsServiceto create consistent, customized error responses.

### Enhanced Observability and Diagnostics

.NET 10 introduces significant improvements to observability and diagnostics, making it easier to monitor and troubleshoot your ASP.NET Core applications.

* New Built-in Metrics: ASP.NET Core now includes a rich set of new metrics for monitoring key components, including Blazor, Authentication & Authorization, Identity, and the new memory pool.
* Improved Blazor Tracing: Blazor Server tracing has been enhanced to provide more detailed information about circuit activity, making it easier to diagnose issues in real-time.
* Blazor WebAssembly Diagnostic Tools: New diagnostic tools are available for Blazor WebAssembly applications, allowing you to collect CPU performance profiles, capture memory dumps, and gather runtime metrics.

For more details on all the new features, check out theWhat’s new in ASP.NET Core in .NET 10documentation.

## .NET MAUI – Build Native Cross-Platform Apps

.NET MAUIis the best way to build native cross-platform apps for iOS, Android, macOS, and Windows with .NET and C#.

Platform updates:

* Android 16 (API 36 & 36.1)bindings with latest platform features
* iOS 26.0bindings for latest iOS capabilities
* Marshal methods enabled: Improved startup performance by default

Control enhancements:

* HybridWebView: New initialization events (WebViewInitializing,WebViewInitialized) for platform-specific customization,InvokeJavaScriptAsyncoverload, and JavaScript exception handling
* Web request interception: Modify headers, redirect requests, or supply local responses forBlazorWebViewandHybridWebView
* CollectionView/CarouselView: Improved iOS handlers now default
* MediaPicker: Automatic EXIF handling, multi-file selection withPickMultipleAsync, image compression support
* SafeArea management: Enhanced to support multiple platforms from the newSafeAreaEdgesAPI
* Secondary toolbar items: Added for iOS and macOS

XAML improvements:

.NET MAUI in .NET 10 introduces significant XAML enhancements that streamline development and improve performance:

* Global and implicit XML namespaces(opt-in): Simplify XAML markup by eliminating repetitive namespace declarations
* New XAML source generator: Faster build times and better IntelliSense support with compile-time XAML processing

With global namespaces, you can declarexmlnsreferences once in aGlobalXmlns.csfile and use types without prefixes throughout your XAML files:

Before:

<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
 xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
 xmlns:models="clr-namespace:MyApp.Models"
 xmlns:controls="clr-namespace:MyApp.Controls"
 x:Class="MyApp.MainPage">
 <controls:TagView x:DataType="models:Tag" />
</ContentPage>

After:

<ContentPage x:Class="MyApp.MainPage">
 <TagView x:DataType="Tag" />
</ContentPage>

No need to declarexmlns:modelsorxmlns:controlsbecause they are declared globally in aGlobalXmlns.csfile. No prefixes required forTagVieworTag.

MediaPicker multi-file selection example:

var result = await MediaPicker.PickMultipleAsync(new MediaPickerOptions
{
 MaximumWidth = 1024,
 MaximumHeight = 768
});

Additional highlights:

* Aspire integration: New project template with telemetry and service discovery
* Diagnostics: Comprehensive layout performance monitoring withActivitySourceand metrics
* Quality focus: Continued improvements in reliability and performance

Read more inWhat’s new in .NET MAUI 10.

## Entity Framework Core 10 – Advanced Data Access

Entity Framework Core 10brings powerful improvements for data access, including AI-ready vector search, enhanced JSON support, and better complex type handling.

Azure SQL and SQL Server:

* Vector search support: Full support for the newvectordata type andVECTOR_DISTANCE()function, enabling AI workloads like semantic search and RAG with SQL Server 2025 and Azure SQL Database
* JSON data type: Automatic use of SQL Server 2025’s nativejsontype for better performance and safety-query with full LINQ support usingJSON_VALUE()andRETURNINGclauses
* Custom default constraint names: Specify names for default constraints or enable automatic naming for all constraints

Azure Cosmos DB:

* Full-text search: Enable efficient text searches with relevance scoring usingFullTextContains,FullTextContainsAll,FullTextContainsAny, andFullTextScorefunctions
* Hybrid search: Combine vector similarity and full-text search with theRRF(Reciprocal Rank Fusion) function for improved AI search accuracy
* Vector search GA: Vector similarity search is now production-ready with improved model building APIs and support for owned reference entities

Complex Types & JSON:

Complex types bring document-modeling benefits with better performance and simpler schemas:

* Optional complex types: Mark complex types as nullable for more flexible data models
* JSON mapping: Map complex types to single JSON columns with full LINQ query support and efficient bulk updates viaExecuteUpdate
* Struct support: Use .NET structs instead of classes for complex types with proper value semantics
* ExecuteUpdate for JSON: Bulk update JSON column properties efficiently-updates properties in place without loading entire documents

// Update Views count in JSON column
await context.Blogs.ExecuteUpdateAsync(s =>
 s.SetProperty(b => b.Details.Views, b => b.Details.Views + 1));

LINQ & Query Improvements:

* Better parameterized collections: New default translation sends each value as a separate parameter with padding to optimize query plan caching while preserving cardinality information
* LeftJoin and RightJoin support: First-class support for .NET 10’s new LINQ join operators for simpler outer join queries
* Consistent split query ordering: Fixed data consistency issues in split queries with proper ordering across all SQL statements

Additional Highlights:

* Named query filters: Define multiple query filters per entity type and selectively disable specific filters in queries
* ExecuteUpdate with regular lambdas: Build dynamic update operations without complex expression tree code
* Security improvements: Inlined constants are now redacted from logs by default, with analyzer warnings for string concatenation in raw SQL APIs

Learn more inWhat’s New in EF Core 10.

## Windows Development – Modern Desktop Apps

.NET 10 continues to enhance Windows app development acrossWinUI 3,WPF, andWinForms.

Highlights:

* Windows Forms: Improved clipboard handling, portedUITypeEditorsfrom .NET Framework for better migration support
* WPF: Performance improvements, Fluent style updates, quality enhancements
* WinUI 3: Latest Windows App SDK features and improvements

See the docs forWinUI 3,WPF, andWinForms.

## Developer Tools – Your Most Productive Environment Yet

.NET 10 and Visual Studio 2026 deliver a world-class, intelligent development platform that makes you more productive across your entire workflow.

### Visual Studio 2026 – Enhanced Performance and AI-Powered Development

Visual Studio 2026brings groundbreaking productivity with AI deeply integrated into your development workflow. TheVisual Studio 2026 release notesdetail the latest features.

AI-Powered Development:

* Adaptive paste: Copilot adapts pasted code to your file’s context-automatically fixing names, formatting, and translating between languages (e.g., C++ to C#)
* Profiler Copilot Agent: AI assistant that analyzes CPU usage, memory allocations, suggests optimizations, and generates BenchmarkDotNet benchmarks
* Debugger Agent for unit tests: Automatically debugs failing tests, forms hypotheses, applies fixes, and validates solutions iteratively
* Code actions at your fingertips: Right-click context menu provides instant Copilot assistance for common tasks (Explain, Optimize, Generate Tests, etc.)
* Copilot URL context: Reference web documentation directly in Copilot Chat for more accurate responses

Productivity Enhancements:

* Mermaid chart rendering: Visualize flowcharts and diagrams directly in the Markdown editor and Copilot Chat responses
* Enhanced editor controls: Advanced margin capabilities for maximizing your editing experience
* File exclusions in search: Better control over which files are included in search results
* Code coverage for all editions: Dynamic code coverage now available in Professional edition, with tested lines highlighted directly in the editor

Debugging & Diagnostics:

* Inline if-statement evaluation: Debug conditional logic faster with inline values and Copilot insights
* BenchmarkDotNet project template: Jump-start performance benchmarking with built-in CPU profiling and Copilot insights
* CodeLens with Optimize Allocations: Right from your editor, ask Copilot to optimize memory-intensive methods
* Profiler Agent thread summarization: Smart conversation summaries that maintain context when approaching token limits
* CMake diagnostics: Full support for CPU Usage, Events Viewer, memory usage, and File IO tools in CMake projects

Modern Experience:

* New look and feel: Fluent UI design system with 11 new tinted themes and independent editor appearance settings
* Modern settings experience: Streamlined, user-friendly settings interface replacing Tools > Options with better organization and reliability
* SLNX support: Work with the new simplified solution format for cleaner version control withSLNX documentation
* Performance enhancements: Faster startup, better memory management, and improved overall responsiveness
* Aspire integration: Seamless support for Aspire projects with specialized tooling and templates

### GitHub Copilot – Your AI Pair Programmer

GitHub Copilot is integrated throughout Visual Studio and VS Code, helping with code writing, testing, and debugging:

* AI completions for C#: Better context from relevant files
* Fix code issues: AI-assisted problem resolution
* Debug tests: Get help with failed test debugging
* IEnumerable visualizer: AI-powered LINQ expressions
* Modernize to .NET 10: Use GitHub Copilot to help upgrade and modernize your existing .NET applications to .NET 10, getting guidance on breaking changes, new APIs, and best practices

TipUpgrading from an earlier version of .NET? UseGitHub Copilotto help modernize your applications to .NET 10. Copilot can guide you through breaking changes, suggest modern API replacements, and help refactor code to take advantage of new language features and performance improvements.

### C# Dev Kit for Visual Studio Code

TheC# Dev Kitbrings a powerful, streamlined C# development experience to Visual Studio Code. Recent updates include:

* Solution-less workspace mode: Work without automatic solution file creation for simpler projects
* SLNX support: Full support for the new XML-based solution format with improved tooling
* Enhanced Razor editing: Improved IntelliSense, formatting, and code navigation in Blazor and Razor Pages
* Integrated test coverage: Native support for VS Code’s code coverage UI with visual indicators in the editor
* Custom project templates: Create projects from third-party and customdotnet newtemplates directly in VS Code
* NuGet package management: Add, update, and remove packages with integrated commands
* Drag-and-drop file management: Reorganize projects easily within Solution Explorer
* Aspire support: Run and debug Aspire projects with full orchestration support

Learn more in theC# Dev Kit documentation.

### .NET SDK – Powerful CLI Enhancements

The .NET 10 SDK includes powerful CLI enhancements:

* Microsoft.Testing.Platform supportindotnet testfor unified test execution
* Native tab-completion scriptsfor popular shells (bash, fish, PowerShell, zsh, nushell)
* Container images for console appswithout requiring Docker files orEnableSdkContainerSupport
* One-shot tool executionwithdotnet tool execand the newdnxscript
* CLI introspectionwith--cli-schemafor machine-readable command descriptions
* Platform-specific .NET toolssupporting multiple RuntimeIdentifiers with self-contained, trimmed, and AOT options
* Enhanced file-based appswith publish and native AOT support
* SLNX solution format: Simplified, XML-based solution files that are human-readable and easier to manage.Learn more about SLNX

### NuGet – Enhanced Security and Productivity

NuGet continues to evolve with security and productivity improvements:

* Enhanced security:Audit transitive dependencies by default for .NET 10 projects, integration withGitHub Advisory Database, andDependabot supportfor automatic security updates
* MCP support: Publish and consume MCP servers via NuGet
* New NuGet.org: Fresh design with dark mode
* Vulnerability remediation:dotnet package update --vulnerablecommandupdates vulnerable packages to first secure version

Learn more in the.NET SDK documentationandNuGet package auditing improvements.

## .NET 10 Long Term Support

.NET 10 is aLong Term Support (LTS) releaseand will be supported forthree years, until November 10, 2028. LTS releases receive critical updates and security patches, making .NET 10 the recommended version for production applications that require stability and extended support.

.NET follows a predictable annual release cadence with even-numbered LTS releases (3-year support) and odd-numbered Standard Term Support (STS) releases (24-month support). With therecent extension of STS support from 18 to 24 months, both .NET 9 and .NET 8 will reach end of support on November 10, 2026. .NET 10, as an LTS release, will continue to be supported until November 10, 2028.

For complete details on the .NET support policy and release schedule, visit the.NET support policy page.

## Get Started with .NET 10

.NET 10 and Visual Studio 2026 are available now. Get started today:

Download .NET 10Install Visual Studio 2026Watch .NET Conf

Learn more:

* What’s new in .NET 10:Runtime,Libraries,SDK
* What’s new in C# 14
* What’s new in F# 10
* What’s new in ASP.NET Core
* What’s new in Aspire
* AI in .NET
* What’s new in .NET MAUI
* What’s new in EF Core
* Windows App SDK release notes
* Visual Studio 2026 release notes

We can’t wait to see what you build with .NET 10!

Category
.NET
.NET MAUI
AI
ASP.NET Core
Blazor
C#
F#
NuGet
Performance
Visual Studio
Visual Studio Code
WinForms
WPF
Topics
.NET 10
Featured
featured-post

Share



## Author

.NET Team

.NET is the free, open-source, cross-platform framework for building modern apps and powerful cloud services.





## Read next

November 5, 2025

### How Copilot Studio uses .NET and WebAssembly for performance and innovation

Daniel Roth

November 4, 2025

### Get Ready for .NET Conf 2025!

Jon Galloway



## Stay informed

Get notified when new posts are published.



Subscribe

By subscribing you agree to our
Terms of Use
 and
Privacy



Follow this blog



Are you sure you wish to delete this
 comment?

OK

Cancel
