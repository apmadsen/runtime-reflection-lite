[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     Module

# Module : [Member](member.md)

The `Module` class represents a module.

## Properties

### name -> _str_

The module name.

### members -> _[MemberCollection](member_collection.md)_

The module members.

### classes -> _[MemberCollectionSubset](member_collection_subset.md)[[Class](class.md)]_

The modules classes.

### functions -> _[MemberCollectionSubset](member_collection_subset.md)[[Function](function.md)]_

The modules functions.

### modules -> _[MemberCollectionSubset](member_collection_subset.md)[Module]_

The modules imported modules.

### variables -> _[MemberCollectionSubset](member_collection_subset.md)[[Variable](variable.md)]_

The modules variables.