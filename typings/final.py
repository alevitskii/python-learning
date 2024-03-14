from typing import Final, final


@final
class C:
    foo: Final = 5

    @final
    def hello(self) -> None:
        print("hello hello world")


class D(C):
    foo = 6

    # this is supposed to fail but for some reason it doesn't
    def hello(self) -> None:
        print("goodbye world")


def main() -> None:
    foo: Final = 5
    foo = 6


if __name__ == "__main__":
    main()
