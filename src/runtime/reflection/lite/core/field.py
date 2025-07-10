from typing import Any

from runtime.reflection.lite.core.member import Member
from runtime.reflection.lite.core.member_type import MemberType

class Field(Member):
    __slots__ = [ "__field_type" ]

    def __init__(
        self,
        field_type: type[Any]
    ):
        super().__init__(MemberType.FIELD)
        self.__field_type = field_type

    @property
    def field_type(self) -> type[Any] | None:
        """The fields annotated or inferred type.
        """
        return self.__field_type

