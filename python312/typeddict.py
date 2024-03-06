from typing import Any, TypedDict, Unpack


# not ok f(x=1, y=2)
# ok f(x={}, y={})
def f(**kwargs: dict[str, Any]):
    pass


# ok f(x=1, y=2)
def f2(**kwargs: Any):
    pass


class D(TypedDict):
    x: int
    y: str


def f3(**kwargs: Unpack[D]):
    pass


def main() -> None:
    # f(x=1, y=2)
    f(x={}, y={})
    f2(x=1, y=2)
    f3(x=1, y="")


if __name__ == "__main__":
    main()
