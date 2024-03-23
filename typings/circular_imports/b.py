from __future__ import annotations

from typing import TYPE_CHECKING

# TYPE_CHECKING is False at runtime so runtime is not affected by this import
# but type checkers know how to deal with it and resolve the type
# another solution is to defer the imports inside the function
# (this can also deal with runtime circular imports)
if TYPE_CHECKING:
    from a import A


class B:
    def __init__(self) -> None:
        self.a_items: list[A] = []

    def baz(self) -> int:
        return 9001

    def register_a(self, a: A) -> None:  # a: 'A' also works
        self.a_items.append(a)
