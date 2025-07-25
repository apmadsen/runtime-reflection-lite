from typing import Any, Callable, cast, overload
from typingutils import AnyFunction, is_type
from types import FrameType, ModuleType, MethodType
from sys import modules
from types import FunctionType, MethodType
from inspect import (
    Parameter as InspectParameter, FrameInfo,
    getattr_static, signature as builtin_get_signature, stack, unwrap
)

from runtime.reflection.lite.core.access_mode import AccessMode
from runtime.reflection.lite.core.delegate import Delegate
from runtime.reflection.lite.core.member import Member
from runtime.reflection.lite.core.member_type import MemberType
from runtime.reflection.lite.core.member_filter import MemberFilter
from runtime.reflection.lite.core.member_collection import InternalMemberCollection, MemberCollection
from runtime.reflection.lite.core.member_info import MemberInfo
from runtime.reflection.lite.core.undefined import Undefined
from runtime.reflection.lite.core.signature import Signature
from runtime.reflection.lite.core.parameter import Parameter
from runtime.reflection.lite.core.parameter_kind import ParameterKind
from runtime.reflection.lite.core.parameter_mapper import ParameterMapper
from runtime.reflection.lite.core.module import Module
from runtime.reflection.lite.core.function import Function
from runtime.reflection.lite.core.class_ import Class
from runtime.reflection.lite.core.field import Field
from runtime.reflection.lite.core.variable import Variable
from runtime.reflection.lite.core.function_kind import FunctionKind
from runtime.reflection.lite.core.method import Method
from runtime.reflection.lite.core.constructor import Constructor
from runtime.reflection.lite.core.property_ import Property
from runtime.reflection.lite.core.deferred_reflection import DeferredReflection
from runtime.reflection.lite.core.attributes import (
    INIT, CLASS, DICT, GET, SELF, GLOBALS, BUILTINS, CALL, MRO,
    TEXT_SIGNATURE, MODULE, FILE, ANNOTATIONS, ABSTRACT_METOD, NAME
)
from runtime.reflection.lite.core.types import FUNCTION_TYPES, METHOD_TYPES
from runtime.reflection.lite.core.misc import get_annotations, get_access_mode, is_special_attribute, is_delegate



def resolve(
    annotation: str,
    globals: dict[str, Any] | None = None,
    builtins: dict[str, Any] | None = None,
    locals: dict[str, Any] | None = None
) -> Any:
    annotation = annotation.replace("'", "").replace('"', "")

    if globals: # pragma: no cover
        globals = { **globals , **(builtins or  __builtins__)}

        try:
            result = eval(annotation, globals, locals)
            return result
        except:
            pass

    # fallback
    for frame in stack()[1:]: # pragma: no cover
        if frame.filename == __file__:
            continue

        globals = { **frame.frame.f_globals , **frame.frame.f_builtins}
        locals = frame.frame.f_locals

        try:
            return eval(annotation, globals, locals)
        except:
            pass

    raise Exception(f"Unable to resolve {annotation}") # pragma: no cover

def get_frame(
    obj: Any,
    stack: list[FrameInfo],
    parent: Any | None
) -> FrameType | None: # pragma: no cover
    module = None

    if hasattr(obj, MODULE):
        module = modules[getattr(obj, MODULE)]
    elif parent and hasattr(parent, MODULE):
        module = modules[getattr(parent, MODULE)]

    if module and hasattr(module, FILE):
        for frame in stack:
            if frame.filename == module.__file__:
                frame_locals = frame.frame.f_locals.values()
                if parent is not None and parent in frame_locals:
                    return frame.frame
                elif obj in frame_locals:
                    return frame.frame

@overload
def get_signature(
    fn: AnyFunction, /
) -> Signature:
    """Gets the signature of the specified function.
    For edge cases, it may be necessary to include the _parent_ parameter.

    Args:
        fn (AnyFunction): The reflected function.

    Returns:
        Signature: Returns a Signature instance.
    """
    ...
@overload
def get_signature(
    fn: AnyFunction,
    parent: type[Any] | ModuleType | FrameType, /
) -> Signature:
    """Gets the signature of the specified function.

    Args:
        fn (AnyFunction): The reflected function.
        parent (type[Any] | ModuleType | FrameType): The function parent.

    Returns:
        Signature: Returns a Signature instance.
    """
    ...
@overload
def get_signature(
    fn: AnyFunction,
    parent: type[Any] | ModuleType | FrameType | None = None, /,
    globals: dict[str, Any] | None = None,
    builtins: dict[str, Any] | None = None,
    locals: dict[str, Any] | None = None
) -> Signature:
    ...
def get_signature(
    fn: AnyFunction,
    parent: type[Any] | ModuleType | FrameType | None = None, /,
    globals: dict[str, Any] | None = None,
    builtins: dict[str, Any] | None = None,
    locals: dict[str, Any] | None = None
) -> Signature:
    fn = unwrap(fn)
    sig = builtin_get_signature(fn)

    if hasattr(fn, SELF) and ( self := getattr(fn, SELF) ):
        parent = self

    parameters = list(sig.parameters.values())
    globals = globals or getattr(fn, GLOBALS) if hasattr(fn, GLOBALS) else None
    builtins = builtins or getattr(fn, BUILTINS) if hasattr(fn, BUILTINS) else None

    if locals is None and ( frame := get_frame(fn, stack()[1:], parent) ): # pragma: no cover
        locals = frame.f_locals

    if parameters:
        first_param = parameters[0].name.lower()

        if isinstance(fn, MethodType) and first_param in ("self", "cls"): # pragma: no cover
            parameters = parameters[1:]
        elif first_param in ("self", "cls") and hasattr(fn, SELF): # pragma: no cover
            parameters = parameters[1:]
        elif first_param == "self":
            if hasattr(fn, CALL) and ( call := getattr(fn, CALL) ): # pragma: no cover
                if hasattr(call, TEXT_SIGNATURE) and ( text_sig := getattr(call, TEXT_SIGNATURE) ):
                    if cast(str, text_sig).startswith("($self"):
                        parameters = parameters[1:]

    for index, parameter in enumerate(parameters):
        changed = False

        if isinstance(parameter.annotation, str):
            parameter_type = resolve(parameter.annotation, globals, builtins, locals)
            parameter = parameter.replace(annotation = parameter_type)
            changed = True

        if changed:
            parameters[index] = parameter

    if sig.return_annotation is InspectParameter.empty:
        return_type = Undefined
    elif isinstance(sig.return_annotation, str):
        return_type = resolve(sig.return_annotation, globals, builtins, locals)
    else:
        return_type = sig.return_annotation

    return Signature(
        ParameterMapper(
            [
                Parameter(
                    p.name,
                    ParameterKind(p.kind),
                    Undefined if p.annotation is InspectParameter.empty else p.annotation,
                    Undefined if p.default is InspectParameter.empty else p.default
                ) for p in parameters
            ]
        ),
        return_type
    )

@overload
def get_members(obj: type[Any] | ModuleType | FrameType) -> MemberCollection:
    """Gets the members (functions and properties) of a class, module or frame.

    Args:
        cls (type[Any]): The class reflected.

    Returns:
        MemberCollection: Returns a MemberCollection.
    """
    ...
@overload
def get_members(obj: type[Any] | ModuleType | FrameType, *, filter: MemberFilter) -> MemberCollection:
    """Gets the members (functions and properties) of a class, module or frame.

    Args:
        cls (type[Any]): The class reflected.
        filter (MemberFilter): A filter defining which members are returned.

    Returns:
        MemberCollection: Returns a MemberCollection.
    """
    ...
@overload
def get_members(obj: type[Any] | ModuleType | FrameType, *, predicate: Callable[[MemberInfo], bool]) -> MemberCollection:
    """Gets the members (functions and properties) of a class, module or frame.

    Args:
        cls (type[Any]): The class reflected.
        predicate (Callable[[MemberInfo], bool]): A predicate function used to filter the members returned.

    Returns:
        MemberCollection: Returns a MemberCollection.
    """
    ...
@overload
def get_members(obj: type[Any] | ModuleType | FrameType, *, filter: MemberFilter, predicate: Callable[[MemberInfo], bool]) -> MemberCollection:
    """Gets the members (functions and properties) of a class, module or frame.

    Args:
        cls (type[Any]): The class reflected.
        filter (MemberFilter): A filter defining which members are returned.
        predicate (Callable[[MemberInfo], bool]): A predicate function used to filter the members returned.

    Returns:
        MemberCollection: Returns a MemberCollection.
    """
    ...
def get_members(obj: type[Any] | ModuleType | FrameType, *, filter: MemberFilter = MemberFilter.DEFAULT, predicate: Callable[[MemberInfo], bool] | None = None) -> MemberCollection:
    result = InternalMemberCollection()

    members = set(dir(obj))
    cls_dict = getattr(obj, DICT)
    annotations = get_annotations(obj)
    inherited_annotations: dict[str, str | type[Any]] = {}
    bases: set[type[Any]] = set()
    members = members.union(set(annotations.keys()))

    if isinstance(obj, type):
        bases = set(getattr(obj, MRO)[1:])
        for base_cls in bases:
            base_annotations = get_annotations(base_cls)
            inherited_annotations = {**inherited_annotations, **base_annotations }

        inherited_annotations = { **annotations, **inherited_annotations }

    globals: dict[str, Any] | None = getattr(obj, GLOBALS) if hasattr(obj, GLOBALS) else None
    builtins: dict[str, Any] | None = getattr(obj, BUILTINS) if hasattr(obj, BUILTINS) else None
    locals: dict[str, Any] = {}

    def fn_resolve_annotation(member: str) -> Any:
        if member in annotations and ( annotation_val := annotations[member] ):
            if isinstance(annotation_val, str):
                try:
                    if frame := get_frame(obj, stack()[2:], obj): # pragma: no cover
                        locals.update(frame.f_locals)
                    resolved = resolve(annotation_val, globals=globals, builtins=builtins, locals=locals)
                except: # pragma: no cover
                    resolved = Undefined

                annotations[member] = resolved
                return resolved
            else:
                return annotation_val


    for member in members:
        parent = obj
        member_info: MemberInfo | None = None
        member_name, access_mode = get_access_mode(parent, member)
        member_obj: Member | DeferredReflection[Member] | None = None
        is_special = is_special_attribute(member)
        value: Any | None = None
        attribute_value: Any | None = None
        attribute_base_value: Any | None = None

        if access_mode == AccessMode.PRIVATE and filter & MemberFilter.PRIVATE != MemberFilter.PRIVATE:
            continue
        elif access_mode == AccessMode.PROTECTED and filter & MemberFilter.PROTECTED != MemberFilter.PROTECTED:
            continue
        elif is_special and filter & MemberFilter.SPECIAL != MemberFilter.SPECIAL:
            continue

        if member in annotations and ( annotation_val := annotations[member] ):
            if isinstance(annotation_val, str):
                try:
                    annotation = resolve(annotation_val, globals=globals, builtins=builtins, locals=locals)
                except: # pragma: no cover
                    annotation = Undefined
            else:
                pass # pragma: no cover

        if hasattr(obj, member):
            value = getattr(obj, member)
            if member in cls_dict:
                attribute_value = cls_dict[member]
                attribute_base_value = attribute_value
            elif isinstance(obj, type):
                for base_cls in bases:
                    basecls_dict = getattr(base_cls, DICT)
                    if member in basecls_dict:
                        parent = base_cls
                        attribute_base_value = basecls_dict[member]
                        break
                pass # pragma: no cover
            else:
                pass # pragma: no cover
        elif member in annotations:
            pass
        else:
            continue # pragma: no cover

        if isinstance(value, (*FUNCTION_TYPES, *METHOD_TYPES)):
            if filter & MemberFilter.FUNCTIONS_AND_METHODS != MemberFilter.FUNCTIONS_AND_METHODS:
                continue # pragma: no cover
            try:
                static_value = getattr_static(parent, member)
                signature = get_signature(value, parent, globals=globals, builtins=builtins, locals=locals)
                is_abstract = cast(bool, getattr(value, ABSTRACT_METOD)) if hasattr(value, ABSTRACT_METOD) else False

                if isinstance(parent, type):
                    self_value = getattr(value, SELF) if hasattr(value, SELF)  else None

                    if member == INIT:
                        member_info = MemberInfo(member_name, member, Constructor, MemberType.METHOD, access_mode, parent is not obj, obj)
                        if not predicate or predicate(member_info):
                            member_obj = Constructor(parent, signature, value)
                        else:
                            pass # pragma: no cover
                    elif static_value and isinstance(static_value, classmethod) or self_value and is_type(self_value):
                        member_info = MemberInfo(member_name, member, Method, MemberType.METHOD, access_mode, parent is not obj, obj)
                        if not predicate or predicate(member_info):
                            member_obj = Method(MemberType.METHOD, FunctionKind.CLASS_METHOD, parent, signature, is_abstract, value)
                        else:
                            pass # pragma: no cover
                    elif isinstance(static_value, staticmethod):
                        member_info = MemberInfo(member_name, member, Method, MemberType.METHOD, access_mode, parent is not obj, obj)
                        if not predicate or predicate(member_info):
                            member_obj = Method(MemberType.METHOD, FunctionKind.STATIC_METHOD, parent, signature, is_abstract, value)
                        else:
                            pass # pragma: no cover
                    else:
                        member_info = MemberInfo(member_name, member, Method, MemberType.METHOD, access_mode, parent is not obj, obj)
                        if not predicate or predicate(member_info):
                            member_obj = Method(MemberType.METHOD, FunctionKind.METHOD, parent, signature, is_abstract, value)
                        else:
                            pass # pragma: no cover
                else:
                    member_info = MemberInfo(member_name, member, Function, MemberType.FUNCTION, access_mode, parent is not obj, obj)
                    if not predicate or predicate(member_info):
                        member_obj = Function(MemberType.FUNCTION, FunctionKind.FUNCTION, signature, value)
                    else:
                        pass # pragma: no cover

            except ValueError as _ex:
                pass
            except Exception as _ex:
                pass
        elif isinstance(value, property) and isinstance(parent, type):
            if filter & MemberFilter.PROPERTIES != MemberFilter.PROPERTIES:
                continue # pragma: no cover
            member_info = MemberInfo(member_name, member, Property, MemberType.PROPERTY, access_mode, parent is not obj, obj)
            if not predicate or predicate(member_info):
                is_abstract = cast(bool, getattr(value, ABSTRACT_METOD)) if hasattr(value, ABSTRACT_METOD) else False
                getter = get_signature(cast(FunctionType, value.fget), parent, globals=globals, builtins=builtins, locals=locals)
                setter = get_signature(value.fset, parent, globals=globals, builtins=builtins, locals=locals) if value.fset else None
                deleter = get_signature(value.fdel, parent, globals=globals, builtins=builtins, locals=locals) if value.fdel else None
                member_obj = Property(parent, getter, setter, deleter, is_abstract, value)
            else:
                pass # pragma: no cover

        elif isinstance(value, type) and value is not object and value != obj and member != CLASS and getattr(value, NAME) == member:
            if filter & MemberFilter.CLASSES != MemberFilter.CLASSES:
                continue # pragma: no cover
            member_info = MemberInfo(member_name, member, Class, MemberType.CLASS, access_mode, parent is not obj, obj)
            if not predicate or predicate(member_info):
                def defer_resolve_class(value: type[Any]) -> DeferredReflection[Class]:
                    class Resolve:
                        resolved: Class | None = None
                        def __call__(self) -> Class:
                            if not self.resolved:
                                members = get_members(value)
                                cls_bases = set(getattr(value, MRO)[1:])
                                self.resolved = Class(
                                    getattr(value, NAME),
                                    cls_bases,
                                    members,
                                    value
                                )
                            return self.resolved
                    return Resolve()
                member_obj = defer_resolve_class(value)
            else:
                pass # pragma: no cover
        elif isinstance(value, ModuleType):
            if filter & MemberFilter.MODULES != MemberFilter.MODULES:
                continue # pragma: no cover
            member_info = MemberInfo(member_name, member, Module, MemberType.MODULE, access_mode, parent is not obj, obj)
            if not predicate or predicate(member_info):
                def defer_resolve_module(value: ModuleType) -> DeferredReflection[Module]:
                    class Resolve:
                        resolved: Module | None = None
                        def __call__(self) -> Module:
                            if not self.resolved:
                                members = get_members(value)
                                self.resolved = Module(
                                    getattr(value, NAME),
                                    members,
                                    value
                                )
                            return self.resolved
                    return Resolve()
                member_obj = defer_resolve_module(value)
            else:
                pass # pragma: no cover
        elif isinstance(parent, type) and attribute_base_value != None and is_delegate(attribute_base_value):
            if filter & MemberFilter.DELEGATES != MemberFilter.DELEGATES:
                continue # pragma: no cover
            member_info = MemberInfo(member_name, member, Delegate, MemberType.DELEGATE, access_mode, parent is not obj, obj)
            if not predicate or predicate(member_info):
                annotation = fn_resolve_annotation(member)
                member_obj = Delegate(annotation or cast(type[Any], type(value) if value else Undefined), parent, value)
            else:
                pass # pragma: no cover
            pass
        elif isinstance(parent, type):
            if filter & MemberFilter.FIELDS_AND_VARIABLES != MemberFilter.FIELDS_AND_VARIABLES:
                continue # pragma: no cover
            member_info = MemberInfo(member_name, member, Field, MemberType.FIELD, access_mode, parent is not obj, obj)
            if not predicate or predicate(member_info):
                annotation = fn_resolve_annotation(member)
                member_obj = Field(annotation or cast(type[Any], type(value) if value else Undefined), parent)
            else:
                pass # pragma: no cover
        else:
            if filter & MemberFilter.FIELDS_AND_VARIABLES != MemberFilter.FIELDS_AND_VARIABLES:
                continue # pragma: no cover
            member_info = MemberInfo(member_name, member, Variable, MemberType.VARIABLE, access_mode, parent is not obj, obj)
            if not predicate or predicate(member_info):
                annotation = fn_resolve_annotation(member)
                member_obj = Variable(annotation or cast(type[Any], type(value) if value else Undefined))
            else:
                pass # pragma: no cover

        if member_obj and member_info:
            result.append(member_name, member_info, member_obj)

    return result.complete()
