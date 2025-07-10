[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     MemberCollection

# MemberCollection : Mapping[str, tuple[MemberInfo, Member]]

The `MemberCollection` class is a collection of members structured as a dictionary.

## Functions

### subset(member_class: _type[T]_) -> _MemberCollectionSubset[T]_:

Creates a subset of members matching the specified class `T` derived from `Member`.

### subset(member_class: _type[T]_, predicate: _Callable[[MemberInfo], bool]) -> _MemberCollectionSubset[T]_:

Creates a subset of members matching the specified class `T` derived from `Member` and where predicate returns `True`.

### subset_modules() -> _MemberCollectionSubset[Module]_

Creates a subset of `Module` members

### subset_classes() -> _MemberCollectionSubset[Class]_

Creates a subset of `Class` members

### subset_methods() -> _MemberCollectionSubset[Method]_

Creates a subset of `Method` members

### subset_functions() -> _MemberCollectionSubset[Function]_

Creates a subset of `Function` members

### subset_properties() -> _MemberCollectionSubset[Property]_

Creates a subset of `Property` members

### subset_fields() -> _MemberCollectionSubset[Field]_

Creates a subset of `Field` members

### subset_variables() -> _MemberCollectionSubset[Variable]_

Creates a subset of `Variable` members