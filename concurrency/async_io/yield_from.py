import inspect
from collections.abc import Generator

var = None


def nested_generator() -> Generator[None, int, None]:
    for _ in range(5):
        try:
            k = yield
            print(f"inner generator received = {k}")
        except Exception as e:
            print(f"caught an exception: {e}")


def outer_generator() -> Generator[None, int, None]:
    global var
    nested_gen = nested_generator()
    var = nested_gen
    yield from nested_gen


def main() -> None:
    gen = outer_generator()
    next(gen)

    for i in range(6):
        try:
            if i == 1:
                gen.throw(Exception("deliberate exception"))
            elif i == 4:
                gen.close()  # yield from also propagates close()
                print(f"Outer generator state: {inspect.getgeneratorstate(gen)}")
                print(f"Inner generator state: {inspect.getgeneratorstate(var)}")  # type: ignore
            else:
                gen.send(i)
        except StopIteration:
            print(f"Caught exception on iteration {i}")


if __name__ == "__main__":
    main()
