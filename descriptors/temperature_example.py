from __future__ import annotations

from typing import ClassVar, Self, overload


class TemperatureDescriptor:
    def __init__(self, name: str | None = None):
        self._name = name

    @overload
    def __get__(self, instance: None, owner: type[Temperature]) -> Self: ...

    @overload
    def __get__(
        self, instance: Temperature, owner: type[Temperature] | None = None
    ) -> int: ...

    def __get__(
        self, instance: Temperature | None, owner: type[Temperature] | None = None
    ) -> Self | int:
        if instance is None:
            return self
        return instance._celsius

    def __set__(self, instance: Temperature, value: int) -> None:
        if not isinstance(value, int | float):
            raise ValueError(f"{value!r} is not numerical")
        instance._celsius = value

    def __delete__(self, instance: Temperature) -> None:
        del instance._celsius


class Temperature:
    celsius: ClassVar = TemperatureDescriptor()

    def __init__(self) -> None:
        self._celsius = 0

    def toFahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32


if __name__ == "__main__":
    temperature = Temperature()
    temperature.celsius = 23  # type: ignore
    print(f"Celsius: {temperature.celsius}")
    print(f"Fahrenheit: {temperature.toFahrenheit()}")
    # temperature.celsius = "123"
    del temperature
