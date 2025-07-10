[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     get_constructor

# get_constructor(cls: _type[Any]_) -> _Signature_

The `get_constructor` function gets the signature of the specified class' constructor. Note that overloads aren't taken into account.
This function returns the same signature as `get_signature(getattr(cls, "__init__"), cls)`.

## Parameters

- cls `type[Any]`: The class of which the constructor is reflected.
