# pyright: basic
# ruff: noqa
from pytest import raises as assert_raises

from runtime.reflection.lite import reflect
from runtime.reflection.lite.core.resolving import resolve
from runtime.reflection.lite.core.modules import load_module



def test_load_module_by_name():
    mod, attrs = load_module("tests.referred_class")
    assert "Referred" in attrs

def test_load_module_by_path():
    mod, attrs = load_module("tests/referred_class.py") # module might already be in sys.modules due to the test_load_by_name() test
    assert "Referred" in attrs

    mod, attrs = load_module("tests/standalone_module.py") # this module is not refererred anywhere else, so it should not be in sys.modules
    assert "Standalone" in attrs
