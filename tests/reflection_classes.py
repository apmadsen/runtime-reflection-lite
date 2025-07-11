# pyright: basic
from __future__ import annotations
from typing import TYPE_CHECKING, Any, List, overload
from abc import (
    ABC, abstractmethod,
    abstractproperty, abstractclassmethod, abstractstaticmethod # pyright: ignore[reportDeprecated]
)
import datetime
import json
import tests.reflection_modules as reflection_modules


if TYPE_CHECKING:
    from typing import Sequence


Variable1: int | None = 2
Variable2: str | None = None
Variable3 = 2.354

class Class1:

    def __init__(self, field1: int, field2: str, field3: float, field4: bool) -> None:
        self.field1 = field1
        self._field2 = field2
        self.__field3 = field3
        self.__field4 = field4

    field1: int
    _field2: str
    __field3: float

    @property
    def field2(self) -> str:
        return self._field2

    @property
    def field3(self) -> float:
        return self.__field3

    @property
    def field4(self) -> bool:
        return self.__field4


class Class2(Class1):
    def __init__(self, field1: int, field2: str, field3: float, field4: bool, field5: datetime.datetime, field6: int, field7: float, field8: str):
        super().__init__(field1, field2, field3, field4)
        self.field5 = field5
        self._field6 = field6
        self.__field7 = field7
        self.__field8 = field8

    field5: datetime.datetime
    _field6: int
    __field7: float


    @property
    def field6(self) -> int:
        return self._field6

    @property
    def field7(self) -> float:
        return self.__field7

    @property
    def field8(self) -> str:
        return self.__field8


class Class3:
    def __init__(self, seq: Sequence[str]):
        pass

class Class4:
    __prop: int = 0

    @property
    def prop(self) -> int:
        return self.__prop

    @prop.setter
    def prop(self, value: int):
        self.__prop = value



    def test_method(self, value: Any) -> Any:
        return value

    @classmethod
    def test_classmethod(cls, value: Any) -> Any:
        return value

    @staticmethod
    def test_staticmethod(value: Any) -> Any:
        return value



class ClassBaseA:
    a: bool = True
    _a: bool
    __a: bool # pyright: ignore[reportUnusedVariable]

    @property
    def prop_a(self) -> bool:
        ...
    @prop_a.setter
    def prop_a(self, value: bool):
        ...

    def _base1(self) -> bool:
        ...

    def _base2(self) -> bool:
        ...

    @overload
    def _base_a(self) -> bool:
        ...
    @overload
    def _base_a(self, x: int) -> bool:
        ...
    def _base_a(self, x: int | None = 2) -> bool:
        ...

class ClassBaseB:
    b: int = 33
    _b: int
    __b: int # pyright: ignore[reportUnusedVariable]

    @property
    def prop_b(self) -> int:
        ...
    @prop_b.setter
    def prop_b(self, value: int):
        ...

    def test_base1(self) -> int:
        ...
    def test_base_b(self) -> int:
        ...

    class NestedClassB:
        ...

class WithDelegate:
    def __get__(self, instance: object, cls: type) -> str:
        return "Test"

class ClassDerived(ClassBaseA, ClassBaseB):
    y: float = 2.0
    _y: float
    __y: float # pyright: ignore[reportUnusedVariable]

    Dlg = WithDelegate()

    @overload
    def __init__(self) -> None:
        ...
    @overload
    def __init__(self, y: float) -> None:
        ...
    def __init__(self, y: float | None = None):
        ...


    @property
    def prop_derived(self) -> float:
        ...
    @prop_derived.setter
    def prop_derived(self, value: float):
        ...

    def test_base2(self) -> bool:
        ...
    def test_derived(self) -> str:
        ...
    def self_referencing(self) -> ClassDerived:
        ...

    class NestedClass:
        ...

    class _NestedClassProtected:
        ...
    class __NestedClassPrivate: # pyright: ignore[reportUnusedVariable]
        ...





class Class5:
    field1: int = 0
    field2: int

    def __init__(self):
        pass

    @property
    def prop1(self) -> int:
        return 33

    @property
    def prop2(self) -> str:
        return "sdg"
    @prop2.setter
    def prop2(self, value: str) -> None:
        pass

    @prop2.setter
    def prop2(self, value: str) -> None:
        pass


    def test(self, s: str) -> str:
        return "test"

    class SubClass:
        @property
        def prop1(self) -> float:
            return 3.14

class Class6:
    @property
    def prop1(self) -> int:
        return 1

    @property
    def prop2(self) -> int:
        ...

    @property
    def prop3(self) -> int:
        ...

    @overload
    def _test1(self, x: str) -> bool:
        ...
    @overload
    def _test1(self, x: int) -> bool:
        ...
    def _test1(self, x: str | int) -> bool:
        return True

    def _test2(self, x: List[str] = [ "test" ]) -> None:
        ...

    class Class7:
        def _test2(self, y: float) -> str:
            return "Hey"

class AbstractClass(ABC):

    @property
    def prop1(self) -> int:
        return 1

    @abstractproperty  # pyright: ignore[reportDeprecated, reportArgumentType]
    def prop2(self) -> int:
        ...

    @property
    @abstractmethod
    def prop3(self) -> int:
        ...

    @abstractmethod
    def _test1(self) -> bool:
        ...

    @abstractclassmethod  # pyright: ignore[reportDeprecated, reportArgumentType]
    def _test2(cls) -> bool:
        ...

    @abstractstaticmethod  # pyright: ignore[reportDeprecated, reportArgumentType]
    def _test3() -> bool:
        ...

    @classmethod
    @abstractmethod
    def _test4(cls) -> bool:
        ...

    @staticmethod
    @abstractmethod
    def _test5() -> bool:
        ...


class Class7:
    def __init__(self, value: str):
        ...

    @property
    def value(self) -> str:
        ...
    @value.setter
    def value(self, value: str) -> str:
        ...

    def do_something1(self, suffix: str | None = None) -> str:
        ...

    @classmethod
    def do_something2(cls, y: float) -> str:
        ...

    @staticmethod
    def do_something3(x: int) -> None:
        ...

    def _semi_private_function(self) -> None:
        ...

    def __private_function(self) -> None:
        ...

class Class8:
    def __init__(self, x: "int"):
        ...

class Class9:
    ...

class Class10(Class8, Class9):
    ...

def public_function() -> None:
    ...

def _semi_private_function() -> None:
    ...

def __private_function() -> None:
    ...

class10 = Class10

class Class11:
    b: int = 1
    _b: int = 2
    __b: int = 3

class Class12:
    b: int
    _b: int
    __b: int