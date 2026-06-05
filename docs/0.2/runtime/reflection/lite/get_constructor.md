[Documentation](../../../../documentation.md) >
 [v0.2](../../../version.md) >
  [runtime](../../module.md) >
   [reflection](../module.md) >
    [lite](module.md) >
     get_constructor

# get_constructor(cls: _type[Any]_) -> _[Signature](signature.md)_

> __Updates as of version 0.2:__
> - The term _constructor_ no longer explicitly refer to the`__init__` function of a class. Instead both `__new__` and `__init__` functions are evaluated, and the most applicable one is selected. This is because of how `__new__` functions take precedence over `__init__` functions when instantiating classes.
> - When no `__new__` or `__init__` methods are defined on a class, the returned signature will now default to one without any paramaters even though `object.__new__` and `object.__init__` is defined as `(*args, **kwargs)`.

The `get_constructor` function gets the signature of the specified class' constructor. Note that overloads aren't taken into account and that in certain cases, constructors may not return an instance of the class itself (if a special
`__new__` function is defined).



## Parameters

- cls `type[Any]`: The class of which the constructor is reflected.
