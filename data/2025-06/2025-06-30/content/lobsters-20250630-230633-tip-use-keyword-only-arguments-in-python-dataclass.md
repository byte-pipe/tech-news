---
title: 'Tip: Use keyword-only arguments in Python dataclasses – ChipLog — Christian Hammond'
url: https://chipx86.blog/2025/06/29/tip-use-keyword-only-arguments-in-python-dataclasses/
site_name: lobsters
fetched_at: '2025-06-30T23:06:33.024161'
original_url: https://chipx86.blog/2025/06/29/tip-use-keyword-only-arguments-in-python-dataclasses/
date: '2025-06-30'
description: Python dataclasses are a really nice feature for constructing classes that primarily hold or work with data. They can be a good alternative to using dictionaries, since they allow you to add methods, dynamic properties, and subclasses. They can also be a good alternative to building your own class by hand, since they don't need…
tags: python
---

Pythondataclassesare a really nice feature for constructing classes that primarily hold or work with data. They can be a good alternative to using dictionaries, since they allow you to add methods, dynamic properties, and subclasses. They can also be a good alternative to building your own class by hand, since they don’t need a custom__init__()that reassigns attributes and provide methods like__eq__()out of the box.

One small tip to keeping dataclasses maintainable is to always construct them withkw_only=True, like so:

from dataclasses import dataclass

@dataclass(kw_only=True)
class MyDataClass:
 x: int
 y: str
 z: bool = True

This will construct an__init__()that looks like this:

class MyDataClass:
 def __init__(
 self,
 *,
 x: int,
 y: str,
 z: bool = True,
 ) -> None:
 self.x = x
 self.y = y
 self.z = z

Instead of:

class MyDataClass:
 def __init__(
 self,
 x: int,
 y: str,
 z: bool = True,
 ) -> None:
 self.x = x
 self.y = y
 self.z = z

That*in the argument list means everything that follows must be passed as a keyword argument, instead of a positional argument.

There are two reasons you probably want to do this:

1. It allows you to reorder the fields on the dataclass without breaking callers. Positional arguments means a caller can useMyDataClass(1, 'foo', False), and if you remove/reorder any of these arguments, you’ll break those callers unexpectedly. By forcing callers to useMyDataClass(x=1, y='foo', z=False), you remove this risk.
2. It allows subclasses to add required fields. Normally, any field with a default value (likezabove) will force any fields following it to also have a default. And that includesallfields defined by subclasses. Usingkw_only=Truegives subclasses the flexibility to decide for themselves which fields must be provided by the caller and which have a default.

These reasons are more important for library authors than anything. We spend a lot of time trying to ensure backwards-compatibility and forwards-extensibility inReview Board, so this is an important topic for us. And if you’re developing something reusable with dataclasses, it might be for you, too.

Update:One important point I left out is Python compatibility. This flag was introduced in Python 3.10, so if you’re supporting older versions, you won’t be able to use this just yet. If you want to optimistically enable this just on 3.10+, one approach would be:

import sys
from dataclasses import dataclass

if sys.version_info[:2] >= (3, 10):
 dataclass_kwargs = {
 'kw_only': True,
 }
else:
 dataclass_kwargs = {}

...

@dataclass(**dataclass_kwargs)
class MyDataClass:
 ...
...

But this won’t solve the subclassing issue, so you’d still need to ensure any subclasses use default arguments if you want to support versions prior to 3.10.
