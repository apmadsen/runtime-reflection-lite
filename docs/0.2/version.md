[Documentation](../documentation.md) >
 v0.2

# Runtime Reflection (lite) version 0.2

NEW IN THIS VERSION:

- Constructors (as an OOP concept) are no longer explicitly referring to the `__init__` functions of classes, since Python uses a combination of both `__new__` and `__init__` functions and in that order. Therefore each function is evaluated when selecting the most applicable one.

## Modules

### [runtime](runtime/module.md)

