[![Test](https://github.com/apmadsen/runtime-reflection-lite/actions/workflows/python-test.yml/badge.svg)](https://github.com/apmadsen/runtime-reflection-lite/actions/workflows/python-test.yml)
[![Coverage](https://github.com/apmadsen/runtime-reflection-lite/actions/workflows/python-test-coverage.yml/badge.svg)](https://github.com/apmadsen/runtime-reflection-lite/actions/workflows/python-test-coverage.yml)
[![Stable Version](https://img.shields.io/pypi/v/runtime-reflection-lite?label=stable&sort=semver&color=blue)](https://github.com/apmadsen/runtime-reflection-lite/releases)
![Pre-release Version](https://img.shields.io/github/v/release/apmadsen/runtime-reflection-lite?label=pre-release&include_prereleases&sort=semver&color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/runtime-reflection-lite)
[![PyPI Downloads](https://static.pepy.tech/badge/runtime-reflection-lite/week)](https://pepy.tech/projects/runtime-reflection-lite)

# Runtime Reflection Lite

Lightweight runtime reflection for Python — with proper type awareness.

## 🚀 Why this exists

Python has powerful introspection capabilities, but working with them in practice can be messy:

- Type hints are not always resolved
- Metadata is scattered across different APIs
- Understanding structure at runtime requires a lot of boilerplate

This library provides a **clean and consistent abstraction layer** for inspecting Python code at runtime.

👉 The goal is simple:
Make runtime structure **easy to access, understand, and use**


## ✨ Features

- 🔍 Inspect modules, classes, and functions
- 🧠 Resolve type hints (including forward references)
- 🔐 Understand encapsulation and structure
- ⚡ Lightweight implementation (no source code parsing)
- 🧩 Clean API for building higher-level tooling



## 📦 Use cases

This library is especially useful when building:

- Frameworks
- Dependency injection systems
- Code analysis tools
- Runtime validation systems
- Developer tooling

👉 If you're working with **dynamic architectures**, this removes a lot of friction.


## 🏗 Design philosophy

Unlike heavier reflection systems, this project deliberately avoids:

- ❌ Parsing source code
- ❌ Full AST inspection

This keeps it:

✅ Fast
✅ Predictable
✅ Easy to integrate


## ⚙️ Example

```python
from runtime.reflection.lite import MemberFilter, MemberInfo, Class, Method, reflect, get_signature, get_members

class Class1:
     def __init__(self, value: str):
          self.__value = value

     def do_something(self, suffix: str | None = None) -> str:
          return self.__value + (suffix or "")

reflection: Class = reflect(Class1)
reflection.constructor.signature # -> (value: str)
member_info, method = reflection.members.subset_methods()["do_something"] # -> tuple[MemberInfo, Method]

signature1 = get_signature(Class1.do_something) # -> (suffix: str | None) -> str
signature2 = get_signature(Class1.__init__) # -> (value: str)

members = get_members(Class1, filter = MemberFilter.FUNCTIONS_AND_METHODS)
member_info, member = members["do_something"] # -> MemberInfo, Member
```

## Full documentation

[Go to documentation](https://github.com/apmadsen/runtime-reflection-lite/blob/main/docs/documentation.md)