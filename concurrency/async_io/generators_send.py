from collections.abc import Generator


# The send() method assigns the value within the generator function
# and then returns the next value yielded by the generator
def generator_function() -> Generator[None, int, None]:
    while True:
        item = yield
        print(f"received {item}")


def generator_function2() -> Generator[None, int, None]:
    item = yield
    print(f"received {item}")


def main() -> None:
    gen = generator_function()
    next(gen)  # next(gen) == gen.send(None)
    gen.send(37)

    gen = generator_function2()
    next(gen)
    try:
        gen.send(37)
    except StopIteration as e:
        print(f"Caught {e!r}")


if __name__ == "__main__":
    main()
