# If we're defining decorators with arguments, it's preferred to make them keyword-only.
from collections.abc import Callable
from functools import partial, wraps
from typing import overload

DEFAULT_X = 1
DEFAULT_Y = 2


# decorator_naive()(function)() == decorated(function)() == wrapped()
@overload
def decorator_naive[R](
    function: None = None, *, x: int = DEFAULT_X, y: int = DEFAULT_Y
) -> Callable[[Callable[[int, int], R]], Callable[[], R]]: ...


# decorator_naive(function)() == wrapped()
@overload
def decorator_naive[R](
    function: Callable[[int, int], R], *, x: int = DEFAULT_X, y: int = DEFAULT_Y
) -> Callable[[], R]: ...


# NAIVE: Creating the decorator function
def decorator_naive[R](
    function: Callable[[int, int], R] | None = None,
    *,
    x: int = DEFAULT_X,
    y: int = DEFAULT_Y,
) -> Callable[[], R] | Callable[[Callable[[int, int], R]], Callable[[], R]]:
    if function is None:  # called as `@decorator(...)`

        def decorated(fn: Callable[[int, int], R]) -> Callable[[], R]:
            @wraps(fn)
            def wrapped() -> R:
                return fn(x, y)

            return wrapped

        return decorated
    else:  # called as `@decorator`

        @wraps(function)
        def wrapped() -> R:
            return function(x, y)

        return wrapped


@decorator_naive(x=3, y=4)
def my_function_naive(x: int, y: int) -> int:
    print("result naive =", x + y)
    return x + y


@decorator_naive
def my_function_naive2(x: int, y: int) -> int:
    print("result naive =", x + y)
    return x + y


# decorator_rec(function)() == wrapped()
@overload
def decorator_rec[R](
    function: Callable[[int, int], R], *, x: int = DEFAULT_X, y: int = DEFAULT_Y
) -> Callable[[], R]: ...


# decorator_rec()(function)() == lambda(function)() == wrapped()
@overload
def decorator_rec[R](
    function: None = None, *, x: int = DEFAULT_X, y: int = DEFAULT_Y
) -> Callable[[Callable[[int, int], R]], Callable[[], R]]: ...


# Creating the decorator function
def decorator_rec[R](
    function: Callable[[int, int], R] | None = None,
    *,
    x: int = DEFAULT_X,
    y: int = DEFAULT_Y,
) -> Callable[[], R] | Callable[[Callable[[int, int], R]], Callable[[], R]]:
    if function is None:
        return partial(decorator_rec, x=x, y=y)
        # return lambda f: decorator_rec(f, x=x, y=y)

    @wraps(function)
    def wrapped() -> R:
        return function(x, y)

    return wrapped


# Applying the decorator
@decorator_rec(x=3, y=4)
def my_function_rec(x: int, y: int) -> int:
    print("result rec =", x + y)
    return x + y


# Applying the decorator
@decorator_rec
def my_function_rec2(x: int, y: int) -> int:
    print("result rec =", x + y)
    return x + y


def main() -> None:
    my_function_naive()
    my_function_naive2()

    my_function_rec()
    my_function_rec2()


if __name__ == "__main__":
    main()
