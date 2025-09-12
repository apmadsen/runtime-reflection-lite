[Documentation](../../../../documentation.md) >
 [v0.2](../../../version.md) >
  [runtime](../../module.md) >
   [reflection](../module.md) >
    [lite](module.md) >
     get_constructor

# is_prototypically_equivalent(cls: _type[Any]_, protocol: _type[Any]_) -> _bool_

The `is_prototypically_equivalent` function checks if class matches a given protocol class. While Python has limited support for comparing classes with protocols via the builtin `isinstance` and `issubclass` functions, this function does an indepth comparison of all constructors, properties, functions and methods, including their signatures.

> Note #1: The protocol class doesn't necessarily have to be a subclass of `typing.Protocol`, but it's considered good practise, and helps the IDE/type checkers.

> Note #2: When the protocol class is a subclass of `typing.Protocol`, constructors cannot be checked due to the way `typing.Protocol` replaces the `__init__` function with an empty one.

## Parameters

- cls `type[Any]`: The class to check.
- protocol `type[Any]`: The protocol class to check against.


### Example

```python
from runtime.reflection.lite import is_prototypically_equivalent

class Proto1:

     def __init__(self, prop1: str, prop2: int):
          ...

     @property
     def prop1(self) -> str:
          ...

     @property
     def prop2(self) -> int:
          ...

class Proto2:

     @property
     def prop1(self) -> str:
          ...
     @property
     def prop3(self) -> int:
          ...

class Class1:

     def __init__(self, prop1: str, prop2: int):
          ...

     @property
     def prop1(self) -> str:
          ...

     @property
     def prop2(self) -> int:
          ...

assert is_prototypically_equivalent(Class1, Proto1)
assert not is_prototypically_equivalent(Class1, Proto2)
```