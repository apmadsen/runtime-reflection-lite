# pyright: basic
from typing import Sequence, Any
from runtime.reflection.lite.core import Signature, ParameterKind, Undefined

def explore(signature: Signature) -> tuple[type | None, Sequence[tuple[str, ParameterKind, type[Any] | Undefined, Any]]]:
    return (
        signature.return_type,
        [
            (
                p.name,
                p.kind,
                p.parameter_type,
                p.default
            )
            for p in signature.parameters
        ]
    )
