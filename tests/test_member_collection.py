# pyright: basic
from pytest import raises as assert_raises

from runtime.reflection.lite import (
    ParameterKind, Undefined, Function, Constructor, Variable, Field, Class,
    Method, Property, FunctionKind, AccessMode, MemberType, Module, get_members
)

from tests.reflection_classes import Class4, Class5, Class6, Class7, Class8, Class9, Class10, AbstractClass


def test_members_collection():
    members = get_members(Class10)

    assert set(members.keys()).issuperset([
        "__init__"
    ])

    info, member = members["__init__"]
    assert member in members
    assert "__init__" in members.keys()
    assert info in dict(members.values())
    assert dict(members.items())["__init__"][1] is member

    assert len(members) > 0
    assert any(list(iter(members)))
    constructors = members.subset(Constructor)
    assert any(list(iter(constructors)))
    assert len(constructors) == 1
    assert isinstance(constructors.subset(lambda m: m.name == "__init__")[0][1], Constructor)

def test_example():
    import runtime.reflection.lite
    from runtime.reflection.lite import get_members

    members = get_members(runtime.reflection.lite)
    functions = members.subset_functions()
    classes = members.subset_classes()

    info, member = functions["get_signature"]
    assert info.access_mode == runtime.reflection.lite.AccessMode.PUBLIC
    assert member.kind == runtime.reflection.lite.FunctionKind.FUNCTION

    assert "Member" in classes
