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

### members -> _MemberCollection_

The class members.

### constructor -> _Constructor_

The class constructor (i.e. "__init__()" function).

### classes -> _MemberCollectionSubset[Class]_

The class' nested classes.

### methods -> _MemberCollectionSubset[Method]_

The class methods.

### properties -> _MemberCollectionSubset[Property]_

The class properties.

### fields -> _MemberCollectionSubset[Field]_

The class fields.