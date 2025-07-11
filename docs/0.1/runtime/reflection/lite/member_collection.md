[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     MemberCollection

# MemberCollection : Mapping[str, tuple[[MemberInfo](member_info.md), Member]]

The `MemberCollection` class is a collection of members structured as a dictionary.

## Functions

### subset(member_class: _type[T]_) -> _[MemberCollectionSubset](member_collection_subset.md)[T]_:

Creates a subset of members matching the specified class `T` derived from `Member`.

### subset(member_class: _type[T]_, predicate: _Callable[[[MemberInfo](member_info.md)], bool]_) -> _[MemberCollectionSubset](member_collection_subset.md)[T]_:

Creates a subset of members matching the specified class `T` derived from `Member` and where predicate returns `True`.

### subset_modules() -> _[MemberCollectionSubset](member_collection_subset.md)[[Module](module.md)]_

Creates a subset of `Module` members

### subset_classes() -> _[MemberCollectionSubset](member_collection_subset.md)[[Class](class.md)]_

Creates a subset of `Class` members

### subset_methods() -> _[MemberCollectionSubset](member_collection_subset.md)[[Method](method.md)]_

Creates a subset of `Method` members

### subset_functions() -> _[MemberCollectionSubset](member_collection_subset.md)[[Function](function.md)]_

Creates a subset of `Function` members

### subset_properties() -> _[MemberCollectionSubset](member_collection_subset.md)[[Property](property.md)]_

Creates a subset of `Property` members

### subset_fields() -> _[MemberCollectionSubset](member_collection_subset.md)[[Field](field.md)]_

Creates a subset of `Field` members

### subset_variables() -> _[MemberCollectionSubset](member_collection_subset.md)[[Variable](variable.md)]_

Creates a subset of `Variable` members