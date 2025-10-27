from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tests.referred_class import Referred

class Referring:
    def __init__(self, ref: Referred) -> None:
        self.ref = ref

