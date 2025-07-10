[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     get_signature

# get_signature(fn: _AnyFunction_) -> _Signature_

# get_signature(fn: _AnyFunction_, parent: _type[Any] | ModuleType | FrameType_) -> _Signature_

The `get_signature` function gets the signature of the specified function. For edge cases, it may be necessary to include the _parent_ parameter.

## Parameters

- fn `AnyFunction`: The function to reflect upon.
- parent `type[Any]`: The class to which the function belongs (if any). Defaults to `None`.

### Example

```python
from runtime.reflection.lite import get_signature

class Class1:
     def __init__(self, value: str):
          self.__value = value

     def do_something(self, suffix: str | None = None) -> str:
          return self.__value + (suffix or "")

signature1 = get_signature(Class1.do_something) # -> (suffix: str | None) -> str
signature2 = get_signature(Class1.__init__) # -> (value: str)
```