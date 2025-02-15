from __future__ import annotations

from collections.abc import Callable
from typing import ClassVar, Self, overload


class Validation:
    """A configurable validation callable."""

    def __init__(
        self,
        validation_function: Callable[..., bool],
        error_msg: str,
    ) -> None:
        self.validation_function = validation_function
        self.error_msg = error_msg

    def __call__(self, value: object) -> None:
        if not self.validation_function(value):
            raise ValueError(f"{value!r} {self.error_msg}")


class Field[T]:
    """A class attribute with validation functions configured over it."""

    def __init__(self, *validations: Validation):
        self._name = ""
        self._validations = validations

    def __set_name__(self, owner: type[T], name: str) -> None:
        self._name = name

    @overload
    def __get__(self, instance: None, owner: type[T]) -> Self: ...

    @overload
    def __get__(self, instance: T, owner: type[T] | None = None) -> T: ...

    def __get__(self, instance: T | None, owner: type[T] | None = None) -> object:
        if instance is None:
            return self
        return vars(instance)[self._name]

    def _validate(self, value: object) -> None:
        for validation in self._validations:
            validation(value)

    def __set__(self, instance: T, value: object) -> None:
        self._validate(value)
        vars(instance)[self._name] = value


class ClientClass:
    descriptor: ClassVar = Field[Self](
        Validation(lambda x: isinstance(x, (int, float)), "is not a number"),
        Validation(lambda x: x >= 0, "is not >= 0"),
    )


def main() -> None:
    client = ClientClass()

    # if __set__ is not implemented, it'll override the descriptor
    print(client.descriptor)
    # https://github.com/python/mypy/issues/14969
    client.descriptor = 42  # type: ignore
    print(client.descriptor)

    # NOTE: Uncomment the following one by one to see the generated errors
    # client.descriptor = -42
    # client.descriptor = "invalid value"


if __name__ == "__main__":
    main()
