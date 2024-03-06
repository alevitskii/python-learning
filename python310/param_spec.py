import logging
from collections.abc import Callable
from threading import Lock
from typing import Concatenate, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


def add_logging(f: Callable[P, T]) -> Callable[P, T]:
    """A type-safe decorator to add logging to a function."""

    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f"{f.__name__} was called")
        return f(*args, **kwargs)

    return inner


@add_logging
def add_two(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y


# Use this lock to ensure that only one thread is executing a function
# at any time.
my_lock = Lock()
R = TypeVar("R")


def with_lock(f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
    """A type-safe decorator which provides a lock."""

    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        # Provide the lock as the first argument.
        return f(my_lock, *args, **kwargs)

    return inner


@with_lock
def sum_threadsafe(lock: Lock, numbers: list[float]) -> float:
    """Add a list of numbers together in a thread-safe manner."""
    with lock:
        return sum(numbers)


def main() -> None:
    # We don't need to pass in the lock ourselves thanks to the decorator.
    sum_threadsafe([1.1, 2.2, 3.3])


if __name__ == "__main__":
    main()
