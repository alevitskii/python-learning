from typing import Generator, Iterator


# Generator[<yield type>, <send type>, <return type>]
def my_range(x: int) -> Generator[int, None, None]:
    value = 0
    while value < x:
        yield value
        value += 1


# you can also do this
def my_range2(x: int) -> Iterator[int]:
    value = 0
    while value < x:
        yield value
        value += 1


def gen() -> Generator[int, str, bool]:
    s = yield 1
    print(s)
    yield 2
    print("about to end")
    return False


def main() -> None:
    thing = gen()
    value = next(thing)
    print(f"got from generator: {value}")
    value2 = thing.send("hello hello")
    print(f"got from generator: {value2}")
    try:
        next(thing)
    except StopIteration as e:
        ret, *_ = e.args
        print(f"got this out of exceptions: {ret}")


if __name__ == "__main__":
    main()
