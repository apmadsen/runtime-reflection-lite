[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     get_members

# get_members(obj: _type[Any] | ModuleType | FrameType_) -> _list[Member]_

The `get_members` function gets the members (functions and properties) of a class, module or frame.

## Parameters

- obj `type[Any] | ModuleType | FrameType`: The class, module or frame of which to get members.

### Example:

```python
import runtime.reflection.lite
from runtime.reflection.lite import get_members

members = get_members(runtime.reflection.lite)
functions = members.subset_functions()
classes = members.subset_classes()

info, member = functions["get_signature"]
assert info.access_mode == runtime.reflection.lite.AccessMode.PUBLIC
assert member.kind == runtime.reflection.lite.FunctionKind.FUNCTION

assert "Member" in classes
```