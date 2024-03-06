from typing import TypeAlias


class C[T]:
    pass


def f[T: C, U, V](x: T) -> list[T]:
    return [x]


async def g[T](): ...


Old = int
Newer: TypeAlias = int
type Newest = int
type NewestWithGeneric[T: int] = list[T]


def main() -> None:
    print(isinstance(5, Old))
    # don't use new types if they're checked during runtime
    # print(isinstance(5, Newest))


if __name__ == "__main__":
    main()
