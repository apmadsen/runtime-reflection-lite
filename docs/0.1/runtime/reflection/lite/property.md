[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     Property

# Property : [Member](member.md)

The `Property` class represents a class property.

## Properties

### bound_cls -> _type[Any]_

The propertys bound class.

### property_type -> _type[Any]_

The property type.

### getter -> _Signature_

The signature of the property getter.

### setter -> _Signature | None_

The signature of the property setter (if any).

### deleter -> _Signature | None_

The signature of the property deleter (if any).

### is_readonly -> _bool_

Indicates if property is readonly or not (i.e. has a setter).

### is_abstract -> _bool_

Indicates if property is abstract.