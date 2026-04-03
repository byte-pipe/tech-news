---
title: Use Your Type System • Chris Dzombak
url: https://www.dzombak.com/blog/2025/07/use-your-type-system/
site_name: hackernews
fetched_at: '2025-07-25T10:20:51.260688'
original_url: https://www.dzombak.com/blog/2025/07/use-your-type-system/
author: ingve
date: '2025-07-25'
published_date: '2025-07-24T14:29:29.000Z'
---

Today I'm discussing a trivially simple technique that I've rarely seen used in production codebases.

In programming, we often need to deal with simple values that can be represented by simple, generic types built into our programming language or provided by libraries: types like integer, string, or UUID.

In any nontrivial codebase, this inevitably leads to bugs when, for example, a string representing a user ID gets used as an account ID, or when a critical function accepts three integer arguments and someone mixes up the correct order when calling it.

A much better solution is todefine different typesand use them when representing different things!intorstringare excellent building blocks, but passing them around your system as-is means you slowly but inevitably lose important context:what they actually represent.

## Example

Here's a trivial example of what that might look like. Imagine if, instead of using plain old UUIDs, each of your models defined its own ID type:

type AccountID uuid.UUID
type UserID uuid.UUID

func UUIDTypeMixup() {
 {
 userID := UserID(uuid.New())
 DeleteUser(userID)
 // no error
 }

 {
 accountID := AccountID(uuid.New())
 DeleteUser(accountID)
 // ^ error: Cannot use 'accountID' (type AccountID) as the type UserID
 }

 {
 accountID := uuid.New()
 DeleteUserUntyped(accountID)
 // no error at compile time; likely error at runtime
 }
}

## In libwx

I previously discussed this in my 2015 talk, "String is not a sufficient type." I've found a great demonstration case for the technique in my weather & atmospheric calculations library for Golang,libwx. This library definestypes for every measurement it deals with, along with methods for converting between the different types (for example,Km.Miles()).

This prevents the user from making mistakes that would be all too easy if the library dealt entirely infloat64s:

I've shared a slightly longer example on GitHub:

// Declare a temperature in Fahrenheit
temp := libwx.TempF(84)

// Declare a relative humidity in percent:
humidity := libwx.RelHumidity(67)

// Attempt to calculate the dew point using a function that takes
// Celsius instead of Fahrenheit:
fmt.Printf("Dew point: %.1fºF\n",
	libwx.DewPointC(temp, humidity))

// Note the compiler prevents us from making this mistake; it gives us
// the following error:
// Cannot use 'temp' (type libwx. TempF) as the type TempC

// Attempt to calculate the dew point, but mix up the function arga:
fmt.Printf("Dew point: %.1fºF\n",
	libwx.DewPointF(humidity, temp))

// Again, the compiler prevents us from making this error.

## Conclusion

Your type system is there to help you. Use it.

Your models should each have their own ID type. Public and even private functions should often avoid dealing in floats or integers alone.

I've seenso manybugs in real systems due to mixing up integers, strings, or UUIDs that represent different things. Meanwhile, it's simple to set up types that entirely eliminate this class of bug, even in a language like Go that isn't known for having a particularly powerful type system. It's absolutely astounding to me that this technique is not broadly used.

You can find all the code used in this post on GitHub:

GitHub - cdzombak/libwx_types_lab
Contribute to cdzombak/libwx_types_lab development by creating an account on GitHub.
GitHub
cdzombak
