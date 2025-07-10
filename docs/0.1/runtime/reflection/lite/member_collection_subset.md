[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     MemberCollectionSubset

# MemberCollectionSubset : Iterable[tuple[MemberInfo, T]]

The `MemberCollectionSubset` class is a collection of members created as a subset of an ordinary `MemberCollection`.

## Functions

### subset(predicate: _Callable[[MemberInfo], bool]) -> _MemberCollectionSubset[T]_:

Creates a subsets from the subset using a predicate function.
