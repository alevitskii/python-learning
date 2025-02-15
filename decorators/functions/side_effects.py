from __future__ import annotations

# Generally, it's better to have all side effects on the lowest level (inside wrapped)

EVENTS_REGISTRY = {}


# it's executed when imported (thus prepopulated during runtime)
def register_event[T](event_cls: type[T]) -> type[T]:
    """Place the class for the event into the registry to make it accessible in
    the module.
    """
    EVENTS_REGISTRY[event_cls.__name__] = event_cls
    return event_cls


class Event:
    """A base event object"""


class UserEvent:
    TYPE = "user"


@register_event
class UserLoginEvent(UserEvent):
    """Represents the event of a user when it has just accessed the system."""


@register_event
class UserLogoutEvent(UserEvent):
    """Event triggered right after a user abandoned the system."""


def main() -> None:
    print(EVENTS_REGISTRY, "\n")
    print(
        sorted(EVENTS_REGISTRY.keys()) == sorted(("UserLoginEvent", "UserLogoutEvent"))
    )


if __name__ == "__main__":
    main()
