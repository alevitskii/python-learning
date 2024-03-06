from typing import Generic, TypeAlias, TypeVarTuple

Ts = TypeVarTuple("Ts")


class Array(Generic[*Ts]):
    pass


# x dimension - int, y dimension - int, values - float
x: Array[int, int, float]


def double(a: Array[*Ts]) -> Array[*Ts]: ...


def add_dimension(a: Array[*Ts]) -> Array[int, *Ts]: ...


t: TypeAlias = tuple[int, int]
t2: TypeAlias = tuple[*t, float, str]  # tuple[int, int, float, str]

# tuple with single string and variable number of ints
t3: TypeAlias = tuple[str, *tuple[int, ...]]


def f(*args: *t3):
    s, *ints = args


def main() -> None:
    pass


if __name__ == "__main__":
    main()
