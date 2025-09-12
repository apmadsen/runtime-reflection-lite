from typing import Any

from runtime.reflection.lite.core.objects.parameter_kind import ParameterKind
from runtime.reflection.lite.core.objects.signature import Signature
from runtime.reflection.lite.core.objects.member_filter import MemberFilter
from runtime.reflection.lite.core.attributes import INIT, NEW
from runtime.reflection.lite.core import get_signature, get_members, DEFAULT_CTOR

def get_constructor(cls: type[Any]) -> Signature: # pragma: no cover
    """Gets the signature of the specified class' constructor. Note that overloads aren't taken into account.

    Args:
        cls (type[Any]): The class reflected.

    Returns:
        Signature: Returns a function signature.
    """

    attrs = {
        member: getattr(cls, member)
        for member in (NEW, INIT)
        if hasattr(cls, member)
    }
    applicable_constructor = INIT

    if NEW in attrs and attrs[NEW] is not object.__new__:
        applicable_constructor = NEW

    if attrs[applicable_constructor] in (object.__init__, object.__new__):
        return DEFAULT_CTOR

    return get_signature(getattr(cls, applicable_constructor), cls)

def has_parameterless_constructor(cls: type[Any]) -> bool:
    """Checks if type has a parameterless constructor.

    Args:
        cls (type[Any]): The class reflected.

    Returns:
        bool: Returns True if type can be instantiated without parameters.
    """
    ctor = get_constructor(cls)

    if ctor is DEFAULT_CTOR:
        return True
    elif is_parameterless_function(ctor):
        return True
    else:
        return False

def is_parameterless_function(sig: Signature) -> bool:
    return not any([
        p
        for p in sig.parameters
        if p.kind in (
            ParameterKind.POSITIONAL,
            ParameterKind.POSITIONAL_OR_KEYWORD,
            ParameterKind.KEYWORD
        )
    ])

def is_prototypically_equivalent(cls: type[Any], protocol: type[Any]) -> bool:
    protocol_members = get_members(protocol, filter = MemberFilter.PROPERTIES | MemberFilter.FUNCTIONS_AND_METHODS | MemberFilter.FIELDS_AND_VARIABLES)
    protocol_ctor = protocol_members.subset_constructors()
    protocol_properties = protocol_members.subset_properties()
    protocol_methods = protocol_members.subset_methods()
    protocol_fields = protocol_members.subset_fields()

    class_members = get_members(cls, filter = MemberFilter.PROPERTIES | MemberFilter.FUNCTIONS_AND_METHODS | MemberFilter.FIELDS_AND_VARIABLES)
    class_ctor = class_members.subset_constructors()
    class_properties = class_members.subset_properties()
    class_methods = class_members.subset_methods()
    class_fields = class_members.subset_fields()

    # check constructor
    ## note that typing.Protocol replaces constructors on its subclasses,
    ## so if protocol class is derived from typing.Protocol, this check will always pass
    if protocol_ctor and ( ctor := protocol_ctor[0][1] ) and ctor.signature is not DEFAULT_CTOR:
        if not is_parameterless_function(ctor.signature):
            if class_ctor and ( ref_ctor := class_ctor[0][1] ) and ref_ctor.signature != ctor.signature:
                return False
    # elif class_ctor and not is_parameterless_function(class_ctor[0][1].signature):
    #     return False

    # check properties
    for _, prop in protocol_properties:
        if prop.name in class_properties:
            _, ref_prop = class_properties[prop.name]
            # check getter
            if prop.getter != ref_prop.getter:
                return False # pragma: no cover # the property definition ensures that this will never happen under normal circumstances
            # check setter
            if prop.setter and not ref_prop.setter:
                return False
            elif prop.setter and ref_prop.setter and prop.setter != ref_prop.setter:
                return False
            # check deleter
            if prop.deleter and not ref_prop.deleter:
                return False
            elif prop.deleter and ref_prop.deleter and prop.deleter != ref_prop.deleter:
                return False
        else:
            return False

    # check methods
    for _, fn in protocol_methods:
        if fn.name not in class_methods:
            return False
        _, ref_fn = class_methods[fn.name]
        if fn.signature != ref_fn.signature:
            return False

    # check fields
    for _, fld in protocol_fields:
        if fld.name not in class_fields:
            return False
        _, ref_fld = class_fields[fld.name]
        if fld.field_type != ref_fld.field_type:
            return False


    return True