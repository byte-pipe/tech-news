---
title: Ruby 4.0.0 Released | Ruby
url: https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/
site_name: hackernews_api
fetched_at: '2025-12-26T11:06:47.266549'
original_url: https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/
author: FBISurveillance
date: '2025-12-25'
description: We are pleased to announce the release of Ruby 4.0.0.Ruby 4.0 introduces “Ruby Box” and “ZJIT”, and adds many improvements.
tags:
- hackernews
- trending
---

# Ruby 4.0.0 Released

Posted bynaruseon 25 Dec 2025

We are pleased to announce the release of Ruby 4.0.0.
Ruby 4.0 introduces “Ruby Box” and “ZJIT”, and adds many improvements.

## Ruby Box

Ruby Box is a new (experimental) feature to provide separation about definitions. Ruby Box is enabled when an environment variableRUBY_BOX=1is specified. The class isRuby::Box.

Definitions loaded in a box are isolated in the box. Ruby Box can isolate/separate monkey patches, changes of global/class variables, class/module definitions, and loaded native/ruby libraries from other boxes.

Expected use cases are:

* Run test cases in box to protect other tests when the test case uses monkey patches to override something
* Run web app boxes in parallel to execute blue-green deployment on an app server in a Ruby process
* Run web app boxes in parallel to evaluate dependency updates for a certain period of time by checking response diff using Ruby code
* Used as the foundation (low-level) API to implement kind of “package” (high-level) API (it is not designed yet)

For the detail of “Ruby Box”, seeRuby::Box.
[Feature #21311] [Misc #21385]

## ZJIT

ZJIT is a new just-in-time (JIT) compiler, which is developed as the next generation of YJIT. You need Rust 1.85.0 or newer to build Ruby with ZJIT support, and ZJIT is enabled when--zjitis specified.

We’re building a new compiler for Ruby because we want to both raise the performance ceiling (bigger compilation unit size and SSA IR) and encourage more outside contribution (by becoming a more traditional method compiler). Seeour blog postfor more details.

ZJIT is faster than the interpreter, but not yet as fast as YJIT. We encourage you to experiment with ZJIT, but maybe hold off on deploying it in production for now. Stay tuned for Ruby 4.1 ZJIT.

## Ractor Improvements

Ractor, Ruby’s parallel execution mechanism, has received several improvements. A new class,Ractor::Port, was introduced to address issues related to message sending and receiving (seeour blog post). Additionally,Ractor.shareable_procmakes it easier to shareProcobjects between Ractors.

On the performance side, many internal data structures have been improved to significantly reduce contention on a global lock, unlocking better parallelism. Ractors also now share less internal data, resulting in less CPU cache contention when running in parallel.

Ractor was first introduced in Ruby 3.0 as an experimental feature. We aim to remove its “experimental” status next year.

## Language changes

* *nilno longer callsnil.to_a, similar to how**nildoes
not callnil.to_hash. [Feature #21047]
* Logical binary operators (||,&&,andandor) at the
beginning of a line continue the previous line, like fluent dot.
The following code examples are equal:ifcondition1&&condition2...endPreviously:ifcondition1&&condition2...endifcondition1&&condition2...end[Feature #20925]

## Core classes updates

Note: We’re only listing outstanding class updates.

* ArrayArray#rfindhas been added as a more efficient alternative toarray.reverse_each.find[Feature #21678]Array#findhas been added as a more efficient override ofEnumerable#find[Feature #21678]
* Array#rfindhas been added as a more efficient alternative toarray.reverse_each.find[Feature #21678]
* Array#findhas been added as a more efficient override ofEnumerable#find[Feature #21678]
* BindingBinding#local_variablesdoes no longer include numbered parameters.
Also,Binding#local_variable_get,Binding#local_variable_set, andBinding#local_variable_defined?reject to handle numbered parameters.
[Bug #21049]Binding#implicit_parameters,Binding#implicit_parameter_get, andBinding#implicit_parameter_defined?have been added to access
numbered parameters and “it” parameter. [Bug #21049]
* Binding#local_variablesdoes no longer include numbered parameters.
Also,Binding#local_variable_get,Binding#local_variable_set, andBinding#local_variable_defined?reject to handle numbered parameters.
[Bug #21049]
* Binding#implicit_parameters,Binding#implicit_parameter_get, andBinding#implicit_parameter_defined?have been added to access
numbered parameters and “it” parameter. [Bug #21049]
* EnumeratorEnumerator.producenow accepts an optionalsizekeyword argument
to specify the size of the enumerator. It can be an integer,Float::INFINITY, a callable object (such as a lambda), ornilto
indicate unknown size. When not specified, the size defaults toFloat::INFINITY.# Infinite enumeratorenum=Enumerator.produce(1,size:Float::INFINITY,&:succ)enum.size# => Float::INFINITY# Finite enumerator with known/computable sizeabs_dir=File.expand_path("./baz")# => "/foo/bar/baz"traverser=Enumerator.produce(abs_dir,size:->{abs_dir.count("/")+1}){raiseStopIterationifit=="/"File.dirname(it)}traverser.size# => 4[Feature #21701]
* Enumerator.producenow accepts an optionalsizekeyword argument
to specify the size of the enumerator. It can be an integer,Float::INFINITY, a callable object (such as a lambda), ornilto
indicate unknown size. When not specified, the size defaults toFloat::INFINITY.# Infinite enumeratorenum=Enumerator.produce(1,size:Float::INFINITY,&:succ)enum.size# => Float::INFINITY# Finite enumerator with known/computable sizeabs_dir=File.expand_path("./baz")# => "/foo/bar/baz"traverser=Enumerator.produce(abs_dir,size:->{abs_dir.count("/")+1}){raiseStopIterationifit=="/"File.dirname(it)}traverser.size# => 4[Feature #21701]
* ErrorHighlightWhen an ArgumentError is raised, it now displays code snippets for
both the method call (caller) and the method definition (callee).
[Feature #21543]test.rb:1:in 'Object#add': wrong number of arguments (given 1, expected 2) (ArgumentError)

 caller: test.rb:3
 | add(1)
 ^^^
 callee: test.rb:1
 | def add(x, y) = x + y
 ^^^
 from test.rb:3:in '<main>'
* When an ArgumentError is raised, it now displays code snippets for
both the method call (caller) and the method definition (callee).
[Feature #21543]test.rb:1:in 'Object#add': wrong number of arguments (given 1, expected 2) (ArgumentError)

 caller: test.rb:3
 | add(1)
 ^^^
 callee: test.rb:1
 | def add(x, y) = x + y
 ^^^
 from test.rb:3:in '<main>'
* FiberIntroduce support forFiber#raise(cause:)argument similar toKernel#raise. [Feature #21360]
* Introduce support forFiber#raise(cause:)argument similar toKernel#raise. [Feature #21360]
* Fiber::SchedulerIntroduceFiber::Scheduler#fiber_interruptto interrupt a fiber with a
given exception. The initial use case is to interrupt a fiber that is
waiting on a blocking IO operation when the IO operation is closed.
[Feature #21166]IntroduceFiber::Scheduler#yieldto allow the fiber scheduler to
continue processing when signal exceptions are disabled.
[Bug #21633]Reintroduce theFiber::Scheduler#io_closehook for asynchronousIO#close.InvokeFiber::Scheduler#io_writewhen flushing the IO write buffer.
[Bug #21789]
* IntroduceFiber::Scheduler#fiber_interruptto interrupt a fiber with a
given exception. The initial use case is to interrupt a fiber that is
waiting on a blocking IO operation when the IO operation is closed.
[Feature #21166]
* IntroduceFiber::Scheduler#yieldto allow the fiber scheduler to
continue processing when signal exceptions are disabled.
[Bug #21633]
* Reintroduce theFiber::Scheduler#io_closehook for asynchronousIO#close.
* InvokeFiber::Scheduler#io_writewhen flushing the IO write buffer.
[Bug #21789]
* FileFile::Stat#birthtimeis now available on Linux via the statx
system call when supported by the kernel and filesystem.
[Feature #21205]
* File::Stat#birthtimeis now available on Linux via the statx
system call when supported by the kernel and filesystem.
[Feature #21205]
* IOIO.selectacceptsFloat::INFINITYas a timeout argument.
[Feature #20610]A deprecated behavior, process creation byIOclass methods
with a leading|, was removed. [Feature #19630]
* IO.selectacceptsFloat::INFINITYas a timeout argument.
[Feature #20610]
* A deprecated behavior, process creation byIOclass methods
with a leading|, was removed. [Feature #19630]
* KernelKernel#inspectnow checks for the existence of a#instance_variables_to_inspectmethod,
allowing control over which instance variables are displayed in the#inspectstring:classDatabaseConfigdefinitialize(host,user,password)@host=host@user=user@password=passwordendprivatedefinstance_variables_to_inspect=[:@host,:@user]endconf=DatabaseConfig.new("localhost","root","hunter2")conf.inspect#=> #<DatabaseConfig:0x0000000104def350 @host="localhost", @user="root">[Feature #21219]A deprecated behavior, process creation byKernel#openwith a
leading|, was removed. [Feature #19630]
* Kernel#inspectnow checks for the existence of a#instance_variables_to_inspectmethod,
allowing control over which instance variables are displayed in the#inspectstring:classDatabaseConfigdefinitialize(host,user,password)@host=host@user=user@password=passwordendprivatedefinstance_variables_to_inspect=[:@host,:@user]endconf=DatabaseConfig.new("localhost","root","hunter2")conf.inspect#=> #<DatabaseConfig:0x0000000104def350 @host="localhost", @user="root">[Feature #21219]
* A deprecated behavior, process creation byKernel#openwith a
leading|, was removed. [Feature #19630]
* MathMath.log1pandMath.expm1are added. [Feature #21527]
* Math.log1pandMath.expm1are added. [Feature #21527]
* PathnamePathname has been promoted from a default gem to a core class of Ruby.
[Feature #17473]
* Pathname has been promoted from a default gem to a core class of Ruby.
[Feature #17473]
* ProcProc#parametersnow shows anonymous optional parameters as[:opt]instead of[:opt, nil], making the output consistent with when the
anonymous parameter is required. [Bug #20974]
* Proc#parametersnow shows anonymous optional parameters as[:opt]instead of[:opt, nil], making the output consistent with when the
anonymous parameter is required. [Bug #20974]
* RactorRactor::Portclass was added for a new synchronization mechanism
to communicate between Ractors. [Feature #21262]port1=Ractor::Port.newport2=Ractor::Port.newRactor.newport1,port2do|port1,port2|port1<<1port2<<11port1<<2port2<<12end2.times{pport1.receive}#=> 1, 22.times{pport2.receive}#=> 11, 12Ractor::Portprovides the following methods:Ractor::Port#receiveRactor::Port#send(orRactor::Port#<<)Ractor::Port#closeRactor::Port#closed?As a result,Ractor.yieldandRactor#takewere removed.Ractor#joinandRactor#valuewere added to wait for the
termination of a Ractor. These are similar toThread#joinandThread#value.Ractor#monitorandRactor#unmonitorwere added as low-level
interfaces used internally to implementRactor#join.Ractor.selectnow only accepts Ractors and Ports. If Ractors are given,
it returns when a Ractor terminates.Ractor#default_portwas added. EachRactorhas a default port,
which is used byRactor.send,Ractor.receive.Ractor#close_incomingandRactor#close_outgoingwere removed.Ractor.shareable_procandRactor.shareable_lambdaare introduced
to make shareable Proc or lambda.
[Feature #21550], [Feature #21557]
* Ractor::Portclass was added for a new synchronization mechanism
to communicate between Ractors. [Feature #21262]port1=Ractor::Port.newport2=Ractor::Port.newRactor.newport1,port2do|port1,port2|port1<<1port2<<11port1<<2port2<<12end2.times{pport1.receive}#=> 1, 22.times{pport2.receive}#=> 11, 12Ractor::Portprovides the following methods:Ractor::Port#receiveRactor::Port#send(orRactor::Port#<<)Ractor::Port#closeRactor::Port#closed?As a result,Ractor.yieldandRactor#takewere removed.
* Ractor::Port#receive
* Ractor::Port#send(orRactor::Port#<<)
* Ractor::Port#close
* Ractor::Port#closed?
* Ractor#joinandRactor#valuewere added to wait for the
termination of a Ractor. These are similar toThread#joinandThread#value.
* Ractor#monitorandRactor#unmonitorwere added as low-level
interfaces used internally to implementRactor#join.
* Ractor.selectnow only accepts Ractors and Ports. If Ractors are given,
it returns when a Ractor terminates.
* Ractor#default_portwas added. EachRactorhas a default port,
which is used byRactor.send,Ractor.receive.
* Ractor#close_incomingandRactor#close_outgoingwere removed.
* Ractor.shareable_procandRactor.shareable_lambdaare introduced
to make shareable Proc or lambda.
[Feature #21550], [Feature #21557]
* RangeRange#to_setnow performs size checks to prevent issues with
endless ranges. [Bug #21654]Range#overlap?now correctly handles infinite (unbounded) ranges.
[Bug #21185]Range#maxbehavior on beginless integer ranges has been fixed.
[Bug #21174] [Bug #21175]
* Range#to_setnow performs size checks to prevent issues with
endless ranges. [Bug #21654]
* Range#overlap?now correctly handles infinite (unbounded) ranges.
[Bug #21185]
* Range#maxbehavior on beginless integer ranges has been fixed.
[Bug #21174] [Bug #21175]
* RubyA new toplevel moduleRubyhas been defined, which contains
Ruby-related constants. This module was reserved in Ruby 3.4
and is now officially defined. [Feature #20884]
* A new toplevel moduleRubyhas been defined, which contains
Ruby-related constants. This module was reserved in Ruby 3.4
and is now officially defined. [Feature #20884]
* Ruby::BoxA new (experimental) feature to provide separation about definitions.
For the detail of “Ruby Box”, seedoc/language/box.md.
[Feature #21311] [Misc #21385]
* A new (experimental) feature to provide separation about definitions.
For the detail of “Ruby Box”, seedoc/language/box.md.
[Feature #21311] [Misc #21385]
* SetSetis now a core class, instead of an autoloaded stdlib class.
[Feature #21216]Set#inspectnow uses a simpler display, similar to literal arrays.
(e.g.,Set[1, 2, 3]instead of#<Set: {1, 2, 3}>). [Feature #21389]Passing arguments toSet#to_setandEnumerable#to_setis now deprecated.
[Feature #21390]
* Setis now a core class, instead of an autoloaded stdlib class.
[Feature #21216]
* Set#inspectnow uses a simpler display, similar to literal arrays.
(e.g.,Set[1, 2, 3]instead of#<Set: {1, 2, 3}>). [Feature #21389]
* Passing arguments toSet#to_setandEnumerable#to_setis now deprecated.
[Feature #21390]
* SocketSocket.tcp&TCPSocket.newaccepts anopen_timeoutkeyword argument to specify
the timeout for the initial connection. [Feature #21347]When a user-specified timeout occurred inTCPSocket.new, eitherErrno::ETIMEDOUTorIO::TimeoutErrorcould previously be raised depending on the situation.
This behavior has been unified so thatIO::TimeoutErroris now consistently raised.
(Please note that, inSocket.tcp, there are still cases whereErrno::ETIMEDOUTmay be raised in similar situations, and that in both casesErrno::ETIMEDOUTmay be
raised when the timeout occurs at the OS level.)
* Socket.tcp&TCPSocket.newaccepts anopen_timeoutkeyword argument to specify
the timeout for the initial connection. [Feature #21347]
* When a user-specified timeout occurred inTCPSocket.new, eitherErrno::ETIMEDOUTorIO::TimeoutErrorcould previously be raised depending on the situation.
This behavior has been unified so thatIO::TimeoutErroris now consistently raised.
(Please note that, inSocket.tcp, there are still cases whereErrno::ETIMEDOUTmay be raised in similar situations, and that in both casesErrno::ETIMEDOUTmay be
raised when the timeout occurs at the OS level.)
* StringUpdate Unicode to Version 17.0.0 and Emoji Version 17.0.
[Feature #19908][Feature #20724][Feature #21275] (also applies to Regexp)String#strip,strip!,lstrip,lstrip!,rstrip, andrstrip!are extended to accept*selectorsarguments. [Feature #21552]
* Update Unicode to Version 17.0.0 and Emoji Version 17.0.
[Feature #19908][Feature #20724][Feature #21275] (also applies to Regexp)
* String#strip,strip!,lstrip,lstrip!,rstrip, andrstrip!are extended to accept*selectorsarguments. [Feature #21552]
* ThreadIntroduce support forThread#raise(cause:)argument similar toKernel#raise. [Feature #21360]
* Introduce support forThread#raise(cause:)argument similar toKernel#raise. [Feature #21360]

## Stdlib updates

We only list stdlib changes that are notable feature changes.

Other changes are listed in the following sections. We also listed release history from the previous bundled version that is Ruby 3.4.0 if it has GitHub releases.

The following bundled gems are promoted from default gems.

* ostruct 0.6.30.6.1 tov0.6.2,v0.6.3
* 0.6.1 tov0.6.2,v0.6.3
* pstore 0.2.00.1.4 tov0.2.0
* 0.1.4 tov0.2.0
* benchmark 0.5.00.4.0 tov0.4.1,v0.5.0
* 0.4.0 tov0.4.1,v0.5.0
* logger 1.7.01.6.4 tov1.6.5,v1.6.6,v1.7.0
* 1.6.4 tov1.6.5,v1.6.6,v1.7.0
* rdoc 7.0.26.14.0 tov6.14.1,v6.14.2,v6.15.0,v6.15.1,v6.16.0,v6.16.1,v6.17.0,v7.0.0,v7.0.1,v7.0.2,v7.0.3
* 6.14.0 tov6.14.1,v6.14.2,v6.15.0,v6.15.1,v6.16.0,v6.16.1,v6.17.0,v7.0.0,v7.0.1,v7.0.2,v7.0.3
* win32ole 1.9.21.9.1 tov1.9.2
* 1.9.1 tov1.9.2
* irb 1.16.01.14.3 tov1.15.0,v1.15.1,v1.15.2,v1.15.3,v1.16.0
* 1.14.3 tov1.15.0,v1.15.1,v1.15.2,v1.15.3,v1.16.0
* reline 0.6.30.6.0 tov0.6.1,v0.6.2,v0.6.3
* 0.6.0 tov0.6.1,v0.6.2,v0.6.3
* readline 0.0.4
* fiddle 1.1.81.1.6 tov1.1.7,v1.1.8
* 1.1.6 tov1.1.7,v1.1.8

The following default gem is added.

* win32-registry 0.1.2

The following default gems are updated.

* RubyGems 4.0.3
* bundler 4.0.3
* date 3.5.13.4.1 tov3.5.0,v3.5.1
* 3.4.1 tov3.5.0,v3.5.1
* delegate 0.6.10.4.0 tov0.5.0,v0.6.0,v0.6.1
* 0.4.0 tov0.5.0,v0.6.0,v0.6.1
* digest 3.2.13.2.0 tov3.2.1
* 3.2.0 tov3.2.1
* english 0.8.10.8.0 tov0.8.1
* 0.8.0 tov0.8.1
* erb 6.0.14.0.4 tov5.1.2,v5.1.3,v6.0.0,v6.0.1
* 4.0.4 tov5.1.2,v5.1.3,v6.0.0,v6.0.1
* error_highlight 0.7.1
* etc 1.4.6
* fcntl 1.3.01.2.0 tov1.3.0
* 1.2.0 tov1.3.0
* fileutils 1.8.01.7.3 tov1.8.0
* 1.7.3 tov1.8.0
* forwardable 1.4.01.3.3 tov1.4.0
* 1.3.3 tov1.4.0
* io-console 0.8.20.8.1 tov0.8.2
* 0.8.1 tov0.8.2
* io-nonblock 0.3.2
* io-wait 0.4.00.3.2 tov0.3.3,v0.3.5.test1,v0.3.5,v0.3.6,v0.4.0
* 0.3.2 tov0.3.3,v0.3.5.test1,v0.3.5,v0.3.6,v0.4.0
* ipaddr 1.2.8
* json 2.18.02.9.1 tov2.10.0,v2.10.1,v2.10.2,v2.11.0,v2.11.1,v2.11.2,v2.11.3,v2.12.0,v2.12.1,v2.12.2,v2.13.0,v2.13.1,v2.13.2,v2.14.0,v2.14.1,v2.15.0,v2.15.1,v2.15.2,v2.16.0,v2.17.0,v2.17.1,v2.18.0
* 2.9.1 tov2.10.0,v2.10.1,v2.10.2,v2.11.0,v2.11.1,v2.11.2,v2.11.3,v2.12.0,v2.12.1,v2.12.2,v2.13.0,v2.13.1,v2.13.2,v2.14.0,v2.14.1,v2.15.0,v2.15.1,v2.15.2,v2.16.0,v2.17.0,v2.17.1,v2.18.0
* net-http 0.9.10.6.0 tov0.7.0,v0.8.0,v0.9.0,v0.9.1
* 0.6.0 tov0.7.0,v0.8.0,v0.9.0,v0.9.1
* openssl 4.0.03.3.1 tov3.3.2,v4.0.0
* 3.3.1 tov3.3.2,v4.0.0
* optparse 0.8.10.6.0 tov0.7.0,v0.8.0,v0.8.1
* 0.6.0 tov0.7.0,v0.8.0,v0.8.1
* pp 0.6.30.6.2 tov0.6.3
* 0.6.2 tov0.6.3
* prism 1.7.01.5.2 tov1.6.0,v1.7.0
* 1.5.2 tov1.6.0,v1.7.0
* psych 5.3.15.2.2 tov5.2.3,v5.2.4,v5.2.5,v5.2.6,v5.3.0,v5.3.1
* 5.2.2 tov5.2.3,v5.2.4,v5.2.5,v5.2.6,v5.3.0,v5.3.1
* resolv 0.7.00.6.2 tov0.6.3,v0.7.0
* 0.6.2 tov0.6.3,v0.7.0
* stringio 3.2.03.1.2 tov3.1.3,v3.1.4,v3.1.5,v3.1.6,v3.1.7,v3.1.8,v3.1.9,v3.2.0
* 3.1.2 tov3.1.3,v3.1.4,v3.1.5,v3.1.6,v3.1.7,v3.1.8,v3.1.9,v3.2.0
* strscan 3.1.63.1.2 tov3.1.3,v3.1.4,v3.1.5,v3.1.6
* 3.1.2 tov3.1.3,v3.1.4,v3.1.5,v3.1.6
* time 0.4.20.4.1 tov0.4.2
* 0.4.1 tov0.4.2
* timeout 0.6.00.4.3 tov0.4.4,v0.5.0,v0.6.0
* 0.4.3 tov0.4.4,v0.5.0,v0.6.0
* uri 1.1.11.0.4 tov1.1.0,v1.1.1
* 1.0.4 tov1.1.0,v1.1.1
* weakref 0.1.40.1.3 tov0.1.4
* 0.1.3 tov0.1.4
* zlib 3.2.23.2.1 tov3.2.2
* 3.2.1 tov3.2.2

The following bundled gems are updated.

* minitest 6.0.0
* power_assert 3.0.12.0.5 tov3.0.0,v3.0.1
* 2.0.5 tov3.0.0,v3.0.1
* rake 13.3.113.2.1 tov13.3.0,v13.3.1
* 13.2.1 tov13.3.0,v13.3.1
* test-unit 3.7.53.6.7 to3.6.8,3.6.9,3.7.0,3.7.1,3.7.2,3.7.3,3.7.4,3.7.5
* 3.6.7 to3.6.8,3.6.9,3.7.0,3.7.1,3.7.2,3.7.3,3.7.4,3.7.5
* rexml 3.4.4
* rss 0.3.20.3.1 to0.3.2
* 0.3.1 to0.3.2
* net-ftp 0.3.90.3.8 tov0.3.9
* 0.3.8 tov0.3.9
* net-imap 0.6.20.5.8 tov0.5.9,v0.5.10,v0.5.11,v0.5.12,v0.5.13,v0.6.0,v0.6.1,v0.6.2
* 0.5.8 tov0.5.9,v0.5.10,v0.5.11,v0.5.12,v0.5.13,v0.6.0,v0.6.1,v0.6.2
* net-smtp 0.5.10.5.0 tov0.5.1
* 0.5.0 tov0.5.1
* matrix 0.4.30.4.2 tov0.4.3
* 0.4.2 tov0.4.3
* prime 0.1.40.1.3 tov0.1.4
* 0.1.3 tov0.1.4
* rbs 3.10.03.8.0 tov3.8.1,v3.9.0.dev.1,v3.9.0.pre.1,v3.9.0.pre.2,v3.9.0,v3.9.1,v3.9.2,v3.9.3,v3.9.4,v3.9.5,v3.10.0.pre.1,v3.10.0.pre.2,v3.10.0
* 3.8.0 tov3.8.1,v3.9.0.dev.1,v3.9.0.pre.1,v3.9.0.pre.2,v3.9.0,v3.9.1,v3.9.2,v3.9.3,v3.9.4,v3.9.5,v3.10.0.pre.1,v3.10.0.pre.2,v3.10.0
* typeprof 0.31.1
* debug 1.11.11.11.0 tov1.11.1
* 1.11.0 tov1.11.1
* base64 0.3.00.2.0 tov0.3.0
* 0.2.0 tov0.3.0
* bigdecimal 4.0.13.1.8 tov3.2.0,v3.2.1,v3.2.2,v3.2.3,v3.3.0,v3.3.1,v4.0.0,v4.0.1
* 3.1.8 tov3.2.0,v3.2.1,v3.2.2,v3.2.3,v3.3.0,v3.3.1,v4.0.0,v4.0.1
* drb 2.2.32.2.1 tov2.2.3
* 2.2.1 tov2.2.3
* syslog 0.3.00.2.0 tov0.3.0
* 0.2.0 tov0.3.0
* csv 3.3.53.3.2 tov3.3.3,v3.3.4,v3.3.5
* 3.3.2 tov3.3.3,v3.3.4,v3.3.5
* repl_type_completor 0.1.12

### RubyGems and Bundler

Ruby 4.0 bundled RubyGems and Bundler version 4. see the following links for details.

* Upgrading to RubyGems/Bundler 4 - RubyGems Blog
* 4.0.0 Released - RubyGems Blog
* 4.0.1 Released - RubyGems Blog
* 4.0.2 Released - RubyGems Blog
* 4.0.3 Released - RubyGems Blog

## Supported platforms

* WindowsDropped support for MSVC versions older than 14.0 (_MSC_VER 1900).
This means Visual Studio 2015 or later is now required.
* Dropped support for MSVC versions older than 14.0 (_MSC_VER 1900).
This means Visual Studio 2015 or later is now required.

## Compatibility issues

* The following methods were removed from Ractor due to the addition ofRactor::Port:Ractor.yieldRactor#takeRactor#close_incomingRactor#close_outgoing[Feature #21262]
* Ractor.yield
* Ractor#take
* Ractor#close_incoming
* Ractor#close_outgoing
* ObjectSpace._id2refis deprecated. [Feature #15408]
* Process::Status#&andProcess::Status#>>have been removed.
They were deprecated in Ruby 3.3. [Bug #19868]
* rb_path_checkhas been removed. This function was used for$SAFEpath checking which was removed in Ruby 2.7,
and was already deprecated.
[Feature #20971]
* A backtrace forArgumentErrorof “wrong number of arguments” now
include the receiver’s class or module name (e.g., inFoo#barinstead of inbar). [Bug #21698]
* Backtraces no longer displayinternalframes.
These methods now appear as if it is in the Ruby source file,
consistent with other C-implemented methods. [Bug #20968]Before:ruby -e '[1].fetch_values(42)'
<internal:array>:211:in 'Array#fetch': index 42 outside of array bounds: -1...1 (IndexError)
 from <internal:array>:211:in 'block in Array#fetch_values'
 from <internal:array>:211:in 'Array#map!'
 from <internal:array>:211:in 'Array#fetch_values'
 from -e:1:in '<main>'After:$ ruby -e '[1].fetch_values(42)'
-e:1:in 'Array#fetch_values': index 42 outside of array bounds: -1...1 (IndexError)
 from -e:1:in '<main>'

## Stdlib compatibility issues

* CGI library is removed from the default gems. Now we only providecgi/escapefor
the following methods:CGI.escapeandCGI.unescapeCGI.escapeHTMLandCGI.unescapeHTMLCGI.escapeURIComponentandCGI.unescapeURIComponentCGI.escapeElementandCGI.unescapeElement[Feature #21258]
* CGI.escapeandCGI.unescape
* CGI.escapeHTMLandCGI.unescapeHTML
* CGI.escapeURIComponentandCGI.unescapeURIComponent
* CGI.escapeElementandCGI.unescapeElement
* With the move ofSetfrom stdlib to core class,set/sorted_set.rbhas
been removed, andSortedSetis no longer an autoloaded constant. Please
install thesorted_setgem andrequire 'sorted_set'to useSortedSet.
[Feature #21287]
* Net::HTTPThe default behavior of automatically setting theContent-Typeheader
toapplication/x-www-form-urlencodedfor requests with a body
(e.g.,POST,PUT) when the header was not explicitly set has been
removed. If your application relied on this automatic default, your
requests will now be sent without a Content-Type header, potentially
breaking compatibility with certain servers.
[GH-net-http #205]
* The default behavior of automatically setting theContent-Typeheader
toapplication/x-www-form-urlencodedfor requests with a body
(e.g.,POST,PUT) when the header was not explicitly set has been
removed. If your application relied on this automatic default, your
requests will now be sent without a Content-Type header, potentially
breaking compatibility with certain servers.
[GH-net-http #205]

## C API updates

* IOrb_thread_fd_closeis deprecated and now a no-op. If you need to expose
file descriptors from C extensions to Ruby code, create anIOinstance
usingRUBY_IO_MODE_EXTERNALand userb_io_close(io)to close it (this
also interrupts and waits for all pending operations on theIOinstance). Directly closing file descriptors does not interrupt pending
operations, and may lead to undefined behaviour. In other words, if twoIOobjects share the same file descriptor, closing one does not affect
the other. [Feature #18455]
* rb_thread_fd_closeis deprecated and now a no-op. If you need to expose
file descriptors from C extensions to Ruby code, create anIOinstance
usingRUBY_IO_MODE_EXTERNALand userb_io_close(io)to close it (this
also interrupts and waits for all pending operations on theIOinstance). Directly closing file descriptors does not interrupt pending
operations, and may lead to undefined behaviour. In other words, if twoIOobjects share the same file descriptor, closing one does not affect
the other. [Feature #18455]
* GVLrb_thread_call_with_gvlnow works with or without the GVL.
This allows gems to avoid checkingruby_thread_has_gvl_p.
Please still be diligent about the GVL. [Feature #20750]
* rb_thread_call_with_gvlnow works with or without the GVL.
This allows gems to avoid checkingruby_thread_has_gvl_p.
Please still be diligent about the GVL. [Feature #20750]
* SetA C API forSethas been added. The following methods are supported:
[Feature #21459]rb_set_foreachrb_set_newrb_set_new_caparb_set_lookuprb_set_addrb_set_clearrb_set_deleterb_set_size
* A C API forSethas been added. The following methods are supported:
[Feature #21459]rb_set_foreachrb_set_newrb_set_new_caparb_set_lookuprb_set_addrb_set_clearrb_set_deleterb_set_size
* rb_set_foreach
* rb_set_new
* rb_set_new_capa
* rb_set_lookup
* rb_set_add
* rb_set_clear
* rb_set_delete
* rb_set_size

## Implementation improvements

* Class#new(ex.Object.new) is faster in all cases, but especially when passing keyword arguments. This has also been integrated into YJIT and ZJIT. [Feature #21254]
* GC heaps of different size pools now grow independently, reducing memory usage when only some pools contain long-lived objects
* GC sweeping is faster on pages of large objects
* “Generic ivar” objects (String, Array,TypedData, etc.) now use a new internal “fields” object for faster instance variable access
* The GC avoids maintaining an internalid2reftable until it is first used, makingobject_idallocation and GC sweeping faster
* object_idandhashare faster on Class and Module objects
* Larger bignum Integers can remain embedded using variable width allocation
* Random,Enumerator::Product,Enumerator::Chain,Addrinfo,StringScanner, and some internal objects are now write-barrier protected,
which reduces GC overhead.

### Ractor

A lot of work has gone into making Ractors more stable, performant, and usable. These improvements bring Ractor implementation closer to leaving experimental status.

* Performance improvementsFrozen strings and the symbol table internally use a lock-free hash set [Feature #21268]Method cache lookups avoid locking in most casesClass (and generic ivar) instance variable access is faster and avoids lockingCPU cache contention is avoided in object allocation by using a per-ractor counterCPU cache contention is avoided in xmalloc/xfree by using a thread-local counterobject_idavoids locking in most cases
* Frozen strings and the symbol table internally use a lock-free hash set [Feature #21268]
* Method cache lookups avoid locking in most cases
* Class (and generic ivar) instance variable access is faster and avoids locking
* CPU cache contention is avoided in object allocation by using a per-ractor counter
* CPU cache contention is avoided in xmalloc/xfree by using a thread-local counter
* object_idavoids locking in most cases
* Bug fixes and stabilityFixed possible deadlocks when combining Ractors and ThreadsFixed issues with require and autoload in a RactorFixed encoding/transcoding issues across RactorsFixed race conditions in GC operations and method invalidationFixed issues with processes forking after starting a RactorGC allocation counts are now accurate under RactorsFixed TracePoints not working after GC [Bug #19112]
* Fixed possible deadlocks when combining Ractors and Threads
* Fixed issues with require and autoload in a Ractor
* Fixed encoding/transcoding issues across Ractors
* Fixed race conditions in GC operations and method invalidation
* Fixed issues with processes forking after starting a Ractor
* GC allocation counts are now accurate under Ractors
* Fixed TracePoints not working after GC [Bug #19112]

## JIT

* ZJITIntroduce anexperimental method-based JIT compiler.
 Where available, ZJIT can be enabled at runtime with the--zjitoption or by callingRubyVM::ZJIT.enable.
When building Ruby, Rust 1.85.0 or later is required to include ZJIT support.As of Ruby 4.0.0, ZJIT is faster than the interpreter, but not yet as fast as YJIT.
We encourage experimentation with ZJIT, but advise against deploying it in production for now.Our goal is to make ZJIT faster than YJIT and production-ready in Ruby 4.1.
* Introduce anexperimental method-based JIT compiler.
 Where available, ZJIT can be enabled at runtime with the--zjitoption or by callingRubyVM::ZJIT.enable.
When building Ruby, Rust 1.85.0 or later is required to include ZJIT support.
* As of Ruby 4.0.0, ZJIT is faster than the interpreter, but not yet as fast as YJIT.
We encourage experimentation with ZJIT, but advise against deploying it in production for now.
* Our goal is to make ZJIT faster than YJIT and production-ready in Ruby 4.1.
* YJITRubyVM::YJIT.runtime_statsratio_in_yjitno longer works in the default build.
Use--enable-yjit=statsonconfigureto enable it on--yjit-stats.Addinvalidate_everythingto default stats, which is
incremented when every code is invalidated by TracePoint.Addmem_size:andcall_threshold:options toRubyVM::YJIT.enable.
* RubyVM::YJIT.runtime_statsratio_in_yjitno longer works in the default build.
Use--enable-yjit=statsonconfigureto enable it on--yjit-stats.Addinvalidate_everythingto default stats, which is
incremented when every code is invalidated by TracePoint.
* ratio_in_yjitno longer works in the default build.
Use--enable-yjit=statsonconfigureto enable it on--yjit-stats.
* Addinvalidate_everythingto default stats, which is
incremented when every code is invalidated by TracePoint.
* Addmem_size:andcall_threshold:options toRubyVM::YJIT.enable.
* RJIT--rjitis removed. We will move the implementation of the third-party JIT API
to theruby/rjitrepository.
* --rjitis removed. We will move the implementation of the third-party JIT API
to theruby/rjitrepository.

SeeNEWSorcommit logsfor more details.

With those changes,3889 files changed, 230769 insertions(+), 297003 deletions(-)since Ruby 3.4.0!

Merry Christmas, a Happy New Year, and Happy Hacking with Ruby 4.0!

## Download

* https://cache.ruby-lang.org/pub/ruby/4.0/ruby-4.0.0.tar.gzSIZE: 23955109
SHA1: 754e39e9ad122e1b6deaed860350bac133a35ed3
SHA256: 2e8389c8c072cb658c93a1372732d9eac84082c88b065750db1e52a5ac630271
SHA512: 688254e939b197d564e896fb951bc1abf07142f489e91c5ed0b11f68f52d6adb6b1f86616fe03f1f0bb434beeef7e75e158b9c616afb39bb34403b0b78d2ee19
* https://cache.ruby-lang.org/pub/ruby/4.0/ruby-4.0.0.tar.xzSIZE: 18008368
SHA1: 05ec670e86f84325c5353ef2f2888e53b6adc602
SHA256: a72bacee9de07283ebc19baa4ac243b193129f21aa4e168c7186fb1fe7d07fe1
SHA512: 2d5b2e566eaf70a5f3ea6ce6afc0611c0415de58a41336ef7a0b855c9a91eda9aa790a5f8b48e40a1eb9d50f8ea0f687216e617f16c8d040a08474f3116518a4
* https://cache.ruby-lang.org/pub/ruby/4.0/ruby-4.0.0.zipSIZE: 29253204
SHA1: 0b69f89d1d140157251c0d3a6032f6c45cdf81e8
SHA256: 70cb1bf89279b86ab9a975d504607c051fc05ee03e311d550a5541b65e373455
SHA512: a72e076ef618c0aeb9d20cf22e6fb12fda36809c0064ef0f98153b95a0bac257ef606342444a38f992c4594bf376a4d264686cf597463aa6f111220798784302

## What is Ruby

Ruby was first developed by Matz (Yukihiro Matsumoto) in 1993,
and is now developed as Open Source. It runs on multiple platforms
and is used all over the world especially for web development.

## Recent News

### A New Look for Ruby's Documentation

Following the ruby-lang.org redesign, we have more news to celebrate Ruby’s 30th anniversary: docs.ruby-lang.org has a completely new look with Aliki—RDoc’s new default theme.

Posted byStan Loon 23 Dec 2025

### Redesign our Site Identity

We are excited to announce a comprehensive redesign of our site. The design for this update was created by Taeko Akatsuka.

Posted byHiroshi SHIBATAon 22 Dec 2025

### Ruby 4.0.0 preview3 Released

We are pleased to announce the release of Ruby 4.0.0-preview3.
Ruby 4.0 introduces Ruby::Box and “ZJIT”, and adds many improvements.

Posted bynaruseon 18 Dec 2025

### Ruby 3.4.8 Released

Ruby 3.4.8 has been released.

Posted byk0kubunon 17 Dec 2025

More News...
