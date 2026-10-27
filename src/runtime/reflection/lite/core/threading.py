from threading import RLock
from types import TracebackType
from typing import Protocol


class LockProtocol(Protocol): # pragma no cover
    def __enter__(self) -> None:
        ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None):
        ...


Lock: type[LockProtocol] = RLock # pyright: ignore[reportAssignmentType]

try:
    from runtime.threading import Lock  # pyright: ignore[reportUnusedImport, reportMissingImports, reportUnknownVariableType]  # noqa: F401
except ImportError:
    pass