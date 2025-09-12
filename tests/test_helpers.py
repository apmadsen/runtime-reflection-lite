# pyright: basic
# ruff: noqa
from pytest import raises as assert_raises
from typing import Protocol

from runtime.reflection.lite import has_parameterless_constructor
from runtime.reflection.lite.core import DEFAULT_CTOR

from tests.explore import explore
from tests.reflection_classes import Class4, Class6, Class5

def test_has_parameterless_constructor():
    class Parameterless1:
        pass
    class Parameterless2:
        def __init__(self):
            pass
    class Parameterless3:
        def __new__(cls):
            pass
    class PerameterisedClass1:
        def __init__(self, p: str):
            pass
    class PerameterisedClass2:
        def __new__(cls, p: str):
            pass



    for cls in (Parameterless1, Parameterless2, Parameterless3):
        assert has_parameterless_constructor(cls)

    for cls in (PerameterisedClass1, PerameterisedClass2):
        assert not has_parameterless_constructor(cls)
