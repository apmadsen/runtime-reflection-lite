from typing import Any
from typingutils import get_type_name

from runtime.reflection.lite.core.objects.member import Member
from runtime.reflection.lite.core.objects.member_type import MemberType

class Variable(Member):
    __slots__ = [ "__variable_type" ]

    def __init__(
        self,
        name: str,
        variable_type: type[Any]
    ):
        super().__init__(name, MemberType.VARIABLE)
        self.__variable_type = variable_type

    @property
    def variable_type(self) -> type[Any]:
        """The variables annotated or inferred type.
        """
        return self.__variable_type

    def __str__(self) -> str: # pragma: no cover
        return get_type_name(self.variable_type) if self.variable_type else str(self.variable_type)

    def __repr__(self) -> str:
        return f"Variable {self.name}: {self}"