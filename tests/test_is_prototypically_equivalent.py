# pyright: basic
# ruff: noqa
from pytest import raises as assert_raises
from typing import Any, Protocol, runtime_checkable

from runtime.reflection.lite import is_prototypically_equivalent



def test_basic():
    class Proto1(Protocol):

        def __init__(self, prop1: str, prop2: int):
            ...

        @property
        def prop1(self) -> str:
            ...

        @property
        def prop2(self) -> int:
            ...

    class Proto2: # protocols need not inherit typing.Protocol

        @property
        def prop1(self) -> str:
            ...
    class Proto3(Protocol):

        @property
        def prop1(self) -> str:
            ...
        @property
        def prop3(self) -> int:
            ...

    class Proto4(Protocol):
        Text: str

    class Proto5(Protocol):
        Number: int

    class Class1:
        Number: int

        def __init__(self, prop1: str, prop2: int):
            ...

        @property
        def prop1(self) -> str:
            ...

        @property
        def prop2(self) -> int:
            ...

    assert is_prototypically_equivalent(Class1, Proto1)
    assert is_prototypically_equivalent(Class1, Proto2)
    assert not is_prototypically_equivalent(Class1, Proto3)
    assert not is_prototypically_equivalent(Class1, Proto4)
    assert is_prototypically_equivalent(Class1, Proto5)

def test_constructors():
     # typing.Protocol class doesn't support constructors (in fact it replaces it with an empty one)
    class Proto1:
        def __init__(self, prop1: str):
            ...

        @property
        def prop1(self) -> str:
            ...

    class Proto2:
        @property
        def prop1(self) -> str:
            ...

    class Class1:

        def __init__(self, prop1: str):
            ...

        @property
        def prop1(self) -> str:
            ...

    class Class2:

        @property
        def prop1(self) -> str:
            ...

    assert is_prototypically_equivalent(Class1, Proto1)
    assert is_prototypically_equivalent(Class1, Proto2)
    assert not is_prototypically_equivalent(Class2, Proto1)
    assert is_prototypically_equivalent(Class2, Proto2)

def test_property_setters():

    class Proto1(Protocol):
        @property
        def prop1(self) -> str:
            ...

    class Proto2(Protocol):
        @property
        def prop1(self) -> str:
            ...
        @prop1.setter
        def prop1(self, value: str):
            ...

    class Class1:
        @property
        def prop1(self) -> str:
            ...

    class Class2:
        @property
        def prop1(self) -> str:
            ...
        @prop1.setter
        def prop1(self, value: str):
            ...

    class Class3:
        @property
        def prop1(self) -> str:
            ...
        @prop1.setter
        def prop1(self, value: int):
            ...

    assert is_prototypically_equivalent(Class1, Proto1)
    assert not is_prototypically_equivalent(Class1, Proto2)
    assert not is_prototypically_equivalent(Class3, Proto2)
    assert is_prototypically_equivalent(Class2, Proto2)
    assert is_prototypically_equivalent(Class2, Proto1)

def test_property_deleters():

    class Proto1(Protocol):
        @property
        def prop1(self) -> str:
            ...

    class Proto2(Protocol):
        @property
        def prop1(self) -> str:
            ...
        @prop1.deleter
        def prop1(self):
            ...

    class Class1:
        @property
        def prop1(self) -> str:
            ...

    class Class2:
        @property
        def prop1(self) -> str:
            ...
        @prop1.deleter
        def prop1(self):
            ...

    class Class3:
        @property
        def prop1(self) -> str:
            ...
        @prop1.deleter
        def prop1(self, x: bool):
            ...

    assert is_prototypically_equivalent(Class1, Proto1)
    assert not is_prototypically_equivalent(Class1, Proto2)
    assert not is_prototypically_equivalent(Class3, Proto2)
    assert is_prototypically_equivalent(Class2, Proto2)
    assert is_prototypically_equivalent(Class2, Proto1)

def test_methods():
    class Proto1:
        def func(self, x: int, y: int) -> int:
            ...

    class Proto2:
        def func(self, x: float, y: float) -> float:
            ...

    class Proto3:
        def func(self, x: int, y: int) -> str:
            ...

    class Class1:
        def func(self, x: int, y: int) -> int:
            ...

    class Class2:
        def func(self, x: float, y: float) -> float:
            ...

    class Class3:
        def func(self, x: int, y: int) -> str:
            ...

    class Class4:
        def func1(self, x: int, y: int) -> int:
            ...

    assert is_prototypically_equivalent(Class1, Proto1)
    assert not is_prototypically_equivalent(Class1, Proto2)
    assert not is_prototypically_equivalent(Class2, Proto1)
    assert is_prototypically_equivalent(Class2, Proto2)
    assert not is_prototypically_equivalent(Class1, Proto3)
    assert not is_prototypically_equivalent(Class2, Proto3)
    assert not is_prototypically_equivalent(Class3, Proto1)
    assert not is_prototypically_equivalent(Class3, Proto1)
    assert not is_prototypically_equivalent(Class4, Proto1)

def test_fields():
    class Proto1:
        Field1: str
        Field2: int

    class Class1:
        Field1: str
        Field2: int

    class Class2:
        Field1: str
        Field2: int
        Field3: bool

    class Class3:
        Field2: int
        Field3: bool

    class Class4:
        Field1: int
        Field2: bool

    assert is_prototypically_equivalent(Class1, Proto1)
    assert is_prototypically_equivalent(Class2, Proto1)
    assert not is_prototypically_equivalent(Class3, Proto1)
    assert not is_prototypically_equivalent(Class4, Proto1)
