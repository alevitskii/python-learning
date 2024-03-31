import functools
import logging
from typing import Callable, Concatenate, ParamSpec, TypeVar

logging.basicConfig()

P = ParamSpec("P")
R = TypeVar("R")


def prints_hi(f: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(f)
    def prints_hi_inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print("ohai")
        return f(*args, **kwargs)

    return prints_hi_inner


@prints_hi
def hello(name: str) -> int:
    print(f"hello hello {name}")
    return 5


def add_logger(
    f: Callable[Concatenate[logging.Logger, P], R],
) -> Callable[P, R]:
    @functools.wraps(f)
    def add_logger_inner(*args: P.args, **kwargs: P.kwargs) -> R:
        logger = logging.getLogger(f.__module__)
        return f(logger, *args, **kwargs)

    return add_logger_inner


# it's usually not a good idea to modify the signature
@add_logger
def do_something(logger: logging.Logger, name: str, age: int) -> int:
    logger.warning("oh noes!")
    print(f"hello {name}, I hear your age is {age}")
    return age * age


def main() -> None:
    x = do_something("jeff", 22)
    print(x)


if __name__ == "__main__":
    main()
