[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     Delegate

# Delegate : [Member](member.md)

The `Delegate` class represents a class delegate field. A delegate is am object which has a `__get__(instance: objuect, owner: type)` function.

## Properties

### delegate_type -> _type[Any] | None_

The delegate fields type annotation or inferred type.

### parent_cls -> _type[Any]_

The class on which the delegate field is defined.

### reflected -> _Any_

The reflected delegate (not a weak reference because not all objects support this)