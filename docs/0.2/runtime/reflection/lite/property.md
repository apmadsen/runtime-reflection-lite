[Documentation](../../../../documentation.md) >
 [v0.2](../../../version.md) >
  [runtime](../../module.md) >
   [reflection](../module.md) >
    [lite](module.md) >
     Property

# Property : [Member](member.md)

The `Property` class represents a class property.

## Properties

### bound_cls -> _type[Any]_

The propertys bound class.

### property_type -> _type[Any]_

The property type.

### getter -> _[Signature](signature.md)_

The signature of the property getter.

### setter -> _[Signature](signature.md) | None_

The signature of the property setter (if any).

### deleter -> _[Signature](signature.md) | None_

The signature of the property deleter (if any).

### is_readonly -> _bool_

Indicates if property is readonly or not (i.e. has a setter).

### is_abstract -> _bool_

Indicates if property is abstract.

### reflected -> _property_

The reflected function (not a weak reference because the property object does not support this)