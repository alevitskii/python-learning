from typing import Any, Callable


def f() -> tuple[int, str, float]:
    return 1, "foo", 1.5


# all ints but variable in length
def g() -> tuple[int, ...]:
    # linter can infer that it's a list of ints, it's just to make it more apparent
    x: list[int] = [1, 2, 3, 4]
    return tuple(x)


# any set of arguments in Callable
def get_function_info(func: Callable[..., Any]) -> str:
    return f"{func.__name__}(...)"


if __name__ == "__main__":
    func: Callable[[], tuple[int, ...]] = g
