---
title: A new Go API for JSON - The Go Programming Language
url: https://go.dev/blog/jsonv2
site_name: tldr
content_file: tldr-a-new-go-api-for-json-the-go-programming-language
fetched_at: '2026-11-05T15:23:52.496552'
original_url: https://go.dev/blog/jsonv2
date: '2026-11-05'
description: Go 1.27 introduces new encoding/json/v2 and encoding/json/jsontext packages.
tags:
- tldr
---

# The Go Blog

# A new Go API for JSON

Michael Pratt, Joe Tsai, Daniel Martí, Johan Brandhorst-Satzkorn, Roger Peppe, Chris Hines, and Damien Neil4 November 2026

## Introduction

JavaScript Object Notation (JSON)is a simple data interchange format, the most popular data format used on the internet, and widely read and written by Go programs.
Go has included support for JSON in the standard library since well before Go 1.0.
We first we wrote aboutsupport for JSON in Gomore than 15 years ago!

Over time, packages evolve with the needs of their users, andencoding/jsonis no exception.
Last year, we wrote about anew experimental API for JSONdesigned to bring long-awaited improvements and fixes.

After additional feedback and refinement, the newencoding/json/v2andencoding/json/jsontextpackages are stable and generally available in Go 1.27!
This post is an updated version of thearticle introducing the experiment, describing the problems withencoding/json, and an introduction to the new packages.

## Problems withencoding/json

Overall,encoding/jsonhas held up well.
The idea of marshaling and unmarshaling arbitrary Go types
with some default representation in JSON, combined with the ability to
customize the representation, has proven to be highly flexible.
However, in the years since its introduction,
various users have identified numerous shortcomings.

### Behavior flaws

There are various behavioral flaws inencoding/json:

* Imprecise handling of JSON syntax: Over the years, JSON has seen
increased standardization in order for programs to properly communicate.
Generally, decoders have become stricter at rejecting ambiguous inputs,
to reduce the chance that two implementations will have different
(successful) interpretations of a particular JSON value.encoding/jsoncurrently accepts invalid UTF-8,
whereas the latest Internet Standard (RFC 8259) requires valid UTF-8.
The default behavior should report an error in the presence of invalid UTF-8,
instead of introducing silent data corruption,
which may cause problems downstream.encoding/jsoncurrently accepts objects with duplicate member names.
RFC 8259 does not specify how to handle duplicate names,
so an implementation is free to choose an arbitrary value,
merge the values, discard the values, or report an error.
The presence of a duplicate name results in a JSON value
without a universally agreed upon meaning.
This could beexploited by attackers in security applicationsand has been exploited before (as inCVE-2017-12635).
The default behavior should err on the side of safety and reject duplicate names.
* encoding/jsoncurrently accepts invalid UTF-8,
whereas the latest Internet Standard (RFC 8259) requires valid UTF-8.
The default behavior should report an error in the presence of invalid UTF-8,
instead of introducing silent data corruption,
which may cause problems downstream.
* encoding/jsoncurrently accepts objects with duplicate member names.
RFC 8259 does not specify how to handle duplicate names,
so an implementation is free to choose an arbitrary value,
merge the values, discard the values, or report an error.
The presence of a duplicate name results in a JSON value
without a universally agreed upon meaning.
This could beexploited by attackers in security applicationsand has been exploited before (as inCVE-2017-12635).
The default behavior should err on the side of safety and reject duplicate names.
* Leaking nilness of slices and maps: JSON is often used to communicate with
programs using JSON implementations that do not allownullto be unmarshaled
into a data type expected to be a JSON array or object.
Sinceencoding/jsonmarshals a nil slice or map as a JSONnull,
this may lead to errors when unmarshaling by other implementations.A surveyindicated that most Go users prefer that nil slices and maps
are marshaled as an empty JSON array or object by default.
* Case-insensitive unmarshaling: When unmarshaling, a JSON object member name
is resolved to a Go struct field name using a case-insensitive match.
This is a surprising default, a potential security vulnerability, and a performance limitation.
* Inconsistent calling of methods: Due to an implementation detail,MarshalJSONmethods declared on a pointer receiver
areinconsistently called byencoding/json. While regarded as a bug,
this cannot be fixed as too many applications depend on the current behavior.

### API deficiencies

The API ofencoding/jsoncan be tricky or restrictive:

* It is difficult to correctly unmarshal from anio.Reader.
Users often writejson.NewDecoder(r).Decode(v),
which fails to reject trailing junk at the end of the input.
* Options can be set on theEncoderandDecodertypes,
but cannot be used with theMarshalandUnmarshalfunctions.
Similarly, types implementing theMarshalerandUnmarshalerinterfaces
cannot make use of the options and there is no way to plumb options down the call stack.
For example, theDecoder.DisallowUnknownFieldsoption loses its effect
when calling a customUnmarshalJSONmethod.
* TheCompact,Indent, andHTMLEscapefunctions write to abytes.Bufferinstead of something more flexible like a[]byteorio.Writer.
This limits the usability of those functions.

### Performance limitations

Setting aside internal implementation details,
the public API commits it to certain performance limitations:

* MarshalJSON: TheMarshalJSONinterface method forces the implementation
to allocate the returned[]byte. Also, the semantics require thatencoding/jsonverify that the result is valid JSON
and also to reformat it to match the specified indentation.
* UnmarshalJSON: TheUnmarshalJSONinterface method requires that
a complete JSON value be provided (without any trailing data).
This forcesencoding/jsonto parse the JSON value to be unmarshaled
in its entirety to determine where it ends before it can callUnmarshalJSON.
Afterwards, theUnmarshalJSONmethod itself must parse the provided JSON value again.
* Lack of streaming: Even though theEncoderandDecodertypes operate
on anio.Writerorio.Reader, they buffer the entire JSON value in memory.
TheDecoder.Tokenmethod for reading individual tokens is allocation-heavy
and there is no corresponding API for writing tokens.

Furthermore, if the implementation of aMarshalJSONorUnmarshalJSONmethod
recursively calls theMarshalorUnmarshalfunction,
then the performance becomes quadratic.

## Trying to fixencoding/jsondirectly

Introducing a new, incompatible major version of a package is a heavy consideration.
If possible, we should try to fix the existing package.

While it is relatively easy to add new features,
it is difficult to change existing features.
Unfortunately, these problems are inherent consequences of the existing API,
making them practically impossible to fix within theGo 1 compatibility promise.

We could in principle declare separate names, such asMarshalV2orUnmarshalV2,
but that is tantamount to creating a parallel namespace within the same package.
This leads us toencoding/json/v2(henceforth calledv2),
where we can make these changes within a separatev2namespace
in contrast toencoding/json(henceforth calledv1).

## Building onencoding/json/jsontext

Before discussing thev2API, we first introduce theencoding/json/jsontextpackage
that lays the foundation for improvements to JSON in Go.

JSON serialization in Go can be broken down into two primary components:

* syntactic functionalitythat is concerned with processing JSON based on its grammar, and
* semantic functionalitythat defines the relationship between JSON values and Go values.

We use the terms “encode” and “decode” to describe syntactic functionality and
the terms “marshal” and “unmarshal” to describe semantic functionality.
We aim to provide a clear distinction between functionality
that is purely concerned with encoding versus that of marshaling.

This diagram provides an overview of this separation.
Purple blocks represent types, while blue blocks represent functions or methods.
The direction of the arrows approximately represents the flow of data.
The bottom half of the diagram, implemented by thejsontextpackage,
contains functionality that is only concerned with syntax,
while the upper half, implemented by thejson/v2package,
contains functionality that assigns semantic meaning to syntactic data
handled by the bottom half.

The basic API ofjsontextis the following:

package jsontext

type Encoder struct { ... }
func NewEncoder(io.Writer, ...Options) *Encoder
func (*Encoder) WriteValue(Value) error
func (*Encoder) WriteToken(Token) error

type Decoder struct { ... }
func NewDecoder(io.Reader, ...Options) *Decoder
func (*Decoder) ReadValue() (Value, error)
func (*Decoder) ReadToken() (Token, error)

type Kind byte
type Value []byte
func (Value) Kind() Kind
type Token struct { ... }
func (Token) Kind() Kind

Thejsontextpackage provides functionality for interacting with JSON
at a syntactic level and derives its name fromRFC 8259, section 2where the grammar for JSON data is literally calledJSON-text.
Since it only interacts with JSON at a syntactic level,
it does not depend on Go reflection.

TheEncoderandDecoderprovide support for encoding and decoding JSON values and tokens.
The constructorsaccept variadic optionsthat affect the particular behavior of encoding and decoding.
Unlike theEncoderandDecodertypes declared inv1,
the new types injsontextavoid muddling the distinction between syntax and
semantics and operate in a truly streaming manner.

A JSON value is a complete unit of data and is represented in Go asa named[]byte.
It is identical toRawMessageinv1, which is now a type alias tojsontext.Value.
A JSON value is syntactically composed of one or more JSON tokens.
A JSON token is represented in Go as theopaqueTokentypewith constructors and accessor methods.
It is analogous toTokeninv1but is designed represent arbitrary JSON tokens without allocation.

To resolve the fundamental performance problems with
theMarshalJSONandUnmarshalJSONinterface methods,
we need an efficient way of encoding and decoding JSON
as a streaming sequence of tokens and values.
Inv2, we introduce theMarshalJSONToandUnmarshalJSONFrominterface methods
that operate on anEncoderorDecoder, allowing the methods’ implementations
to process JSON in a purely streaming manner. Thus, thejsonpackage need not
be responsible for validating or formatting a JSON value returned byMarshalJSON,
nor would it need to be responsible for determining the boundaries of a JSON value
provided toUnmarshalJSON. These responsibilities belong to theEncoderandDecoder.

## Introducingencoding/json/v2

Building on thejsontextpackage, we now introduce theencoding/json/v2package.
It is designed to fix the problems inv1,
while remaining familiar to users of thev1package.
Our goal is that usages ofv1will operatemostlythe same if directly migrated tov2.

Here, we primarily cover the high-level API ofv2.
For examples on how to use it, we encourage readers to
studythe examples in thev2package,
the “Working with JSON” tutorial, or
readAnton Zhiyanov’s blog covering the topic.

The basic API ofv2is the following:

package json

func Marshal(in any, opts ...Options) (out []byte, err error)
func MarshalWrite(out io.Writer, in any, opts ...Options) error
func MarshalEncode(out *jsontext.Encoder, in any, opts ...Options) error

func Unmarshal(in []byte, out any, opts ...Options) error
func UnmarshalRead(in io.Reader, out any, opts ...Options) error
func UnmarshalDecode(in *jsontext.Decoder, out any, opts ...Options) error

TheMarshalandUnmarshalfunctions
have a signature similar tov1, but accept options to configure their behavior.
TheMarshalWriteandUnmarshalReadfunctions
directly operate on anio.Writerorio.Reader,
avoiding the need to temporarily construct anEncoderorDecoderjust to write or read from such types.
TheMarshalEncodeandUnmarshalDecodefunctions
operate on ajsontext.Encoderandjsontext.Decoderand
is actually the underlying implementation of the previously mentioned functions.
Unlikev1, options are a first-class argument to each of the marshal and unmarshal functions,
greatly extending the flexibility and configurability ofv2.
There areseveral options availableinv2which are not covered by this article.

### Type-specified customization

Similar tov1,v2allows types to define their own JSON representation
by satisfying particular interfaces.

type Marshaler interface {
 MarshalJSON() ([]byte, error)
}
type MarshalerTo interface {
 MarshalJSONTo(*jsontext.Encoder) error
}

type Unmarshaler interface {
 UnmarshalJSON([]byte) error
}
type UnmarshalerFrom interface {
 UnmarshalJSONFrom(*jsontext.Decoder) error
}

TheMarshalerandUnmarshalerinterfaces
are identical to those inv1.
The newMarshalerToandUnmarshalerFrominterfaces
allow a type to represent itself as JSON using ajsontext.Encoderorjsontext.Decoder.
This allows options to be forwarded down the call stack, since options
can be retrieved via theOptionsaccessor method on theEncoderorDecoder.

SeetheOrderedObjectexamplefor how to implement a custom type that maintains the ordering of JSON object members.

### Caller-specified customization

Inv2, the caller ofMarshalandUnmarshalcan also specify
a custom JSON representation for any arbitrary type,
where caller-specified functions take precedence over type-defined methods
or the default representation for a particular type.

func WithMarshalers(*Marshalers) Options

type Marshalers struct { ... }
func MarshalFunc[T any](fn func(T) ([]byte, error)) *Marshalers
func MarshalToFunc[T any](fn func(*jsontext.Encoder, T) error) *Marshalers

func WithUnmarshalers(*Unmarshalers) Options

type Unmarshalers struct { ... }
func UnmarshalFunc[T any](fn func([]byte, T) error) *Unmarshalers
func UnmarshalFromFunc[T any](fn func(*jsontext.Decoder, T) error) *Unmarshalers

MarshalFuncandMarshalToFuncconstruct a custom marshaler that can be passed to aMarshalcall
usingWithMarshalersto override the marshaling of particular types.
Similarly,UnmarshalFuncandUnmarshalFromFuncsupport similar customization forUnmarshal.

TheProtoJSONexampledemonstrates how this feature allows serialization of allproto.Messagetypes
to be handled by theprotojsonpackage.

### Behavior differences

Whilev2aims to behavemostlythe same asv1,
its behavior has changedin some waysto address problems inv1, most notably:

* v2reports an error in the presence of invalid UTF-8.
* v2reports an error if a JSON object contains a duplicate name.
* v2marshals a nil Go slice or Go map as an empty JSON array or JSON object, respectively.
* v2unmarshals a JSON object into a Go struct using a
case-sensitive match from the JSON member name to the Go field name.
* v2redefines theomitemptytag option to omit a field if it would have
encoded as an “empty” JSON value (which arenull,"",[], and{}).
* v2reports an error when trying to serialize atime.Duration,
which currently hasno default representation,
but provides options to let the caller decide.

For most behavior changes, there is a struct tag option or caller-specified option
that can configure the behavior to operate underv1orv2semantics,
or even other caller-determined behavior.
See “Migrating to v2” for more information.

### Performance optimizations

TheMarshalperformance ofv2is roughly at parity withv1.
Sometimes it is slightly faster, but other times it is slightly slower.
TheUnmarshalperformance ofv2is significantly faster thanv1,
with benchmarks demonstrating improvements of up to 10x.

In order to obtain greater performance gains,
existing implementations ofMarshalerandUnmarshalershould
migrate to also implementMarshalerToandUnmarshalerFrom,
so that they can benefit from processing JSON in a purely streaming manner.
For example, recursive parsing of OpenAPI specifications inUnmarshalJSONmethods
significantly hurt performance in a particular service of Kubernetes
(seekubernetes/kube-openapi#315),
while switching toUnmarshalJSONFromimproved performance by orders of magnitude.

For more benchmark details, see thego-json-experiment/jsonbenchrepository.

On top of structural improvements, we’re continuing to invest in performance optimizations in the implementation forcaseswhere thev2implementation is slower thanv1.
You can expect additional improvements in Go 1.28.

## Compatibility

TheGo 1 compatibility promiseis a core guarantee from the Go project that allows developers to build applications that will stand the test of time and continue working on future versions of Go.

The originalencoding/jsonand newencoding/json/v2packages are of course both subject to the Go 1 compatibility promise.
Applications usingv1will continue to be supported indefinitely and need not ever migrate tov2.

That said, when designing thev2packages we wanted to do better than keepingv1supported.
We wanted to ensure thatv1andv2arecompatible with one anotherso that packages using different versions can work together.
Doing so allows a smooth ecosystem migration rather than forcing users to use one version or another due to the choices of their dependencies.

For instance, suppose your package usesv2to marshal a struct containing a field with a type defined in another package.
That package may use the originalv1MarshalJSONmethod to define its marshaling behavior.
No problem,v2supportsMarshalJSONmethods, so marshaling will continue working as expected.

Vice versa, suppose your package usesv1to marshal the same struct.
The other package may use thev2MarshalJSONTomethod for better performance.
No problem here either, as thev1implementation supportsv2’sMarshalJSONTomethod under the hood.

We’ve achieved this by designing the new packages such that, under the hood,v1is implemented in terms ofv2.
As mentioned above,v2supports a variety ofOptions.
Each behavior difference is controlled by one of the these options.
Thus,v1can be implemented in terms ofv2by passing the full set ofv1compatibility options.

With this approach, backwards-compatible additions such as new methods (e.g.,MarshalJSONTo) or new struct tags (e.g.,embed) are automatically supported to the benefit of existingv1users.

## Migration

Implementingv1in terms ofv2options has the additional benefit of allowing gradual migration of callsites.

encoding/jsondocumentsthe full set of behavior differences betweenv1andv2, and which option controls that behaviors.

Many applications can migrate directly tov2with no visible behavior changes, but applications that depend onv1behavior can use the options to change only the behaviors they depend on.

For example, we can select allv2behavior except for allowing duplicate names:

json.Marshal(..., json.DefaultOptionsV2(), jsontext.AllowDuplicateName(true))

Alternatively, we can select allv1behavior except for disallowing duplicate names:

json.Marshal(..., jsonv1.DefaultOptionsV1(), jsontext.AllowDuplicateName(false))

Theencoding/json/v2Migration Guidegoes into more detail, covering a variety of scenarios for approaching migration of an application fromv1tov2.

## More information

For additional references on working with the new JSON packages, see:

* The “Working with JSON” tutorial,
* Theencoding/json/v2andencoding/json/jsontextpackage documentation,
* Theencoding/jsonpackage’sv2comparison documentation,
* and theencoding/json/v2Migration Guide.

## A long time coming

The planning for a new major version ofencoding/jsonspanned years.
In late 2020, spurred on by the inability to fix issues in the current package,
Daniel Martí (one of the maintainers ofencoding/json) first drafted his
thoughts onwhat a hypotheticalv2package should look like.
Separately, after previous work on theGo API for Protocol Buffers,
Joe Tsai was disappointed thattheprotojsonpackageneeded to use a custom JSON implementation becauseencoding/jsonwas
neither capable of adhering to the stricter JSON standard that the
Protocol Buffer specification required,
nor of efficiently serializing JSON in a streaming manner.

Believing a brighter future for JSON was both beneficial and achievable,
Daniel and Joe joined forces to brainstorm onv2andstarted to build a prototype(with the initial code being a polished version of the JSON serialization logic from the Go protobuf module).
Over time, a few others (Roger Peppe, Chris Hines, Johan Brandhorst-Satzkorn, Damien Neil, Austin Clements, and Michael Pratt)
joined the effort by providing design review, code review, and regression testing.
Many of the early discussions are publicly available in ourrecorded meetingsandmeeting notes.
Later discussions are available in ourencoding/json/v2working group meeting notes.

This work has been public since the beginning,
and we increasingly involved the wider Go community,
first with aGopherCon talkanddiscussion posted in late 2023,formal proposal posted in early 2025,
and finallyadoptingencoding/json/v2as a Go experiment in Go 1.25for wider-scale testing by all Go users.

Thev2effort took about 6 years to reach this point,
incorporating feedback from many contributors and also gaining valuable
empirical experience from use in production settings.

It’s worth noting that it’s largely been developed and promoted by people
not employed by Google, demonstrating that the Go project is a collaborative endeavor
with a thriving global community dedicated to improving the Go ecosystem.

Thank you to everyone that contributed!

Previous article:Our Response To The eMudhra Key Disclosure IncidentBlog Index