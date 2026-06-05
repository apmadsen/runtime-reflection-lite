[Documentation](../../../../documentation.md) >
 [v0.2](../../../version.md) >
  [runtime](../../module.md) >
   [reflection](../module.md) >
    [lite](module.md) >
     reflect

# reflect(obj: _type[Any]_) -> _[Class](class.md)_

Reflects on a class object.

## Parameters

- obj `type[Any]`: The class to reflect upon.

# reflect(obj: _ModuleType_) -> _[Module](_module.md)_

Reflects on a module.

## Parameters

- obj `ModuleType`: The module to reflect upon.

### Example

```python
from runtime.reflection.lite import reflect

class Class1:
     def __init__(self, value: str):
          self.__value = value

     def do_something(self, suffix: str | None = None) -> str:
          return self.__value + (suffix or "")

reflection = reflect(Class1) # -> Class
```