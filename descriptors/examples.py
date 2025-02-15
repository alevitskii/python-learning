from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from types import MethodType
from typing import Any, ClassVar, Self, overload


# 1st example
# Simulation of a class method
class Method[T]:
    def __init__(self, name: str) -> None:
        self.name = name

    def __call__(self, instance: T, arg1: str, arg2: str) -> None:
        print(f"{self.name}: {instance} called with {arg1=} and {arg2=}")

    @overload
    def __get__(self, instance: None, owner: type[T]) -> Self: ...

    @overload
    def __get__(self, instance: T, owner: type[T] | None = None) -> MethodType: ...

    def __get__(
        self, instance: T | None, owner: type[T] | None = None
    ) -> MethodType | Self:
        if instance is None:
            return self
        return MethodType(self, instance)


class MyClass:
    method: ClassVar = Method[Self]("Internal call")


# 2nd example
# @property, @classmethod, and @staticmethod decorators are descriptors.
# Use a decorator class when defining a decorator that we want to apply to class methods,
# and implement the __get__() method on it.
# I didn't manage to type annotate this class. VSCode type stubs use Any too...
class classproperty:
    def __init__(self, fget: Callable[[Any], Any]) -> None:
        self.fget = fget

    def __get__(self, instance: Any, owner: type | None = None) -> Any:
        if instance is None:
            return self
        return self.fget(owner)


class TableEvent:
    schema = "public"
    table = "user"

    @classproperty
    def topic(cls) -> str:
        prefix = ""
        return f"{prefix}{cls.schema}.{cls.table}"


# 3rd example
# Each name defined in a slot will have its own descriptor that will store the value for retrieval later.
@dataclass
class Coordinate2D:
    __slots__ = ("lat", "long")

    lat: float
    long: float

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.lat}, {self.long})"


def main() -> None:
    # 1st example
    instance = MyClass()
    Method[MyClass]("External call")(instance, "first", "second")
    instance.method("first", "second")

    # 2nd example
    print(TableEvent.topic)
    print(TableEvent().topic)

    print(repr(Coordinate2D(10, 20)))


if __name__ == "__main__":
    main()
