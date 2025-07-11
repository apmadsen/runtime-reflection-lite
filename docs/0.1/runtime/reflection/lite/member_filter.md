[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [runtime](/docs/0.1/runtime/module.md) >
   [reflection](/docs/0.1/runtime/reflection/module.md) >
    [lite](/docs/0.1/runtime/reflection/lite/module.md) >
     MemberFilter

# MemberFilter : Enum

The `MemberFilter` class is a bitmap of the filter options which can be used in the `get_members` function.

## Members
- MODULES `1`: Return modules
- CLASSES `2`: Return classes
- FUNCTIONS_AND_METHODS `4`: Return functions and methods
- PROPERTIES `8`: Return properties
- FIELDS_AND_VARIABLES `16`: Return fields and variables
- DELEGATES `32`: Return delegates
- PROTECTED `128`: Return protected members (attributes starting with a single underscore)
- PRIVATE `192`: Return private and protected attributes (members starting with a single underscore or double underscore)
- SPECIAL `256`: Return special members (attributes starting and ending with a double underscore)
- DEFAULT `511`: Return all members