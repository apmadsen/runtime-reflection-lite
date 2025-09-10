from typing import Any, cast
from types import FrameType, ModuleType
from typingutils import AnyFunction
from deprecated import deprecated

from runtime.reflection.lite.core.objects.parameter_kind import ParameterKind
from runtime.reflection.lite.core.objects.signature import Signature
from runtime.reflection.lite.core.attributes import INIT, NEW
from runtime.reflection.lite.core import get_signature, DEFAULT_CTOR

@deprecated("Use get_signature() instead", version = "0.1.0")
def reflect_function(
    fn: AnyFunction,
    cls: object | None = None
) -> Signature: # pragma: no cover
    """Gets the signature of the specified function.

    Args:
        fn (AnyFunction): The function on which to reflect.
        cls (object | None, optional): The class to which the function belongs (if any). Defaults to None.

    Returns:
        Signature: Returns a function signature.
    """
    return get_signature(fn, cast(type[Any] | FrameType | ModuleType, cls))

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
    elif not any([ p for p in ctor.parameters if p.kind in (ParameterKind.POSITIONAL, ParameterKind.POSITIONAL_OR_KEYWORD, ParameterKind.KEYWORD) ]):
        return True
    else:
        return False