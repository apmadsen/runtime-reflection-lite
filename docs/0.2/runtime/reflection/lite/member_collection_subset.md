[Documentation](../../../../documentation.md) >
 [v0.2](../../../version.md) >
  [runtime](../../module.md) >
   [reflection](../module.md) >
    [lite](module.md) >
     MemberCollectionSubset

# MemberCollectionSubset : Iterable[tuple[[MemberInfo](member_info.md), T]]

The `MemberCollectionSubset` class is a collection of members created as a subset of an ordinary `MemberCollection`.

## Functions

### subset(predicate: _Callable[[[MemberInfo](member_info.md)], bool]) -> _MemberCollectionSubset[T]_:

Creates a subsets from the subset using a predicate function.
