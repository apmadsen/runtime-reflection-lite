from inspect import Parameter, Signature

from runtime.reflection.lite.core.exceptions.internal_exception import InternalException


class Meta(type): # pragma: no cover

    def __bool__(self):
        return False

    def __eq__(self, other: object) -> bool:
        return other is Undefined or other in [ Signature.empty, Parameter.empty, None ]

    def __repr__(cls):
        return "Undefined"

    def __str__(self) -> str:
        return "Undefined"

    def __hash__(self) -> int:
        return type.__hash__(self)


class Undefined(metaclass=Meta):
    """The Undefined class represents a value that hasn't been defined.
    """
    def __new__(cls):
        raise InternalException("Undefined type is not supposed to be instantiated") # pragma: no cover

