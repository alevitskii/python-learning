from typing import Never, assert_never, assert_type


def f() -> Never:  # alias for NoReturn
    ...


# illegal to call
def f1(x: Never) -> None: ...


def g(x: int | str) -> None:
    if isinstance(x, int):
        print(f"got int: {x}")
    elif isinstance(x, str):
        print(f"got str: {x}")
    else:
        # we don't expect this line be reacheable
        # similar to raise AssertionError(f"unreachable: {x}")
        assert_never(x)


def g1(x: int | str) -> None:
    if isinstance(x, int):
        print(f"got int: {x}")
        return

    # ...

    # it's not enforced in runtime
    # assert_type(x, int)
    assert_type(x, str)


def main() -> None:
    # f1()
    g(1)
    g1("123")


if __name__ == "__main__":
    main()
