[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [runtime](/docs/0.0/runtime/module.md) >
   [reflection](/docs/0.0/runtime/reflection/module.md) >
    [lite](/docs/0.0/runtime/reflection/lite/module.md) >
     reflect_function

# reflect_function(fn: _AnyFunction_, cls: _object | None_ = _None_) -> _Signature_

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