# pyright: basic
# ruff: noqa
from pytest import raises as assert_raises

from runtime.reflection.lite import ParameterKind, Undefined, get_constructor, get_signature, reflect
from runtime.reflection.lite.core import DEFAULT_CTOR

from tests.explore import explore
from tests.reflection_classes import Class4, Class6, Class5

def test_get_constructor():
    signature1 = get_constructor(dict)
    e1 = explore(signature1)
    assert e1 ==  (
        Undefined,
        [
            ("args", ParameterKind.ARGS, Undefined, Undefined),
            ("kwargs", ParameterKind.KWARGS, Undefined, Undefined),
        ]
    )

    signature2 = get_constructor(Class4)
    e2 = explore(signature2)
    assert e2 ==  (
        Undefined,
        [

        ]
    )

    signature21 = get_signature(Class4().__init__)
    assert signature2 != signature21
    assert Class4.__init__ is object.__init__ and Class4.__new__ is object.__new__ and signature2 is DEFAULT_CTOR

    signature3 = get_constructor(Class6)
    e3 = explore(signature3)
    assert e3 ==  (
        Undefined,
        [

        ]
    )

    signature31 = get_signature(Class6().__init__)
    assert signature3 != signature31
    assert Class6.__init__ is object.__init__ and Class6.__new__ is object.__new__ and signature3 is DEFAULT_CTOR

    signature4 = get_constructor(Class5)
    e4 = explore(signature4)
    assert e4 ==  (
        Undefined, []
    )

    signature41 = get_signature(Class5().__init__)
    assert signature4 == signature41
    assert Class5.__init__ is not object.__init__ and Class5.__new__ is object.__new__ and signature4 is not DEFAULT_CTOR

def test_get_constructor_from_new():
    class ClassWithNew:
        arg1: str
        arg2: int

        def __new__(cls, arg1: str, *, arg2: int):
            inst = object.__new__(cls)
            inst.arg1 = arg1
            inst.arg2 = arg2
            return inst

    class DerivedClass(ClassWithNew):
        def __init__(self, arg1: str, *, arg2: int):
            ...
        pass
    class ClassWithNewAndInit:
        arg1: str
        arg2: int

        def __new__(cls, arg1: str, *, arg2: int) -> int:
            return 35

        def __init__(self, arg2: int):
            ...

    n = ClassWithNew("Test", arg2 = 2)
    n2 = ClassWithNewAndInit("Test", arg2 = 2)

    ref = reflect(ClassWithNew)
    ctor = get_constructor(ClassWithNew)
    assert ref.constructor.name == "__new__"
    assert ctor == ref.constructor.signature

    ref = reflect(DerivedClass)
    ctor = get_constructor(DerivedClass)
    assert ref.constructor.name == "__new__"
    assert ctor == ref.constructor.signature

    ref = reflect(ClassWithNewAndInit)
    ctor = get_constructor(ClassWithNewAndInit)
    assert ref.constructor.name == "__new__"
    assert ctor == ref.constructor.signature

    ref = reflect(Class4)
    ctor = get_constructor(Class4)
    assert ref.constructor.name == "__init__"
    assert ctor == ref.constructor.signature
