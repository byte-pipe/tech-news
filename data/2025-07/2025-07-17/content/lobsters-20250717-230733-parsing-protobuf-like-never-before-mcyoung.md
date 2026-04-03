---
title: Parsing Protobuf Like Never Before · mcyoung
url: https://mcyoung.xyz/2025/07/16/hyperpb/
site_name: lobsters
fetched_at: '2025-07-17T23:07:33.214598'
original_url: https://mcyoung.xyz/2025/07/16/hyperpb/
date: '2025-07-17'
tags: go, performance
---

2025-07-16 • 4119 words • 45 minutes

•

#go
 •
#dark-arts
 •
#protobuf



# Parsing Protobuf Like Never Before





Historically I have worked on many projects related to high-performance Protobuf, be that on the C++ runtime, on the Rust runtime, or on integratingUPB, the fastest Protobuf runtime, written by my colleagueJosh Haberman. Igenerallydon’t post directly about my current job, but my most recent toy-turned-product is something I’m very excited to write about:hyperpb.



Here’s how we measure up against other Go Protobuf parsers. This is a subset of my benchmarks, since the benchmark suite contains many dozens of specimens. This was recorded on an AMD Zen 4 machine.






Throughput for various configurations ofhyperpb(colored bars) vs. competing parsers (grey bars). Each successivehyperpbincludes all previous optimizations, corresponding tozerocopy mode,arena reuse, andprofile-guided optimization. Bigger is better.





Traditionally, Protobuf backends would generate parsers by generating source code specialized to each type. Naively, this would give the best performance, because everything would be “right-sized” to a particular message type. Unfortunately, now that we know better, there are a bunch of drawbacks:


1. Every type you care about must be compiled ahead-of-time. Tricky for when you want to build something generic over schemas your users provide you.
2. Every type contributes to a cost on the instruction cache, meaning that if your program parses a lot of different types, it will essentially flush your instruction cache any time you enter a parser. Worse still, if a parse involves enough types, the parser itself will hit instruction decoding throughput issues.


These effects are not directly visible in normal workloads, but other side-effects are visible: for example, giant switches on field numbers can turn into chains of branch instructions, meaning that higher-numbered fields will be quite slow. Even binary-searching on field numbers isn’t exactly ideal. However, we know that every Protobuf codec ever emits fields in index order (i.e., declaration order in the.protofile), which is a data conditioning fact we don’t take advantage of with a switch.



UPB solves this problem. It is a small C kernel for parsing Protobuf messages, which is completely dynamic: a UPB “parser” is actually a collection of data tables that are evaluated by atable-driven parser. In other words, a UPB parser is actually configuration for an interpreter VM, which executes Protobuf messages as its bytecode. UPB also contains many arena optimizations to improve allocation throughput when parsing complex messages.



hyperpbis a brand new library, written in the most cursed Go imaginable, which brings many of the optimizations of UPB to Go, and many new ones, while being tuned to Go’s own weird needs. The result leaves the competition in the dust in virtually every benchmark, while being completely runtime-dynamic. This means it’s faster than Protobuf Go’s own generated code,andvtprotobuf(a popular but non-conforming1parser generator for Go).



This post is about some of the internals ofhyperpb. I have also prepared a more sales-ey writeup, which you can read onthe Buf blog.



## Why Reinvent UPB?



UPB is awesome. It can slot easily into any language that has C FFI, which is basically every language ever.



Unfortunately, Go’s C FFI is really, really bad. It’s hard to overstate how bad cgo is. There isn’t a good way to cooperate with C on memory allocation (C can’t really handle Go memory without a lot of problems, due to the GC). Having C memory get cleaned up by the GC requires finalizers, which are very slow. Calling into C is very slow, because Go pessimistically assumes that C requires a large stack, and also calling into C does nasty things to the scheduler.



All of these things can be worked around, of course. For a while I considered compiling UPB to assembly, and rewriting that assembly into Go’s awful assembly syntax2, and then having Go assemble UPB out of that. This presents a few issues though, particularly because Go’s assembly calling convention is still in the stone age3(arguments are passed on the stack), and because we would still need to do a lot of work to get UPB to match theprotoreflectAPI.



Go also has a few… unique qualities that make writing a Protobuf interpreter an interesting challenge withexcitingoptimization opportunities.



First, of course, is the register ABI, which onx86_64gives us a whoppingnineargument and return registers, meaning that we can simply pass the entire parser state in registers all the time.



Second is that Go does not have much UB to speak of, so we can get away with a lot of very evil pointer crimes that we could not in C++ or Rust.



Third is that Protobuf Go has a robust reflection system that we can target if we design specifically for it.



Also, the Go ecosystem seems much more tolerant of less-than-ideal startup times (because the languageloveslife-before-main due toinit()functions), so unlike UPB, we can require that the interpreter’s program be generated at runtime, meaning that we can design for online PGO. In other words, we have the perfect storm to create the first-ever Protobuf JIT compiler (which we also refer to as “online PGO” or “real-time PGO”).



## hyperpb’s API



Right now,hyperpb’s API is very simple. There arehyperpb.Compile*functions that accept some representation of a message descriptor, and return a*hyperpb.MessageType, which implements theprotoreflecttype APIs. This can be used to allocate a new*hyperpb.Message, which you can shove intoproto.Unmarshaland do reflection on the result. However, you can’t mutate*hyperpb.Messages currently, because the main use-cases I am optimizing for are read-only. All mutations panic instead.



The hero use-case, using Buf’sprotovalidatelibrary, uses reflection to execute validation predicates. It looks like this:


// Compile a new message type, deserializing an encoded FileDescriptorSet.

msgType

:=

hyperpb
.
CompileForBytes
(
schema
,

"my.api.v1.Request"
)

// Allocate a new message of that type.

msg

:=

hyperpb
.
NewMessage
(
msgType
)

// Unmarshal like you would any other message, using proto.Unmarshal.

if

err

:=

proto
.
Unmarshal
(
data
,

msg
);

err

!=

nil

{


// Handle parse failure.

}

// Validate the message. Protovalidate uses reflection, so this Just Works.

if

err

:=

protovalidate
.
Validate
(
msg
);

err

!=

nil

{


// Handle validation failure.

}
Go


We tell users to make sure to cache the compilation step because compilation can be arbitrarily slow: it’s an optimizing compiler! This is not unlike the same warning onregexp.Compile, which makes it easy to teach users how to use this API correctly.



In addition to the main API, there’s a bunch of performance tuning knobs for the compiler, for unmarshaling, and for recording profiles. Types can be recompiled using a recorded profile to be more optimized for the kinds of messages that actually come on the wire.hyperpbPGO4affects a number of things that we’ll get into as I dive into the implementation details.



## The Guts



Most of the core implementation lives underinternal/tdp. The main components are as follows:


1. tdp, which defines the “object code format” for the interpreter. This includes definitions for describing types and fields to the parser.
2. tdp/compiler, which contains all of the code for converting aprotoreflect.MessageDescriptorinto atdp.Library, which contains all of the types relevant to a particular parsing operation.
3. tdp/dynamicdefines what dynamic message types look like. The compiler does a bunch of layout work that gets stored intdp.Typevalues, which adynamic.Messageinterprets to find the offsets of fields within itself.
4. tdp/vmcontains the core interpreter implementation, including the VM state that is passed in registers everywhere. It also includes hand-optimized routines for parsing varints and validating UTF-8.
5. tdp/thunksdefinesarchetypes, which are classes of fields that all use the same layout and parsers. This corresponds roughly to a(presence, kind)pair, but not exactly. There are around 200 different archetypes.


This article won’t be a deep-dive into everything in the parser, and even this excludes large portions ofhyperpb. For example, theinternal/arenapackage is already described in a different blogpost of mine. I recommend taking a look at that to learn about how we implement a GC-friendly arena forhyperpb.



Instead, I will give a brief overview of how the object code is organized and how the parser interprets it. I will also go over a few of the more interesting optimizations we have.



### tdp.Type



EveryMessageDescriptorthat is reachable from the root message (either as a field or as an extension) becomes atdp.Type. This contains the dynamic size of the corresponding message type, a pointer to the type’s default parser (there can be more than one parser for a type) and a variable number oftdp.Fieldvalues. These specify the offset of each field and provide accessor thunks, for actually extracting the value of the field.



Atdp.TypeParseris what the parser VM interprets alongside encoded Protobuf data. It contains all of the information needed for decoding a message in compact form, includingtdp.FieldParsers for each of its fields (and extensions), as well as a hashtable for looking up a field by tag, which is used by the VM as a fallback.



Thetdp.FieldParsers each contain:


1. The same offset information as atdp.Field.
2. The field’s tag, in a special format.
3. A function pointer that gets called to parse the field.
4. The next field(s) to try parsing after this one is parsed.


Eachtdp.FieldParseractually corresponds to a possible tag on a record for this message. Some fields have multiple different tags: for example, arepeated int32can have aVARINT-type tag for the repeated representation, and aLEN-type tag for the packed representation.



Each field specifies which fields to try next. This allows the compiler to performfield scheduling, by carefully deciding which order to try fields in based both on their declaration order and a rough estimation of their “hotness”, much like branch scheduling happens in a program compiler. This avoids almost all of the work of looking up the next field in the common case, because we have already pre-loaded the correct guess.



I haven’t managed to nail down a good algorithm for this yet, but I am working on a system for implementing a type of “branch prediction” for PGO, that tries to provide better predictions for the next fields to try based on what has been seen before.



The offset information for a field is more than just a memory offset. Atdp.Offsetincludes a bit offset, for fields which request allocation of individual bits in the message’s bitfields. These are used to implement the hasbits ofoptionalfields (and the values ofboolfields). It also includes a byte offset for larger storage. However, this byte offset can be negative, in which case it’s actually an offset into thecold region.



In many messages, most fields won’t be set, particularly extensions. But we would like to avoid having to allocate memory for the very rare (i.e., “cold”) fields. For this, a special “cold region” exists in a separate allocation from the main message, which is referenced via a compressed pointer. If a message happens to need a cold field set, it takes a slow path to allocate a cold region only if needed. Whether a field is cold is a dynamic property that can be affected by PGO.



### The Parser VM



The parser is designed to make maximal use of Go’s generous ABI without spilling anything to the stack that isn’t absolutely necessary. The parser state consists of eight 64-bit integers, split across two types:vm.P1andvm.P2. Unfortunately, these can’t be merged due to acompiler bug, as documented invm/vm.go.



Every parser function takes these two structs as its first two arguments, and returns them as its first two results. This ensures that register allocation tries its darnedest to keep those eight integers in the first eight argument registers, even across calls. This leads to the common idiom of


var

n

int

p1
,

p2
,

n

=

DoSomething
(
p1
,

p2
)
Go


Overwriting the parser state like this ensures that future uses of p1 and p2 use the values thatDoSomethingplaces in registers for us.



I spent a lot of time and a lot of profiling catching all of the places where Go would incorrectly spill parser state to the stack, which would result in stalls. I found quite a few codegen bugs in the process. Particularly notable (and shocking!) is#73589. Go has somehow made it a decade without a very basic pointer-to-SSA lifting pass (for comparison, this is a heavy-lifting cleanup pass (mem2reg) in LLVM).



The core loop of the VM goes something like this:


1. Are we out of bytes to parse? If so, pop a parser stack frame5. If we popped the last stack frame, parsing is done; return success.
2. Parse a tag. This does not fully decode the tag, becausetdp.FieldParsers contain a carefully-formatted, partially-decoded tag to reduce decoding work.
3. Check if the next field we would parse matches the tag.If yes, call the function pointertdp.Field.Parser; update the current field totdp.Field.NextOk; goto 1.If no, update the current field totdp.Field.NextErr; goto 3.If no “enough times”, fall through.
4. If yes, call the function pointertdp.Field.Parser; update the current field totdp.Field.NextOk; goto 1.
5. If no, update the current field totdp.Field.NextErr; goto 3.
6. If no “enough times”, fall through.
7. Slow path: hittdp.Field.Tagsto find the matching field for that tag.If matched, go to 3a.If not, this is an unknown field; put it into the unknown field set; parse a tag and goto 4.
8. If matched, go to 3a.
9. If not, this is an unknown field; put it into the unknown field set; parse a tag and goto 4.


Naturally, this is implemented as a single function whose control flow consists exclusively ofifs andgotos, because getting Go to generate good control flow otherwise proved too hard.



Now, you might be wondering why the hot loop for the parser includescalling a virtual function. Conventional wisdom holds that virtual calls are slow. After all, the actual virtual call instruction is quite slow, because it’s an indirect branch, meaning that it can easily stall the CPU. However, it’s actuallymuch faster than the alternativesin this case, due to a few quirks of our workload and how modern CPUs are designed:


1. Modern CPUs are notgreatat traversing complex “branch mazes”. This means that selecting one of ~100 alternatives using branches, even if they are well-predicted and you use unrolled binary search, is still likely to result in frequent mispredictions, and is an obstacle to other JIT optimizations in the processor’s backend.
2. Predicting a single indirect branch with dozens of popular targetsissomething modern CPUs are pretty good at. Chips and Cheese have agreat writeupon the indirect prediction characteristics of Zen 4 chips.


In fact, the “optimized” form of a large switch is a jump table, which is essentially an array of function pointers. Rather than doing a large number of comparisons and direct branches, a jump table turns a switch into a load and an indirect branch.



This is great news for us, because it means we can make use of a powerful assumption about most messages: most messages only feature a handful of field archetypes. How often is it that you see a message which has more in it thanint32,int64,string, and submessages? In effect, this allows us to have a very large “instruction set”, consisting of all of the different field archetypes, but a particular message only pays for what it uses. The fewer archetypes it usesat runtime, the better the CPU can predict this indirect jump.



On the other hand, we can just keep adding archetypes over time to specialize for common parse workloads, which PGO can select for. Adding new archetypes that are not used by most messages does not incur a performance penalty.



## Other Optimizations



We’ve already discussed the hot/cold split, and briefly touched on the message bitfields used forbools and hasbits. I’d like to mention a few other cool optimizations that help cover all our bases, as far as high-performance parsing does.



### Zerocopy Strings



The fastestmemcpyimplementation is the one you don’t call. For this reason, we try to, whenever possible, avoid copying anything out of the input buffer.strings andbytesare represented aszc.Ranges, which are a packed pair of offset+length in auint64. Protobuf is not able to handle lengths greater than 2GB properly, so we can assume that this covers all the data we could ever care about. This means that abytesfield is 8 bytes, rather than 24, in our representation.



Zerocopy is also used for packed fields. For example, arepeated doublewill typically be encoded as aLENrecord. The number offloat64s in this record is equal to its length divided by 8, and thefloat64s are already encoded in IEEE754 format for us. So we can just retain the whole repeated fields as azc.Range. Of course, we need to be able to handle cases where there are multiple disjoint records, so the backingrepeated.Scalarscan also function as a 24-byte arena slice. Being able to switch between these modes gracefully is a delicate and carefully-tested part of the repeated field thunks.



Surprisingly, we also use zerocopy for varint fields, such asrepeated int32. Varints are variable-length, so we can’t just index directly into the packed buffer to get thenth element… unless all of the elements happen to be the same size. In the case that every varint is one byte (so, between 0 and 127), we can zerocopy the packed field. This is a relatively common scenario, too, so it results in big savings6. Wealreadycount the number of varints in the packed field in order to preallocate space for it, so this doesn’t add extra cost. This counting is very efficient because I have manually vectorized the loop.



### Repeated Preloads



PGO records the median size of each repeated/map field, and that is used to calculate a “preload” for each repeated field. Whenever the field is first allocated, it is pre-allocated using the preload to try to right-size the field with minimal waste.



Using the median ensures that large outliers don’t result in huge memory waste; instead, this guarantees that at least 50% of repeated fields will only need to allocate from the arena once. Packed fields don’t use the preload, since in the common case only one record appears for packed fields. This mostly benefits string- and message-typed repeated fields, which can’t be packed.



### Map Optimizations



We don’t use Go’s built-in map, because it has significant overhead in some cases: in particular, it has to support Go’s mutation-during-iteration semantics, as well as deletion. Although both are Swisstables7under the hood, my implementation can afford to take a few shortcuts. It also allows our implementation to use arena-managed memory.swiss.Tablesare used both for the backing store ofmapfields, and for maps inside oftdp.Types.



Currently, the hash used is the variant offxhash used by the Rust compiler. This greatly out-performs Go’smaphashfor integers, but maphash is better for larger strings. I hope to maybe switch to maphash at some point for large strings, but it hasn’t been a priority.



### Arena Reuse



Hitting the Go allocator is always going to be a little slow, because it’s a general-case allocator. Ideally, we should learn the estimated memory requirements for a particular workload, and then allocate a single block of that size for the arena to portion out.



The best way to do this is viaarena reuseIn the context of a service, each request has a bounded lifetime on the message that it parses. Once that lifetime is over (the request is complete), the message is discarded. This gives the programmer an opportunity toresetthe backing arena, so that it keeps its largest memory block for re-allocation.



You can show that over time, this will cause the arena to never hit the Go allocator. If the largest block is too small for a message, a block twice as large will wind up getting allocated. Messages that use the same amount of memory will keep doubling the largest block, until the largest block is large enough to fit the whole message. Memory usage will be at worst 2x the size of this message. Note that, thanks to extensive use of zero-copy optimizations, we can often avoid allocating memory for large portions of the message.



Of course, arena re-use poses a memory safety danger, if the previously allocated message is kept around after the arena is reset. For this reason, it’s not the default behavior. Using arena resets is a double-digit percentage improvement, however.



### Oneof Unions



Go does not properly support unions, because the GC does not keep the necessary book-keeping to distinguish a memory location that may be an integerora pointer at runtime. Instead, this gets worked around using interfaces, which is always a pointer to some memory. Go’s GC can handle untyped pointers just fine, so this just works.



The generated API for Protobuf Go uses interface values foroneofs. This API is… pretty messy to use, unfortunately, and triggers unnecessary allocations, (much likeoptionalfields do in the open API).



However, my arena design (read about it here) makes it possible to store arena pointers on the arena as if they are integers, since the GC does not need to scan through arena memory. Thus, ouroneofs are true unions, like in C++.



## Conclusion



hyperpbis really exciting because its growing JIT capabilities offer an improvement in the state of the art over UPB. It’s also been a really fun challenge working around Go compiler bugs to get the best assembly possible. The code is already so well-optimized that re-building the benchmarks with the Go compiler’s own PGO mode (based on a profile collected from the benchmarks) didn’t really seem to move the needle!



I’m always working on makinghyperpbbetter (I get paid for it!) and I’m always excited to try new optimizations. If you think of something, file an issue! I have meticulously commented most things withinhyperpb, so it should be pretty easy to get an idea of where things are if you want to contribute.



I would like to write more posts diving into some of the weeds of the implementation. I can’t promise anything, but there’s lots to talk about. For now… have fun source-diving!



There’s a lot of other things we could be doing: for example, we could be using SIMD to parse varints, we could have smarter parser scheduling, we could be allocating small submessages inline to improve locality… there’s still so much we can do!



And most importantly, I hope you’ve learned something new about performance optimization!



1. vtprotobuf getsa lotof things wrong that make it beat us in like two benchmarks, because it’ssosloppy. For example, vtprotobuf believes that it’s ok to not validate UTF-8 strings. This isnon-conformingbehavior. It also believes that map entries’ fields are always in order and always populated, meaning that valid Protobuf messages containing maps can be parsedincorrectly. This sloppiness is unacceptable, which is whyhyperpbgoes to great lengths to implement all of Protobuf correctly.↩
2. Never gonna let Rob live that one down. Of all of Rob’s careless design decisions, the assembler is definitely one of the least forgivable ones.↩
3. There are only really two pieces of code inhyperpbthat could benefit from hand-written assembly: varint decoding and UTF-8 validation. Both of these vectorize well, however,ABI0is so inefficient that no hand-written implementation will be faster.If I do wind up doing this, it will require a build tag likehyperasm, along with something like-gcflags=buf.build/go/hyperpb/internal/asm/...=-+to treat the assembly implementations as part of the Go runtime, allowing the use ofABIInternal. But even then, this only speeds up parsing of large (>2 byte) varints.↩
4. This is PGO performed byhyperpbitself; this is unrelated togc’s own PGO mode, which seems to not actually makehyperpbfaster.↩
5. Yes, the parser manages its own stack separate from the goroutine stack. This ensures that nothing in the parser has to be reentrant. The only time the stack is pushed to is when we “recurse” into a submessage.↩
6. Large packed repeated fields are where the biggest wins are for us. Being able to zero-copy large packedint32fields full of small values allows us to eliminate all of the overhead that the other runtimes are paying for; we also choose different parsing strategies depending on the byte-to-varint ratio of the record.Throughput for various repeated field benchmarks. This excludes therepeated fixed32benchmarks, since those achieve such high throughputs (~20 Gbps) that they make the chart unreadable.These optimizations account for the performance difference betweendescriptor/#00anddescriptor/#01in the first benchmark chart. The latter is aFileDescriptorSetcontainingSourceCodeInfo, Protobuf’s janky debuginfo format. It is dominated byrepeated int32fields.NB: This chart is currently missing the Y-axis, I need to have it re-made.↩
7. Map parsing performance has been a bit of a puzzle.vtprotobufcheats by rejecting some valid map entry encodings, such as (in Protoscope){1: {"key"}}(value is implied to be""), while mis-parsing others, such as{2: {"value"} 1: {"key"}}(fields can go in any order), since they don’t actually validate the field numbers likehyperpbdoes.Here’s where the benchmarks currently stand for maps:Throughput for various map parsing benchmarks.Maps, I’m told, are not very popular in Protobuf, so they’re not something I have tried to optimize as hard as packed repeated fields.↩





## Related Posts










2025-07-16

•

4119

words

•

45

minutes


•

#go

•

#dark-arts

•

#protobuf



# ParsingProtobufLikeNeverBefore





HistoricallyIhaveworkedonmanyprojectsrelatedtohigh-performanceProtobuf,bethatontheC++runtime,ontheRustruntime,oronintegratingUPB,thefastestProtobufruntime,writtenbymycolleagueJoshHaberman.Igenerallydon’tpostdirectlyaboutmycurrentjob,butmymostrecenttoy-turned-productissomethingI’mveryexcitedtowriteabout:hyperpb.



Here’showwemeasureupagainstotherGoProtobufparsers.Thisisasubsetofmybenchmarks,sincethebenchmarksuitecontainsmanydozensofspecimens.ThiswasrecordedonanAMDZen4machine.






Throughputforvariousconfigurationsofhyperpb(coloredbars)vs.competingparsers(greybars).Eachsuccessivehyperpbincludesallpreviousoptimizations,correspondingtozerocopymode,arenareuse,andprofile-guidedoptimization.Biggerisbetter.





Traditionally,Protobufbackendswouldgenerateparsersbygeneratingsourcecodespecializedtoeachtype.Naively,thiswouldgivethebestperformance,becauseeverythingwouldbe“right-sized”toaparticularmessagetype.Unfortunately,nowthatweknowbetter,thereareabunchofdrawbacks:


1. Everytypeyoucareaboutmustbecompiledahead-of-time.Trickyforwhenyouwanttobuildsomethinggenericoverschemasyourusersprovideyou.
2. Everytypecontributestoacostontheinstructioncache,meaningthatifyourprogramparsesalotofdifferenttypes,itwillessentiallyflushyourinstructioncacheanytimeyouenteraparser.Worsestill,ifaparseinvolvesenoughtypes,theparseritselfwillhitinstructiondecodingthroughputissues.


Theseeffectsarenotdirectlyvisibleinnormalworkloads,butotherside-effectsarevisible:forexample,giantswitchesonfieldnumberscanturnintochainsofbranchinstructions,meaningthathigher-numberedfieldswillbequiteslow.Evenbinary-searchingonfieldnumbersisn’texactlyideal.However,weknowthateveryProtobufcodeceveremitsfieldsinindexorder(i.e.,declarationorderinthe.protofile),whichisadataconditioningfactwedon’ttakeadvantageofwithaswitch.



UPBsolvesthisproblem.ItisasmallCkernelforparsingProtobufmessages,whichiscompletelydynamic:aUPB“parser”isactuallyacollectionofdatatablesthatareevaluatedbyatable-drivenparser.Inotherwords,aUPBparserisactuallyconfigurationforaninterpreterVM,whichexecutesProtobufmessagesasitsbytecode.UPBalsocontainsmanyarenaoptimizationstoimproveallocationthroughputwhenparsingcomplexmessages.



hyperpbisabrandnewlibrary,writteninthemostcursedGoimaginable,whichbringsmanyoftheoptimizationsofUPBtoGo,andmanynewones,whilebeingtunedtoGo’sownweirdneeds.Theresultleavesthecompetitioninthedustinvirtuallyeverybenchmark,whilebeingcompletelyruntime-dynamic.Thismeansit’sfasterthanProtobufGo’sowngeneratedcode,andvtprotobuf(apopularbutnon-conforming1parsergeneratorforGo).



Thispostisaboutsomeoftheinternalsofhyperpb.Ihavealsopreparedamoresales-eywriteup,whichyoucanreadontheBufblog.



## WhyReinventUPB?



UPBisawesome.ItcansloteasilyintoanylanguagethathasCFFI,whichisbasicallyeverylanguageever.



Unfortunately,Go’sCFFIisreally,reallybad.It’shardtooverstatehowbadcgois.Thereisn’tagoodwaytocooperatewithConmemoryallocation(Ccan’treallyhandleGomemorywithoutalotofproblems,duetotheGC).HavingCmemorygetcleanedupbytheGCrequiresfinalizers,whichareveryslow.CallingintoCisveryslow,becauseGopessimisticallyassumesthatCrequiresalargestack,andalsocallingintoCdoesnastythingstothescheduler.



Allofthesethingscanbeworkedaround,ofcourse.ForawhileIconsideredcompilingUPBtoassembly,andrewritingthatassemblyintoGo’sawfulassemblysyntax2,andthenhavingGoassembleUPBoutofthat.Thispresentsafewissuesthough,particularlybecauseGo’sassemblycallingconventionisstillinthestoneage3(argumentsarepassedonthestack),andbecausewewouldstillneedtodoalotofworktogetUPBtomatchtheprotoreflectAPI.



Goalsohasafew…uniquequalitiesthatmakewritingaProtobufinterpreteraninterestingchallengewithexcitingoptimizationopportunities.



First,ofcourse,istheregisterABI,whichonx86_64givesusawhoppingnineargumentandreturnregisters,meaningthatwecansimplypasstheentireparserstateinregistersallthetime.



SecondisthatGodoesnothavemuchUBtospeakof,sowecangetawaywithalotofveryevilpointercrimesthatwecouldnotinC++orRust.



ThirdisthatProtobufGohasarobustreflectionsystemthatwecantargetifwedesignspecificallyforit.



Also,theGoecosystemseemsmuchmoretolerantofless-than-idealstartuptimes(becausethelanguageloveslife-before-mainduetoinit()functions),sounlikeUPB,wecanrequirethattheinterpreter’sprogrambegeneratedatruntime,meaningthatwecandesignforonlinePGO.Inotherwords,wehavetheperfectstormtocreatethefirst-everProtobufJITcompiler(whichwealsorefertoas“onlinePGO”or“real-timePGO”).



## hyperpb’sAPI



Rightnow,hyperpb’sAPIisverysimple.Therearehyperpb.Compile*functionsthatacceptsomerepresentationofamessagedescriptor,andreturna*hyperpb.MessageType,whichimplementstheprotoreflecttypeAPIs.Thiscanbeusedtoallocateanew*hyperpb.Message,whichyoucanshoveintoproto.Unmarshalanddoreflectionontheresult.However,youcan’tmutate*hyperpb.Messagescurrently,becausethemainuse-casesIamoptimizingforareread-only.Allmutationspanicinstead.



Theherouse-case,usingBuf’sprotovalidatelibrary,usesreflectiontoexecutevalidationpredicates.Itlookslikethis:



//

Compile

a

new

message

type,

deserializing

an

encoded

FileDescriptorSet.

msgType

:=

hyperpb
.
CompileForBytes
(
schema
,

"my.api.v1.Request"
)

//

Allocate

a

new

message

of

that

type.

msg

:=

hyperpb
.
NewMessage
(
msgType
)

//

Unmarshal

like

you

would

any

other

message,

using

proto.Unmarshal.

if

err

:=

proto
.
Unmarshal
(
data
,

msg
);

err

!=

nil

{


//

Handle

parse

failure.

}

//

Validate

the

message.

Protovalidate

uses

reflection,

so

this

Just

Works.

if

err

:=

protovalidate
.
Validate
(
msg
);

err

!=

nil

{


//

Handle

validation

failure.

}
Go



Wetelluserstomakesuretocachethecompilationstepbecausecompilationcanbearbitrarilyslow:it’sanoptimizingcompiler!Thisisnotunlikethesamewarningonregexp.Compile,whichmakesiteasytoteachusershowtousethisAPIcorrectly.



InadditiontothemainAPI,there’sabunchofperformancetuningknobsforthecompiler,forunmarshaling,andforrecordingprofiles.Typescanberecompiledusingarecordedprofiletobemoreoptimizedforthekindsofmessagesthatactuallycomeonthewire.hyperpbPGO4affectsanumberofthingsthatwe’llgetintoasIdiveintotheimplementationdetails.



## TheGuts



Mostofthecoreimplementationlivesunderinternal/tdp.Themaincomponentsareasfollows:


1. tdp,whichdefinesthe“objectcodeformat”fortheinterpreter.Thisincludesdefinitionsfordescribingtypesandfieldstotheparser.
2. tdp/compiler,whichcontainsallofthecodeforconvertingaprotoreflect.MessageDescriptorintoatdp.Library,whichcontainsallofthetypesrelevanttoaparticularparsingoperation.
3. tdp/dynamicdefineswhatdynamicmessagetypeslooklike.Thecompilerdoesabunchoflayoutworkthatgetsstoredintdp.Typevalues,whichadynamic.Messageinterpretstofindtheoffsetsoffieldswithinitself.
4. tdp/vmcontainsthecoreinterpreterimplementation,includingtheVMstatethatispassedinregisterseverywhere.Italsoincludeshand-optimizedroutinesforparsingvarintsandvalidatingUTF-8.
5. tdp/thunksdefinesarchetypes,whichareclassesoffieldsthatallusethesamelayoutandparsers.Thiscorrespondsroughlytoa(presence,kind)pair,butnotexactly.Therearearound200differentarchetypes.


Thisarticlewon’tbeadeep-diveintoeverythingintheparser,andeventhisexcludeslargeportionsofhyperpb.Forexample,theinternal/arenapackageisalreadydescribedinadifferentblogpostofmine.IrecommendtakingalookatthattolearnabouthowweimplementaGC-friendlyarenaforhyperpb.



Instead,Iwillgiveabriefoverviewofhowtheobjectcodeisorganizedandhowtheparserinterpretsit.Iwillalsogooverafewofthemoreinterestingoptimizationswehave.



### tdp.Type



EveryMessageDescriptorthatisreachablefromtherootmessage(eitherasafieldorasanextension)becomesatdp.Type.Thiscontainsthedynamicsizeofthecorrespondingmessagetype,apointertothetype’sdefaultparser(therecanbemorethanoneparserforatype)andavariablenumberoftdp.Fieldvalues.Thesespecifytheoffsetofeachfieldandprovideaccessorthunks,foractuallyextractingthevalueofthefield.



Atdp.TypeParseriswhattheparserVMinterpretsalongsideencodedProtobufdata.Itcontainsalloftheinformationneededfordecodingamessageincompactform,includingtdp.FieldParsersforeachofitsfields(andextensions),aswellasahashtableforlookingupafieldbytag,whichisusedbytheVMasafallback.



Thetdp.FieldParserseachcontain:


1. Thesameoffsetinformationasatdp.Field.
2. Thefield’stag,inaspecialformat.
3. Afunctionpointerthatgetscalledtoparsethefield.
4. Thenextfield(s)totryparsingafterthisoneisparsed.


Eachtdp.FieldParseractuallycorrespondstoapossibletagonarecordforthismessage.Somefieldshavemultipledifferenttags:forexample,arepeatedint32canhaveaVARINT-typetagfortherepeatedrepresentation,andaLEN-typetagforthepackedrepresentation.



Eachfieldspecifieswhichfieldstotrynext.Thisallowsthecompilertoperformfieldscheduling,bycarefullydecidingwhichordertotryfieldsinbasedbothontheirdeclarationorderandaroughestimationoftheir“hotness”,muchlikebranchschedulinghappensinaprogramcompiler.Thisavoidsalmostalloftheworkoflookingupthenextfieldinthecommoncase,becausewehavealreadypre-loadedthecorrectguess.



Ihaven’tmanagedtonaildownagoodalgorithmforthisyet,butIamworkingonasystemforimplementingatypeof“branchprediction”forPGO,thattriestoprovidebetterpredictionsforthenextfieldstotrybasedonwhathasbeenseenbefore.



Theoffsetinformationforafieldismorethanjustamemoryoffset.Atdp.Offsetincludesabitoffset,forfieldswhichrequestallocationofindividualbitsinthemessage’sbitfields.Theseareusedtoimplementthehasbitsofoptionalfields(andthevaluesofboolfields).Italsoincludesabyteoffsetforlargerstorage.However,thisbyteoffsetcanbenegative,inwhichcaseit’sactuallyanoffsetintothecoldregion.



Inmanymessages,mostfieldswon’tbeset,particularlyextensions.Butwewouldliketoavoidhavingtoallocatememoryfortheveryrare(i.e.,“cold”)fields.Forthis,aspecial“coldregion”existsinaseparateallocationfromthemainmessage,whichisreferencedviaacompressedpointer.Ifamessagehappenstoneedacoldfieldset,ittakesaslowpathtoallocateacoldregiononlyifneeded.WhetherafieldiscoldisadynamicpropertythatcanbeaffectedbyPGO.



### TheParserVM



TheparserisdesignedtomakemaximaluseofGo’sgenerousABIwithoutspillinganythingtothestackthatisn’tabsolutelynecessary.Theparserstateconsistsofeight64-bitintegers,splitacrosstwotypes:vm.P1andvm.P2.Unfortunately,thesecan’tbemergedduetoacompilerbug,asdocumentedinvm/vm.go.



Everyparserfunctiontakesthesetwostructsasitsfirsttwoarguments,andreturnsthemasitsfirsttworesults.Thisensuresthatregisterallocationtriesitsdarnedesttokeepthoseeightintegersinthefirsteightargumentregisters,evenacrosscalls.Thisleadstothecommonidiomof



var

n

int

p1
,

p2
,

n

=

DoSomething
(
p1
,

p2
)
Go



Overwritingtheparserstatelikethisensuresthatfutureusesofp1andp2usethevaluesthatDoSomethingplacesinregistersforus.



IspentalotoftimeandalotofprofilingcatchingalloftheplaceswhereGowouldincorrectlyspillparserstatetothestack,whichwouldresultinstalls.Ifoundquiteafewcodegenbugsintheprocess.Particularlynotable(andshocking!)is#73589.Gohassomehowmadeitadecadewithoutaverybasicpointer-to-SSAliftingpass(forcomparison,thisisaheavy-liftingcleanuppass(mem2reg)inLLVM).



ThecoreloopoftheVMgoessomethinglikethis:


1. Areweoutofbytestoparse?Ifso,popaparserstackframe5.Ifwepoppedthelaststackframe,parsingisdone;returnsuccess.
2. Parseatag.Thisdoesnotfullydecodethetag,becausetdp.FieldParserscontainacarefully-formatted,partially-decodedtagtoreducedecodingwork.
3. Checkifthenextfieldwewouldparsematchesthetag.Ifyes,callthefunctionpointertdp.Field.Parser;updatethecurrentfieldtotdp.Field.NextOk;goto1.Ifno,updatethecurrentfieldtotdp.Field.NextErr;goto3.Ifno“enoughtimes”,fallthrough.
4. Ifyes,callthefunctionpointertdp.Field.Parser;updatethecurrentfieldtotdp.Field.NextOk;goto1.
5. Ifno,updatethecurrentfieldtotdp.Field.NextErr;goto3.
6. Ifno“enoughtimes”,fallthrough.
7. Slowpath:hittdp.Field.Tagstofindthematchingfieldforthattag.Ifmatched,goto3a.Ifnot,thisisanunknownfield;putitintotheunknownfieldset;parseatagandgoto4.
8. Ifmatched,goto3a.
9. Ifnot,thisisanunknownfield;putitintotheunknownfieldset;parseatagandgoto4.


Naturally,thisisimplementedasasinglefunctionwhosecontrolflowconsistsexclusivelyofifsandgotos,becausegettingGotogenerategoodcontrolflowotherwiseprovedtoohard.



Now,youmightbewonderingwhythehotloopfortheparserincludescallingavirtualfunction.Conventionalwisdomholdsthatvirtualcallsareslow.Afterall,theactualvirtualcallinstructionisquiteslow,becauseit’sanindirectbranch,meaningthatitcaneasilystalltheCPU.However,it’sactuallymuchfasterthanthealternativesinthiscase,duetoafewquirksofourworkloadandhowmodernCPUsaredesigned:


1. ModernCPUsarenotgreatattraversingcomplex“branchmazes”.Thismeansthatselectingoneof~100alternativesusingbranches,eveniftheyarewell-predictedandyouuseunrolledbinarysearch,isstilllikelytoresultinfrequentmispredictions,andisanobstacletootherJIToptimizationsintheprocessor’sbackend.
2. PredictingasingleindirectbranchwithdozensofpopulartargetsissomethingmodernCPUsareprettygoodat.ChipsandCheesehaveagreatwriteupontheindirectpredictioncharacteristicsofZen4chips.


Infact,the“optimized”formofalargeswitchisajumptable,whichisessentiallyanarrayoffunctionpointers.Ratherthandoingalargenumberofcomparisonsanddirectbranches,ajumptableturnsaswitchintoaloadandanindirectbranch.



Thisisgreatnewsforus,becauseitmeanswecanmakeuseofapowerfulassumptionaboutmostmessages:mostmessagesonlyfeatureahandfuloffieldarchetypes.Howoftenisitthatyouseeamessagewhichhasmoreinitthanint32,int64,string,andsubmessages?Ineffect,thisallowsustohaveaverylarge“instructionset”,consistingofallofthedifferentfieldarchetypes,butaparticularmessageonlypaysforwhatituses.Thefewerarchetypesitusesatruntime,thebettertheCPUcanpredictthisindirectjump.



Ontheotherhand,wecanjustkeepaddingarchetypesovertimetospecializeforcommonparseworkloads,whichPGOcanselectfor.Addingnewarchetypesthatarenotusedbymostmessagesdoesnotincuraperformancepenalty.



## OtherOptimizations



We’vealreadydiscussedthehot/coldsplit,andbrieflytouchedonthemessagebitfieldsusedforboolsandhasbits.I’dliketomentionafewothercooloptimizationsthathelpcoverallourbases,asfarashigh-performanceparsingdoes.



### ZerocopyStrings



Thefastestmemcpyimplementationistheoneyoudon’tcall.Forthisreason,wetryto,wheneverpossible,avoidcopyinganythingoutoftheinputbuffer.stringsandbytesarerepresentedaszc.Ranges,whichareapackedpairofoffset+lengthinauint64.Protobufisnotabletohandlelengthsgreaterthan2GBproperly,sowecanassumethatthiscoversallthedatawecouldevercareabout.Thismeansthatabytesfieldis8bytes,ratherthan24,inourrepresentation.



Zerocopyisalsousedforpackedfields.Forexample,arepeateddoublewilltypicallybeencodedasaLENrecord.Thenumberoffloat64sinthisrecordisequaltoitslengthdividedby8,andthefloat64sarealreadyencodedinIEEE754formatforus.Sowecanjustretainthewholerepeatedfieldsasazc.Range.Ofcourse,weneedtobeabletohandlecaseswheretherearemultipledisjointrecords,sothebackingrepeated.Scalarscanalsofunctionasa24-bytearenaslice.Beingabletoswitchbetweenthesemodesgracefullyisadelicateandcarefully-testedpartoftherepeatedfieldthunks.



Surprisingly,wealsousezerocopyforvarintfields,suchasrepeatedint32.Varintsarevariable-length,sowecan’tjustindexdirectlyintothepackedbuffertogetthenthelement…unlessalloftheelementshappentobethesamesize.Inthecasethateveryvarintisonebyte(so,between0and127),wecanzerocopythepackedfield.Thisisarelativelycommonscenario,too,soitresultsinbigsavings6.Wealreadycountthenumberofvarintsinthepackedfieldinordertopreallocatespaceforit,sothisdoesn’taddextracost.ThiscountingisveryefficientbecauseIhavemanuallyvectorizedtheloop.



### RepeatedPreloads



PGOrecordsthemediansizeofeachrepeated/mapfield,andthatisusedtocalculatea“preload”foreachrepeatedfield.Wheneverthefieldisfirstallocated,itispre-allocatedusingthepreloadtotrytoright-sizethefieldwithminimalwaste.



Usingthemedianensuresthatlargeoutliersdon’tresultinhugememorywaste;instead,thisguaranteesthatatleast50%ofrepeatedfieldswillonlyneedtoallocatefromthearenaonce.Packedfieldsdon’tusethepreload,sinceinthecommoncaseonlyonerecordappearsforpackedfields.Thismostlybenefitsstring-andmessage-typedrepeatedfields,whichcan’tbepacked.



### MapOptimizations



Wedon’tuseGo’sbuilt-inmap,becauseithassignificantoverheadinsomecases:inparticular,ithastosupportGo’smutation-during-iterationsemantics,aswellasdeletion.AlthoughbothareSwisstables7underthehood,myimplementationcanaffordtotakeafewshortcuts.Italsoallowsourimplementationtousearena-managedmemory.swiss.Tablesareusedbothforthebackingstoreofmapfields,andformapsinsideoftdp.Types.



Currently,thehashusedisthevariantoffxhashusedbytheRustcompiler.Thisgreatlyout-performsGo’smaphashforintegers,butmaphashisbetterforlargerstrings.Ihopetomaybeswitchtomaphashatsomepointforlargestrings,butithasn’tbeenapriority.



### ArenaReuse



HittingtheGoallocatorisalwaysgoingtobealittleslow,becauseit’sageneral-caseallocator.Ideally,weshouldlearntheestimatedmemoryrequirementsforaparticularworkload,andthenallocateasingleblockofthatsizeforthearenatoportionout.



ThebestwaytodothisisviaarenareuseInthecontextofaservice,eachrequesthasaboundedlifetimeonthemessagethatitparses.Oncethatlifetimeisover(therequestiscomplete),themessageisdiscarded.Thisgivestheprogrammeranopportunitytoresetthebackingarena,sothatitkeepsitslargestmemoryblockforre-allocation.



Youcanshowthatovertime,thiswillcausethearenatoneverhittheGoallocator.Ifthelargestblockistoosmallforamessage,ablocktwiceaslargewillwindupgettingallocated.Messagesthatusethesameamountofmemorywillkeepdoublingthelargestblock,untilthelargestblockislargeenoughtofitthewholemessage.Memoryusagewillbeatworst2xthesizeofthismessage.Notethat,thankstoextensiveuseofzero-copyoptimizations,wecanoftenavoidallocatingmemoryforlargeportionsofthemessage.



Ofcourse,arenare-useposesamemorysafetydanger,ifthepreviouslyallocatedmessageiskeptaroundafterthearenaisreset.Forthisreason,it’snotthedefaultbehavior.Usingarenaresetsisadouble-digitpercentageimprovement,however.



### OneofUnions



Godoesnotproperlysupportunions,becausetheGCdoesnotkeepthenecessarybook-keepingtodistinguishamemorylocationthatmaybeanintegerorapointeratruntime.Instead,thisgetsworkedaroundusinginterfaces,whichisalwaysapointertosomememory.Go’sGCcanhandleuntypedpointersjustfine,sothisjustworks.



ThegeneratedAPIforProtobufGousesinterfacevaluesforoneofs.ThisAPIis…prettymessytouse,unfortunately,andtriggersunnecessaryallocations,(muchlikeoptionalfieldsdointheopenAPI).



However,myarenadesign(readaboutithere)makesitpossibletostorearenapointersonthearenaasiftheyareintegers,sincetheGCdoesnotneedtoscanthrougharenamemory.Thus,ouroneofsaretrueunions,likeinC++.



## Conclusion



hyperpbisreallyexcitingbecauseitsgrowingJITcapabilitiesofferanimprovementinthestateoftheartoverUPB.It’salsobeenareallyfunchallengeworkingaroundGocompilerbugstogetthebestassemblypossible.Thecodeisalreadysowell-optimizedthatre-buildingthebenchmarkswiththeGocompiler’sownPGOmode(basedonaprofilecollectedfromthebenchmarks)didn’treallyseemtomovetheneedle!



I’malwaysworkingonmakinghyperpbbetter(Igetpaidforit!)andI’malwaysexcitedtotrynewoptimizations.Ifyouthinkofsomething,fileanissue!Ihavemeticulouslycommentedmostthingswithinhyperpb,soitshouldbeprettyeasytogetanideaofwherethingsareifyouwanttocontribute.



Iwouldliketowritemorepostsdivingintosomeoftheweedsoftheimplementation.Ican’tpromiseanything,butthere’slotstotalkabout.Fornow…havefunsource-diving!



There’salotofotherthingswecouldbedoing:forexample,wecouldbeusingSIMDtoparsevarints,wecouldhavesmarterparserscheduling,wecouldbeallocatingsmallsubmessagesinlinetoimprovelocality…there’sstillsomuchwecando!



Andmostimportantly,Ihopeyou’velearnedsomethingnewaboutperformanceoptimization!



1. vtprotobufgetsalotofthingswrongthatmakeitbeatusinliketwobenchmarks,becauseit’ssosloppy.Forexample,vtprotobufbelievesthatit’soktonotvalidateUTF-8strings.Thisisnon-conformingbehavior.Italsobelievesthatmapentries’fieldsarealwaysinorderandalwayspopulated,meaningthatvalidProtobufmessagescontainingmapscanbeparsedincorrectly.Thissloppinessisunacceptable,whichiswhyhyperpbgoestogreatlengthstoimplementallofProtobufcorrectly.↩
2. NevergonnaletRoblivethatonedown.OfallofRob’scarelessdesigndecisions,theassemblerisdefinitelyoneoftheleastforgivableones.↩
3. Thereareonlyreallytwopiecesofcodeinhyperpbthatcouldbenefitfromhand-writtenassembly:varintdecodingandUTF-8validation.Bothofthesevectorizewell,however,ABI0issoinefficientthatnohand-writtenimplementationwillbefaster.IfIdowindupdoingthis,itwillrequireabuildtaglikehyperasm,alongwithsomethinglike-gcflags=buf.build/go/hyperpb/internal/asm/...=-+totreattheassemblyimplementationsaspartoftheGoruntime,allowingtheuseofABIInternal.Buteventhen,thisonlyspeedsupparsingoflarge(>2byte)varints.↩
4. ThisisPGOperformedbyhyperpbitself;thisisunrelatedtogc’sownPGOmode,whichseemstonotactuallymakehyperpbfaster.↩
5. Yes,theparsermanagesitsownstackseparatefromthegoroutinestack.Thisensuresthatnothingintheparserhastobereentrant.Theonlytimethestackispushedtoiswhenwe“recurse”intoasubmessage.↩
6. Largepackedrepeatedfieldsarewherethebiggestwinsareforus.Beingabletozero-copylargepackedint32fieldsfullofsmallvaluesallowsustoeliminatealloftheoverheadthattheotherruntimesarepayingfor;wealsochoosedifferentparsingstrategiesdependingonthebyte-to-varintratiooftherecord.Throughputforvariousrepeatedfieldbenchmarks.Thisexcludestherepeatedfixed32benchmarks,sincethoseachievesuchhighthroughputs(~20Gbps)thattheymakethechartunreadable.Theseoptimizationsaccountfortheperformancedifferencebetweendescriptor/#00anddescriptor/#01inthefirstbenchmarkchart.ThelatterisaFileDescriptorSetcontainingSourceCodeInfo,Protobuf’sjankydebuginfoformat.Itisdominatedbyrepeatedint32fields.NB:ThischartiscurrentlymissingtheY-axis,Ineedtohaveitre-made.↩
7. Mapparsingperformancehasbeenabitofapuzzle.vtprotobufcheatsbyrejectingsomevalidmapentryencodings,suchas(inProtoscope){1:{"key"}}(valueisimpliedtobe""),whilemis-parsingothers,suchas{2:{"value"}1:{"key"}}(fieldscangoinanyorder),sincetheydon’tactuallyvalidatethefieldnumberslikehyperpbdoes.Here’swherethebenchmarkscurrentlystandformaps:Throughputforvariousmapparsingbenchmarks.Maps,I’mtold,arenotverypopularinProtobuf,sothey’renotsomethingIhavetriedtooptimizeashardaspackedrepeatedfields.↩





## RelatedPosts
