from typing import Any
from typingutils import get_type_name

from runtime.reflection.lite.core.objects.member import Member
from runtime.reflection.lite.core.objects.member_type import MemberType

class Field(Member):
    __slots__ = [ "__field_type", "__parent_cls" ]

    def __init__(
        self,
        name: str,
        field_type: type[Any],
        parent_cls: type[Any]
    ):
        super().__init__(name, MemberType.FIELD)
        self.__field_type = field_type
        self.__parent_cls = parent_cls

    @property
    def field_type(self) -> type[Any]:
        """The fields annotated or inferred type.
        """
        return self.__field_type

    @property
    def parent_cls(self) -> type[Any]:
        """The class on which the field is defined.
        """
        return self.__parent_cls

    def __str__(self) -> str: # pragma: no cover
        return get_type_name(self.field_type) if self.field_type else str(self.field_type)

    def __repr__(self) -> str:
        return f"Field {self.name}: {self}"