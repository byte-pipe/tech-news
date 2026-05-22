---
title: jnigen and swiftgen in 2026 - some lessons learned - DEV Community
url: https://dev.to/orestesgaolin/jnigen-and-swiftgen-in-2026-some-lessons-learned-16ni
site_name: devto
content_file: devto-jnigen-and-swiftgen-in-2026-some-lessons-learned-d
fetched_at: '2026-05-22T19:34:51.128318'
original_url: https://dev.to/orestesgaolin/jnigen-and-swiftgen-in-2026-some-lessons-learned-16ni
author: Dominik Roszkowski
date: '2026-05-20'
description: Package jni 1.0.0 was recently published. It's a good opportunity to share some of my lessons from... Tagged with flutter, dart, jni, ffi.
tags: '#flutter, #dart, #jni, #ffi'
---

Packagejni 1.0.0was recently published. It's a good opportunity to share some of my lessons from working with native interop over the last few years.

There were some breaking changes between jni 0.14/0.15 and 1.0.0, so if you were using jni and jnigen in the past, you may face some extra work when upgrading. This article was written after I got annoyed with the AI agent incorrect output when working on the migration.

## Migration tojni@1.0.0

I found that the quickest way to do it was to comment out all my native integration code first, just to rebuild the Android project and regenerate bindings afterwards.

Some APIs have changed (back) to more reasonable names, e.g.,toDartString()is nowtoString(), or methods for setting properties becamesetters(_service.onReplyListener(_listener!);is now_service.onReplyListener = _listener!;). There are also some annoying changes like constructor overrides changing numbers, e.g.,Intent.new$2can now beIntent.new$12...

Moreover, the new recommended way to define bindings configuration isno longer a yaml file, but rather a simple Dart script. I quite enjoy this new approach, as it hides the magic behind the code generation, and you can just add some pre- and post-processing logic to the generated code. It seems that the convention will be to put these into thetool/directory and run them withdart run tool/jnigen.dartordart run tool/swiftgen.dart.

You can see example migration commits for simple Flutter apps:

* from 0.15 to 1.0.0here.
* from 0.14 to 1.0.0here

Below I share some of the lessons I learned while working with jnigen and swiftgen in last few years. In the last few months I managed to update some of my packages:

* screen_brightness_monitor
* play_in_app_update
* uikit_bindings
* android_intent
* foreground_service_interop

## jnigen (Android)

Quick recap:

* You can use jnigen to generate Dart bindings for both explicit and compiled Java/Kotlin code.
* Before generating the bindings you need to build the Android app at least once.1
* You can include both project-specific classes, as well as Android SDK types.
* There are some built-in helpers for common Android utilities, which now have been migrated topackage:jni_flutter.

### Generator script (tool/jnigen.dart)

Example generator script for a plugin with two classes and one callback interface (callback pattern explained in the next section):

import
 
'dart:io'
;

import
 
'package:jnigen/jnigen.dart'
;

void
 
main
(
List
<
String
>
 
args
)
 
{

 
final
 
packageRoot
 
=
 
Platform
.
script
.
resolve
(
'../'
);

 
generateJniBindings
(
Config
(

 
outputConfig:
 
OutputConfig
(

 
dartConfig:
 
DartCodeOutputConfig
(

 
path:
 
packageRoot
.
resolve
(
'lib/src/my_plugin.g.dart'
),

 
structure:
 
OutputStructure
.
singleFile
,

 
),

 
),

 
androidSdkConfig:
 
AndroidSdkConfig
(

 
addGradleDeps:
 
true
,

 
androidExample:
 
'example'
,
 
// Points to example app for Gradle resolution

 
),

 
sourcePath:
 
[
packageRoot
.
resolve
(
'android/src/main/java/'
)],

 
classes:
 
[

 
'com.example.MyCallback'
,
 
// List ALL classes to bind

 
'com.example.MyPlugin'
,

 
],

 
));

}

Enter fullscreen mode

Exit fullscreen mode

### Callbacks: use Kotlin interfaces

If you want to receive data back from native code to Dart, the approach I found is to define a callback interface. Then on the Dart side you can wrap it with more user-friendly API likeStreamController. Often, it's sufficient to just expose the callback directly.

Define a dedicated Kotlin interface. jnigen generates a type-safeimplement()method and$Mixin:

// Generates BrightnessCallback.implement($BrightnessCallback(...))

@Keep

interface
 
BrightnessCallback
 
{

 
@Keep

 
fun
 
onBrightnessChanged
(
brightness
:
 
Int
)

}

Enter fullscreen mode

Exit fullscreen mode

Then in Dart:

final
 
callback
 
=
 
BrightnessCallback
.
implement
(

 
$BrightnessCallback
(

 
onBrightnessChanged:
 
(
brightness
)
 
{
 
/* ... */
 
},

 
onBrightnessChanged$async
:
 
true
,
 
// Non-blocking (listener pattern)

 
),

);

native
.
startObserving
(
callback
);

Enter fullscreen mode

Exit fullscreen mode

### Getting access to Context and Activity - package:jni_flutter

There are some small changes to accessing Android Context (androidApplicationContext) and current Activity. It's now part of thepackage:jni_flutter. Moreover, to get the current Activity, you need to pass the currentengineId.

final
 
engineId
 
=
 
PlatformDispatcher
.
instance
.
engineId
;

if
 
(
engineId
 
==
 
null
)
 
{

 
print
(
'Error: Engine ID is null'
);

 
return
;

}

final
 
activity
 
=
 
androidActivity
(
engineId
);

if
 
(
activity
 
==
 
null
)
 
{

 
print
(
'Error: Activity is null'
);

 
return
;

}

activity
.
as
(
a
.
Activity
.
type
)
.
startActivityForResult
(
intent
,
 
1
);

Enter fullscreen mode

Exit fullscreen mode

### Casting

To castJObjectonto a desired type, useas()with the generated type:

final
 
brightnessMonitor
 
=
 
native
.
getBrightnessMonitor
();

final
 
brightness
 
=
 
brightnessMonitor
.
as
(
ScreenBrightnessMonitor
.
type
)
.
brightness
;

Enter fullscreen mode

Exit fullscreen mode

### Arrays

It's a bit cumbersome, but once you know, you know:

final
 
array
 
=
 
JArray
.
of
<
JString
>(
JString
.
type
,
 
[
"cc@example.com"
.
toJString
()]);

Enter fullscreen mode

Exit fullscreen mode

### The$async: trueFlag

I found that I'm basically always usingasync: truefor callbacks. There's some dedicatedthreading documentation, but not sure how up-to-date it is.

### Annotate with@Keep

ProGuard/R8 strips unreferenced classes. Annotate every class, interface, property, and method that jnigen binds:

@Keep

class
 
ScreenBrightnessMonitor
(
private
 
val
 
context
:
 
Context
)
 
{

 
@
get
:
Keep
 
// For Kotlin properties, use @get:Keep

 
val
 
brightness
:
 
Int

 
get
()
 
=
 
/* ... */

 
@Keep

 
fun
 
startObserving
(
callback
:
 
BrightnessCallback
)
 
{
 
/* ... */
 
}

}

Enter fullscreen mode

Exit fullscreen mode

### Issues while regenerating bindings

Sometimes, despite changing Kotlin code and rebuilding with gradle, the jnigen generator may throw errors likeUnexpected end of input (at character 1). In my case, the workaround is to rerun the Gradle build without cache.

cd 
android
./gradlew :your_plugin_name:assembleDebug 
--no-daemon
 
--console
=
plain 
--refresh-dependencies
 
--rerun-tasks

cd
 ..
dart run tool/jnigen.dart

Enter fullscreen mode

Exit fullscreen mode

### Memory management

When using jni bindings, you have to remember about native Java objects that are getting referenced on each instantiation.

The overall assumption is that you don't have to manually manage them. Once all references (in both Java and Dart) to an object are gone, Java's garbage collector (GC) can reclaim it. Similarly, JObjects attach a native finalizer to their global references. Therefore, when the Dart GC collects them, the underlying Java reference is released.

However, sometimes you may want to control the lifecycle of objects more explicitly. Read more on reference management in thededicated documentation. To manually release a JNI global reference, call.release()on the Dart side:

void
 
dispose
()
 
{

 
native
.
stopObserving
();

 
callback
?.
release
();

 
native
.
release
();

}

Enter fullscreen mode

Exit fullscreen mode

## swiftgen (iOS)

Swiftgen is still not stable, but I've had some success using it so far. The Swift code needs to be compatible with Objective-C, and swiftgen handles the bridging to Dart viaswift2objcandffigen.

I have publishedpackage:screen_brightness_monitorthat uses swiftgen for iOS bindings.

### Generator script (tool/swiftgen.dart)

Similarly to jnigen, I recommend using a Dart script for configuration. Here's an example for a plugin with one class and one callback protocol:

import
 
'dart:io'
;

import
 
'package:ffigen/ffigen.dart'
 
as
 
fg
;

import
 
'package:logging/logging.dart'
;

import
 
'package:swiftgen/swiftgen.dart'
;

Future
<
void
>
 
main
()
 
async
 
{

 
final
 
logger
 
=
 
Logger
(
'swiftgen'
);

 
logger
.
onRecord
.
listen
((
record
)
 
{

 
stderr
.
writeln
(
'
${record.level.name}
: 
${record.message}
'
);

 
});

 
final
 
packageRoot
 
=
 
Platform
.
script
.
resolve
(
'../'
);

 
// Resolve SDK path/version manually:

 
final
 
sdkPath
 
=
 
(
await
 
Process
.
run
(
'xcrun'
,
 
[

 
'--sdk'
,
 
'iphoneos'
,
 
'--show-sdk-path'
,

 
]))
.
stdout
.
toString
()
.
trim
();

 
final
 
sdkVersion
 
=
 
(
await
 
Process
.
run
(
'xcrun'
,
 
[

 
'--sdk'
,
 
'iphoneos'
,
 
'--show-sdk-version'
,

 
]))
.
stdout
.
toString
()
.
trim
();

 
await
 
SwiftGenerator
(

 
target:
 
Target
(

 
triple:
 
'arm64-apple-ios
$sdkVersion
'
,

 
sdk:
 
Uri
.
directory
(
sdkPath
),

 
),

 
inputs:
 
[

 
ObjCCompatibleSwiftFileInput
(

 
files:
 
[

 
packageRoot
.
resolve
(
'ios/Classes/MyWidget.swift'
),

 
],

 
),

 
],

 
output:
 
Output
(

 
module:
 
'my_plugin'
,

 
dartFile:
 
packageRoot
.
resolve
(
'lib/src/my_plugin_ios.g.dart'
),

 
objectiveCFile:
 
packageRoot
.
resolve
(
'ios/Classes/my_plugin.m'
),

 
),

 
ffigen:
 
FfiGeneratorOptions
(

 
objectiveC:
 
fg
.
ObjectiveC
(

 
interfaces:
 
fg
.
Interfaces
(

 
include:
 
(
decl
)
 
=
>
 
decl
.
originalName
 
==
 
'MyWidget'
,

 
),

 
protocols:
 
fg
.
Protocols
(

 
include:
 
(
decl
)
 
=
>
 
decl
.
originalName
 
==
 
'MyCallback'
,

 
),

 
),

 
),

 
)
.
generate
(
logger:
 
logger
);

}

Enter fullscreen mode

Exit fullscreen mode

### ObjCCompatibleSwiftFileInputvsSwiftFileInput

* SwiftFileInput: For pure Swift code. swift2objc wraps it in ObjC-compatible wrappers.
* ObjCCompatibleSwiftFileInput: For Swift code that'salready@objcannotated. Skips the wrapping step -- simpler, fewer surprises.Prefer this when you control the Swift code.

## Writing ObjC-compatible Swift

All types exposed to Dart must be@objcannotated and inherit fromNSObject(for classes):

// Protocol — callback interface

@objc
 
public
 
protocol
 
BrightnessCallback
 
{

 
@objc
 
func
 
onBrightnessChanged
(
_
 
brightness
:
 
Int
)

}

// Class — must inherit NSObject

@objc
 
public
 
class
 
ScreenBrightnessMonitor
:
 
NSObject
 
{

 
@objc
 
public
 
override
 
init
()
 
{
 
super
.
init
()
 
}

 
@objc
 
public
 
var
 
brightness
:
 
Int
 
{
 
/* ... */
 
}

 
@objc
 
public
 
func
 
startObserving
(
callback
:
 
BrightnessCallback
)
 
{
 
/* ... */
 
}

 
@objc
 
public
 
func
 
stopObserving
()
 
{
 
/* ... */
 
}

}

Enter fullscreen mode

Exit fullscreen mode

Rules:

* Classes must inheritNSObject(direct or indirect).
* Use@objc publicon everything ffigen should see.
* Overridinginit()requiresoverride+ callingsuper.init().
* Only ObjC-compatible types work:Int,String,Bool,NSObjectsubclasses, protocols. No Swift structs, enums with associated values, or generics.

## ffigen include filters

By default, ffigen generates bindings foreverythingin the ObjC header. Useincludefilters to limit output to your types only:

ffigen:
 
FfiGeneratorOptions
(

 
objectiveC:
 
fg
.
ObjectiveC
(

 
interfaces:
 
fg
.
Interfaces
(

 
include:
 
(
decl
)
 
=
>
 
decl
.
originalName
 
==
 
'ScreenBrightnessMonitor'
,

 
),

 
protocols:
 
fg
.
Protocols
(

 
include:
 
(
decl
)
 
=
>
 
decl
.
originalName
 
==
 
'BrightnessCallback'
,

 
),

 
),

),

Enter fullscreen mode

Exit fullscreen mode

Without filters, you'll get bindings forNSObject,NSString, etc. -- hundreds of unnecessary lines.

### Implementing ObjC protocols in Dart

swiftgen/ffigen generates three flavors for each protocol:

Method

Use When

implement(...)

Callback runs synchronously, blocking the ObjC caller until Dart returns

implementAsListener(...)

Callback is non-blocking
 -- ObjC caller continues immediately (use for observers/notifications)

implementAsBlocking(...)

Callback blocks the ObjC thread and waits for Dart to complete

For observer/notification patterns, useimplementAsListener:

final
 
callback
 
=
 
BrightnessCallback$Builder
.
implementAsListener
(

 
onBrightnessChanged_:
 
(
brightness
)
 
{

 
controller
.
add
(
brightness
);

 
},

);

native
.
startObservingWithCallback
(
callback
);

Enter fullscreen mode

Exit fullscreen mode

### SDK version workaround

When building my package, I found thatTarget.iOSArm64Latest()may crash withFormatExceptionif swift2objc's_parseVersionregex can't parse your Xcode SDK version string. The workaround is to resolve the SDK path and version manually viaxcrunand construct theTargetdirectly (see generator script above). Perhaps I did something wrong?

### Generated files

swiftgen producestwofiles:

1. Dart bindings(lib/src/..._ios.g.dart) -- extension types wrapping ObjC objects
2. ObjC bindings(ios/Classes/....m) -- C functions that ffigen's Dart code calls viadart:ffi

Both must be committed. The.mfile must be in a location picked up by the podspec (Classes/**/*).

### ObjC method names (iOS)

Swiftfunc startObserving(callback:)becomesstartObservingWithCallback:in ObjC (and thus in the Dart binding). Check the generated.g.dartfor actual method names.

### Podspecsource_files

Must include both the Swift source and the generated.mfile.Classes/**/*covers both.

## Cross-platform Dart wrapper

Neither jnigen nor swiftgen will generate a single API for both platforms (as opposed topackage:pigeon). Below I share a simple pattern I used in my plugin to expose a common API to users.

### Abstract class + factory constructor

Define an abstract class with a factory constructor that instantiates the correct platform implementation at runtime:

// lib/src/brightness_monitor.dart

import
 
'dart:io'
 
show
 
Platform
;

import
 
'brightness_monitor_android.dart'
;

import
 
'brightness_monitor_ios.dart'
;

abstract
 
class
 
BrightnessMonitor
 
{

 
factory
 
BrightnessMonitor
()
 
{

 
if
 
(
Platform
.
isAndroid
)
 
return
 
BrightnessMonitorAndroid
();

 
if
 
(
Platform
.
isIOS
)
 
return
 
BrightnessMonitorIos
();

 
throw
 
UnsupportedError
(
'Unsupported platform'
);

 
}

 
int
 
get
 
brightness
;

 
Stream
<
int
>
 
get
 
onBrightnessChanged
;

 
void
 
dispose
();

}

Enter fullscreen mode

Exit fullscreen mode

Each platform file imports only its own generated bindings, so platform-specificdart:ffisymbols don't conflict.

### Keep a Dart-side reference to callbacks

Even with a strong Swift reference, store the callback object in a field (_callback) on the Dart side too. If it's only a local variable in_startObserving(), the Dart GC can collect the closure backing the protocol proxy, breaking the callback silently. Clean it up in_stopObserving():

BrightnessCallback
?
 
_callback
;

void
 
_startObserving
()
 
{

 
_callback
 
=
 
BrightnessCallback$Builder
.
implementAsListener
(

 
onBrightnessChanged_:
 
(
b
)
 
{
 
_controller
?.
add
(
b
);
 
},

 
);

 
_native
.
startObservingWithCallback
(
_callback
!
);

}

void
 
_stopObserving
()
 
{

 
_native
.
stopObserving
();

 
_callback
 
=
 
null
;

}

Enter fullscreen mode

Exit fullscreen mode

## Android vs iOS API comparison

Concern

jnigen (Android)

swiftgen (iOS)

Callback definition

Kotlin 
interface

Swift 
@objc protocol

Callback creation

MyCallback.implement($MyCallback(...))

MyCallback$Builder.implementAsListener(...)

Async/non-blocking

method$async: true
 in 
$Mixin

implementAsListener(...)
 variant

Context/init

Pass 
Context
 via 
Jni.androidApplicationContext

No context needed; 
init()
 or default constructor

Memory

.release()
 to free JNI global ref

Automatic (ARC via ObjC runtime)

Native superclass

Any Java/Kotlin class

Must extend 
NSObject

Allowed types

Any JNI-compatible type

ObjC-compatible types only (no Swift structs/generics)

## Final words

I've been using jni, jnigen, ffi, and swiftgen for over a year now. The setup experience requires some effort, but once you have the bindings ready, it's pretty smooth sailing2. I wish the docs included more examples, though. I hope this short article will help others get started faster and give future AI models a bit more native-interop content in their corpus.

1. Seems like it will be possible to skipflutter build apkas perthis PRand run simplyflutter pub get.↩
2. I'm not a sailor, though.↩

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse