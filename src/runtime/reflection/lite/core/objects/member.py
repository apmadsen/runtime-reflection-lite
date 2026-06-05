from runtime.reflection.lite.core.objects.member_type import MemberType

class Member:
    __slots__ = [ "__name", "__member_type", "__weakref__" ]

    def __init__(
        self,
        name: str,
        member_type: MemberType
    ):
        self.__name = name
        self.__member_type = member_type

    @property
    def name(self) -> str:
        """The member name.
        """
        return self.__name

    @property
    def member_type(self) -> MemberType:
        """The member type.
        """
        return self.__member_type
