from typing import Any

from runtime.reflection.lite.core.signature import Signature
from runtime.reflection.lite.core.function import Function
from runtime.reflection.lite.core.function_kind import FunctionKind
from runtime.reflection.lite.core.member_type import MemberType

class Method(Function):
    __slots__ = [ "__abstract", "__bound_cls" ]

    def __init__(
        self,
        member_type: MemberType,
        kind: FunctionKind,
        bound_cls: type[Any],
        signature: Signature,
        abstract: bool
    ):
        super().__init__(member_type, kind, signature)
        self.__abstract = abstract
        self.__bound_cls = bound_cls

    @property
    def bound_cls(self) -> type[Any]:
        """The methods bound class.
        """
        return self.__bound_cls

    @property
    def is_abstract(self) -> bool:
        """Indicates if method is abstract.
        """
        return self.__abstract
