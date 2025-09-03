from typing import Any, cast
from typingutils import get_type_name
from inspect import Parameter as InspectParameter

from runtime.reflection.lite.core.objects.parameter_kind import ParameterKind

class Parameter:
    """The Parameter class represents a function parameter.
    """
    __slots__ = ["__name", "__kind", "__doc", "__parameter_type", "__default"]

    def __init__(
        self,
        name: str,
        kind: ParameterKind,
        parameter_type: type[Any],
        default: Any
    ):
        self.__name = name
        self.__kind = kind
        self.__parameter_type = parameter_type
        self.__default = default

    @property
    def name(self) -> str:
        """The parameter name.
        """
        return self.__name

    @property
    def kind(self) -> ParameterKind:
        """The parameter kind.
        """
        return self.__kind

    @property
    def parameter_type(self) -> type[Any]:
        """The parameter type.
        """
        return self.__parameter_type

    @property
    def default(self) -> Any:
        """The parameter default value.
        """
        return self.__default

    def __eq__(self, o: object) -> bool: # pragma: no cover
        if isinstance(o, Parameter):
            return (
                self.name == o.name
                and self.kind == o.kind
                and self.parameter_type == o.parameter_type
            )
        elif isinstance(o, InspectParameter):
            return (
                self.name == o.name
                and cast(int, self.kind) == o.kind
                and self.parameter_type == o.annotation
            )

        return False

    def __str__(self) -> str: # pragma: no cover
        str_type = get_type_name(self.parameter_type) if self.parameter_type else str(self.parameter_type)
        str_default = f"={self.__default}" if self.__default else ""
        return f"{self.__name}: {str_type}{str_default}"

    def __repr__(self) -> str:
        return f"Parameter {self}"