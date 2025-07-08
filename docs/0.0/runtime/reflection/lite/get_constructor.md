[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [runtime](/docs/0.0/runtime/module.md) >
   [reflection](/docs/0.0/runtime/reflection/module.md) >
    [lite](/docs/0.0/runtime/reflection/lite/module.md) >
     get_constructor

# get_constructor(cls: _type[Any]_) -> _Signature_

The `get_constructor` function gets the signature of the specified class' constructor. Note that overloads aren't taken into account.
This function returns the same signature as `reflect_function(getattr(cls, "__init__"), cls)`.

## Parameters

- cls `type[Any]`: The class of which the constructor is reflected.
