[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     reflect_function

# reflect_function(fn: _AnyFunction_, cls: _object | None_ = _None_) -> _[Signature](signature.md)_

> DEPRECATED SINCE VERSION 0.1.0. USE [get_signature](get_signature.md) INSTEAD...

The `reflect_function` function gets the signature of the specified function. For edge cases, it may be necessary to include the _cls_ parameter.

## Parameters

- fn `AnyFunction`: The function to reflect upon.
- cls `type[Any]`: The class to which the function belongs (if any). Defaults to `None`.

### Example

```python
from runtime.reflection.lite import reflect_function

class Class1:
     def __init__(self, value: str):
          self.__value = value

     def do_something(self, suffix: str | None = None) -> str:
          return self.__value + (suffix or "")

signature1 = reflect_function(Class1.do_something) # -> (suffix: str | None) -> str
signature2 = reflect_function(Class1.__init__) # -> (value: str)
```