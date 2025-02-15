from __future__ import annotations

import datetime as dt
from collections.abc import Callable
from dataclasses import dataclass
from functools import partial
from typing import Any, Self, overload

type Transformation[T] = Callable[[T], str]


class BaseFieldTransformation[T, U]:
    def __init__(self, transformation: Transformation[T]) -> None:
        self._name = ""
        self.transformation = transformation

    def __set_name__(self, owner: type[U], name: str) -> None:
        self._name = name

    @overload
    def __get__(self, instance: None, owner: type[U]) -> Self: ...

    @overload
    def __get__(self, instance: U, owner: type[U]) -> str: ...

    def __get__(self, instance: U | None, owner: type[U]) -> str | Self:
        if instance is None:
            return self
        raw_value = vars(instance)[self._name]
        return self.transformation(raw_value)

    def __set__(self, instance: U, value: T) -> None:
        vars(instance)[self._name] = value


ShowOriginal = partial(BaseFieldTransformation, transformation=lambda _: _)
HideField = partial(BaseFieldTransformation, transformation=lambda _: "**redacted**")
FormatTime = partial(
    BaseFieldTransformation[dt.datetime, Any],
    transformation=lambda ft: ft.strftime("%Y-%m-%d %H:%M"),
)


@dataclass
class LoginEvent:
    type S = LoginEvent

    username: BaseFieldTransformation[str, S] = ShowOriginal()
    password: BaseFieldTransformation[str, S] = HideField()
    ip: BaseFieldTransformation[str, S] = ShowOriginal()
    timestamp: BaseFieldTransformation[dt.datetime, S] = FormatTime()

    def serialize(self) -> dict[str, str]:
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp,
        }


def main() -> None:
    le = LoginEvent(
        "john", "secret password", "1.1.1.1", dt.datetime.now(dt.timezone.utc)
    )
    print(vars(le))
    print(le.serialize())
    print(le.password)


if __name__ == "__main__":
    main()
