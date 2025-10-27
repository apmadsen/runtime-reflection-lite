from typing import Any
import typing
from types import ModuleType
from os import path
from sys import modules
from importlib import import_module, util
from contextlib import contextmanager
from functools import lru_cache

from runtime.reflection.lite.core.attributes import DICT, FILE


def load_module(name: str) -> tuple[ModuleType, dict[str, Any]]:
    """Loads a module by its name or filename.

    Args:
        name (str): The name or filename of the module.

    Returns:
        tuple[ModuleType, dict[str, Any]]: Returns the module itself and its dict of attributes.
    """

    if not name:
        raise ValueError #pragma: no cover
    elif name in modules:
        module = modules[name]
    elif path.isfile(name):
        module = _load_by_file(name)
    else:
        module = _load_by_name(name, path.abspath(path.curdir))

    module_dict: dict[str, Any] = getattr(module, DICT) or {}

    if hasattr(module, FILE) and "TYPE_CHECKING" in module_dict:
        # some of the module definitions are hidden to supress circular imports, and to overcome this,
        # we load a copy of the module with typing.TYPE_CHECKING set to True
        with patch(typing, TYPE_CHECKING = True):
            if ( spec := util.spec_from_file_location(name + "_typed", getattr(module, FILE)) ) and spec.loader:
                typed_module = util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(typed_module)
                except:  # noqa: E722
                    pass
                    # log.warning(f"Failed to completely load module {name} for type checking")

                module_dict = { **module_dict, **{ k:v for k,v in getattr(typed_module, DICT).items() if k not in module_dict } }

    return module, module_dict

@lru_cache()
def _load_by_name(name: str, cd: str) -> ModuleType: # cd argument is there to differentiate caching points by the current dir
    return modules[name] if name in modules else import_module(name)

@lru_cache()
def _load_by_file(file_path: str) -> ModuleType:
    found = [
        module
        for module in modules.values()
        if hasattr(module, FILE)
        and ( file := getattr(module, FILE) )
        and path.abspath(file) == path.abspath(file_path)
    ]

    if found:
        return found[0]

    module_name = path.splitext(path.basename(file_path))[0]

    if ( spec := util.spec_from_file_location(module_name, file_path) ) and spec.loader:
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    else:
        raise Exception(f"Unable to load module {module_name} from {file_path}")


@contextmanager
def patch(target: Any, **attributes: Any):
    """Patches a runtime module by setting the value of one or more of its attributes.

    Args:
        target (Any): The target module.
    """

    old_values = {
        attr: getattr(target, attr)
        for attr in attributes.keys()
    }

    try:

        for attr, value in attributes.items():
            setattr(target, attr, value)

        yield

    finally:
        # revert back to the original values
        for attr, value in attributes.items():
            setattr(target, attr, old_values[attr])
