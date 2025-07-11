[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     Class

# Class : [Member](member.md)

The `Class` class represents a class.

## Properties

### name -> _str_

The class name.

### bases -> _tuple[type[Any], ...]_

The class bases.

### members -> _[MemberCollection](member_collection.md)_

The class members.

### constructor -> _[Constructor](constructor.md)_

The class constructor (i.e. "__init__()" function).

### classes -> _[MemberCollectionSubset](member_collection_subset.md)[[Class](class.md)]_

The class' nested classes.

### methods ->  _[MemberCollectionSubset](member_collection_subset.md)[[Method](method.md)]_

The class methods.

### properties ->  _[MemberCollectionSubset](member_collection_subset.md)[[Property](property.md)]_

The class properties.

### fields ->  _[MemberCollectionSubset](member_collection_subset.md)[[Field](field.md)]_

The class fields.

### reflected -> _ReferenceType[type[Any]]_

The reflected class (a weak reference)