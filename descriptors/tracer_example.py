from typing import ClassVar, Self, overload


class HistoryTracedAttribute[T, V]:
    """Trace the values of this attribute into another one given by the name at `trace_attribute_name`."""

    def __init__(self, trace_attribute_name: str) -> None:
        self._trace_attribute_name = trace_attribute_name
        self._name = ""

    def __set_name__(self, owner: type[T], name: str) -> None:
        self._name = name

    @overload
    def __get__(self, instance: None, owner: type[T]) -> Self: ...

    @overload
    def __get__(self, instance: T, owner: type[T] | None = None) -> V: ...

    def __get__(self, instance: T | None, owner: type[T] | None = None) -> V | Self:
        if instance is None:
            return self
        value: V = vars(instance)[self._name]
        return value

    def __set__(self, instance: T, value: V) -> None:
        self._track_change_in_value_for_instance(instance, value)
        vars(instance)[self._name] = value

    def _track_change_in_value_for_instance(self, instance: T, value: V) -> None:
        self._set_default(instance)
        if self._needs_to_track_change(instance, value):
            vars(instance)[self._trace_attribute_name].append(value)

    def _needs_to_track_change(self, instance: T, value: V) -> bool:
        """Determine if the value change needs to be traced or not.

        Rules for adding a value to the trace:
            * If the value is not previously set (it's the first one).
            * If the new value is != than the current one.
        """
        try:
            current_value: V = vars(instance)[self._name]
        except KeyError:
            return True
        return value != current_value

    def _set_default(self, instance: T) -> None:
        vars(instance).setdefault(self._trace_attribute_name, [])


class Traveler:
    """
    A person visiting several cities.
    We wish to track the path of the traveller, as he/she is visiting each new city.
    """

    type City = str

    current_city: ClassVar = HistoryTracedAttribute[Self, City]("cities_visited")

    def __init__(self, name: str, current_city: City) -> None:
        self.name = name
        self.current_city = current_city  # type: ignore


def main() -> None:
    alice = Traveler("Alice", "Barcelona")
    alice.current_city = "Paris"  # type: ignore
    alice.current_city = "Brussels"  # type: ignore
    alice.current_city = "Amsterdam"  # type: ignore

    print(vars(alice)["cities_visited"])
    print(alice.cities_visited)  # type: ignore


if __name__ == "__main__":
    main()
