from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime

# SimpleNamespace is a holder for attributes, it doesn't have a defined structure
from types import SimpleNamespace
from typing import Any, ClassVar, Self


def hide_field(field: object) -> str:
    return "**redacted**"


def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")


def show_original(event_field: object) -> object:
    return event_field


class EventSerializer[T]:
    """Apply the transformations to an Event object based on its properties and
    the definition of the function to apply to each field.
    """

    def __init__(
        self, serialization_fields: Mapping[str, Callable[[Any], Any]]
    ) -> None:
        """Created with a mapping of fields to functions."""
        self.serialization_fields = serialization_fields

    def serialize(self, event: T) -> dict[str, object]:
        """Get all the attributes from ``event``, apply the transformations to
        each attribute, and place it in a dictionary to be returned.
        """
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_fields.items()
        }


class Serialization[T]:
    """A class decorator created with transformation functions to be applied
    over the fields of the class instance.
    """

    def __init__(self, **transformations: Callable[[Any], Any]) -> None:
        """The ``transformations`` dictionary contains the definition of how to
        map the attributes of the instance of the class, at serialization time.
        """
        self.serializer = EventSerializer[T](transformations)

    def __call__(self, event_class: type[T]) -> type[T]:
        """Called when being applied to ``event_class``, will replace the
        ``serialize`` method of this one by a new version that uses the
        serializer instance.
        """

        def serialize_method(event_instance: T) -> dict[str, object]:
            return self.serializer.serialize(event_instance)

        setattr(event_class, "serialize", serialize_method)
        return event_class


# Given how ugly this looks, it might be better to do without generics
@Serialization["LoginEvent"](
    username=str.lower,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    timestamp: datetime

    serialize: ClassVar[Callable[[Self], dict[str, object]]]

    def __str__(self) -> str:
        return str(self.serialize())


def main() -> None:
    le = LoginEvent("Jonh", "secret", "127.0.0.1", datetime.now())
    print(le)

    # Creating serialization fields
    serialization_fields = {
        "username": str.upper,
        "name": str.title,
    }

    # Creating event and an EventSerialization object
    event = SimpleNamespace(username="usr", name="name")
    actual_result = EventSerializer[SimpleNamespace](serialization_fields).serialize(
        event
    )
    print(actual_result)

    # Creating object holding expected result and comparing against actual result
    expected_result = {
        "username": event.username.upper(),
        "name": event.name.title(),
    }
    print(actual_result == expected_result)


if __name__ == "__main__":
    main()
