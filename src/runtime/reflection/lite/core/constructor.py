from typing import Any

from runtime.reflection.lite.core.signature import Signature
from runtime.reflection.lite.core.method import Method
from runtime.reflection.lite.core.function_kind import FunctionKind
from runtime.reflection.lite.core.undefined import Undefined
from runtime.reflection.lite.core.member_type import MemberType

class Constructor(Method):
    __slots__ = [ ]

    def __init__(
        self,
        bound_cls: type[Any],
        signature: Signature
    ):
        super().__init__(MemberType.CONSTRUCTOR, FunctionKind.CONSTRUCTOR, bound_cls, signature, False)

    @property
    def return_type(self) -> type[Any]:
        return Undefined