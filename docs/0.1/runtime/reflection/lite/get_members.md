[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     get_members

# get_members(obj: _type[Any] | ModuleType | FrameType_) -> _[MemberCollection](member_collection.md)_
The `get_members` function gets the members (functions and properties) of a class, module or frame.

## Parameters

- obj `type[Any] | ModuleType | FrameType`: The class, module or frame of which to get members.

# get_members(obj: _type[Any] | ModuleType | FrameType_, *, filter: _MemberFilter_) -> _[MemberCollection](member_collection.md)_
The `get_members` function gets the members (functions and properties) of a class, module or frame.

## Parameters

- obj `type[Any] | ModuleType | FrameType`: The class, module or frame of which to get members.
- filter `MemberFilter`: A filter defining which members are returned.

# get_members(obj: _type[Any] | ModuleType | FrameType_, *, predicate: _Callable[[[MemberInfo](member_info.md)], bool]_) -> _[MemberCollection](member_collection.md)_

The `get_members` function gets the members (functions and properties) of a class, module or frame.

## Parameters

- obj `type[Any] | ModuleType | FrameType`: The class, module or frame of which to get members.
- predicate `(MemberInfo) -> bool`: A predicate function used to filter the members returned.

# get_members(obj: _type[Any] | ModuleType | FrameType_, *, filter: _MemberFilter_, predicate: _Callable[[[MemberInfo](member_info.md)], bool]_) -> _[MemberCollection](member_collection.md)_

The `get_members` function gets the members (functions and properties) of a class, module or frame.

## Parameters

- obj `type[Any] | ModuleType | FrameType`: The class, module or frame of which to get members.
- filter `MemberFilter`: A filter defining which members are returned.
- predicate `(MemberInfo) -> bool`: A predicate function used to filter the members returned.

### Example:

```python
import runtime.reflection.lite
from runtime.reflection.lite import MemberFilter, get_members

members = get_members(runtime.reflection.lite, filter = MemberFilter.CLASSES | MemberFilter.FUNCTIONS_AND_METHODS)
functions = members.subset_functions()
classes = members.subset_classes()

info, member = functions["get_signature"]
assert info.access_mode == runtime.reflection.lite.AccessMode.PUBLIC
assert member.kind == runtime.reflection.lite.FunctionKind.FUNCTION

assert "Member" in classes
```