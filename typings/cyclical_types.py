from __future__ import annotations

from typing import NamedTuple, Protocol


# mypy used to not understand cyclical types, except for Protocols
# a workaround was to create a protocol
# now it's fixed
class _Example(Protocol):
    @property
    def val(self) -> int: ...
    @property
    def children(self) -> tuple[_Example, ...]: ...
    def val_squared(self) -> int: ...


class Example(NamedTuple):
    val: int
    children: tuple[_Example, ...] = ()

    def val_squared(self) -> int:
        return self.val * self.val


class ExampleNow(NamedTuple):
    val: int
    children: tuple[ExampleNow, ...] = ()

    def val_squared(self) -> int:
        return self.val * self.val


def main() -> None:
    ex1 = Example(1)
    ex2 = Example(2, (ex1,))

    # reveal_type(ex2.children[0].children[0].children[0])

    print(ex1)
    print(ex2)

    exn1 = ExampleNow(1)
    exn2 = ExampleNow(2, (exn1,))

    # reveal_type(ex2.children[0].children[0].children[0])

    print(exn1)
    print(exn2)


if __name__ == "__main__":
    main()
