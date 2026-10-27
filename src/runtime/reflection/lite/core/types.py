from types import (
    BuiltinFunctionType,
    BuiltinMethodType,
    ClassMethodDescriptorType,
    FunctionType,
    LambdaType,
    MethodDescriptorType,
    MethodType,
    MethodWrapperType,
    WrapperDescriptorType,
)

FUNCTION_TYPES = (
    FunctionType, LambdaType,
    BuiltinFunctionType, WrapperDescriptorType
)
METHOD_TYPES = (
    MethodType, BuiltinMethodType, MethodWrapperType,
    MethodDescriptorType, ClassMethodDescriptorType
)
FUNCTION_AND_METHOD_TYPES = FunctionType | LambdaType | BuiltinFunctionType | WrapperDescriptorType | MethodType | BuiltinMethodType | MethodWrapperType | MethodDescriptorType | ClassMethodDescriptorType
