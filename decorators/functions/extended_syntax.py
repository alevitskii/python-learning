from collections.abc import Callable


def _log[**P, R](f: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R:
    print(f"calling {f.__qualname__!r} with {args=} and {kwargs=}")
    return f(*args, **kwargs)


@(lambda f: lambda *args, **kwargs: _log(f, *args, **kwargs))
def func(x: int) -> int:
    return x + 1


def main() -> None:
    # Probably it's not possible to type annonate a lambda decorator
    func(3)  # type: ignore


if __name__ == "__main__":
    main()
