[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     MemberInfo

# MemberInfo

The `MemberInfo` class contains information about a member and is used in the `MemberCollection` class.

## Properties

### name -> _str_

The member name.

### org_name -> _str_

The original member name (names of private class members are mangled by prefixing the class name).

### member_class -> _type[Member]_

The member class.

### member_type -> _MemberType_

The member type.

### access_mode -> _AccessMode_

The member access mode (or encapsulation).

### is_inherited -> _bool_

Indicates whether or not member is inherited from a base class.

### is_special -> _bool_

Indicates whether or not member is a special pythonic member (i.e. it's name starts and ends with a double underscore).

### parent -> _type[Any] | ModuleType | FrameType_

The object that defines the member.